#!/usr/bin/env python3
"""Bridge a visual design to the code that produces it.

Given a class name seen in a browser, this answers: which template writes it,
which block encloses it, which SCSS file styles it, and which JS plugin binds
to the same element. That chain is what a screen design implementation needs.

    extract_design_bridge.py --source <vendor/shopware> --out FILE
    extract_design_bridge.py --source <vendor/shopware> --count
"""
from __future__ import annotations

import argparse
import collections
import os
import re
import sys

import swsource

SCSS_DIR = "storefront/Resources/app/storefront/src/scss"
THEME_JSON = "storefront/Resources/theme.json"

CLASS_ATTR_RE = re.compile(r'class="([^"]*)"')
SCSS_TOP_RE = re.compile(r"^\.([a-z][a-z0-9-]*)", re.M)
SCSS_ANY_RE = re.compile(r"\.([a-z][a-z0-9-]{2,})")
DATA_ATTR_RE = re.compile(r"data-([a-z][a-z0-9-]*)")
IMPORT_RE = re.compile(r"^@import\s+['\"]([^'\"]+)['\"]", re.M)


def template_classes(source: str):
    """Return {class: {templates}} and {class: {blocks}} for static class names."""
    by_template = collections.defaultdict(set)
    by_block = collections.defaultdict(set)
    for rel, text in swsource.iter_templates(source):
        blocks = swsource.nested_blocks(text)
        # Walk the file so each class can be attributed to the block it sits in.
        positions = [(m.start(), m.group(1)) for m in swsource.BLOCK_OR_END_RE.finditer(text)]
        stack: list[str] = []
        marks = []
        for pos, token in positions:
            if token.startswith("block"):
                stack.append(token.split()[1])
            elif stack:
                stack.pop()
            marks.append((pos, list(stack)))

        def block_at(pos: int):
            current: list[str] = []
            for mark_pos, stack_state in marks:
                if mark_pos <= pos:
                    current = stack_state
                else:
                    break
            return current

        for match in CLASS_ATTR_RE.finditer(text):
            enclosing = block_at(match.start())
            for token in match.group(1).split():
                if not re.fullmatch(r"[a-z][a-z0-9-]*", token):
                    continue  # skip Twig expressions and interpolations
                by_template[token].add(rel)
                if enclosing:
                    by_block[token].add((rel, enclosing[-1]))
    return by_template, by_block


def scss_index(source: str):
    """Return {class: {scss files}} for every selector the stylesheets define."""
    root = os.path.join(source, SCSS_DIR)
    index = collections.defaultdict(set)
    files = []
    if not os.path.isdir(root):
        return index, files
    for dirpath, _dirs, names in os.walk(root):
        for name in sorted(names):
            if not name.endswith(".scss"):
                continue
            full = os.path.join(dirpath, name)
            rel = os.path.relpath(full, root).replace(os.sep, "/")
            files.append(rel)
            with open(full, encoding="utf-8", errors="replace") as handle:
                text = handle.read()
            for cls in set(SCSS_ANY_RE.findall(text)):
                index[cls].add(rel)
    return index, sorted(files)


def js_selectors(source: str):
    """Return {data-attribute: plugin} from main.js registrations."""
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import extract_js

    out = {}
    for reg in extract_js.parse_main(source):
        selector = reg["selector"]
        if selector.startswith("["):
            out[selector.strip("[]").split("=")[0]] = reg["plugin"]
    return out


def template_data_attrs(source: str):
    """Return {data-attribute: {templates}}."""
    out = collections.defaultdict(set)
    for rel, text in swsource.iter_templates(source):
        for attr in DATA_ATTR_RE.findall(text):
            out["data-" + attr].add(rel)
    return out


def render(source: str) -> list[str]:
    by_template, by_block = template_classes(source)
    scss, scss_files = scss_index(source)
    js = js_selectors(source)
    data_attrs = template_data_attrs(source)

    styled = sorted(c for c in by_template if c in scss)

    lines = [swsource.stamp("extract_design_bridge.py", source, SCSS_DIR), ""]
    lines.append("# Shopware Storefront — from a design to the code")
    lines.append("")
    lines.append(
        "Start from what a design shows — a component, a class in the inspector — and end at the "
        "block to override, the stylesheet to change and the plugin that must keep working."
    )
    lines.append("")
    lines.append(
        f"**{len(by_template)} static classes in templates, {len(styled)} of them styled by "
        f"one of {len(scss_files)} stylesheets, {len(js)} JavaScript selectors.**"
    )
    lines.append("")
    lines += swsource.toc(
        [
            "The four questions",
            "Where styling lives",
            "Class to template, block and stylesheet",
            "Behaviour attached to markup",
            "Classes with no stylesheet of their own",
        ]
    )

    lines.append("## The four questions")
    lines.append("")
    lines.append(
        "1. **Which template writes this markup?** Look the class up below, or search the block "
        "catalogues for the component name."
    )
    lines.append(
        "2. **Which block do I override?** Take the innermost block containing the change. "
        "Overriding a parent replaces every child inside it."
    )
    lines.append(
        "3. **Where is it styled?** The stylesheet column. Change it through your theme's SCSS and "
        "the theme variables, not by editing the core file."
    )
    lines.append(
        "4. **What behaviour is attached?** Keep the `data-*` attribute the plugin binds to, and "
        "the child selectors its options name."
    )
    lines.append("")
    lines.append(
        "Bootstrap 5 supplies the grid and utilities, so classes such as `row`, `col-*`, `d-flex` "
        "and `btn` come from the framework and are configured through the theme's Bootstrap "
        "variables rather than overridden per component."
    )
    lines.append("")

    lines.append("## Where styling lives")
    lines.append("")
    lines.append("The stylesheet tree, and what each directory is for:")
    lines.append("")
    lines.append("- **`abstract/`** — variables, functions and mixins. No output of its own.")
    lines.append("- **`base/`** — element defaults and the reboot.")
    lines.append("- **`component/`** — one file per reusable component, matching the template names.")
    lines.append("- **`layout/`** — the page frame: header, footer, navigation, containers.")
    lines.append("- **`page/`** — styles scoped to one page type.")
    lines.append("- **`skin/`** — the visual layer on top of the structural styles.")
    lines.append("- **`vendor/`** — Bootstrap and third-party stylesheets.")
    lines.append("")
    theme = os.path.join(source, THEME_JSON)
    if os.path.isfile(theme):
        lines.append(
            "`Resources/theme.json` names the entry points, so a theme overriding "
            "`base.scss` variables reaches every file below it."
        )
        lines.append("")

    lines.append("## Class to template, block and stylesheet")
    lines.append("")
    lines.append(
        "Only classes written literally in a template appear here; a class built from a Twig "
        "expression cannot be indexed statically."
    )
    lines.append("")
    lines.append("| Class | Stylesheet | Template | Innermost block |")
    lines.append("|---|---|---|---|")
    for cls in styled:
        sheets = ", ".join(f"`{s}`" for s in sorted(scss[cls])[:3])
        if len(scss[cls]) > 3:
            sheets += f" +{len(scss[cls]) - 3}"
        templates = sorted(by_template[cls])
        tpl_cell = f"`{templates[0]}`"
        if len(templates) > 1:
            tpl_cell += f" +{len(templates) - 1}"
        blocks = sorted({b for _t, b in by_block.get(cls, set())})
        blk_cell = f"`{blocks[0]}`" if blocks else "—"
        if len(blocks) > 1:
            blk_cell += f" +{len(blocks) - 1}"
        lines.append(f"| `.{cls}` | {sheets} | {tpl_cell} | {blk_cell} |")
    lines.append("")

    lines.append("## Behaviour attached to markup")
    lines.append("")
    lines.append(
        "Removing or renaming one of these attributes removes the behaviour, and nothing fails "
        "loudly when it happens."
    )
    lines.append("")
    lines.append("| Attribute | Plugin | Templates carrying it |")
    lines.append("|---|---|---|")
    for attr in sorted(js):
        templates = sorted(data_attrs.get(attr, set()))
        cell = ", ".join(f"`{t}`" for t in templates[:2]) or "— (set by JavaScript)"
        if len(templates) > 2:
            cell += f" +{len(templates) - 2}"
        lines.append(f"| `{attr}` | `{js[attr]}` | {cell} |")
    lines.append("")

    lines.append("## Classes with no stylesheet of their own")
    lines.append("")
    lines.append(
        "These are written by templates but not styled in the core SCSS: they come from "
        "Bootstrap, or exist purely as hooks for JavaScript and tests. Styling one is a theme "
        "addition rather than an override."
    )
    lines.append("")
    unstyled = sorted(c for c in by_template if c not in scss)
    for index in range(0, len(unstyled), 8):
        lines.append(" ".join(f"`.{c}`" for c in unstyled[index: index + 8]))
    lines.append("")
    return lines


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    swsource.add_source_arg(parser)
    args = parser.parse_args()
    by_template, _by_block = template_classes(args.source)
    scss, files = scss_index(args.source)
    js = js_selectors(args.source)
    if args.count:
        print(f"static classes in templates = {len(by_template)}")
        print(f"scss files = {len(files)}")
        print(f"classes with a stylesheet = {len([c for c in by_template if c in scss])}")
        print(f"js selectors = {len(js)}")
        return 0
    swsource.emit(render(args.source), args.out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
