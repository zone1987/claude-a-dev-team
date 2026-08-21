#!/usr/bin/env python3
"""Prove a plugin covers its source, in both directions.

  forward   every enumerated source unit maps to a plugin file   (UNCOVERED, DANGLING, STALE)
  reverse   every identifier the plugin documents exists upstream (INVENTED)

The reverse direction is the one that catches invention, and it is why a forward-only audit is
worth much less than half of one. Generalised from octo-api's check_sitemap.py and audit_pages.py.

Reads a local mirror by default so a verdict is reproducible and needs no network. A re-run that
changes verdict with no change to the plugin means it is reading the live site.

Usage:
    audit_coverage.py --plugin P --sitemap URL --pages DIR [--map FILE] [--write]
    audit_coverage.py --plugin P --spec openapi.yaml
Exit code is non-zero on any finding.
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Terms a reader would look up. Everything else is prose.
BACKTICK = re.compile(r"`([^`\n]{3,44})`")
CAMEL = re.compile(r"\b([a-z]+[A-Z][A-Za-z]{2,})\b")
SCREAMING_VALUE = re.compile(r"\b([A-Z]{3,}(?:_[A-Z0-9]+)*)\b")
IDENT = re.compile(r"^[a-z_][A-Za-z0-9_]*$")

STOP = set(
    "the a an and or of to in is are for with be this that it as on by from you your we our can "
    "will not if when use used using see also all any each per via has have had was were which "
    "what how why where who them they".split()
)


class Findings:
    def __init__(self) -> None:
        self.rows: list[tuple[str, str]] = []

    def add(self, kind: str, detail: str) -> None:
        self.rows.append((kind, detail))

    def report(self) -> int:
        by: dict[str, list[str]] = {}
        for kind, detail in self.rows:
            by.setdefault(kind, []).append(detail)
        for kind in ("UNCOVERED", "DANGLING", "STALE", "INVENTED", "UNDOCUMENTED"):
            for d in by.get(kind, []):
                print(f"  {kind:13} {d}")
        return 1 if self.rows else 0


def sitemap_pages(url: str, pages_dir: str) -> list[str]:
    """Page paths from a mirrored sitemap. The mirror is the reproducible input."""
    local = os.path.join(pages_dir, "sitemap.xml")
    if not os.path.exists(local):
        print(f"no mirrored sitemap at {local}\n"
              "mirror it first, so the audit is reproducible:\n"
              f"  curl -sS {url} -o {local}", file=sys.stderr)
        sys.exit(3)
    xml = open(local, encoding="utf-8", errors="replace").read()
    host = re.match(r"(https?://[^/]+)", url)
    base = host.group(1) if host else ""
    return [u.replace(base, "").strip("/") for u in re.findall(r"<loc>([^<]+)</loc>", xml)]


def spec_units(path: str) -> list[str]:
    """Operations and schemas from an OpenAPI or JSON Schema document."""
    text = open(path, encoding="utf-8").read()
    try:
        doc = json.loads(text)
    except json.JSONDecodeError:
        try:
            import yaml
        except ImportError:
            print("a YAML spec needs PyYAML; convert it to JSON first", file=sys.stderr)
            sys.exit(3)
        doc = yaml.safe_load(text)
    units = []
    for p, item in (doc.get("paths") or {}).items():
        for method in item:
            if method.lower() in ("get", "post", "put", "patch", "delete", "head", "options"):
                units.append(f"{method.upper()} {p}")
    units += sorted((doc.get("components") or {}).get("schemas") or {})
    return units


def plugin_text(plugin: str) -> tuple[str, set[str]]:
    """All markdown in a plugin's skills, and the set of files present."""
    base = os.path.join(REPO, "plugins", plugin)
    files, chunks = set(), []
    for f in sorted(glob.glob(os.path.join(base, "skills", "*", "*.md"))
                    + glob.glob(os.path.join(base, "*.md"))):
        files.add(os.path.relpath(f, base))
        chunks.append(open(f, encoding="utf-8", errors="replace").read())
    return "\n".join(chunks), files


def documented_terms(text: str) -> set[str]:
    out = set()
    for rx in (BACKTICK, CAMEL, SCREAMING_VALUE):
        for m in rx.findall(text):
            t = m.strip()
            if t.lower() in STOP or len(t) < 3:
                continue
            out.add(t)
    return out


def load_map(path: str) -> dict[str, list[str]]:
    if not path or not os.path.exists(path):
        return {}
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def load_excluded(path: str) -> dict[str, str]:
    """Terms deliberately not mirrored, each with its reason.

    An explicit list beats a clever pattern: every exclusion is then a decision someone can
    review, where a regex that quietly drops a class of term is indistinguishable from a bug.
    """
    if not path or not os.path.exists(path):
        return {}
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    missing = [k for k, v in data.items() if not str(v).strip()]
    if missing:
        print(f"exclusion list carries no reason for: {', '.join(missing[:5])}", file=sys.stderr)
        sys.exit(3)
    return data


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--plugin", required=True)
    ap.add_argument("--sitemap")
    ap.add_argument("--spec")
    ap.add_argument("--repo", metavar="SHA")
    ap.add_argument("--pages", default="")
    ap.add_argument("--map", default="", help="JSON: source unit -> [files covering it]")
    ap.add_argument("--excluded", default="", help="JSON: term -> reason it is not documented")
    ap.add_argument("--write", action="store_true", help="emit DOCUMENTATION-MAP.md")
    args = ap.parse_args()

    if args.sitemap:
        units = sitemap_pages(args.sitemap, args.pages or "/tmp/mirror")
        label = args.sitemap
    elif args.spec:
        units = spec_units(args.spec)
        label = args.spec
    elif args.repo:
        print("--repo needs a tree listing; pass it through --map for now", file=sys.stderr)
        return 3
    else:
        ap.print_usage(sys.stderr)
        return 3

    text, present = plugin_text(args.plugin)
    coverage = load_map(args.map)
    excluded = load_excluded(args.excluded)
    f = Findings()

    for unit in units:
        files = coverage.get(unit)
        if not files:
            # With no explicit map, a unit counts as covered when the plugin mentions its last
            # path segment. Coarse on purpose: an explicit map is what makes this exact.
            token = unit.rstrip("/").split("/")[-1].split(" ")[-1]
            if token and token.lower() in text.lower():
                continue
            f.add("UNCOVERED", f"{unit} maps to nothing")
            continue
        for target in files:
            if target not in present:
                f.add("DANGLING", f"{unit} -> {target} does not exist")

    for unit in sorted(set(coverage) - set(units)):
        f.add("STALE", f"{unit} is mapped but no longer in the source")

    if args.spec:
        spec_names = set()
        raw = open(args.spec, encoding="utf-8", errors="replace").read()
        spec_names |= set(re.findall(r"^\s*([A-Za-z_][A-Za-z0-9_]*):", raw, re.M))
        for term in sorted(documented_terms(text)):
            if not IDENT.match(term) or term in excluded:
                continue
            if term not in spec_names and term not in raw:
                f.add("INVENTED", f"'{term}' is documented but absent from {os.path.basename(args.spec)}")

    print(f"{len(units)} units enumerated from {label}")
    print(f"{len(units) - sum(1 for k, _ in f.rows if k == 'UNCOVERED')}/{len(units)} covered")
    if excluded:
        print(f"{len(excluded)} term(s) excluded, each with a stated reason")

    rc = f.report()

    if args.write:
        out = os.path.join(REPO, "plugins", args.plugin, "DOCUMENTATION-MAP.md")
        lines = ["<!-- generated by scripts/audit_coverage.py — do not edit -->", "",
                 "# Documentation map", "",
                 f"Every one of the {len(units)} units enumerated from `{label}`, and where this "
                 "plugin covers it.", "", "| Source unit | Covered by |", "|---|---|"]
        for unit in units:
            files = coverage.get(unit) or ["(matched by mention)"]
            lines.append(f"| `{unit}` | " + ", ".join(f"`{x}`" for x in files) + " |")
        lines += ["", "## Source", "", f"Enumerated from {label}, read at generation time.", ""]
        with open(out, "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines))
        print(f"wrote {os.path.relpath(out, REPO)}")

    return rc


if __name__ == "__main__":
    sys.exit(main())
