#!/usr/bin/env python3
"""Record a carried documentation page: verify coverage, update INVENTORY.json and the checklist.

One page is only done when its identifier coverage is 100 percent (COV-11), its hash is recorded
(COV-09) and the checklist entry is ticked. Doing all three in one command is what keeps them from
drifting apart.

    record_page.py --plugin P --slug guides/... --covers skills/x/references/Y.md [...]
"""
from __future__ import annotations

import argparse
import collections
import hashlib
import json
import os
import subprocess
import sys

PLUGIN_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(os.path.dirname(PLUGIN_DIR))
PLUGINS = os.path.join(REPO, os.path.basename(os.path.dirname(PLUGIN_DIR)))
MIRROR = ('/private/tmp/claude-501/-Users-andreasgerhardt-Projekte-Claude-Plugins/'
          'bd3fc95d-db20-47fe-8904-38993f670a97/scratchpad/swdev')
CHECKLIST = os.path.join(PLUGIN_DIR, 'SHOPWARE-DOCS-CHECKLIST.json')
BASE = 'https://developer.shopware.com/docs/'


def mirror_path(slug: str) -> str:
    return os.path.join(MIRROR, slug.replace('/', '_').replace('.html', '') + '.html')


def coverage(slug: str, plugin: str) -> tuple[int, list[str]]:
    out = subprocess.run(
        ['python3', os.path.join(PLUGIN_DIR, 'scripts', 'page_coverage.py'),
         mirror_path(slug), os.path.join(PLUGINS, plugin, 'skills/*/references/*.md')],
        capture_output=True, text=True, cwd=REPO)
    text = out.stdout.strip()
    pct = int(text.split('%')[0]) if '%' in text else 0
    missing = []
    if 'missing:' in text:
        missing = [x.strip(" '[]") for x in text.split('missing:')[1].split(',')]
    return pct, missing


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--plugin', required=True)
    ap.add_argument('--slug', required=True, help='path under /docs/, with or without .html')
    ap.add_argument('--covers', nargs='+', required=True,
                    help='plugin-relative reference files carrying the page')
    ap.add_argument('--date', default='2026-08-21')
    ap.add_argument('--force', action='store_true', help='record even below 100 percent coverage')
    args = ap.parse_args()

    slug = args.slug[:-5] if args.slug.endswith('.html') else args.slug
    f = mirror_path(slug)
    if not os.path.exists(f):
        print(f'not mirrored: {f}', file=sys.stderr)
        return 2

    pct, missing = coverage(slug, args.plugin)
    if pct < 100 and not args.force:
        print(f'{pct}% coverage — {len(missing)} identifier(s) still absent: {missing[:8]}',
              file=sys.stderr)
        print('COV-11 wants 100 percent. Carry them, or pass --force with a reason.', file=sys.stderr)
        return 1

    inv_path = os.path.join(PLUGINS, args.plugin, 'INVENTORY.json')
    url = BASE + slug + '.html'
    if os.path.exists(inv_path):
        inv = json.load(open(inv_path), object_pairs_hook=collections.OrderedDict)
    else:
        inv = collections.OrderedDict([
            ('$comment', 'Documentation inventory. Read before re-auditing: an identical page hash '
                         'proves the page has not changed, whatever the date says (COV-10).'),
            ('plugin', args.plugin), ('recorded', args.date),
            ('source', {'documentation': BASE, 'sitemap': 'https://developer.shopware.com/sitemap.xml',
                        'base': BASE, 'version': '6.7'}),
            ('pages', 0), ('urls', []), ('entries', [])])

    sha = hashlib.sha256(open(f, 'rb').read()).hexdigest()
    entry = {'page': url, 'sha256': sha, 'covers': args.covers, 'extracted': args.date}
    inv['entries'] = [e for e in inv['entries'] if e['page'] != url] + [entry]
    inv['urls'] = sorted({e['page'] for e in inv['entries']})
    inv['pages'] = len(inv['entries'])
    inv['recorded'] = args.date
    with open(inv_path, 'w') as fh:
        json.dump(inv, fh, indent=1)
        fh.write('\n')

    d = json.load(open(CHECKLIST))
    hit = False
    for i in d['items']:
        if i['slug'] == slug + '.html':
            i['status'] = 'done'
            hit = True
    if hit:
        with open(CHECKLIST, 'w') as fh:
            json.dump(d, fh, indent=1)
    done = sum(1 for i in d['items'] if i['status'] == 'done')

    print(f'{pct}% · {args.plugin} INVENTORY.json now {inv["pages"]} pages · '
          f'checklist {done}/{d["pages"]}' + ('' if hit else ' · WARNING: slug not in checklist'))
    return 0


if __name__ == '__main__':
    sys.exit(main())
