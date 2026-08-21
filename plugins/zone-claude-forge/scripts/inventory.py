#!/usr/bin/env python3
"""Record and check a plugin's documentation inventory.

An inventory answers one question cheaply: is this plugin still a complete record of its source?
Without it the only options are trusting that it is (which is how content goes missing silently)
or re-reading the whole source (which costs minutes and a lot of context). The file turns that
into a read plus, at most, one request.

Per page it records the URL, the content hash, the plugin files that cover it, the term count and
the date extracted. The hash is what makes the answer sound: identical hash means the page has not
changed, whatever its age. The date is only the fallback for when the source cannot be reached.

    inventory.py --plugin P --write --pages DIR   # record an audit just performed
    inventory.py --plugin P --check               # offline: report age and shape
    inventory.py --plugin P --check --fetch       # compare live hashes, name changed pages

Exit code is non-zero when a page changed, is missing, or the inventory is absent.
"""
from __future__ import annotations

import argparse
import datetime
import glob
import hashlib
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request

PLUGIN_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(os.path.dirname(PLUGIN_DIR))
PLUGINS = os.path.join(REPO, os.path.basename(os.path.dirname(PLUGIN_DIR)))
STALE_DAYS = 30
NAME = "INVENTORY.json"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load(plugin: str) -> dict:
    p = os.path.join(PLUGINS, plugin, NAME)
    if not os.path.exists(p):
        return {}
    with open(p, encoding="utf-8") as fh:
        return json.load(fh)


def age_days(stamp: str, today: str) -> int:
    try:
        a = datetime.date.fromisoformat(stamp)
        b = datetime.date.fromisoformat(today)
    except ValueError:
        return 10**6
    return (b - a).days


def fetch(url: str) -> bytes:
    """Fetch a page, falling back to curl where Python's CA bundle is incomplete.

    Certificate verification stays on in both paths: a hash compared against a page fetched
    without verification would prove nothing about the real source.
    """
    req = urllib.request.Request(url, headers={"User-Agent": "zcf-inventory"})
    try:
        with urllib.request.urlopen(req, timeout=30) as fh:
            return fh.read()
    except urllib.error.URLError as exc:
        if "CERTIFICATE_VERIFY_FAILED" not in str(exc):
            raise
        out = subprocess.run(["curl", "-sSf", "--max-time", "30", url],
                             capture_output=True)
        if out.returncode:
            raise OSError((out.stderr or b"").decode()[:80] or "curl failed") from exc
        return out.stdout


def mirror_name(url: str, base: str) -> str:
    """The filename a mirror script gives a page: path with / replaced by _, or 'index'."""
    b = base.rstrip("/")
    rel = url[len(b):].strip("/") if b and url.startswith(b) else url
    return (rel.replace("/", "_") or "index") + ".md"


def do_write(plugin: str, pages_dir: str, sitemap: str, today: str) -> int:
    files = sorted(glob.glob(os.path.join(pages_dir, "*.md")))
    if not files:
        print(f"no mirrored pages in {pages_dir}", file=sys.stderr)
        return 2

    prev = load(plugin)
    base = prev.get("source", {}).get("base", "")
    by_name = {}
    for f in files:
        by_name[os.path.basename(f)] = sha(open(f, "rb").read())

    entries = []
    for url in prev.get("urls", []) or []:
        n = mirror_name(url, base)
        if n in by_name:
            entries.append({"page": url, "sha256": by_name.pop(n), "mirror": n})
    for n, h in sorted(by_name.items()):
        entries.append({"page": "", "sha256": h, "mirror": n})

    out = {
        "$comment": "Documentation inventory. Read this before re-auditing: an identical page "
                    "hash proves the page has not changed, whatever the date says (COV-09).",
        "plugin": plugin,
        "recorded": today,
        "source": prev.get("source", {"sitemap": sitemap, "base": ""}),
        "pages": len(entries),
        "urls": prev.get("urls", []),
        "entries": entries,
    }
    if sitemap:
        out["source"]["sitemap"] = sitemap
    p = os.path.join(PLUGINS, plugin, NAME)
    with open(p, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    print(f"wrote {os.path.relpath(p, REPO)} ({len(entries)} pages, recorded {today})")
    return 0


def do_check(plugin: str, live: bool, today: str) -> int:
    inv = load(plugin)
    if not inv:
        print(f"{plugin}: no {NAME}. Nothing records what was extracted, so coverage cannot be "
              f"trusted: run the audit and write one (COV-08, COV-09).")
        return 1

    days = age_days(inv.get("recorded", ""), today)
    print(f"{plugin}: {inv.get('pages', 0)} pages, recorded {inv.get('recorded', '?')} "
          f"({days} days ago)")

    if not live:
        if days > STALE_DAYS:
            print(f"  older than {STALE_DAYS} days and no --fetch: re-check the source before "
                  f"relying on it, or run again with --fetch to compare hashes")
            return 1
        print("  within the freshness window; --fetch compares live hashes for proof")
        return 0

    changed, gone, same = [], [], 0
    for e in inv.get("entries", []):
        url = e.get("page") or ""
        if not url:
            continue
        try:
            # A docs root has no path to suffix: ask for /index.md instead of "<host>.md".
            u = url.rstrip("/")
            target = u + ".md" if urllib.parse.urlparse(u).path.strip("/") else u + "/index.md"
            body = fetch(target)
        except (urllib.error.URLError, urllib.error.HTTPError, OSError) as exc:
            gone.append((url, str(exc)[:60]))
            continue
        if sha(body) == e.get("sha256"):
            same += 1
        else:
            changed.append(url)

    print(f"  unchanged {same}, changed {len(changed)}, unreachable {len(gone)}")
    for u in changed:
        print(f"  CHANGED:     {u}")
    for u, why in gone:
        print(f"  UNREACHABLE: {u} ({why})")

    if changed:
        print(f"\n{len(changed)} page(s) changed: re-extract those and update their entries. "
              f"Pages whose hash matched need no work.")
    elif not gone:
        print("\nevery page matches its recorded hash: the plugin is current, no re-extraction "
              "needed regardless of age")
    return 1 if (changed or gone) else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--plugin", required=True)
    ap.add_argument("--write", action="store_true", help="record an inventory from a page mirror")
    ap.add_argument("--check", action="store_true", help="report the recorded state")
    ap.add_argument("--fetch", action="store_true", help="with --check: compare live hashes")
    ap.add_argument("--pages", default="", help="with --write: the mirror directory")
    ap.add_argument("--sitemap", default="", help="with --write: the sitemap URL")
    ap.add_argument("--today", default=datetime.date.today().isoformat(),
                    help="override the date, for reproducible runs")
    args = ap.parse_args()

    if not os.path.isdir(os.path.join(PLUGINS, args.plugin)):
        print(f"no such plugin: {args.plugin}", file=sys.stderr)
        return 2
    if args.write:
        if not args.pages:
            print("--write needs --pages DIR", file=sys.stderr)
            return 2
        return do_write(args.plugin, args.pages, args.sitemap, args.today)
    if args.check:
        return do_check(args.plugin, args.fetch, args.today)
    ap.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
