#!/usr/bin/env python3
"""Two-direction coverage proof for the discord-rest skill.

Forward:  every table row, enum value, endpoint, code block and prose line of each
          mirrored page appears in the generated reference file.
Reverse:  every endpoint path and table row in the reference files exists upstream,
          so nothing was invented.

Usage:
    python3 verify_rest_coverage.py --mirror <dir> --skill <dir>
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from build_rest_reference import (  # noqa: E402
    PAGES,
    ROUTE_RE,
    clean_route_path,
)

TABLE_ROW_RE = re.compile(r"^\s*\|(.+)\|\s*$")
SEPARATOR_RE = re.compile(r"^\s*\|[\s:\-|]+\|\s*$")


def norm(s: str) -> str:
    """Normalise a cell for comparison: strip markdown links, escapes, whitespace."""
    # <ManualAnchor> is scaffolding the transform removes, including where upstream
    # embeds it inline in a heading; ignore it on both sides of the comparison.
    s = re.sub(r"<ManualAnchor\s+id=\"[^\"]*\"\s*/>", "", s)
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = s.replace("\\_", "_").replace("\\{", "{").replace("\\}", "}")
    s = s.replace("\\*", "*").replace("\\|", "|").replace("\\`", "`")
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def table_rows(text: str) -> list[tuple[str, ...]]:
    rows = []
    in_fence = False
    for line in text.split("\n"):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence or SEPARATOR_RE.match(line):
            continue
        m = TABLE_ROW_RE.match(line)
        if m:
            cells = tuple(norm(c) for c in m.group(1).split("|"))
            if any(cells):
                rows.append(cells)
    return rows


def code_blocks(text: str) -> list[str]:
    blocks, cur, in_fence = [], [], False
    for line in text.split("\n"):
        stripped = line.lstrip()
        if stripped.startswith("```"):
            if in_fence:
                blocks.append(norm_code("\n".join(cur)))
                cur = []
            in_fence = not in_fence
            continue
        if in_fence:
            cur.append(line.strip())
    return blocks


def norm_code(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def routes(text: str) -> list[str]:
    return [
        f"{m.group(1)} {clean_route_path(m.group(2))}" for m in ROUTE_RE.finditer(text)
    ]


HEADING_RE = re.compile(r"^#{1,6}\s+(.*)$")


def headings(text: str) -> list[str]:
    out, in_fence = [], False
    for line in text.split("\n"):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        # Accordion bodies are indented upstream; strip it so a nested '######'
        # label is classified as a heading in both source and generated file.
        m = HEADING_RE.match(line.lstrip())
        if m:
            out.append(norm(m.group(1)))
    return out


GEN_ROUTE_RE = re.compile(r"^### ([A-Z]+) (/\S*)\s*$", re.M)


def prose_lines(text: str) -> list[str]:
    """Non-table, non-fence, non-heading content lines, normalised."""
    out, in_fence = [], False
    for line in text.split("\n"):
        s = line.strip()
        if s.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence or not s:
            continue
        if TABLE_ROW_RE.match(line) or SEPARATOR_RE.match(line):
            continue
        if HEADING_RE.match(s):
            continue
        out.append(norm(s))
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--mirror", required=True, type=Path)
    ap.add_argument("--skill", required=True, type=Path)
    args = ap.parse_args()

    failures = 0
    totals = {
        "rows": 0,
        "routes": 0,
        "blocks": 0,
        "headings": 0,
        "prose": 0,
    }

    for stem in sorted(PAGES):
        out_name = PAGES[stem][0]
        src = (args.mirror / f"{stem}.md").read_text()
        gen = (args.skill / out_name).read_text()

        problems: list[str] = []

        # --- forward: rows
        src_rows = table_rows(src)
        gen_rows = set(table_rows(gen))
        missing_rows = [r for r in src_rows if r not in gen_rows]
        totals["rows"] += len(src_rows)
        if missing_rows:
            problems.append(f"{len(missing_rows)} table rows missing: {missing_rows[:3]}")

        # --- forward: routes
        src_routes = routes(src)
        gen_routes = {f"{m.group(1)} {m.group(2)}" for m in GEN_ROUTE_RE.finditer(gen)}
        totals["routes"] += len(src_routes)
        missing_routes = [r for r in src_routes if r not in gen_routes]
        if missing_routes:
            problems.append(f"{len(missing_routes)} routes missing: {missing_routes[:3]}")

        # --- reverse: no invented routes
        extra_routes = [r for r in gen_routes if r not in set(src_routes)]
        if extra_routes:
            problems.append(f"INVENTED routes: {extra_routes[:3]}")

        # --- forward: code blocks
        src_blocks = [b for b in code_blocks(src) if b]
        gen_blocks = set(code_blocks(gen))
        totals["blocks"] += len(src_blocks)
        missing_blocks = [b for b in src_blocks if b not in gen_blocks]
        if missing_blocks:
            problems.append(
                f"{len(missing_blocks)} code blocks missing: "
                f"{[b[:60] for b in missing_blocks[:2]]}"
            )

        # --- forward: headings (the page's own H1 is intentionally replaced)
        src_heads = [h for h in headings(src) if h]
        gen_heads = set(headings(gen))
        totals["headings"] += len(src_heads)
        missing_heads = [
            h
            for h in src_heads
            if h not in gen_heads and h != norm(PAGES[stem][1])
        ]
        if missing_heads:
            problems.append(f"{len(missing_heads)} headings missing: {missing_heads[:5]}")

        # --- forward: prose lines
        src_prose = prose_lines(src)
        gen_prose_set = set(prose_lines(gen))
        # scaffolding lines legitimately removed
        def scaffold(p: str) -> bool:
            # Lines the transform is *supposed* to remove: the documentation-index
            # preamble, the export const JS, ManualAnchor tags, container tags, and
            # the page subtitle (which is re-emitted in the generated header).
            if p.startswith("> ## Documentation Index"):
                return True
            if "docs.discord.com/llms.txt" in p:
                return True
            if p.startswith("> Use this file to discover"):
                return True
            if p.startswith(("export const", "return <div", "<span", "</div>", "};")):
                return True
            if p.startswith("<ManualAnchor"):
                return True
            if re.fullmatch(r"</?(Info|Note|Warning|Danger|Accordion)\b[^>]*>", p):
                return True
            # A <Route> line becomes a '### METHOD /path' heading, checked separately.
            if p.startswith("<Route method="):
                return True
            if p.startswith("> Reference for Discord"):
                return True
            return False

        missing_prose = [
            p for p in src_prose if p not in gen_prose_set and not scaffold(p)
        ]
        # allow lines that were folded into a blockquote or accordion heading
        gen_all = norm(gen)
        missing_prose = [p for p in missing_prose if p not in gen_all]
        totals["prose"] += len(src_prose)
        if missing_prose:
            problems.append(
                f"{len(missing_prose)} prose lines missing: {missing_prose[:4]}"
            )

        if problems:
            failures += 1
            print(f"FAIL {out_name}")
            for p in problems:
                print(f"     - {p}")
        else:
            print(
                f"OK   {out_name:26} rows={len(src_rows):4} routes={len(src_routes):3} "
                f"blocks={len(src_blocks):2} headings={len(src_heads):3}"
            )

    print()
    print(
        f"TOTALS  table rows {totals['rows']}  endpoints {totals['routes']}  "
        f"code blocks {totals['blocks']}  headings {totals['headings']}  "
        f"prose lines {totals['prose']}"
    )
    print("FAILURES:", failures)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
