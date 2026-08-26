#!/usr/bin/env python3
"""Generate the Lua event catalogue from the game's own code.

Events are how a mod reacts to the game, and the authoritative list is not published anywhere: it
has to be recovered from the code that registers, triggers and consumes them. This does that from
three angles and merges the results, because no single angle is complete:

  Events.<Name>.Add(...)      consumers — proves the name and shows a real handler signature
  triggerEvent("<Name>", ...) producers in Lua — gives the argument list as passed
  LuaEventManager.AddEvent    registrations

The handler signature is the useful part: a name alone does not tell you what arguments arrive, and
that is exactly what a modder needs. Where a consumer's parameter names are available they are
recorded verbatim, because the game's own naming is the best documentation of meaning.

Usage:
    build_event_index.py --lua-dir DIR --out FILE [--build 42]
"""
from __future__ import annotations

import argparse
import collections
import hashlib
import pathlib
import re
import sys

ADD = re.compile(r'Events\.([A-Za-z0-9_]+)\.Add\s*\(\s*(?:function\s*\(([^)]*)\)|([A-Za-z0-9_.:]+))')
# The game registers named functions far more often than inline ones (395 versus a handful), so the
# signature usually lives in the function's own definition elsewhere. Index every definition so a
# registration by name can be resolved to its parameter list.
FUNC_DEF = re.compile(r'^\s*function\s+([A-Za-z0-9_.:]+)\s*\(([^)]*)\)', re.MULTILINE)
FUNC_ASSIGN = re.compile(r'^\s*([A-Za-z0-9_.:]+)\s*=\s*function\s*\(([^)]*)\)', re.MULTILINE)
REMOVE = re.compile(r'Events\.([A-Za-z0-9_]+)\.Remove')
TRIGGER = re.compile(r'triggerEvent\s*\(\s*"([A-Za-z0-9_]+)"\s*([^)]*)\)')
REGISTER = re.compile(r'LuaEventManager\.AddEvent\s*\(\s*"([A-Za-z0-9_]+)"')
ANY_REF = re.compile(r'Events\.([A-Za-z0-9_]+)')


def side_of(path: str) -> str:
    for part in ("client", "server", "shared"):
        if f"/{part}/" in path or path.startswith(part + "/"):
            return part
    return "?"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--lua-dir", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--build", default="42")
    args = ap.parse_args()

    root = pathlib.Path(args.lua_dir)
    if not root.is_dir():
        print(f"no directory at {root}", file=sys.stderr)
        return 2

    files = sorted(root.rglob("*.lua"))
    digest = hashlib.sha256()
    handlers: dict[str, list[tuple[str, str]]] = collections.defaultdict(list)
    named: dict[str, list[tuple[str, str]]] = collections.defaultdict(list)  # event -> (funcname, file)
    func_params: dict[str, str] = {}
    triggers: dict[str, list[tuple[str, str]]] = collections.defaultdict(list)
    registered: set[str] = set()
    sides: dict[str, set[str]] = collections.defaultdict(set)
    refs: collections.Counter[str] = collections.Counter()

    for f in files:
        raw = f.read_bytes()
        digest.update(raw)
        text = raw.decode("utf-8", errors="replace")
        rel = str(f.relative_to(root))
        side = side_of(rel)
        for m in FUNC_DEF.finditer(text):
            func_params.setdefault(m.group(1), m.group(2).strip())
        for m in FUNC_ASSIGN.finditer(text):
            func_params.setdefault(m.group(1), m.group(2).strip())
        for m in ADD.finditer(text):
            name = m.group(1)
            inline = (m.group(2) or "").strip()
            fname = (m.group(3) or "").strip()
            if m.group(2) is not None:
                handlers[name].append((inline, rel))
            elif fname:
                named[name].append((fname, rel))
            sides[name].add(side)
        for m in REMOVE.finditer(text):
            sides[m.group(1)].add(side)
        for m in TRIGGER.finditer(text):
            name, rest = m.group(1), m.group(2).strip().lstrip(",").strip()
            triggers[name].append((rest, rel))
            sides[name].add(side)
        for m in REGISTER.finditer(text):
            registered.add(m.group(1))
        for m in ANY_REF.finditer(text):
            refs[m.group(1)] += 1
            sides[m.group(1)].add(side)

    # Resolve each named registration to the parameter list of its definition. A dotted name may be
    # defined as `function A.b(...)` or as a method `function A:b(...)`, so try both spellings.
    for event, entries in named.items():
        for fname, rel in entries:
            params = func_params.get(fname)
            if params is None and "." in fname:
                params = func_params.get(fname.replace(".", ":", fname.count(".") - 1 if fname.count(".") > 1 else 1))
            if params is None:
                tail = fname.split(".")[-1].split(":")[-1]
                cands = {v for k, v in func_params.items() if k.split(".")[-1].split(":")[-1] == tail}
                params = next(iter(cands)) if len(cands) == 1 else None
            if params is not None:
                handlers[event].append((params, f"{rel} via {fname}"))

    names = sorted(set(refs) | set(handlers) | set(triggers) | registered)
    source_hash = digest.hexdigest()[:16]

    L: list[str] = [
        f"<!-- generated by scripts/build_event_index.py from Project Zomboid build {args.build} "
        f"media/lua, {len(files)} files, sha256:{source_hash} — do not edit above the prose marker -->",
        "",
        "# Lua event catalogue",
        "",
        f"Every event name reachable through the `Events` table, recovered from the game's own "
        f"{len(files):,} Lua files: **{len(names)} names**, of which {len(handlers)} have at least one "
        f"handler in the game's code and {len(triggers)} are triggered from Lua.",
        "",
        "Register with `Events.<Name>.Add(fn)` and unregister with `Events.<Name>.Remove(fn)` — the "
        "same function reference, or the removal does nothing.",
        "",
        "**The handler signature column is the useful one.** It carries the parameter names the "
        "game's own code uses, verbatim, which is the closest thing to documentation of what each "
        "argument means. An event with no handler in the base game still exists; it simply has no "
        "in-game consumer to copy from.",
        "",
        "**A name here is not proof of an event.** `Events` is an ordinary table, so a few entries are "
        "fields on an unrelated local of the same name. An entry with neither a handler nor a trigger "
        "and only one reference is a candidate for that, and is marked.",
        "",
        "**Sides** are inferred from which directory references the event, not declared: `client` and "
        "`server` mean it is referenced there, and both means both.",
        "",
        "## Contents",
        "",
        "- [Events with a known handler signature](#events-with-a-known-handler-signature)",
        "- [Events referenced without a signature](#events-referenced-without-a-signature)",
        "",
        "## Events with a known handler signature",
        "",
        "| Event | Handler signature | Sides | Refs | Triggered in Lua |",
        "| --- | --- | --- | ---: | --- |",
    ]
    for n in names:
        if n not in handlers:
            continue
        sig = handlers[n][0][0]
        variants = {h[0] for h in handlers[n]}
        sig_cell = f"`function({sig})`"
        if len(variants) > 1:
            sig_cell += f" _(+{len(variants) - 1} other arity/naming in game code)_"
        s = ", ".join(sorted(x for x in sides[n] if x != "?")) or "?"
        trig = "yes" if n in triggers else "no — engine-triggered"
        L.append(f"| `{n}` | {sig_cell} | {s} | {refs[n]} | {trig} |")

    L += ["", "## Events referenced without a signature", "",
          "No handler with an inline function was found in the game's code, so the argument list is "
          "not recoverable this way. Where the event is triggered from Lua, the trigger's arguments "
          "are given instead.", "",
          "| Event | Trigger arguments | Sides | Refs | Note |",
          "| --- | --- | --- | ---: | --- |"]
    for n in names:
        if n in handlers:
            continue
        trig = triggers[n][0][0] if n in triggers else ""
        s = ", ".join(sorted(x for x in sides[n] if x != "?")) or "?"
        note = "registered via LuaEventManager" if n in registered else (
            "single reference — verify it is an event" if refs[n] <= 1 and n not in triggers else "")
        L.append(f"| `{n}` | {('`' + trig + '`') if trig else '_not triggered from Lua_'} | {s} | {refs[n]} | {note} |")
    L.append("")

    out = pathlib.Path(args.out)
    out.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"{len(files)} files, sha256:{source_hash}")
    print(f"{len(names)} event names, {len(handlers)} with a handler signature, "
          f"{len(triggers)} triggered from Lua, {len(registered)} registered -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
