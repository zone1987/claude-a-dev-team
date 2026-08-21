#!/usr/bin/env python3
"""Remove a flat reference whose byte-identical copy already sits in references/.

A half-migrated skill holds both copies of a file: the flat original and the one under
references/. Deleting the flat one is only safe when the two are byte-identical, so that is
checked per file and the run aborts on any difference rather than guessing which is current.

Files present only flat are moved, not deleted. SKILL.md links are then repointed at
references/ and every link is verified to resolve.

    dedupe_references.py --plugin P [--apply]
"""
from __future__ import annotations

import argparse
import filecmp
import glob
import os
import re
import shutil
import subprocess
import sys

PLUGIN_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(os.path.dirname(PLUGIN_DIR))
PLUGINS = os.path.join(REPO, os.path.basename(os.path.dirname(PLUGIN_DIR)))
LINK = re.compile(r"\[([^\]]+)\]\(([^)\s#]+\.md)\)")


def tracked(path: str) -> bool:
    try:
        return subprocess.run(["git", "-C", REPO, "ls-files", "--error-unmatch",
                               os.path.relpath(path, REPO)],
                              capture_output=True).returncode == 0
    except FileNotFoundError:
        return False


def drop(path: str) -> None:
    if tracked(path):
        subprocess.run(["git", "-C", REPO, "rm", "-q", os.path.relpath(path, REPO)], check=True)
    else:
        os.remove(path)


def move(src: str, dst: str) -> None:
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    if tracked(src):
        subprocess.run(["git", "-C", REPO, "mv", os.path.relpath(src, REPO),
                        os.path.relpath(dst, REPO)], check=True)
    else:
        shutil.move(src, dst)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--plugin", required=True)
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    root = os.path.join(PLUGINS, args.plugin, "skills")
    if not os.path.isdir(root):
        print(f"no such plugin: {args.plugin}", file=sys.stderr)
        return 2

    removed = moved = relinked = 0
    for skill_md in sorted(glob.glob(os.path.join(root, "*", "SKILL.md"))):
        d = os.path.dirname(skill_md)
        names = set()
        for f in sorted(glob.glob(os.path.join(d, "*.md"))):
            base = os.path.basename(f)
            if base == "SKILL.md":
                continue
            twin = os.path.join(d, "references", base)
            if os.path.exists(twin):
                if not filecmp.cmp(f, twin, shallow=False):
                    print(f"ABORT: {os.path.relpath(f, REPO)} differs from its references/ copy; "
                          "merge them by hand", file=sys.stderr)
                    return 1
                if args.apply:
                    drop(f)
                removed += 1
            else:
                if args.apply:
                    move(f, twin)
                moved += 1
            names.add(base)

        if not names:
            continue
        text = open(skill_md, encoding="utf-8").read()

        def repoint(m: re.Match) -> str:
            label, target = m.group(1), m.group(2)
            if "/" not in target and target in names:
                return f"[{label}](references/{target})"
            return m.group(0)

        new = LINK.sub(repoint, text)
        if new != text:
            relinked += 1
            if args.apply:
                open(skill_md, "w", encoding="utf-8").write(new)

    verb = "" if args.apply else " (dry run)"
    print(f"{args.plugin}: {removed} duplicate(s) removed, {moved} moved, "
          f"{relinked} SKILL.md relinked{verb}")

    if args.apply:
        bad = 0
        for skill_md in sorted(glob.glob(os.path.join(root, "*", "SKILL.md"))):
            d = os.path.dirname(skill_md)
            for _, t in LINK.findall(open(skill_md, encoding="utf-8").read()):
                if not os.path.exists(os.path.join(d, t)):
                    print(f"  broken link: {os.path.relpath(skill_md, REPO)} -> {t}",
                          file=sys.stderr)
                    bad += 1
        if bad:
            return 1
        print("  every link resolves")
    return 0


if __name__ == "__main__":
    sys.exit(main())
