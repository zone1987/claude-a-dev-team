#!/usr/bin/env python3
"""Repair links that bundling broke by renaming files.

Flattening renames files, so a link written against the old layout ("mt-number-field.md")
no longer resolves. This maps each dangling target to the file whose name ends with it and
rewrites the link. A target with no unique match is reported rather than guessed at.

Usage:
    fix-links.py --plugin shopware-migration [--check]
"""
from __future__ import annotations

import argparse
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LINK = re.compile(r"\]\((?!https?:)([A-Za-z][\w.-]*\.md)\)")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--plugin", required=True)
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    base = os.path.join(ROOT, "plugins", args.plugin, "skills")
    fixed = unresolved = 0
    for skill in sorted(glob.glob(os.path.join(base, "*"))):
        if not os.path.isdir(skill):
            continue
        names = {os.path.basename(f) for f in glob.glob(os.path.join(skill, "*.md"))}
        upper = {n.upper(): n for n in names}
        for path in sorted(glob.glob(os.path.join(skill, "*.md"))):
            text = open(path, encoding="utf-8").read()

            def repl(m: re.Match) -> str:
                nonlocal fixed, unresolved
                target = m.group(1)
                if target in names:
                    return m.group(0)
                want = target.upper().replace("_", "-")
                # The renamed file ends with the old name, prefixed by its topic.
                hits = [n for u, n in upper.items() if u.endswith(want)]
                if len(hits) == 1:
                    fixed += 1
                    return f"]({hits[0]})"
                if len(hits) > 1:
                    # Several topics own a file with this name — SELECT-SOURCE.md,
                    # TABS-SOURCE.md. A sibling link means the one belonging to the same
                    # topic as the file we are editing, so prefer that prefix.
                    # Try the longest topic first: BUTTON-GROUP-INSTALLATION.md belongs to
                    # topic BUTTON-GROUP, not BUTTON, and both exist here.
                    # BUTTON-INSTALLATION.md wants BUTTON-SOURCE.md. Match the exact
                    # name topic+target, not a prefix: a prefix test also accepts
                    # BUTTON-GROUP-SOURCE.md and then two candidates look ambiguous.
                    parts = os.path.splitext(os.path.basename(path))[0].upper().split("-")
                    for cut in range(len(parts) - 1, 0, -1):
                        exact = "-".join(parts[:cut]) + "-" + want
                        same = [n for n in hits if n.upper() == exact]
                        if len(same) == 1:
                            fixed += 1
                            return f"]({same[0]})"
                unresolved += 1
                return m.group(0)

            new = LINK.sub(repl, text)
            if new != text and not args.check:
                with open(path, "w", encoding="utf-8") as fh:
                    fh.write(new)
    verb = "would repair" if args.check else "repaired"
    print(f"{args.plugin}: {verb} {fixed} link(s), {unresolved} still unresolved")
    return 0


if __name__ == "__main__":
    sys.exit(main())
