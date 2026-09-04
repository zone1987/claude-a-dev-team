#!/usr/bin/env python3
"""Generate the registry reference files from reui.io/r/registry.json.

No model sits between the registry and the reference files: the free/premium split,
the item names and the dependency lists are read from the document itself.

  python3 gen_registry_refs.py --registry <path to registry.json> --out <plugin dir>
"""
import argparse, collections, hashlib, json, pathlib, re, sys

FREE_UI = 'registry:ui'
FREE_HOOK = 'registry:hook'
BLOCK = 'registry:block'

GROUP_TITLES = {
    'application': 'Application',
    'data-grid': 'Data Grid',
    'solutions': 'Solutions',
    'ecommerce': 'eCommerce',
    'marketing': 'Marketing',
    'ai-agents': 'AI & Agents',
}


def family(name):
    """c-alert-dialog-3 -> alert-dialog; app-shell-12 -> app-shell."""
    return re.sub(r'-\d+$', '', name[2:] if name.startswith('c-') else name)


def load(path):
    raw = pathlib.Path(path).read_bytes()
    return json.loads(raw), hashlib.sha256(raw).hexdigest()


def reui_deps(item):
    """Registry dependencies that resolve inside the @reui namespace."""
    return sorted({d for d in item.get('registryDependencies', []) if d.startswith('@reui/')})


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)
    return path


def header(title, digest, count):
    return (f'# {title}\n\n'
            f'Generated from `https://reui.io/r/registry.json` '
            f'(sha256 `{digest[:16]}`) by `scripts/gen_registry_refs.py`. '
            f'{count} entries. Do not edit by hand.\n')


def gen_primitives(items, digest, out):
    ui = sorted((i for i in items if i['type'] in (FREE_UI, FREE_HOOK)), key=lambda i: i['name'])
    fams = collections.defaultdict(list)
    for i in ui:
        fams[family(i['name'])].append(i)
    lines = [header('ReUI primitives and hooks — free, no licence', digest, len(ui)),
             '\nEvery entry installs with `shadcn add @reui/<name>` and needs no `REUI_LICENSE_KEY`.\n',
             '\n| Item | Type | npm dependencies | @reui registry dependencies |',
             '\n|---|---|---|---|\n']
    for i in ui:
        deps = ', '.join(f'`{d}`' for d in i.get('dependencies', [])) or '—'
        rdeps = ', '.join(f'`{d}`' for d in reui_deps(i)) or '—'
        lines.append(f'| `{i["name"]}` | {i["type"].split(":")[1]} | {deps} | {rdeps} |\n')
    lines.append('\n## Files per component family\n\n'
                 'Installing the family root pulls its parts in as registry dependencies.\n\n')
    for fam in sorted(fams):
        parts = [i['name'] for i in fams[fam]]
        lines.append(f'- **{fam}** ({len(parts)}): ' + ', '.join(f'`{p}`' for p in parts) + '\n')
    return write(out / 'PRIMITIVES.md', ''.join(lines))


def gen_examples(items, digest, out):
    ex = sorted((i for i in items if i['type'] == BLOCK and not i.get('meta', {}).get('group')),
                key=lambda i: i['name'])
    fams = collections.defaultdict(list)
    for i in ex:
        fams[family(i['name'])].append(i['name'])
    lines = [header('Free component examples (c-*)', digest, len(ex)),
             '\nFree, no licence key. Install one and read the files it adds — that is the fastest\n'
             'correct composition to copy.\n\n',
             f'{len(fams)} families.\n\n',
             '| Family | Count | Items |\n|---|---|---|\n']
    for fam in sorted(fams):
        names = sorted(fams[fam], key=lambda n: (len(n), n))
        lines.append(f'| `{fam}` | {len(names)} | ' + ', '.join(f'`{n}`' for n in names) + ' |\n')
    return write(out / 'EXAMPLES-FREE.md', ''.join(lines))


def gen_blocks(items, digest, out):
    pro = [i for i in items if i.get('meta', {}).get('group')]
    groups = collections.defaultdict(list)
    for i in pro:
        groups[i['meta']['group']].append(i)
    written = []
    index = [header('Premium blocks — Pro or Ultimate licence required', digest, len(pro)),
             '\nEvery block below needs a valid `REUI_LICENSE_KEY` at install time. Free items\n'
             'keep working through the same `@reui` namespace.\n\n',
             '| Group | Blocks | Reference |\n|---|---|---|\n']
    for g in sorted(groups):
        fname = f'BLOCKS-{g.upper().replace("-", "-")}.md'
        index.append(f'| {GROUP_TITLES.get(g, g)} | {len(groups[g])} | '
                     f'[{fname}]({fname}) |\n')
        fams = collections.defaultdict(list)
        for i in groups[g]:
            fams[family(i['name'])].append(i)
        body = [header(f'Premium blocks — {GROUP_TITLES.get(g, g)}', digest, len(groups[g])),
                '\n**Licence: Pro or Ultimate.** Install with '
                '`shadcn add @reui/<name>` once `REUI_LICENSE_KEY` is set.\n']
        for fam in sorted(fams):
            entries = sorted(fams[fam], key=lambda i: (len(i['name']), i['name']))
            body.append(f'\n## {fam} ({len(entries)})\n\n')
            for i in entries:
                title = i.get('title') or fam
                body.append(f'### `{i["name"]}`\n\n{title}\n\n')
                desc = (i.get('description') or '').strip()
                if desc:
                    body.append(f'{desc}\n\n')
                rd = reui_deps(i)
                if rd:
                    body.append('Uses: ' + ', '.join(f'`{d}`' for d in rd) + '\n\n')
                dep = i.get('dependencies', [])
                if dep:
                    body.append('npm: ' + ', '.join(f'`{d}`' for d in dep) + '\n\n')
                docs = (i.get('docs') or '').strip()
                if docs:
                    body.append(docs + '\n\n')
        written.append(write(out / fname, ''.join(body)))
    written.append(write(out / 'BLOCKS-PREMIUM.md', ''.join(index)))
    return written


def gen_matrix(items, digest, out):
    ui = [i for i in items if i['type'] == FREE_UI]
    hooks = [i for i in items if i['type'] == FREE_HOOK]
    ex = [i for i in items if i['type'] == BLOCK and not i.get('meta', {}).get('group')]
    pro = [i for i in items if i.get('meta', {}).get('group')]
    groups = collections.Counter(i['meta']['group'] for i in pro)
    rows = [header('Free vs premium — what installs without a licence', digest, len(items)),
            '\nThe registry document is the authority for this split: an item carrying\n'
            '`meta.group` is a premium block, everything else in it installs free.\n\n',
            '| Tier | What | Count | Licence at install |\n|---|---|---|---|\n',
            f'| Free | primitives (`registry:ui`) | {len(ui)} | none |\n',
            f'| Free | hooks (`registry:hook`) | {len(hooks)} | none |\n',
            f'| Free | component examples (`c-*`) | {len(ex)} | none |\n',
            f'| **Pro** | premium blocks | {len(pro)} | `REUI_LICENSE_KEY` |\n',
            '| **Ultimate** | icons | 638 (2,552 variants) | `REUI_LICENSE_KEY` |\n',
            '| **Ultimate** | full-page templates | 14 | `REUI_LICENSE_KEY` |\n',
            '\nIcons and templates are not served in `registry.json`; '
            '`/r/icons.json` answers `401` without a licence, so their counts come from '
            '`llms.txt`: 638 icons in 4 styles = 2,552 installable variants. '
            '(The pricing table counts the 2,552 variants; the Introduction page\'s "562 icons" '
            'is stale.)\n'
            '\nThe 77 `registry:ui` files make up **22 documented primitives** plus the documented '
            '`file-upload` pattern — 23 documentation pages per build. A primitive ships as a '
            'family of files (`data-grid` pulls in `data-grid-pagination`, `data-grid-table`, ...), '
            'which is why the file count exceeds the component count.\n',
            '\n## Premium block groups\n\n| Group | Blocks |\n|---|---|\n']
    for g, n in sorted(groups.items(), key=lambda kv: -kv[1]):
        rows.append(f'| {GROUP_TITLES.get(g, g)} | {n} |\n')
    rows.append('\n## Telling them apart from a name\n\n'
                '- `c-<component>-<n>` — free example.\n'
                '- `<component>` with no prefix — free primitive.\n'
                '- anything else (`app-shell-3`, `hero-11`, `solution-crm-2`, '
                '`data-grid-base-1`) — premium block.\n'
                '- `@reui/icons/<default|animated>/<style>/<name>` — Ultimate icon.\n')
    return write(out / 'FREE-VS-PREMIUM.md', ''.join(rows))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--registry', required=True)
    ap.add_argument('--out', required=True, help='plugin root')
    a = ap.parse_args()
    doc, digest = load(a.registry)
    items = doc['items']
    root = pathlib.Path(a.out)
    written = [gen_matrix(items, digest, root / 'skills/reui-registry/references'),
               gen_primitives(items, digest, root / 'skills/reui-registry/references'),
               gen_examples(items, digest, root / 'skills/reui-registry/references')]
    written += gen_blocks(items, digest, root / 'skills/reui-blocks/references')
    for w in written:
        if isinstance(w, list):
            continue
        print(f'{w.stat().st_size:9} {w}')
    print(f'\nregistry sha256 {digest}')
    print(f'{len(items)} items')


if __name__ == '__main__':
    main()
