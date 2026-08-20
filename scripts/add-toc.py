#!/usr/bin/env python3
"""Add a table of contents to reference files over 100 lines.

The authoring guidance calls for one on any reference file past 100 lines: without it a reader
has to scroll to learn what a long file even contains. Inserted after the intro paragraph, so
the file still opens with what it is about.

Usage:
    add-toc.py --plugin shopware-merchant [--limit 100] [--check]
"""
from __future__ import annotations

import argparse
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def anchor(heading: str) -> str:
    a = heading.lower().replace("`", "")
    a = re.sub(r"[^\w\s-]", "", a)
    return re.sub(r"\s+", "-", a.strip())


def add(path: str, limit: int, check: bool) -> bool:
    text = open(path, encoding="utf-8").read()
    if text.count("\n") + 1 <= limit or "## Contents" in text:
        return False
    heads = [h for h in re.findall(r"^##\s+(.+)$", text, re.M) if h.strip() != "Contents"]
    if len(heads) < 3:
        return False  # a short section list is noise, not navigation
    toc = ["## Contents", ""] + [f"- [{h}](#{anchor(h)})" for h in heads] + [""]

    lines = text.split("\n")
    # After the H1 and its following prose, before the first H2.
    insert = next((i for i, l in enumerate(lines) if l.startswith("## ")), len(lines))
    if check:
        return True
    out = lines[:insert] + toc + lines[insert:]
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out))
    return True


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--plugin", required=True)
    ap.add_argument("--limit", type=int, default=100)
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    files = [f for f in glob.glob(
        os.path.join(ROOT, "plugins", args.plugin, "skills", "*", "*.md"))
        if not f.endswith("SKILL.md")]
    done = sum(1 for f in sorted(files) if add(f, args.limit, args.check))
    still = sum(1 for f in files
                if (lambda t: t.count("\n") > args.limit and "## Contents" not in t)
                (open(f, encoding="utf-8").read()))
    verb = "would add" if args.check else "added"
    print(f"{verb} a table of contents to {done} file(s); "
          f"{still} file(s) over {args.limit} lines still without one "
          f"(fewer than 3 sections)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
