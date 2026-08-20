#!/usr/bin/env python3
"""Prove a bundling lost nothing, by comparing content against a backup of the old skills.

Names change during bundling and tables of contents are inserted, so a file-by-file hash tells
you nothing. This compares normalised content instead: frontmatter, generated tables of
contents and link targets stripped, then asks whether every source body still appears
somewhere in the result.

Usage:
    verify-bundle.py --plugin shadcn --backup /path/to/backup
"""
from __future__ import annotations

import argparse
import glob
import hashlib
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def core(text: str) -> str:
    text = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.S)        # frontmatter
    text = re.sub(r"## Contents\n\n(?:- \[.*?\]\(#.*?\)\n)+\n?", "", text)  # inserted TOC
    text = re.sub(r"`?[A-Za-z0-9_./-]*\.md`?", "", text)            # renamed links
    return " ".join(text.split())


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--plugin", required=True)
    ap.add_argument("--backup", required=True)
    ap.add_argument("--probe", type=int, default=150)
    args = ap.parse_args()

    target = os.path.join(ROOT, "plugins", args.plugin, "skills")
    blob = " ".join(core(open(f, encoding="utf-8").read())
                    for f in glob.glob(os.path.join(target, "*", "*.md")))

    def lost(paths: list[str]) -> list[str]:
        out = []
        for f in paths:
            c = core(open(f, encoding="utf-8").read())
            if c and c[: args.probe] not in blob:
                out.append(f)
        return out

    skills = sorted(glob.glob(os.path.join(args.backup, "*", "SKILL.md")))
    refs = sorted(glob.glob(os.path.join(args.backup, "*", "references", "**", "*.md"),
                            recursive=True))
    # Every non-reference file the source carried, not just assets/: examples, scripts and
    # templates are content too, and whitelisting cost four example files once already.
    assets = sorted(f for f in glob.glob(os.path.join(args.backup, "*", "*", "**", "*"),
                                         recursive=True)
                    if os.path.isfile(f) and "/references/" not in f)

    lost_s, lost_r = lost(skills), lost(refs)
    # Compare by content, not by path. Bundling deduplicates: two skills shipping the same
    # screenshot end up with one file, so a name-based count reports a loss that did not
    # happen. What matters is that every distinct byte sequence survived.
    def digest(path: str) -> str:
        return hashlib.md5(open(path, "rb").read()).hexdigest()

    have_bytes = {digest(a)
                  for a in glob.glob(os.path.join(target, "**", "*"), recursive=True)
                  if os.path.isfile(a)}
    have_assets = {os.path.basename(a)
                   for a in glob.glob(os.path.join(target, "**", "*"), recursive=True)
                   if os.path.isfile(a)}
    # A copied file may gain a topic prefix, an upper-cased name, or both — "entity-class.md"
    # can land as "EXAMPLES-ADT-SHOPWARE-DAL-ENTITY-CLASS.md". Match on the stem appearing
    # anywhere in a target name rather than on an exact hit.
    def seen(name: str) -> bool:
        stem = os.path.splitext(name)[0].upper().replace("_", "-")
        ext = os.path.splitext(name)[1].lower()
        for h in have_assets:
            hs, he = os.path.splitext(h)
            if he.lower() == ext and (hs.upper() == stem or hs.upper().endswith(stem)):
                return True
        return False

    lost_a = [a for a in assets
              if digest(a) not in have_bytes and not seen(os.path.basename(a))]

    print(f"{args.plugin}")
    print(f"  skill bodies : {len(skills):4} source, {len(lost_s):3} not found")
    print(f"  references   : {len(refs):4} source, {len(lost_r):3} not found")
    print(f"  other files  : {len(assets):4} source, {len(lost_a):3} not found")
    for f in (lost_s + lost_r + lost_a)[:8]:
        print(f"    missing: {f.replace(args.backup + '/', '')}")

    deep = glob.glob(os.path.join(target, "*", "*", "**", "*.md"), recursive=True)
    print(f"  depth > 2    : {len(deep):4}")
    print(f"  result       : {len(glob.glob(os.path.join(target, '*')))} domains, "
          f"{len(glob.glob(os.path.join(target, '*', '*.md')))} md files")
    return 1 if (lost_s or lost_r or lost_a or deep) else 0


if __name__ == "__main__":
    sys.exit(main())
