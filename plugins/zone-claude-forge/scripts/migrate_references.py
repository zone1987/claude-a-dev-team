#!/usr/bin/env python3
"""Move a plugin's reference files into skills/<skill>/references/ and repoint SKILL.md.

REF-04 requires every markdown reference to live in a references/ subdirectory, and DEPTH-01
requires each one to be linked directly from SKILL.md. This script performs that move for an
existing plugin: it relocates the files with `git mv` where the repository is a git checkout,
rewrites the links in SKILL.md, and verifies afterwards that every link resolves.

It never creates an index file, and it refuses to run when one is present, since that layout
downgrades every file behind it to a head -100 preview.

    migrate_references.py --plugin contao [--apply]
"""
from __future__ import annotations

import argparse
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
INDEX_NAMES = {"INDEX.md", "README.md", "CONTENTS.md"}


def git_tracked(path: str) -> bool:
    try:
        return subprocess.run(["git", "-C", REPO, "ls-files", "--error-unmatch", path],
                              capture_output=True).returncode == 0
    except FileNotFoundError:
        return False


def move(src: str, dst: str, apply: bool) -> None:
    if not apply:
        return
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    if git_tracked(os.path.relpath(src, REPO)):
        subprocess.run(["git", "-C", REPO, "mv", os.path.relpath(src, REPO),
                        os.path.relpath(dst, REPO)], check=True)
    else:
        shutil.move(src, dst)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--plugin", required=True)
    ap.add_argument("--apply", action="store_true", help="write the changes (default: dry run)")
    args = ap.parse_args()

    root = os.path.join(PLUGINS, args.plugin, "skills")
    if not os.path.isdir(root):
        print(f"no such plugin: {args.plugin}", file=sys.stderr)
        return 2

    moved = relinked = 0
    for skill_md in sorted(glob.glob(os.path.join(root, "*", "SKILL.md"))):
        d = os.path.dirname(skill_md)
        skill = os.path.basename(d)

        stray = [f for f in glob.glob(os.path.join(d, "references", "*.md"))
                 if os.path.basename(f) in INDEX_NAMES]
        if stray:
            print(f"refusing {skill}: an index file exists ({os.path.basename(stray[0])}); "
                  "delete it and link its targets from SKILL.md instead", file=sys.stderr)
            return 1

        flat = sorted(f for f in glob.glob(os.path.join(d, "*.md"))
                      if os.path.basename(f) != "SKILL.md")
        if not flat:
            continue

        names = {os.path.basename(f) for f in flat}
        for f in flat:
            dst = os.path.join(d, "references", os.path.basename(f))
            print(f"  {'mv' if args.apply else '--'} {os.path.relpath(f, REPO)} -> references/")
            move(f, dst, args.apply)
            moved += 1

        text = open(skill_md, encoding="utf-8").read()

        def repoint(m: re.Match) -> str:
            label, target = m.group(1), m.group(2)
            if os.path.basename(target) in names and "/" not in target:
                return f"[{label}](references/{target})"
            return m.group(0)

        new = LINK.sub(repoint, text)
        if new != text:
            relinked += 1
            if args.apply:
                open(skill_md, "w", encoding="utf-8").write(new)

    print(f"\n{moved} reference(s) moved, {relinked} SKILL.md relinked"
          f"{'' if args.apply else ' (dry run: nothing written)'}")

    if args.apply:
        bad = 0
        for skill_md in sorted(glob.glob(os.path.join(root, "*", "SKILL.md"))):
            d = os.path.dirname(skill_md)
            for _, target in LINK.findall(open(skill_md, encoding="utf-8").read()):
                if not os.path.exists(os.path.join(d, target)):
                    print(f"  broken link: {os.path.relpath(skill_md, REPO)} -> {target}",
                          file=sys.stderr)
                    bad += 1
        print("every link resolves" if not bad else f"{bad} broken link(s)")
        return 1 if bad else 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
