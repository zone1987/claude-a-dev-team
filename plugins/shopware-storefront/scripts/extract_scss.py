#!/usr/bin/env python3
"""Extract every SCSS variable, function, mixin and CSS custom property.

A theme changes appearance by overriding a variable, not by writing rules. That
only works when you know the variable exists, what it defaults to, and whether
it is Bootstrap's or Shopware's — this catalogue answers all three.

    extract_scss.py --source <vendor/shopware> --out FILE
    extract_scss.py --source <vendor/shopware> --count
"""
from __future__ import annotations

import argparse
import collections
import os
import re
import sys

import swsource

SCSS = "storefront/Resources/app/storefront/src/scss"
BOOTSTRAP = "storefront/Resources/app/storefront/node_modules/bootstrap/scss"
THEME_JSON = "storefront/Resources/theme.json"

VAR_RE = re.compile(r"^(\$[\w-]+):\s*(.+?)(?:\s*!default)?\s*;\s*$", re.M)
DEFAULT_RE = re.compile(r"!default\s*;\s*$", re.M)
FUNC_RE = re.compile(r"^@function\s+([\w-]+)\s*\((.*?)\)", re.M)
MIXIN_RE = re.compile(r"^@mixin\s+([\w-]+)\s*(?:\((.*?)\))?", re.M)
CSSVAR_RE = re.compile(r"--(?:#\{\$prefix\}|[\w-]+)[\w-]*:\s*[^;]+;")
CSSVAR_NAME_RE = re.compile(r"(--(?:#\{\$prefix\})?[\w-]+):\s*([^;]+);")


def scan(root: str):
    """Return variables, functions, mixins and custom properties per file."""
    variables, functions, mixins, cssvars = [], [], [], []
    if not os.path.isdir(root):
        return variables, functions, mixins, cssvars
    for dirpath, _dirs, files in os.walk(root):
        for name in sorted(files):
            if not name.endswith(".scss"):
                continue
            full = os.path.join(dirpath, name)
            rel = os.path.relpath(full, root).replace(os.sep, "/")
            with open(full, encoding="utf-8", errors="replace") as handle:
                text = handle.read()
            for match in VAR_RE.finditer(text):
                line_end = text[match.start():match.end()]
                variables.append(
                    {
                        "name": match.group(1),
                        "value": " ".join(match.group(2).split())[:70],
                        "file": rel,
                        "overridable": "!default" in line_end,
                    }
                )
            for match in FUNC_RE.finditer(text):
                functions.append(
                    {"name": match.group(1),
                     "args": " ".join(match.group(2).split())[:60], "file": rel}
                )
            for match in MIXIN_RE.finditer(text):
                mixins.append(
                    {"name": match.group(1),
                     "args": " ".join((match.group(2) or "").split())[:60], "file": rel}
                )
            for match in CSSVAR_NAME_RE.finditer(text):
                cssvars.append(
                    {"name": match.group(1), "value": " ".join(match.group(2).split())[:50],
                     "file": rel}
                )
    return variables, functions, mixins, cssvars


def dedupe(entries, key="name"):
    """Keep the first definition of each name, in file order."""
    seen, out = set(), []
    for entry in entries:
        if entry[key] in seen:
            continue
        seen.add(entry[key])
        out.append(entry)
    return out


def theme_fields(source: str):
    """Return the theme.json config fields; each becomes an SCSS variable."""
    import json

    path = os.path.join(source, THEME_JSON)
    if not os.path.isfile(path):
        return {}
    with open(path, encoding="utf-8") as handle:
        data = json.load(handle)
    return data.get("config", {}).get("fields", {})


def render(source: str) -> list[str]:
    sw_vars, sw_funcs, sw_mixins, sw_css = scan(os.path.join(source, SCSS))
    bs_vars, bs_funcs, bs_mixins, bs_css = scan(os.path.join(source, BOOTSTRAP))
    fields = theme_fields(source)

    sw_vars = dedupe(sw_vars)
    bs_vars = dedupe(bs_vars)
    sw_funcs, bs_funcs = dedupe(sw_funcs), dedupe(bs_funcs)
    sw_mixins, bs_mixins = dedupe(sw_mixins), dedupe(bs_mixins)
    css = dedupe(bs_css + sw_css)

    lines = [swsource.stamp("extract_scss.py", source, SCSS), ""]
    lines.append("# Shopware Storefront — SCSS variables, functions and mixins")
    lines.append("")
    lines.append(
        "Everything a theme can override without writing a single rule. Change a variable and it "
        "reaches every component that derives from it; write a rule and you have changed one place."
    )
    lines.append("")
    lines.append(
        f"**{len(bs_vars)} Bootstrap variables, {len(sw_vars)} Shopware variables, "
        f"{len(css)} CSS custom properties, {len(bs_funcs) + len(sw_funcs)} functions, "
        f"{len(bs_mixins) + len(sw_mixins)} mixins, {len(fields)} theme configuration fields.**"
    )
    lines.append("")
    lines += swsource.toc(
        [
            "How to override a variable",
            "Theme configuration fields",
            "Shopware variables",
            "Bootstrap variables",
            "CSS custom properties",
            "Functions",
            "Mixins",
        ]
    )

    lines.append("## How to override a variable")
    lines.append("")
    lines.append(
        "A variable declared with `!default` takes your value if you set it **before** the file "
        "that declares it is imported. In a theme that means your own SCSS entry point, which the "
        "theme compiler loads ahead of the Storefront's:"
    )
    lines.append("")
    lines.append("```scss")
    lines.append("// <your-theme>/src/Resources/app/storefront/src/scss/overrides.scss")
    lines.append("$primary: #c81e1e;")
    lines.append("$border-radius: 0;")
    lines.append("$container-max-widths: (sm: 540px, md: 720px, lg: 960px, xl: 1320px);")
    lines.append("```")
    lines.append("")
    lines.append(
        "Declare it in `theme.json` under `style`, before `@Storefront`. A variable **without** "
        "`!default` is not meant to be overridden this way — assign to it after the import, or "
        "change the rule that uses it."
    )
    lines.append("")
    lines.append(
        "Three reasons a variable override appears to do nothing: it was set after the declaring "
        "import; the value is also fixed by a `skin/` file later in the cascade; or the component "
        "reads a `--bs-*` custom property at runtime, which a compile-time variable no longer "
        "controls. In the last case set the custom property instead."
    )
    lines.append("")

    lines.append("## Theme configuration fields")
    lines.append("")
    lines.append(
        "Declared in `theme.json`, editable in the administration, and injected as SCSS variables "
        "of the same name. Prefer these over hard-coded values for anything a shop owner might "
        "change."
    )
    lines.append("")
    lines.append("| Field | Type | Default | Tab |")
    lines.append("|---|---|---|---|")
    for name in sorted(fields):
        field = fields[name]
        lines.append(
            f"| `${name}` | {field.get('type', '—')} | "
            f"`{field.get('value', '—')}` | {field.get('block', '—')} |"
        )
    lines.append("")
    lines.append(
        "Read them in Twig with `theme_config('sw-color-brand-primary')`, and in SCSS as `$sw-color-brand-primary`."
    )
    lines.append("")

    lines.append("## Shopware variables")
    lines.append("")
    lines.append(
        "Declared under `src/scss/abstract/variables/` and in the component files. `overridable` "
        "means the declaration carries `!default`."
    )
    lines.append("")
    lines.append("| Variable | Default | Overridable | File |")
    lines.append("|---|---|---|---|")
    for entry in sorted(sw_vars, key=lambda e: e["name"]):
        lines.append(
            f"| `{entry['name']}` | `{entry['value']}` | "
            f"{'yes' if entry['overridable'] else 'no'} | `{entry['file']}` |"
        )
    lines.append("")

    lines.append("## Bootstrap variables")
    lines.append("")
    lines.append(
        "From the vendored Bootstrap. Grouped by the file that declares them, which is also how "
        "the upstream documentation is organised."
    )
    lines.append("")
    by_file = collections.defaultdict(list)
    for entry in bs_vars:
        by_file[entry["file"]].append(entry)
    for path in sorted(by_file):
        lines.append(f"### {path}")
        lines.append("")
        lines.append("| Variable | Default | Overridable |")
        lines.append("|---|---|---|")
        for entry in sorted(by_file[path], key=lambda e: e["name"]):
            lines.append(
                f"| `{entry['name']}` | `{entry['value']}` | "
                f"{'yes' if entry['overridable'] else 'no'} |"
            )
        lines.append("")

    lines.append("## CSS custom properties")
    lines.append("")
    lines.append(
        "Emitted at runtime, so they can be changed per element, per media query or from "
        "JavaScript — unlike an SCSS variable, which is fixed at compile time. `#{$prefix}` "
        "resolves to `bs-`, so `--#{$prefix}body-color` reaches the page as `--bs-body-color`."
    )
    lines.append("")
    lines.append("| Property | Value | File |")
    lines.append("|---|---|---|")
    for entry in sorted(css, key=lambda e: e["name"]):
        lines.append(f"| `{entry['name']}` | `{entry['value']}` | `{entry['file']}` |")
    lines.append("")

    lines.append("## Functions")
    lines.append("")
    lines.append("| Function | Arguments | File | Source |")
    lines.append("|---|---|---|---|")
    for entry in sorted(sw_funcs, key=lambda e: e["name"]):
        lines.append(f"| `{entry['name']}()` | `{entry['args']}` | `{entry['file']}` | Shopware |")
    for entry in sorted(bs_funcs, key=lambda e: e["name"]):
        lines.append(f"| `{entry['name']}()` | `{entry['args']}` | `{entry['file']}` | Bootstrap |")
    lines.append("")

    lines.append("## Mixins")
    lines.append("")
    lines.append(
        "Include with `@include <name>(<args>)`. `media-breakpoint-up` and `media-breakpoint-down` "
        "are the ones a theme uses most — they keep responsive rules on the same breakpoints as "
        "the grid."
    )
    lines.append("")
    lines.append("| Mixin | Arguments | File | Source |")
    lines.append("|---|---|---|---|")
    for entry in sorted(sw_mixins, key=lambda e: e["name"]):
        lines.append(f"| `{entry['name']}` | `{entry['args']}` | `{entry['file']}` | Shopware |")
    for entry in sorted(bs_mixins, key=lambda e: e["name"]):
        lines.append(f"| `{entry['name']}` | `{entry['args']}` | `{entry['file']}` | Bootstrap |")
    lines.append("")
    return lines


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    swsource.add_source_arg(parser)
    args = parser.parse_args()
    sw_vars, sw_funcs, sw_mixins, sw_css = scan(os.path.join(args.source, SCSS))
    bs_vars, bs_funcs, bs_mixins, bs_css = scan(os.path.join(args.source, BOOTSTRAP))
    if args.count:
        print(f"shopware variables = {len(dedupe(sw_vars))}")
        print(f"bootstrap variables = {len(dedupe(bs_vars))}")
        print(f"css custom properties = {len(dedupe(bs_css + sw_css))}")
        print(f"functions = {len(dedupe(sw_funcs)) + len(dedupe(bs_funcs))}")
        print(f"mixins = {len(dedupe(sw_mixins)) + len(dedupe(bs_mixins))}")
        print(f"theme fields = {len(theme_fields(args.source))}")
        return 0
    swsource.emit(render(args.source), args.out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
