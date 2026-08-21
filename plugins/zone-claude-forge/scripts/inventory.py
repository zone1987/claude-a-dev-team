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
import urllib.parse

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
    """Fetch a URL with curl, following redirects (SOURCE-03).

    curl carries the system trust store and follows redirects, which is what documentation hosts
    require: urllib raised CERTIFICATE_VERIFY_FAILED on every docs.ventrata.com page and handed
    back a 301 HTML page instead of docs.contao.org's sitemap, which reads as an absent source
    rather than an error.
    """
    out = subprocess.run(["curl", "-sSfL", "--max-time", "30",
                          "-H", "User-Agent: zcf-inventory", url], capture_output=True)
    if out.returncode:
        raise OSError((out.stderr or b"").decode()[:80] or f"curl exit {out.returncode}")
    return out.stdout


SITEMAP_PATHS = ("/sitemap-pages.xml", "/sitemap.xml", "/sitemap_index.xml", "/docs/sitemap.xml")


def docs_hosts(plugin: str) -> list[str]:
    """The documentation hosts a plugin cites in its SKILL.md Source sections.

    A repository or registry is not documentation to enumerate, so those hosts are excluded:
    a plugin resting only on a pinned repo needs no inventory (COV-09).
    """
    seen: dict[str, int] = {}
    for sm in sorted(glob.glob(os.path.join(PLUGINS, plugin, "skills", "*", "SKILL.md"))):
        text = open(sm, encoding="utf-8", errors="replace").read()
        at = text.find("## Source")
        if at < 0:
            continue
        for host in re.findall(r"https?://([A-Za-z0-9.-]+)", text[at:]):
            if host.endswith(("github.com", "gitlab.com", "github.io", "npmjs.com")):
                continue
            seen[host] = seen.get(host, 0) + 1
    return [h for h, _ in sorted(seen.items(), key=lambda kv: -kv[1])]


def find_sitemap(host: str) -> tuple[str, list[str]]:
    """Locate a sitemap for a host and return it with the page URLs it lists.

    robots.txt is consulted first, since a site that keeps its sitemap off the conventional
    paths still declares it there — docs.contao.org publishes two, one per documentation set.
    """
    candidates = []
    try:
        robots = fetch(f"https://{host}/robots.txt").decode("utf-8", "replace")
        candidates += re.findall(r"(?im)^\s*Sitemap:\s*(\S+)", robots)
    except OSError:
        pass
    candidates += [f"https://{host}{p}" for p in SITEMAP_PATHS]

    merged: list[str] = []
    first = ""
    for url in candidates:
        try:
            xml = fetch(url).decode("utf-8", "replace")
        except OSError:
            continue
        locs = re.findall(r"<loc>([^<]+)</loc>", xml)
        nested = [u for u in locs if u.endswith(".xml")]
        if nested and not [u for u in locs if not u.endswith(".xml")]:
            pages: list[str] = []
            for sub in nested:
                try:
                    pages += re.findall(r"<loc>([^<]+)</loc>",
                                        fetch(sub).decode("utf-8", "replace"))
                except OSError:
                    continue
            locs = [u for u in pages if not u.endswith(".xml")]
        if locs:
            first = first or url
            merged += locs
            if url not in [f"https://{host}{p}" for p in SITEMAP_PATHS]:
                continue          # robots may list several; take them all
            break
    if merged:
        return first, sorted(set(merged))
    return "", []


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


def do_init(plugin: str, today: str, host_override: str, prefix: str = "") -> int:
    """Create an inventory from scratch: find the sitemap, hash every page, record coverage."""
    hosts = [host_override] if host_override else docs_hosts(plugin)
    if not hosts:
        print(f"{plugin}: no documentation host cited in any SKILL.md Source section, so no "
              f"inventory is required (COV-09)")
        return 0

    for host in hosts:
        sitemap, urls = find_sitemap(host)
        if urls:
            break
    else:
        print(f"{plugin}: cited {hosts[0]} but no sitemap was reachable at "
              f"{', '.join(SITEMAP_PATHS)}; record the page list by hand", file=sys.stderr)
        return 1

    if prefix:
        kept = [u for u in urls if u.startswith(prefix)]
        print(f"  {len(kept)} of {len(urls)} pages match {prefix}")
        urls = kept
        if not urls:
            print(f"{plugin}: no page matches {prefix}", file=sys.stderr)
            return 1

    entries, unreachable = [], 0
    for url in urls:
        u = url.rstrip("/")
        target = u + ".md" if urllib.parse.urlparse(u).path.strip("/") else u + "/index.md"
        try:
            body = fetch(target)
        except OSError:
            try:
                body = fetch(u)                     # a site that serves no .md variant
            except OSError:
                unreachable += 1
                continue
        entries.append({"page": url, "sha256": sha(body), "covers": [], "terms": None,
                        "extracted": today})

    out = {
        "$comment": "Documentation inventory. Read this before re-auditing: an identical page "
                    "hash proves the page has not changed, whatever the date says (COV-10).",
        "plugin": plugin,
        "recorded": today,
        "source": {"documentation": prefix or f"https://{host}", "sitemap": sitemap,
                   "base": f"https://{host}/",
                   **({"scope": prefix} if prefix else {})},
        "pages": len(entries),
        "urls": [e["page"] for e in entries],
        "entries": entries,
    }
    if unreachable:
        out["unreachable"] = unreachable
    path = os.path.join(PLUGINS, plugin, NAME)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    print(f"{plugin}: {len(entries)} pages from {sitemap}"
          + (f", {unreachable} unreachable" if unreachable else ""))
    print(f"  wrote {os.path.relpath(path, REPO)} — 'covers' and 'terms' stay empty until a "
          f"coverage audit fills them (COV-08)")
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
        except OSError as exc:
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
    ap.add_argument("--init", action="store_true",
                    help="create an inventory: find the sitemap, hash every page")
    ap.add_argument("--host", default="", help="with --init: override the documentation host")
    ap.add_argument("--prefix", default="",
                    help="with --init: keep only pages whose URL starts with this, for a plugin "
                         "covering one section of a larger docs site")
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
    if args.init:
        return do_init(args.plugin, args.today, args.host, args.prefix)
    if args.check:
        return do_check(args.plugin, args.fetch, args.today)
    ap.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
