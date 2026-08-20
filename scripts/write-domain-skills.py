#!/usr/bin/env python3
"""Write the domain SKILL.md files after bundling.

Each one is a map: what the domain covers, and one bullet per reference file saying what is in
it. The description carries the triggers, and it is the only thing that costs listing budget —
so it is written by hand per domain, not generated from the file names.

Usage:
    write-domain-skills.py --plugin shopware-merchant [--check]
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_spec(plugin: str) -> dict:
    path = os.path.join(ROOT, "scripts", "domain-skills", f"{plugin}.json")
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def title_of(path: str) -> str:
    for line in open(path, encoding="utf-8"):
        if line.startswith("# "):
            return line[2:].strip()
    return os.path.basename(path)[:-3]


def gist_of(path: str, limit: int = 110) -> str:
    text = open(path, encoding="utf-8").read()
    text = re.sub(r"^#.*$", "", text, flags=re.M)
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    for para in text.split("\n\n"):
        p = " ".join(para.split())
        if len(p) > 30 and not p.startswith(("|", "-", "*", "!", "[", "<")):
            p = re.sub(r"\s*\(.*?\)", "", p)
            out = p.split(". ")[0].rstrip(".")
            return (out[: limit - 1] + "…") if len(out) > limit else out
    return ""


def build(plugin: str, domain: str, meta: dict, check: bool) -> tuple[str, int]:
    sk = os.path.join(ROOT, "plugins", plugin, "skills", f"{meta['prefix']}-{domain}")
    files = sorted(f for f in glob.glob(os.path.join(sk, "*.md"))
                   if not f.endswith("SKILL.md"))
    lines = [
        "---",
        f"name: {meta['prefix']}-{domain}",
        f"description: {meta['description']}",
        "---",
        "",
        f"# {meta['title']}",
        "",
        meta["intro"],
        "",
    ]
    if meta.get("notes"):
        lines += [meta["notes"], ""]
    lines += ["## Reference map", ""]
    names = sorted(os.path.basename(f) for f in files)
    # A topic owns every file whose name extends it: SIDEBAR.md owns SIDEBAR-API.md and
    # SIDEBAR-EXAMPLES.md. Those are listed inside the topic's bullet, never as topics of
    # their own — otherwise every file appears twice and the map outgrows the skill.
    topics = [n for n in names
              if not any(n.startswith(o[:-3] + "-") for o in names if o != n and o[:-3] in
                         {x[:-3] for x in names})]
    owned: dict[str, list[str]] = {t: [] for t in topics}
    for n in names:
        if n in owned:
            continue
        parent = max((t for t in topics if n.startswith(t[:-3] + "-")),
                     key=len, default=None)
        if parent:
            owned[parent].append(n)
        else:
            owned[n] = []
    # Keep the map inside the 120-line skill limit: drop the prose gist once a domain has
    # more topics than fit with one.
    terse = len(owned) > 14
    for f in files:
        base = os.path.basename(f)
        if base not in owned:
            continue
        companions = sorted(owned[base])
        bullet = f"- **[{base}]({base})**"
        if not terse:
            gist = gist_of(f)
            if gist:
                bullet += f": {gist}."
        elif companions:
            bullet += ":"
        if companions:
            bullet += " " + ", ".join(f"[{c[:-3]}]({c})" for c in companions) + "."
        lines.append(bullet)
    listed = set(owned) | {c for v in owned.values() for c in v}
    for e in sorted(set(names) - listed):
        gist = gist_of(os.path.join(sk, e))
        lines.append(f"- **[{e}]({e})**" + (f": {gist}." if gist and not terse else "."))
    lines += ["", "## Source", "", meta["source"], ""]

    body = "\n".join(lines)
    if not check:
        with open(os.path.join(sk, "SKILL.md"), "w", encoding="utf-8") as fh:
            fh.write(body)
    return body, len(meta["description"])


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--plugin", required=True)
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    spec = load_spec(args.plugin)
    # Refuse before writing: an over-long description is silently truncated in the listing,
    # which strips exactly the trigger words it was written for.
    over = {d: len({**spec["defaults"], **m}["description"])
            for d, m in spec["domains"].items()
            if len({**spec["defaults"], **m}["description"]) > 200}
    if over:
        print("error: description over 200 characters:", file=sys.stderr)
        for d, n in sorted(over.items()):
            print(f"  {d}: {n}", file=sys.stderr)
        return 1
    total = 0
    print(f"{'skill':34} {'lines':>6} {'desc':>5} {'cost':>6}")
    print("-" * 55)
    for domain, meta in sorted(spec["domains"].items()):
        meta = {**spec["defaults"], **meta}
        body, dlen = build(args.plugin, domain, meta, args.check)
        total += dlen + 109
        flag = "  <- desc > 200" if dlen > 200 else ""
        print(f"{spec['defaults']['prefix']}-{domain:22} {body.count(chr(10)):6} "
              f"{dlen:5} {dlen + 109:6}{flag}")
    print("-" * 55)
    print(f"{'TOTAL listing cost':34} {'':6} {'':5} {total:6}  = {total / 8000 * 100:.1f}% of budget")
    return 0


if __name__ == "__main__":
    sys.exit(main())
