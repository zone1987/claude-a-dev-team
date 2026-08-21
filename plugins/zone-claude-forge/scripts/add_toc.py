#!/usr/bin/env python3
"""Give every reference file over 100 lines a table of contents (TOC-01).

Two details decide whether the block actually works. It must sit inside the first 20 lines,
which is the window the validator reads and roughly what a partial read shows, so it goes
directly after the intro paragraph rather than before the first section. And headings inside
fenced code blocks are not headings: a shell comment starting with ## would otherwise become
a phantom entry.

    add_toc.py [--plugin P] [--apply]
"""
from __future__ import annotations

import argparse
import glob
import os
import re
import sys

PLUGIN_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(os.path.dirname(PLUGIN_DIR))
PLUGINS = os.path.join(REPO, os.path.basename(os.path.dirname(PLUGIN_DIR)))
MIN_LINES = 100
MIN_SECTIONS = 3
WINDOW = 20


def slug(heading: str) -> str:
    """GitHub's anchor form: lowercase, punctuation dropped, spaces to hyphens."""
    s = re.sub(r"`|\*\*|\*|_", "", heading).strip().lower()
    s = re.sub(r"[^\w\s-]", "", s)
    return re.sub(r"\s+", "-", s)


def sections(lines: list[str]) -> list[tuple[int, str]]:
    out, fenced = [], False
    for i, ln in enumerate(lines):
        if ln.lstrip().startswith("```"):
            fenced = not fenced
            continue
        if not fenced and ln.startswith("## "):
            out.append((i, ln[3:].strip()))
    return out


def insert_at(lines: list[str], first_section: int) -> int:
    """After the intro paragraph, and never past the validator's window.

    Landing before the first section keeps the block above the content it indexes; capping at
    WINDOW - 2 keeps it inside the lines the validator and a partial read actually see.
    """
    # Directly before the first section, unless that sits past the window: an intro can run to
    # several short paragraphs (a route line, a note), and splitting it reads as a mistake.
    if first_section <= WINDOW - 2:
        return first_section
    i = 1
    while i < len(lines) and not lines[i].strip():      # blank lines after the H1
        i += 1
    while i < len(lines) and lines[i].strip():          # the first paragraph
        i += 1
    return max(1, min(i, WINDOW - 2))


def process(path: str, apply: bool) -> str:
    text = open(path, encoding="utf-8").read()
    lines = text.splitlines()
    if len(lines) <= MIN_LINES:
        return ""
    secs = [(i, h) for i, h in sections(lines) if h.lower() != "contents"]
    if len(secs) < MIN_SECTIONS:
        return ""
    if any("contents" in ln.lower() for ln in lines[:WINDOW]):
        return ""

    at = insert_at(lines, secs[0][0])
    block = ["## Contents", ""] + [f"- [{h}](#{slug(h)})" for _, h in secs] + [""]
    if lines[at - 1].strip():
        block = [""] + block
    if apply:
        open(path, "w", encoding="utf-8").write("\n".join(lines[:at] + block + lines[at:]) + "\n")
    return f"{os.path.relpath(path, REPO)}: {len(secs)} sections, inserted at line {at}"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--plugin", default="*")
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    done = 0
    for f in sorted(glob.glob(os.path.join(PLUGINS, args.plugin, "skills", "*",
                                           "references", "*.md"))):
        if process(f, args.apply):
            done += 1
    print(f"{done} file(s) need a table of contents" + ("" if args.apply else " (dry run)"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
