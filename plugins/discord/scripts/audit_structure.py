#!/usr/bin/env python3
"""Prove the structural elements of each page survived: headings, tables, code and card titles.

Term coverage proves the vocabulary arrived. It does not prove the *structure* did: a page can keep
every identifier while losing a whole section, and a navigation grid can vanish entirely because its
card titles are attributes rather than prose. That gap is what this checks.

Per page, four counts compared against the reference files that claim it:
  headings     every '#'..'######' heading's text must appear somewhere in the covering files
  tables       source table rows versus rows in the covering files (a floor, not an equality)
  code fences  source fenced blocks versus fences in the covering files
  card titles  every title="..." of an MDX card, which renders as a navigation entry

A heading match is by text, and consolidating several pages legitimately renames one: upstream's
"Authentication for Public Clients" becomes "Public Client Integration" once the section sits inside
a combined file, with the body verbatim underneath. So a heading whose *body* is present is not a
loss. The check therefore verifies the section's content, not its title: for each missing heading it
takes the longest sentence of that section's body and looks for it. Only a heading whose body is also
absent is reported as SECTION-LOST, which is the finding that means content was dropped.
Generic titles ("Next Steps", "Error Handling", "Change Log", "Common Issues") repeat across pages
and carry no fact by themselves, so they are judged solely on their body.

Usage:
    audit_structure.py --mirror DIR [--skill NAME] [--show N]
Exit code is non-zero when a page loses a heading, a card title, or more than 10 % of its tables
or code fences.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

PLUGIN = Path(__file__).resolve().parent.parent

HEADING = re.compile(r"^#{1,6}\s+(.+?)\s*$", re.MULTILINE)
TABLE_ROW = re.compile(r"^\s*\|", re.MULTILINE)
FENCE = re.compile(r"^```", re.MULTILINE)
CARD_TITLE = re.compile(r'title="([^"]+)"')
LINKED = re.compile(r"\[([^\]]*)\]\([^)]*\)")


def clean(text: str) -> str:
    """Strip markdown emphasis and link syntax so a heading matches however it was rendered."""
    text = LINKED.sub(r"\1", text)
    text = re.sub(r"[`*_]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip().lower()


SENTENCE = re.compile(r"[A-Z][^.!?\n]{40,240}[.!?]")


def section_body(text: str, heading: str) -> str:
    """The prose between this heading and the next one at any level."""
    pattern = re.compile(
        r"^#{1,6}\s+" + re.escape(heading) + r"\s*$(.*?)(?=^#{1,6}\s|\Z)",
        re.MULTILINE | re.DOTALL,
    )
    m = pattern.search(text)
    return m.group(1) if m else ""


def section_body_missing(text: str, heading: str, body_clean: str) -> bool:
    """True only when the section's own content cannot be found in the reference files."""
    body = section_body(text, heading)
    if not body.strip():
        return False  # an empty section carries nothing to lose

    # Prefer a long sentence: distinctive enough that a match is not coincidence.
    for sentence in sorted(SENTENCE.findall(body), key=len, reverse=True)[:3]:
        if clean(sentence)[:120] in body_clean:
            return False

    # No usable sentence: fall back to the longest code line, then to any long backticked name.
    for line in sorted((l.strip() for l in body.splitlines()), key=len, reverse=True)[:5]:
        if len(line) > 30 and clean(line)[:80] in body_clean:
            return False

    return True


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--mirror", required=True)
    ap.add_argument("--skill", default=None)
    ap.add_argument("--show", type=int, default=6)
    args = ap.parse_args()

    mirror = Path(args.mirror)
    coverage = json.loads((PLUGIN / "PAGE-COVERAGE.json").read_text(encoding="utf-8"))
    findings: list[str] = []

    print(f"{'page':58s} {'head':>9s} {'tbl':>9s} {'code':>9s} {'card':>7s}")
    for skill, pages in sorted(coverage["pages"].items()):
        if args.skill and skill != args.skill:
            continue
        skill_dir = PLUGIN / "skills" / skill
        if not (skill_dir / "SKILL.md").is_file():
            continue
        body = "\n".join(p.read_text(encoding="utf-8") for p in skill_dir.rglob("*.md"))
        body_clean = clean(body)
        out_tables = len(TABLE_ROW.findall(body))
        out_fences = len(FENCE.findall(body))

        for page in pages:
            src = mirror / (page.replace("/", "__") + ".md")
            if not src.is_file():
                continue
            text = src.read_text(encoding="utf-8")

            heads = [h for h in HEADING.findall(text) if h.strip()]
            candidates = [h for h in heads if clean(h) and clean(h) not in body_clean]
            # A renamed heading is not a loss; a missing body is. Probe each one's content.
            lost_heads = [h for h in candidates if section_body_missing(text, h, body_clean)]
            cards = sorted(set(CARD_TITLE.findall(text)))
            lost_cards = [c for c in cards if clean(c) not in body_clean]
            src_tables = len(TABLE_ROW.findall(text))
            src_fences = len(FENCE.findall(text))

            print(f"{page:58s} {len(heads)-len(lost_heads):4d}/{len(heads):<4d} "
                  f"{min(src_tables, out_tables):4d}/{src_tables:<4d} "
                  f"{min(src_fences, out_fences):4d}/{src_fences:<4d} "
                  f"{len(cards)-len(lost_cards):3d}/{len(cards):<3d}")

            if lost_heads:
                findings.append(f"HEADINGS  {page}: {len(lost_heads)} not found")
                for h in lost_heads[: args.show]:
                    print(f"    heading: {h!r}")
            if lost_cards:
                findings.append(f"CARDS     {page}: {len(lost_cards)} navigation titles not found")
                for c in lost_cards[: args.show]:
                    print(f"    card: {c!r}")
            if src_tables and out_tables < src_tables * 0.9:
                findings.append(f"TABLES    {page}: {out_tables} rows against {src_tables} in source")
            if src_fences and out_fences < src_fences * 0.9:
                findings.append(f"CODE      {page}: {out_fences} fences against {src_fences} in source")

    if findings:
        print()
        for f in findings:
            print(f)
        print(f"\n{len(findings)} finding(s)")
        return 1
    print("\nevery heading, card title, table and code block is accounted for")
    return 0


if __name__ == "__main__":
    sys.exit(main())
