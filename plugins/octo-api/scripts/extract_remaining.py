#!/usr/bin/env python3
"""Render every schema not already covered by a domain or capability skill.

The domain and capability generators cover what an integrator reaches through the core flow.
Whatever is left — shared request wrappers, list envelopes, action results, payment request
variants — still appears in real responses, so it belongs in the plugin. This script closes
that gap so "all 139 schemas" is a fact rather than a claim.

Usage:
    extract_remaining.py --spec openapi.yaml [--out DIR] [--report]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys

import octo_spec as S
from extract_spec import GEN, PROSE, enrich, enum_owners, field_line, toc

PLUGIN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOLD_RE = re.compile(r"\*\*([A-Za-z_][\w\[\]\-\.]*)\*\*")
CODE_RE = re.compile(r"`(\w+)`")


OUT_NAME = "REMAINING-SCHEMAS.md"


# A schema's fields are laid out under a heading naming it: "## `Product`" or
# "### `CheckInLookupRequest`". Anything else is a mention.
# H1 through H4: a dedicated schema file titles it "# `Availability`", while a capability
# file nests it as "### `Availability`".
HEADING_RE = re.compile(r"^#{1,4}\s+`(\w+)`\s*$", re.M)
FIELD_LINE_RE = re.compile(r"^- \*\*([\w\[\]\.\-]+)\*\* \(", re.M)


def fields_under_headings(text: str) -> dict[str, set[str]]:
    """schema name -> the field names rendered beneath its heading in this file.

    A heading alone does not mean the schema is complete: the capability files render only
    the fields a capability adds, under a heading naming the schema it extends. Coverage has
    to compare field sets, not heading presence.
    """
    out: dict[str, set[str]] = {}
    current = None
    for line in text.splitlines():
        h = HEADING_RE.match(line)
        if h:
            current = h.group(1)
            out.setdefault(current, set())
            continue
        if line.startswith("#"):
            # Structural headings — "## Contents", "## Required", "## Fields" — subdivide
            # the schema they sit under. Only "## Source" ends it, and only a heading that
            # names another schema switches it, which HEADING_RE handled above. Resetting on
            # "## Contents" would drop every field that follows the table of contents.
            if line.lstrip("# ").strip().lower() == "source":
                current = None
            continue
        if current:
            m = FIELD_LINE_RE.match(line)
            if m:
                out[current].add(m.group(1))
    return out


def documented(skills_dir: str, exclude: str = "") -> tuple[set[str], set[str], set[str]]:
    """What the plugin documents, at three levels of strictness.

    Returns (mentioned, fields, laid_out):

      mentioned  the schema name appears somewhere — enough to look it up, not enough to
                 build a client against
      fields     every bolded field name, across all files
      laid_out   the schema has its own heading, so its fields are actually rendered there

    The distinction matters: `CheckInLookupRequest` was "mentioned" and its field names all
    happened to occur in other schemas, so a name-plus-fields test called it covered while
    its own definition was missing entirely.

    Pass exclude=OUT_NAME when deciding what this script must render: counting its own
    previous output would make the file shrink to nothing on the second run.
    """
    mentioned: set[str] = set()
    fields: set[str] = set()
    per_schema: dict[str, set[str]] = {}
    for root, _dirs, files in os.walk(skills_dir):
        for fn in files:
            if not fn.endswith(".md") or (exclude and fn == exclude):
                continue
            text = open(os.path.join(root, fn), encoding="utf-8").read()
            mentioned |= set(CODE_RE.findall(text))
            bold = set(BOLD_RE.findall(text))
            mentioned |= bold
            fields |= bold
            for name, fs in fields_under_headings(text).items():
                per_schema.setdefault(name, set()).update(fs)
            # List envelopes have no fields of their own, so a bullet naming them counts.
            for m in re.finditer(r"^- \*\*(\w+)\*\*: array of `\w+`", text, re.M):
                per_schema.setdefault(m.group(1), set())
    return mentioned, fields, per_schema


def render(spec: dict, names: list[str], sha: str) -> str:
    sch = S.schemas(spec)
    resp = S.response_schemas(spec)
    registry = S.enum_registry(spec)
    owners = enum_owners(spec)
    out = [GEN.format(sha=sha[:16]), "", "# Remaining schemas", ""]
    out.append("Every schema whose fields the domain and capability references do not already lay "
               "out: request wrappers, list envelopes, protocol objects, action results and payment "
               "variants. Listed here so the plugin covers all 139 schemas in the specification.")
    out.append("")
    arrays = [n for n in names if S.is_array(sch.get(n) or {})]
    objects = [n for n in names if n not in arrays]
    heads = (["List envelopes"] if arrays else []) + [f"`{n}`" for n in objects]
    if len(heads) > 3:
        out.append(toc(heads))
        out.append("")

    if arrays:
        out.append("## List envelopes")
        out.append("")
        out.append("Array wrappers with no fields of their own. The item schema carries everything.")
        out.append("")
        for n in sorted(arrays):
            item = S.array_item(sch[n]) or "object"
            where = resp.get(n) or []
            line = f"- **{n}**: array of `{item}`."
            if where:
                line += f" Returned by {', '.join(f'`{w}`' for w in where)}."
            out.append(line)
        out.append("")

    for n in sorted(objects):
        sc = sch[n] or {}
        base, caps = S.split_fields(sc)
        enrich(base, registry, owners)
        for _d in caps.values():
            enrich(_d, registry, owners)
        out.append(f"## `{n}`")
        out.append("")
        desc = " ".join((sc.get("description") or "").split())
        cap = S.schema_capability(sc)
        if cap:
            out.append(f"Requires `{cap}` in the `Octo-Capabilities` header.")
            out.append("")
        elif desc:
            out.append(desc.rstrip(".") + ".")
            out.append("")
        where = resp.get(n) or []
        if where:
            out.append(f"Returned by {', '.join(f'`{w}`' for w in where)}.")
            out.append("")
        req = [f for f, i in base.items() if i["required"]]
        if req:
            out.append(f"Required: {', '.join(f'`{r}`' for r in req)}.")
            out.append("")
        if not base and not caps:
            out.append("No properties of its own in the specification: a free-form or "
                       "composed object.")
            out.append("")
        for f, i in base.items():
            out.append(field_line(f, i))
        for c in sorted(caps):
            out.append("")
            out.append(f"With `{c}`:")
            out.append("")
            for f, i in caps[c].items():
                out.append(field_line(f, i))
        out.append("")

    out.append("## Source")
    out.append("")
    out.append(f"Generated from the Ventrata OCTO `openapi.yaml` 3.0.3, sha256 `{sha[:16]}`. "
               "See [docs.ventrata.com](https://docs.ventrata.com).")
    out.append("")
    out.append(PROSE)
    out.append("")
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--spec", required=True)
    ap.add_argument("--out", default=os.path.join(PLUGIN, "skills", "octo-protocol"))
    ap.add_argument("--report", action="store_true")
    args = ap.parse_args()

    spec = S.load(args.spec)
    with open(args.spec, "rb") as fh:
        sha = hashlib.sha256(fh.read()).hexdigest()
    sch = S.schemas(spec)

    have_s, have_f, per_schema = documented(os.path.join(PLUGIN, "skills"), exclude=OUT_NAME)

    # Covered means: every field of this schema is rendered under a heading naming it.
    # A heading with only a capability's additions leaves the base fields undocumented.
    def gap(name: str) -> list[str]:
        base, caps = S.split_fields(sch.get(name) or {})
        every = set(base) | {f for d in caps.values() for f in d}
        return sorted(every - per_schema.get(name, set()))

    missing = sorted(n for n in sch if n not in per_schema or gap(n))

    if args.report:
        print(f"{len(sch) - len(missing)}/{len(sch)} schemas fully rendered")
        for n in missing:
            g = gap(n)
            why = "never rendered" if n not in per_schema else f"{len(g)} field(s) missing"
            print(f"  missing: {n} ({why})")
        return 0 if not missing else 1

    if not missing:
        print("nothing to do: every schema is already documented")
        return 0

    # One file per half when the catch-all grows past what a reader will scan. The split is
    # alphabetical so a schema's location stays predictable.
    SPLIT_AT = 260
    body = render(spec, missing, sha)
    if body.count("\n") > SPLIT_AT and len(missing) > 6:
        half = (len(missing) + 1) // 2
        for part, group in ((1, missing[:half]), (2, missing[half:])):
            piece = render(spec, group, sha).replace(
                "# Remaining schemas",
                f"# Remaining schemas, part {part} ({group[0]}–{group[-1]})", 1)
            target = os.path.join(args.out, OUT_NAME.replace(".md", f"-{part}.md"))
            prose = ""
            if os.path.exists(target):
                old_text = open(target, encoding="utf-8").read()
                if PROSE in old_text:
                    prose = old_text.split(PROSE, 1)[1]
            with open(target, "w", encoding="utf-8") as fh:
                fh.write(piece.rstrip("\n") + prose.rstrip("\n") + "\n" if prose else piece)
            print(f"wrote {target} ({piece.count(chr(10))} lines, {len(group)} schemas)")
        single = os.path.join(args.out, OUT_NAME)
        if os.path.exists(single):
            os.remove(single)
            print(f"removed {single} (superseded by the split)")
        return 0
    path = os.path.join(args.out, OUT_NAME)
    prose = ""
    if os.path.exists(path):
        old = open(path, encoding="utf-8").read()
        if PROSE in old:
            prose = old.split(PROSE, 1)[1]
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(body.rstrip("\n") + prose.rstrip("\n") + "\n" if prose else body)
    print(f"wrote {path} ({body.count(chr(10))} lines, {len(missing)} schemas)")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except BrokenPipeError:
        sys.exit(0)  # piped into head
