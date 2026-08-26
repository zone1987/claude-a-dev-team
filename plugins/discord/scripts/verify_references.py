#!/usr/bin/env python3
"""Prove that no reference file in this plugin is unreachable and no link is dead.

A reference file that no SKILL.md links to is invisible: Claude never learns it exists, so its
content is lost even though the bytes are on disk. A link pointing at a missing file is the same
failure seen from the other side. Both are silent, which is why they are checked mechanically
rather than by reading.

Checks, per skill directory:
  ORPHAN   a file in references/ that SKILL.md does not link to
  MISPLACED a .md file beside SKILL.md instead of in references/ (REF-04)
  DEAD     a relative link in any .md file whose target does not exist
  UPSTREAM a leftover /developers/... link into the live docs site instead of a reference file
  NO-TOC   a file over 100 lines with three or more '##' sections and no table of contents
  LONG     a SKILL.md over 120 lines

Usage:
    verify_references.py [--skills-dir DIR] [--quiet]
Exit code is non-zero when any check fails.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
UPSTREAM_LINK = re.compile(r"\]\((/developers/[^)]+)\)")
HEADING = re.compile(r"^##\s", re.MULTILINE)
TOC_HINT = re.compile(r"^##\s*(Contents|Table of contents)", re.MULTILINE | re.IGNORECASE)

SKILL_MAX_LINES = 120
TOC_MIN_LINES = 100
TOC_MIN_SECTIONS = 3


def local_targets(text: str) -> set[str]:
    """Relative link targets, anchors and external URLs stripped.

    A code sample can contain bracket-then-paren text that reads as a markdown link — a C++
    signature spanning lines is the case that surfaced here. Such a "target" is not a path, and
    treating it as one makes the checker raise instead of report. So a candidate must look like a
    file reference: one line, no whitespace, and short enough to be a real name.
    """
    out = set()
    for raw in LINK.findall(text):
        target = raw.split("#", 1)[0].strip()
        if not target or "://" in target or target.startswith(("mailto:", "/")):
            continue
        if "\n" in target or " " in target or len(target) > 200:
            continue
        out.add(target)
    return out


def check_skill(skill_dir: Path) -> list[str]:
    findings: list[str] = []
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        return [f"MISSING  {skill_dir.name}/SKILL.md — the directory cannot load as a skill"]

    skill_text = skill_md.read_text(encoding="utf-8")
    skill_lines = skill_text.count("\n") + 1
    if skill_lines > SKILL_MAX_LINES:
        findings.append(
            f"LONG     {skill_dir.name}/SKILL.md is {skill_lines} lines, limit is {SKILL_MAX_LINES}"
        )

    # REF-04: references live in references/, each linked directly from SKILL.md.
    linked_from_skill = {t.split("/")[-1] for t in local_targets(skill_text)}
    references_dir = skill_dir / "references"
    references = sorted(references_dir.glob("*.md")) if references_dir.is_dir() else []

    for misplaced in sorted(p for p in skill_dir.glob("*.md") if p.name != "SKILL.md"):
        findings.append(
            f"MISPLACED {skill_dir.name}/{misplaced.name} sits beside SKILL.md; REF-04 puts it in references/"
        )

    for reference in references:
        if reference.name not in linked_from_skill:
            findings.append(
                f"ORPHAN   {skill_dir.name}/references/{reference.name} is not linked from SKILL.md — unreachable"
            )

    for deep in [p for p in skill_dir.rglob("*.md") if p.parent not in (skill_dir, references_dir)]:
        findings.append(
            f"NESTED   {deep.relative_to(skill_dir.parent)} is deeper than references/ — read only in part"
        )

    for md in [skill_md, *references]:
        text = md.read_text(encoding="utf-8")

        for target in local_targets(text):
            if not (md.parent / target).exists():
                findings.append(f"DEAD     {skill_dir.name}/{md.name} -> {target} does not exist")

        for upstream in UPSTREAM_LINK.findall(text):
            findings.append(
                f"UPSTREAM {skill_dir.name}/{md.name} -> {upstream} still points at the live docs site"
            )

        if md.name == "SKILL.md":
            continue
        lines = text.count("\n") + 1
        sections = len(HEADING.findall(text))
        if lines > TOC_MIN_LINES and sections >= TOC_MIN_SECTIONS and not TOC_HINT.search(text):
            findings.append(
                f"NO-TOC   {skill_dir.name}/{md.name} is {lines} lines with {sections} sections and no contents list"
            )

    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--skills-dir", default=str(Path(__file__).resolve().parent.parent / "skills"))
    parser.add_argument("--quiet", action="store_true", help="print findings only")
    args = parser.parse_args()

    skills_root = Path(args.skills_dir)
    if not skills_root.is_dir():
        print(f"no skills directory at {skills_root}", file=sys.stderr)
        return 2

    skill_dirs = sorted(p for p in skills_root.iterdir() if p.is_dir())
    all_findings: list[str] = []
    for skill_dir in skill_dirs:
        findings = check_skill(skill_dir)
        all_findings.extend(findings)
        if not args.quiet:
            refs = len(list((skill_dir / "references").glob("*.md")))
            lines = sum((p.read_text(encoding="utf-8").count("\n") + 1) for p in skill_dir.rglob("*.md"))
            status = "ok" if not findings else f"{len(findings)} finding(s)"
            print(f"{skill_dir.name:24s} {refs:3d} references  {lines:6d} lines  {status}")

    if all_findings:
        print()
        for finding in all_findings:
            print(finding)
        print(f"\n{len(all_findings)} finding(s)")
        return 1

    if not args.quiet:
        print("\nevery reference is reachable, every link resolves")
    return 0


if __name__ == "__main__":
    sys.exit(main())
