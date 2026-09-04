#!/usr/bin/env python3
"""Warn before a shadcn install of a premium @reui item that cannot succeed.

Premium blocks, icons and templates need REUI_LICENSE_KEY and the authenticated
registry form in components.json. Without them the CLI fails with a 401 after
resolving dependencies, which is a slow and confusing way to learn it.

Reports, never blocks (exit 0 on every path).
"""
import json
import os
import re
import sys

# free item shapes in the @reui namespace
FREE_EXAMPLE = re.compile(r'@reui/c-[a-z0-9-]+$')
ICON = re.compile(r'@reui/icons/')

# the free primitives, from registry.json (type registry:ui and registry:hook)
FREE_PRIMITIVES = {
    'alert', 'autocomplete', 'badge', 'cascader', 'code-block', 'data-grid',
    'date-selector', 'event-calendar', 'filters', 'frame', 'gantt', 'icon-stack',
    'icon-tile', 'kanban', 'number-field', 'phone-input', 'rating', 'scrollspy',
    'sortable', 'stepper', 'timeline', 'tree', 'file-upload',
    'use-copy-to-clipboard', 'use-file-upload', 'use-scroll-position', 'use-slider-input',
}


def premium_items(cmd):
    """@reui items in an install command that need a licence."""
    out = []
    for raw in re.findall(r'@reui/[A-Za-z0-9/_-]+', cmd):
        item = raw.rstrip('.,;')
        if FREE_EXAMPLE.match(item):
            continue
        if ICON.search(item):
            out.append((item, 'Ultimate'))
            continue
        name = item.split('/', 1)[1] if '/' in item else ''
        # a primitive, or one of its parts (data-grid-pagination -> data-grid)
        if name in FREE_PRIMITIVES or any(
                name.startswith(p + '-') for p in FREE_PRIMITIVES):
            continue
        out.append((item, 'Pro'))
    return out


def licence_configured(cwd):
    """Both halves have to be there: the key, and the authenticated registry form."""
    key = bool(os.environ.get('REUI_LICENSE_KEY'))
    if not key:
        for name in ('.env.local', '.env'):
            try:
                with open(os.path.join(cwd, name)) as fh:
                    if re.search(r'^\s*REUI_LICENSE_KEY\s*=\s*\S', fh.read(), re.M):
                        key = True
                        break
            except OSError:
                continue
    authed = False
    try:
        with open(os.path.join(cwd, 'components.json')) as fh:
            cfg = json.load(fh)
        entry = (cfg.get('registries') or {}).get('@reui')
        authed = isinstance(entry, dict) and bool(entry.get('headers'))
    except (OSError, ValueError):
        pass
    return key, authed


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0

    if (payload.get('tool_name') or '') != 'Bash':
        return 0
    cmd = ((payload.get('tool_input') or {}).get('command')) or ''
    if not isinstance(cmd, str) or '@reui/' not in cmd or 'shadcn' not in cmd:
        return 0

    items = premium_items(cmd)
    if not items:
        return 0

    cwd = payload.get('cwd') or os.getcwd()
    key, authed = licence_configured(cwd)
    if key and authed:
        return 0

    plans = sorted({p for _, p in items})
    names = ', '.join(f'`{i}`' for i, _ in items[:6])
    verb = 'needs' if len(items) == 1 else 'need'
    missing = []
    if not key:
        missing.append('`REUI_LICENSE_KEY` is not set (env or .env.local)')
    if not authed:
        missing.append('the `@reui` entry in components.json is still the plain string form, '
                       'which sends no Authorization header')

    print(json.dumps({'additionalContext':
        f'[reui] {names} {verb} a {" or ".join(plans)} licence at install, but '
        + ' and '.join(missing) + '. The install will fail with a 401 after resolving '
        'dependencies. See skills/reui-setup/references/LICENSE-SETUP.md. '
        'Free alternatives install unchanged: the primitives and every `@reui/c-*` example.'
    }))
    return 0


if __name__ == '__main__':
    sys.exit(main())
