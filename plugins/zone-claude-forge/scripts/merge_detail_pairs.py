#!/usr/bin/env python3
"""Merge an X.md / X-DETAIL.md pair into one reference file.

Splitting a topic by length is not progressive disclosure, it is one topic in two files: the
short one summarises, the long one repeats it in full, and every lookup costs two reads and a
decision about which file is authoritative (REF-02).

The summary is worth keeping as the lead — it is the orientation a reader wants first — so the
merge keeps it and appends the full reference below, then drops the pointer line that only
existed to bridge the two files. SKILL.md links to -DETAIL.md are removed.

    merge_detail_pairs.py --plugin P [--apply]
"""
from __future__ import annotations

import argparse
import glob
import os
import re
import subprocess
import sys

PLUGIN_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(os.path.dirname(PLUGIN_DIR))
PLUGINS = os.path.join(REPO, os.path.basename(os.path.dirname(PLUGIN_DIR)))

# The bridge between the two files: a "Further reading" section, or a bare pointer line.
POINTER = re.compile(
    r"\n#{2,4} (?:Further reading|Complete reference|Weiterlesen)\s*\n(?:[^\n]*\n)*?(?=\n#{1,4} |\Z)"
    r"|\n[^\n]*\[[^\]]*-DETAIL\.md\][^\n]*\n"
    r"|\n[^\n]*Complete reference:[^\n]*\n",
)


def demote(text: str) -> str:
    """Push every heading down one level so the detail nests under the summary."""
    return re.sub(r"^(#+) ", lambda m: "#" * (len(m.group(1)) + 1) + " ", text, flags=re.M)


def merge(base: str, detail: str) -> str:
    lead = POINTER.sub("\n", open(base, encoding="utf-8").read().rstrip()) .rstrip()
    body = demote(open(detail, encoding="utf-8").read().strip())
    return lead + "\n\n" + body + "\n"


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

    merged = 0
    for detail in sorted(glob.glob(os.path.join(root, "*", "references", "*-DETAIL.md"))):
        base = detail[: -len("-DETAIL.md")] + ".md"
        if not os.path.exists(base):
            continue
        text = merge(base, detail)

        # every heading and table row of both sources must survive
        want = [l.strip() for f in (base, detail)
                for l in open(f, encoding="utf-8").read().splitlines()
                if (l.startswith("|") and not l.startswith("|--")) or l.startswith("#")]
        lost = [l for l in want
                if l.lstrip("#").strip() not in text and l not in text]
        if lost:
            print(f"ABORT: {os.path.relpath(base, REPO)} would lose {len(lost)} line(s), "
                  f"first: {lost[0][:60]}", file=sys.stderr)
            return 1

        if args.apply:
            open(base, "w", encoding="utf-8").write(text)
            subprocess.run(["git", "-C", REPO, "rm", "-q", os.path.relpath(detail, REPO)],
                           check=False)
            if os.path.exists(detail):
                os.remove(detail)
        merged += 1

    # drop the SKILL.md links that pointed at the absorbed files
    relinked = 0
    for sk in sorted(glob.glob(os.path.join(root, "*", "SKILL.md"))):
        txt = open(sk, encoding="utf-8").read()
        new = re.sub(r"\s*\[[^\]]*\]\((?:references/)?[A-Z0-9-]+-DETAIL\.md\)\.?", "", txt)
        new = re.sub(r"\n{3,}", "\n\n", new)
        if new != txt:
            relinked += 1
            if args.apply:
                open(sk, "w", encoding="utf-8").write(new)

    print(f"{args.plugin}: {merged} pair(s) merged, {relinked} SKILL.md cleaned"
          + ("" if args.apply else " (dry run)"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
