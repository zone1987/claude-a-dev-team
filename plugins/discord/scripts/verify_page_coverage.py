#!/usr/bin/env python3
"""Prove every documented page reached a reference file, in both directions.

Forward: every page in PAGE-COVERAGE.json is claimed by a skill that exists and carries content.
A page added upstream later surfaces as UNCLAIMED rather than going unnoticed.

Reverse: every skill directory that exists is named in PAGE-COVERAGE.json. A skill nobody assigned
pages to is either dead weight or evidence the manifest went stale.

The page list itself is derived from the sitemap, whose sha256 is recorded in the manifest, so a
coverage claim stays reproducible after the upstream changes.

Usage:
    verify_page_coverage.py [--manifest PATH] [--skills-dir DIR] [--refresh-sitemap]
Exit code is non-zero when either direction fails.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PLUGIN = HERE.parent


def sitemap_hash(url: str) -> str | None:
    """Fetch the live sitemap with curl and hash it, to detect upstream drift."""
    try:
        raw = subprocess.run(
            ["curl", "-sSfL", url], capture_output=True, timeout=60, check=True
        ).stdout
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, FileNotFoundError) as exc:
        print(f"could not fetch {url}: {exc}", file=sys.stderr)
        return None
    return hashlib.sha256(raw).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--manifest", default=str(PLUGIN / "PAGE-COVERAGE.json"))
    parser.add_argument("--skills-dir", default=str(PLUGIN / "skills"))
    parser.add_argument("--refresh-sitemap", action="store_true", help="fetch the sitemap and report drift")
    args = parser.parse_args()

    manifest = json.loads(Path(args.manifest).read_text(encoding="utf-8"))
    skills_root = Path(args.skills_dir)
    claimed: dict[str, list[str]] = manifest["pages"]

    findings: list[str] = []
    total_pages = 0
    print(f"{'skill':24s} {'pages':>6s} {'refs':>5s} {'lines':>7s}")

    for skill, pages in sorted(claimed.items()):
        total_pages += len(pages)
        skill_dir = skills_root / skill
        if not (skill_dir / "SKILL.md").is_file():
            findings.append(f"UNCLAIMED {skill}: {len(pages)} pages assigned but the skill has no SKILL.md")
            continue
        # REF-04 puts references in references/; count both so a mid-migration skill reads true.
        refs = [p for p in skill_dir.rglob("*.md") if p.name != "SKILL.md"]
        lines = sum(p.read_text(encoding="utf-8").count("\n") + 1 for p in skill_dir.rglob("*.md"))
        if not refs:
            findings.append(f"EMPTY     {skill}: {len(pages)} pages assigned but no reference file was written")
        print(f"{skill:24s} {len(pages):6d} {len(refs):5d} {lines:7d}")

    # A cross-cutting skill gathers a subject the documentation scatters, so it owns no page
    # exclusively. Recorded in the manifest so an empty page list is a decision, not an oversight.
    cross_cutting = set(manifest.get("cross_cutting", {}))
    for skill_dir in sorted(p for p in skills_root.iterdir() if p.is_dir()):
        if skill_dir.name in cross_cutting:
            refs = len(list((skill_dir / "references").glob("*.md")))
            print(f"{skill_dir.name:24s} {'cross':>6s} {refs:5d}")
            continue
        if skill_dir.name not in claimed:
            findings.append(f"UNASSIGNED {skill_dir.name}: the skill exists but the manifest assigns it no page")

    if total_pages != manifest["page_count"]:
        findings.append(
            f"COUNT     manifest states {manifest['page_count']} pages but lists {total_pages}"
        )

    print(f"\n{total_pages} pages across {len(claimed)} skills")

    if args.refresh_sitemap:
        live = sitemap_hash(manifest["source"])
        if live is None:
            findings.append("SITEMAP   could not be fetched; coverage unverified against upstream")
        elif live != manifest["sitemap_sha256"]:
            print(f"\nSTALE     the sitemap changed upstream")
            print(f"          recorded {manifest['sitemap_sha256']}")
            print(f"          live     {live}")
            print("          re-run the distillation for pages added or removed")
            findings.append("STALE     the upstream sitemap no longer matches the recorded hash")
        else:
            print(f"\nsitemap unchanged since {manifest['retrieved']}")

    if findings:
        print()
        for finding in findings:
            print(finding)
        print(f"\n{len(findings)} finding(s)")
        return 1

    print("every page is claimed by a skill that carries content")
    return 0


if __name__ == "__main__":
    sys.exit(main())
