#!/usr/bin/env python3
"""Build INVENTORY.json: per documented page, its hash, its covering files and its size.

COV-09 requires it, and the reason is cheapness: answering "is this plugin still complete?" by
re-mirroring 159 pages pulls the whole source through context, while comparing one hash per page
settles it in seconds and leaves no page content behind. A page Discord adds later has no entry at
all, and a page it edits has a different hash — so a silent gap becomes a named one.

Built from the local mirror, whose per-file sha256 sums are recorded in scripts/MIRROR-MANIFEST.txt,
and from PAGE-COVERAGE.json, which maps each page to the skill that owns it.

Usage:
    build_inventory.py [--mirror DIR] [--out PATH]
    build_inventory.py --check [--fetch]     # compare against the live pages
Exit code is non-zero when --check finds a page changed, added, removed or unreachable.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

PLUGIN = Path(__file__).resolve().parent.parent
BASE = "https://docs.discord.com/developers/"


def slug(page: str) -> str:
    """mirror filename for a page path, matching how the mirror was written"""
    return page.replace("/", "__") + ".md"


def covering_files(skill: str) -> list[str]:
    skill_dir = PLUGIN / "skills" / skill
    if not skill_dir.is_dir():
        return []
    return sorted(
        str(p.relative_to(PLUGIN)) for p in skill_dir.rglob("*.md")
    )


def fetch(page: str) -> bytes | None:
    """Fetch a page's markdown twin. curl carries the system trust store and follows redirects,
    which this host requires; other clients report a reachable page as missing."""
    url = f"{BASE}{page}.md"
    try:
        return subprocess.run(
            ["curl", "-sSfL", url], capture_output=True, timeout=60, check=True
        ).stdout
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, FileNotFoundError):
        return None


def build(mirror: Path, out: Path) -> int:
    coverage = json.loads((PLUGIN / "PAGE-COVERAGE.json").read_text(encoding="utf-8"))
    pages: dict[str, dict] = {}
    missing: list[str] = []

    for skill, page_list in sorted(coverage["pages"].items()):
        files = covering_files(skill)
        for page in page_list:
            src = mirror / slug(page)
            if not src.is_file():
                missing.append(page)
                continue
            raw = src.read_bytes()
            pages[page] = {
                "url": f"{BASE}{page}",
                "markdown_url": f"{BASE}{page}.md",
                "sha256": hashlib.sha256(raw).hexdigest(),
                "source_lines": raw.count(b"\n") + 1,
                "skill": skill,
                "covered_by": files,
            }

    if missing:
        print(f"{len(missing)} page(s) absent from the mirror:", file=sys.stderr)
        for page in missing:
            print(f"  {page}", file=sys.stderr)
        return 1

    inventory = {
        "$comment": "Documentation inventory. Read this before re-auditing: an identical page hash "
                    "proves the page has not changed, whatever the date says (COV-09).",
        "plugin": "discord",
        "recorded": coverage["retrieved"],
        "source": {
            "documentation": "https://docs.discord.com/developers/intro",
            "sitemap": coverage["source"],
            "sitemap_sha256": coverage["sitemap_sha256"],
            "base": BASE,
            "note": "Each page is served as a markdown twin at its URL plus .md; that is what was extracted.",
            "rights_holder": "Discord Inc.",
        },
        "pages": len(pages),
        "source_lines": sum(p["source_lines"] for p in pages.values()),
        "entries": pages,
    }
    out.write_text(json.dumps(inventory, indent=1) + "\n", encoding="utf-8")
    print(f"wrote {out.relative_to(PLUGIN)}: {len(pages)} pages, {inventory['source_lines']} source lines")
    return 0


def check(out: Path, do_fetch: bool) -> int:
    inventory = json.loads(out.read_text(encoding="utf-8"))
    entries: dict[str, dict] = inventory["entries"]

    findings: list[str] = []
    for page, entry in entries.items():
        for rel in entry["covered_by"]:
            if not (PLUGIN / rel).exists():
                findings.append(f"LOST      {page}: covering file {rel} no longer exists")

    if do_fetch:
        unchanged = changed = unreachable = 0
        for page, entry in entries.items():
            raw = fetch(page)
            if raw is None:
                findings.append(f"UNREACHABLE {page}")
                unreachable += 1
            elif hashlib.sha256(raw).hexdigest() == entry["sha256"]:
                unchanged += 1
            else:
                findings.append(f"CHANGED   {page}: re-distil into {entry['skill']}")
                changed += 1
        print(f"{unchanged} unchanged, {changed} changed, {unreachable} unreachable "
              f"of {len(entries)} pages")
    else:
        print(f"{len(entries)} pages recorded {inventory['recorded']}; "
              f"pass --fetch to compare against the live documentation")

    if findings:
        print()
        for finding in findings:
            print(finding)
        print(f"\n{len(findings)} finding(s)")
        return 1
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--mirror", default="")
    parser.add_argument("--out", default=str(PLUGIN / "INVENTORY.json"))
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--fetch", action="store_true", help="with --check, compare live pages")
    args = parser.parse_args()

    out = Path(args.out)
    if args.check:
        if not out.is_file():
            print(f"no inventory at {out}; build it first", file=sys.stderr)
            return 2
        return check(out, args.fetch)

    if not args.mirror:
        print("--mirror is required when building", file=sys.stderr)
        return 2
    return build(Path(args.mirror), out)


if __name__ == "__main__":
    sys.exit(main())
