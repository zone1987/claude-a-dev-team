#!/usr/bin/env python3
"""Register a plugin's skill set in both manifests and keep them identical.

plugin.json and marketplace.json must agree: a path in one that the other lacks, or one that
points at a deleted directory, breaks plugin loading. This writes both from the directory
listing, so they cannot drift.

Usage:
    register-plugin.py --plugin shadcn --version 2.0.0 [--description "..."]
"""
from __future__ import annotations

import argparse
import collections
import glob
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--plugin", required=True)
    ap.add_argument("--version")
    ap.add_argument("--description")
    args = ap.parse_args()

    pdir = os.path.join(ROOT, "plugins", args.plugin)
    skills = sorted("./skills/" + os.path.basename(p)
                    for p in glob.glob(os.path.join(pdir, "skills", "*"))
                    if os.path.isdir(p))
    if not skills:
        print(f"error: no skills found under {pdir}", file=sys.stderr)
        return 1

    missing = [s for s in skills
               if not os.path.exists(os.path.join(pdir, s.lstrip("./"), "SKILL.md"))]
    if missing:
        print(f"error: {len(missing)} skill path(s) have no SKILL.md — not registering:",
              file=sys.stderr)
        for b in missing:
            print(f"  {b}", file=sys.stderr)
        return 1

    pj = os.path.join(pdir, ".claude-plugin", "plugin.json")
    d = json.load(open(pj, encoding="utf-8"), object_pairs_hook=collections.OrderedDict)
    d["skills"] = skills
    d["license"] = "MIT"
    if args.version:
        d["version"] = args.version
    if args.description:
        d["description"] = args.description
    # The repository is public: no private contact details, handle only.
    if isinstance(d.get("author"), dict):
        d["author"].pop("email", None)
        if d["author"].get("name") == "Andreas Gerhardt":
            d["author"] = collections.OrderedDict(
                [("name", "zone1987"), ("url", "https://github.com/zone1987")])
    with open(pj, "w", encoding="utf-8") as fh:
        json.dump(d, fh, indent=2, ensure_ascii=False)
        fh.write("\n")

    mp = os.path.join(ROOT, ".claude-plugin", "marketplace.json")
    m = json.load(open(mp, encoding="utf-8"), object_pairs_hook=collections.OrderedDict)
    hit = False
    for x in m["plugins"]:
        if x["name"] == args.plugin:
            hit = True
            x["skills"] = skills
            x["license"] = "MIT"
            if args.version:
                x["version"] = args.version
            if args.description:
                x["description"] = args.description
            if isinstance(x.get("author"), dict):
                x["author"].pop("email", None)
                if x["author"].get("name") == "Andreas Gerhardt":
                    x["author"] = collections.OrderedDict(
                        [("name", "zone1987"), ("url", "https://github.com/zone1987")])
    if not hit:
        print(f"error: {args.plugin} is not in marketplace.json", file=sys.stderr)
        return 1
    with open(mp, "w", encoding="utf-8") as fh:
        json.dump(m, fh, indent=2, ensure_ascii=False)
        fh.write("\n")

    # Check before writing: a registered path without a SKILL.md breaks plugin loading, so
    # this must refuse rather than warn.
    bad = [s for s in skills
           if not os.path.exists(os.path.join(pdir, s.lstrip("./"), "SKILL.md"))]
    if bad:
        print(f"error: {len(bad)} skill path(s) have no SKILL.md — not registering:",
              file=sys.stderr)
        for b in bad:
            print(f"  {b}", file=sys.stderr)
        return 1
    print(f"{args.plugin}: {len(skills)} skills registered in both manifests"
          + (f", version {d['version']}" if args.version else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
