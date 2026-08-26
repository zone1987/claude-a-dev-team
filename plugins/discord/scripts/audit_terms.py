#!/usr/bin/env python3
"""Prove every term the documentation states appears in the plugin.

Page coverage proves a page was assigned to a skill. Link checking proves a file is reachable.
Neither proves the *content* arrived: a skill can claim 17 pages, link 17 files, and still have
dropped half the fields on each page. This closes that gap by comparing vocabularies.

What counts as a term — chosen because each one is a fact a reader looks up, and a paraphrase
cannot preserve it:
  identifiers   backtick-quoted names: field names, enum values, headers, paths
  constants     SCREAMING_SNAKE_CASE names: events, intents, permissions, error names
  routes        method + path lines produced from the upstream <Route> components
  numbers       every integer in a table cell: opcodes, close codes, bit values, limits

A term present in the mirror and absent from every reference file is reported as MISSING. The
reverse direction — a term in the plugin that is absent upstream — is what catches invention, and
it is reported as INVENTED.

Per-page reporting matters more than a total: 98 % coverage spread evenly is healthy, while 98 %
with one page at 20 % means that page was skimmed.

Usage:
    audit_terms.py --mirror DIR [--skill NAME] [--min-coverage FLOAT] [--show N] [--invented]
Exit code is non-zero when a page falls below --min-coverage (default 0.95).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

PLUGIN = Path(__file__).resolve().parent.parent

BACKTICKED = re.compile(r"`([^`\n]{2,80})`")
CONSTANT = re.compile(r"\b([A-Z][A-Z0-9]*(?:_[A-Z0-9]+)+)\b")
ROUTE = re.compile(r"<Route\s+method=\"([A-Z]+)\">([^<]+)</Route>")
TABLE_NUMBER = re.compile(r"\b(\d{2,10})\b")

# Scaffolding and prose noise that carries no fact, so its absence proves nothing.
# Upstream embeds a markdown link inside a route path — /guilds/[\{guild.id}](/developers/...) —
# and inside table cells. The plugin renders the same path as {guild.id}. Comparing the raw forms
# reports a false miss on every parameterised route, so both sides are normalised first.
MD_LINK = re.compile(r"\[\\?\{?([^\]]*?)\}?\]\([^)]*\)")
ESCAPES = re.compile(r"\\([_*`{}\[\]])")


def normalise(term: str) -> str:
    """Reduce a term to what it identifies, so rendering differences do not read as absence."""
    term = MD_LINK.sub(lambda m: "{" + m.group(1) + "}" if "." in m.group(1) else m.group(1), term)
    term = ESCAPES.sub(r"\1", term)
    term = re.sub(r"\s+", " ", term).strip()
    return term


NOISE = {
    "true", "false", "null", "undefined", "string", "integer", "boolean", "object", "array",
    "number", "snowflake", "id", "name", "type", "value", "http", "https", "json", "GET", "POST",
    "PATCH", "PUT", "DELETE", "TODO", "NOTE", "npm", "node", "python3", "bash", "sh", "js", "ts",
}


# An anchor fragment is a slice of a URL, not a term a reader looks up.
ANCHOR_FRAGMENT = re.compile(r"^-|-$")


# A template expression or a CSS value belongs to the docs site's own page furniture, not to
# Discord's API. Every navigational hub page carries the same two from an image widget, which
# would otherwise report those pages as 0 % covered while nothing was in fact lost.
TEMPLATE_OR_CSS = re.compile(r"\$\{|^calc\(|^center calc\(|px$|%\)$")


def is_lookup_term(token: str) -> bool:
    """A term must be something a reader could look up, or its absence proves nothing."""
    if not token or len(token) < 3:
        return False
    if TEMPLATE_OR_CSS.search(token):
        return False
    if ANCHOR_FRAGMENT.search(token):
        return False
    if token in NOISE or token.lower() in NOISE:
        return False
    if len(token.split()) > 4:
        return False
    return True


def terms_of(text: str, *, with_numbers: bool) -> set[str]:
    found: set[str] = set()

    for raw in BACKTICKED.findall(text):
        token = normalise(raw)
        if is_lookup_term(token):
            found.add(token)

    for const in CONSTANT.findall(text):
        if const not in NOISE and len(const) > 3:
            found.add(const)

    for method, path in ROUTE.findall(text):
        found.add(f"{method} {normalise(path)}")

    if with_numbers:
        for line in text.splitlines():
            if line.lstrip().startswith("|"):
                for num in TABLE_NUMBER.findall(line):
                    found.add(num)

    return found


PARAM = re.compile(r"\{([^}]+)\}")


def present(term: str, haystack: str) -> bool:
    """Match on identity, tolerating only how a path parameter is written.

    Upstream writes a poll answer route as .../answers/answer_id and the plugin as
    .../answers/{answer_id}. Both name the same route, so a brace difference is not a gap —
    while a different path segment still is.
    """
    if term in haystack:
        return True
    if "/" in term:
        braced = re.sub(r"/([a-z][a-z0-9_.]*_id)\b", r"/{\1}", term)
        if braced != term and braced in haystack:
            return True
        bare = PARAM.sub(r"\1", term)
        if bare != term and bare in haystack:
            return True
    return False


def normalise_haystack(text: str) -> str:
    """Apply the same normalisation to the plugin side, so a match is decided on identity."""
    text = ESCAPES.sub(r"\1", text)
    return text


def plugin_text(skill: str | None) -> tuple[str, list[str]]:
    skills_root = PLUGIN / "skills"
    dirs = [skills_root / skill] if skill else sorted(p for p in skills_root.iterdir() if p.is_dir())
    parts: list[str] = []
    names: list[str] = []
    for d in dirs:
        if not d.is_dir():
            continue
        names.append(d.name)
        for md in sorted(d.rglob("*.md")):
            parts.append(md.read_text(encoding="utf-8"))
    return "\n".join(parts), names


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--mirror", required=True)
    parser.add_argument("--skill", default=None, help="audit one skill only")
    parser.add_argument("--min-coverage", type=float, default=0.95)
    parser.add_argument("--show", type=int, default=12, help="missing terms to print per page")
    parser.add_argument("--invented", action="store_true", help="also report plugin terms absent upstream")
    parser.add_argument("--json-out", default="", help="write the full report here")
    args = parser.parse_args()

    mirror = Path(args.mirror)
    coverage = json.loads((PLUGIN / "PAGE-COVERAGE.json").read_text(encoding="utf-8"))

    haystack, audited = plugin_text(args.skill)
    haystack = normalise_haystack(haystack)
    if not haystack:
        print("no skill content to audit", file=sys.stderr)
        return 2

    pages = [
        (skill, page)
        for skill, page_list in sorted(coverage["pages"].items())
        for page in page_list
        if args.skill is None or skill == args.skill
    ]

    report: dict[str, dict] = {}
    failures: list[str] = []
    total_terms = total_found = 0
    all_source_terms: set[str] = set()

    print(f"{'page':62s} {'terms':>6s} {'found':>6s} {'cov':>6s}")
    for skill, page in pages:
        src = mirror / (page.replace("/", "__") + ".md")
        if not src.is_file():
            failures.append(f"NO-MIRROR {page}")
            continue
        text = src.read_text(encoding="utf-8")
        terms = terms_of(text, with_numbers=True)
        all_source_terms |= terms
        if not terms:
            continue

        missing = sorted(t for t in terms if not present(t, haystack))
        found = len(terms) - len(missing)
        cov = found / len(terms)
        total_terms += len(terms)
        total_found += found

        report[page] = {
            "skill": skill,
            "terms": len(terms),
            "found": found,
            "coverage": round(cov, 4),
            "missing": missing,
        }

        flag = "" if cov >= args.min_coverage else "  << below threshold"
        print(f"{page:62s} {len(terms):6d} {found:6d} {cov:6.1%}{flag}")
        if cov < args.min_coverage:
            failures.append(f"THIN      {page} ({cov:.1%}, {len(missing)} terms missing)")
            for term in missing[: args.show]:
                print(f"    missing: {term!r}")
            if len(missing) > args.show:
                print(f"    … and {len(missing) - args.show} more")

    overall = total_found / total_terms if total_terms else 0.0
    print(f"\n{total_found} of {total_terms} source terms present ({overall:.2%})")
    print(f"audited: {', '.join(audited)}")

    if args.invented:
        plugin_terms = terms_of(haystack, with_numbers=False)
        invented = sorted(t for t in plugin_terms if t not in all_source_terms)
        # Cross-references to sibling skills and this marketplace's own vocabulary are expected.
        invented = [t for t in invented if not t.startswith(("discord-", "references/", "scripts/"))]
        print(f"\n{len(invented)} plugin term(s) not found in the mirror (review for invention):")
        for term in invented[:40]:
            print(f"    {term}")
        if len(invented) > 40:
            print(f"    … and {len(invented) - 40} more")

    if args.json_out:
        Path(args.json_out).write_text(json.dumps(report, indent=1) + "\n", encoding="utf-8")
        print(f"\nwrote {args.json_out}")

    if failures:
        print()
        for failure in failures:
            print(failure)
        print(f"\n{len(failures)} page(s) below {args.min_coverage:.0%}")
        return 1

    print(f"\nevery page is at or above {args.min_coverage:.0%} term coverage")
    return 0


if __name__ == "__main__":
    sys.exit(main())
