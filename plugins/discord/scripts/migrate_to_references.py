#!/usr/bin/env python3
"""Move reference files into references/ and repair every link, per REF-04.

REF-04 is blocking in this marketplace: a reference lives in skills/<skill>/references/ and is
linked directly from SKILL.md. Moving the files is the easy half; the half that silently breaks a
plugin is the links, in three places at once — SKILL.md pointing down into references/, a reference
pointing sideways at another reference, and a reference pointing back up at SKILL.md.

Idempotent: running it on an already-migrated skill changes nothing.

Usage:
    migrate_to_references.py [--skill NAME]… [--apply]
Without --apply it reports what it would do and changes nothing.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

PLUGIN = Path(__file__).resolve().parent.parent
SKILLS = PLUGIN / "skills"


def rewrite_links(text: str, names: set[str], *, from_reference: bool) -> tuple[str, int]:
    """Point every link at where the file now lives.

    from_reference=False rewrites SKILL.md: NAME.md -> references/NAME.md
    from_reference=True  rewrites a reference: references/NAME.md -> NAME.md, SKILL.md -> ../SKILL.md
    """
    count = 0

    def repl(match: re.Match[str]) -> str:
        nonlocal count
        label, target = match.group(1), match.group(2)
        anchor = ""
        if "#" in target:
            target, anchor = target.split("#", 1)
            anchor = "#" + anchor
        if "://" in target or target.startswith(("mailto:", "/")):
            return match.group(0)

        base = target.split("/")[-1]
        if base not in names and base != "SKILL.md":
            return match.group(0)

        if from_reference:
            new = "../SKILL.md" if base == "SKILL.md" else base
        else:
            new = base if base == "SKILL.md" else f"references/{base}"

        if new + anchor != target + anchor:
            count += 1
        return f"[{label}]({new}{anchor})"

    return re.sub(r"\[([^\]]*)\]\(([^)]+)\)", repl, text), count


def migrate(skill_dir: Path, apply: bool) -> list[str]:
    skill_md = skill_dir / "SKILL.md"
    loose = sorted(p for p in skill_dir.glob("*.md") if p.name != "SKILL.md")
    references_dir = skill_dir / "references"

    if not loose:
        return [f"{skill_dir.name}: already compliant"]

    names = {p.name for p in loose} | {p.name for p in references_dir.glob("*.md")} if references_dir.is_dir() else {p.name for p in loose}
    actions = [f"{skill_dir.name}: move {len(loose)} file(s) into references/"]

    if apply:
        references_dir.mkdir(exist_ok=True)
        for src in loose:
            dst = references_dir / src.name
            if dst.exists():
                actions.append(f"  REFUSED {src.name}: references/{src.name} already exists")
                continue
            text, n = rewrite_links(src.read_text(encoding="utf-8"), names, from_reference=True)
            dst.write_text(text, encoding="utf-8")
            src.unlink()
            actions.append(f"  moved {src.name} ({n} link(s) rewritten)")

        if skill_md.is_file():
            text, n = rewrite_links(skill_md.read_text(encoding="utf-8"), names, from_reference=False)
            skill_md.write_text(text, encoding="utf-8")
            actions.append(f"  SKILL.md: {n} link(s) rewritten")

    return actions


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--skill", action="append", default=[], help="limit to these skills")
    parser.add_argument("--apply", action="store_true", help="perform the move")
    args = parser.parse_args()

    targets = [SKILLS / s for s in args.skill] if args.skill else sorted(p for p in SKILLS.iterdir() if p.is_dir())
    for skill_dir in targets:
        if not skill_dir.is_dir():
            print(f"no such skill: {skill_dir.name}", file=sys.stderr)
            return 2
        for line in migrate(skill_dir, args.apply):
            print(line)

    if not args.apply:
        print("\ndry run; pass --apply to move")
    return 0


if __name__ == "__main__":
    sys.exit(main())
