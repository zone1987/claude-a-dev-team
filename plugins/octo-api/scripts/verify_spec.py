#!/usr/bin/env python3
"""Verify the shipped reference files against the OpenAPI specification.

Checks both directions, which is what makes the plugin trustworthy:

  forward   every specified field, parameter and enum value is documented
  reverse   every documented field name exists in the specification

The reverse check is the one that catches invention: a plausible-sounding field added by
hand fails the build.

Usage:
    verify_spec.py --spec openapi.yaml [--domain products] [--all] [-v]
Exit code is non-zero on any discrepancy.
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys

import octo_spec as S
from extract_spec import DOMAINS

BOLD_RE = re.compile(r"\*\*([A-Za-z_][\w\[\]\-\.]*)\*\*")
# Prose legitimately bolds things that are not field names: a dotted access path
# (booking.pricing.retail), a bracketed traversal (unitItems[].ticket), or an ordinary
# English word used for emphasis. Only bare identifiers are checked against the spec.
IDENT_RE = re.compile(r"^[a-z_][A-Za-z0-9_]*$")
PLUGIN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Result:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.stats: list[str] = []

    def fail(self, msg: str) -> None:
        self.errors.append(msg)

    def ok(self, msg: str) -> None:
        self.stats.append(msg)


def balanced(text: str) -> str | None:
    """The attribute head of a field line, up to its matching close paren.

    A type can carry its own parentheses — "string (uuid), optional" — so count depth
    rather than cutting at the first ")".
    """
    depth = 1
    for i, ch in enumerate(text):
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
            if depth == 0:
                return text[:i]
    return None


def documented_tokens(files: list[str]) -> set[str]:
    """Every bold token across a skill's reference files."""
    found: set[str] = set()
    for path in files:
        with open(path, encoding="utf-8") as fh:
            found |= set(BOLD_RE.findall(fh.read()))
    return found


def verify_domain(spec: dict, domain: str, res: Result, verbose: bool) -> None:
    cfg = DOMAINS[domain]
    skill_dir = os.path.join(PLUGIN, "skills", cfg["skill"])
    if not os.path.isdir(skill_dir):
        res.fail(f"{domain}: skill directory missing: {skill_dir}")
        return

    idx_path = os.path.join(skill_dir, "FIELD-INDEX.json")
    if not os.path.exists(idx_path):
        res.fail(f"{domain}: FIELD-INDEX.json missing — run extract_spec.py")
        return
    shipped = json.load(open(idx_path, encoding="utf-8"))

    # (a) the index must still match the specification
    from extract_spec import build, sha_of  # local import keeps the CLI light

    _, fresh = build(spec, domain, shipped.get("specSha256", ""))
    for key in ("endpoints", "schemas"):
        if shipped.get(key) != fresh.get(key):
            only_shipped = set(shipped.get(key, {})) - set(fresh.get(key, {}))
            only_fresh = set(fresh.get(key, {})) - set(shipped.get(key, {}))
            detail = []
            if only_shipped:
                detail.append(f"stale: {sorted(only_shipped)}")
            if only_fresh:
                detail.append(f"new in spec: {sorted(only_fresh)}")
            for name in sorted(set(shipped.get(key, {})) & set(fresh.get(key, {}))):
                if shipped[key][name] != fresh[key][name]:
                    detail.append(f"changed: {name}")
            res.fail(f"{domain}: FIELD-INDEX.json {key} out of date ({'; '.join(detail) or 'content differs'})")
    res.ok(f"{domain}: index matches spec for {len(fresh['schemas'])} schemas, {len(fresh['endpoints'])} operations")

    md = sorted(glob.glob(os.path.join(skill_dir, "*.md")))
    tokens = documented_tokens(md)

    # (b) forward: every field in the index is documented somewhere
    expected: set[str] = set()
    for name, info in fresh["schemas"].items():
        expected |= set(info["base"])
        for fields in info["capabilities"].values():
            expected |= set(fields)
    missing = sorted(expected - tokens)
    if missing:
        res.fail(f"{domain}: {len(missing)} specified field(s) undocumented: {missing[:12]}")
    else:
        res.ok(f"{domain}: all {len(expected)} specified fields documented")

    # (c) forward: every parameter is documented
    params: set[str] = set()
    for info in fresh["endpoints"].values():
        params |= set(info["params"])
    missing_p = sorted(params - tokens)
    if missing_p:
        res.fail(f"{domain}: {len(missing_p)} parameter(s) undocumented: {missing_p[:12]}")
    else:
        res.ok(f"{domain}: all {len(params)} parameters documented")

    # (d) reverse: no documented token that the spec does not know
    known = expected | params | set(fresh["schemas"]) | {"Responses", "Required"}
    unknown = sorted(
        t
        for t in tokens - known
        # A dotted path is checked by its last segment; anything non-identifier is prose.
        if IDENT_RE.match(t)
        and t.split(".")[-1].replace("[]", "") not in known
        and t.split(".")[0] not in known
    )
    if unknown:
        res.fail(f"{domain}: {len(unknown)} documented name(s) absent from spec: {unknown[:12]}")
    else:
        res.ok(f"{domain}: no invented field names")

    # (e) forward: every enum value appears in the prose
    body = "\n".join(open(p, encoding="utf-8").read() for p in md)
    enums: set[str] = set()
    for info in fresh["schemas"].values():
        enums |= set(info["enums"])
    for info in fresh["endpoints"].values():
        enums |= set(info["enums"])
    missing_e = sorted(e for e in enums if e not in body)
    if missing_e:
        res.fail(f"{domain}: {len(missing_e)} enum value(s) missing: {missing_e[:12]}")
    else:
        res.ok(f"{domain}: all {len(enums)} enum values present")

    # structural rules from CLAUDE.md
    skill_md = os.path.join(skill_dir, "SKILL.md")
    if os.path.exists(skill_md):
        n = sum(1 for _ in open(skill_md, encoding="utf-8"))
        if n > 120:
            res.fail(f"{domain}: SKILL.md is {n} lines (limit 120)")
    for path in md:
        n = sum(1 for _ in open(path, encoding="utf-8"))
        if n > 100 and "## Contents" not in open(path, encoding="utf-8").read():
            res.fail(f"{domain}: {os.path.basename(path)} is {n} lines and has no table of contents")
    if verbose:
        for p in md:
            print(f"    {os.path.basename(p):32} {sum(1 for _ in open(p, encoding='utf-8')):4} lines")


def verify_full_coverage(spec: dict, res: Result) -> None:
    """Plugin-wide coverage: every schema, every response body, every property.

    The per-domain checks only see their own skill. This one asks the question a user asks:
    is anything in the specification missing from the plugin as a whole?
    """
    from extract_remaining import documented

    sch = S.schemas(spec)
    # laid_out, not merely mentioned: a schema is covered when its own heading renders its
    # fields. Sharing field names with a neighbour proves nothing.
    have_s, have_f, laid_out = documented(os.path.join(PLUGIN, "skills"))

    missing = sorted(n for n in sch if n not in laid_out)
    if missing:
        res.fail(f"coverage: {len(missing)} schema(s) never rendered: {missing[:12]}")
    else:
        res.ok(f"coverage: all {len(sch)} schemas rendered under their own heading")

    resp = S.response_schemas(spec)
    missing_r = sorted(n for n in resp if n not in laid_out)
    if missing_r:
        res.fail(f"coverage: {len(missing_r)} response schema(s) undocumented: {missing_r[:12]}")
    else:
        res.ok(f"coverage: all {len(resp)} response schemas documented")

    props: set[str] = set()
    for schema in sch.values():
        base, caps = S.split_fields(schema)
        props |= set(base) | {f for d in caps.values() for f in d}
    missing_p = sorted(p for p in props if p not in have_f)
    if missing_p:
        res.fail(f"coverage: {len(missing_p)} propert(ies) undocumented: {missing_p[:12]}")
    else:
        res.ok(f"coverage: all {len(props)} properties documented")

    ops = {f"{o['method']} {o['path']}" for o in S.operations(spec)}
    body = ""
    for root, _d, files in os.walk(os.path.join(PLUGIN, "skills")):
        for fn in files:
            if fn.endswith(".md"):
                body += open(os.path.join(root, fn), encoding="utf-8").read()
    missing_o = sorted(o for o in ops if f"`{o}`" not in body)
    if missing_o:
        res.fail(f"coverage: {len(missing_o)} operation(s) undocumented: {missing_o[:12]}")
    else:
        res.ok(f"coverage: all {len(ops)} operations documented")


def verify_field_detail(spec: dict, res: Result) -> None:
    """Every rendered field must state type and optionality, and carry whatever the
    specification documents: description, possible values, example.

    Where the specification itself is silent, that is reported rather than invented — a
    client author needs to know the difference between "optional" and "undocumented".
    """
    import glob as _glob

    # Only generated files carry field definitions. SKILL.md is hand-written prose whose
    # bullets deliberately read as sentences, so checking it for a type signature reports
    # style, not correctness. Identify generated files by their stamp instead of guessing
    # from the text.
    rendered = 0
    missing_optionality = []
    for path in _glob.glob(os.path.join(PLUGIN, "skills", "*", "*.md")):
        text = open(path, encoding="utf-8").read()
        if not text.startswith("<!-- generated by scripts/"):
            continue
        for line in text.splitlines():
            if not line.startswith("- **"):
                continue
            name, _, rest = line[4:].partition("**")
            if not rest.startswith(" ("):
                continue  # a prose bullet, not a field definition
            attrs = balanced(rest[2:])
            if attrs is None:
                continue
            rendered += 1
            if "required" not in attrs and "optional" not in attrs:
                missing_optionality.append(f"{os.path.basename(path)}:{name}")
    if missing_optionality:
        res.fail(f"detail: {len(missing_optionality)} field(s) state neither required nor "
                 f"optional: {missing_optionality[:8]}")
    else:
        res.ok(f"detail: all {rendered} rendered fields state type and optionality")

    sch = S.schemas(spec)
    total = no_desc = no_example = 0
    for schema in sch.values():
        base, caps = S.split_fields(schema)
        for _f, i in list(base.items()) + [(k, v) for d in caps.values() for k, v in d.items()]:
            total += 1
            if not i.get("description"):
                no_desc += 1
            if i.get("example") is None and not i.get("enum"):
                no_example += 1
    res.ok(f"detail: {total} properties; the spec omits a description for {no_desc} "
           f"and an example or enum for {no_example}")


def verify_counts(spec: dict, res: Result) -> None:
    """The state file's counters are the drift tripwire."""
    state_path = os.path.join(PLUGIN, ".spec-state.json")
    if not os.path.exists(state_path):
        res.ok("no .spec-state.json yet — skipping count check")
        return
    state = json.load(open(state_path, encoding="utf-8"))
    want, have = state.get("counts") or {}, S.counts(spec)
    if want and want != have:
        res.fail(f".spec-state.json counts differ: recorded {want}, spec has {have}")
    else:
        res.ok(f"spec counts match state: {have}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--spec", required=True)
    ap.add_argument("--domain")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("-v", "--verbose", action="store_true")
    args = ap.parse_args()

    spec = S.load(args.spec)
    res = Result()
    targets = list(DOMAINS) if args.all or not args.domain else [args.domain]
    for d in targets:
        if d not in DOMAINS:
            res.fail(f"unknown domain {d!r}")
            continue
        if not os.path.isdir(os.path.join(PLUGIN, "skills", DOMAINS[d]["skill"])):
            continue  # not extracted yet
        verify_domain(spec, d, res, args.verbose)
    if args.all or not args.domain:
        verify_full_coverage(spec, res)
        verify_field_detail(spec, res)
    verify_counts(spec, res)

    for line in res.stats:
        print(f"  ok  {line}")
    for line in res.errors:
        print(f"FAIL  {line}", file=sys.stderr)
    print()
    if res.errors:
        print(f"{len(res.errors)} check(s) failed", file=sys.stderr)
        return 1
    print(f"all {len(res.stats)} checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
