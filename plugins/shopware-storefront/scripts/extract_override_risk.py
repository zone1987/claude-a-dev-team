#!/usr/bin/env python3
"""Map which JavaScript plugin needs which selector in which Twig block.

Overriding a block that carries a selector a plugin queries removes the
behaviour, and nothing fails loudly: the plugin initialises, finds nothing and
does nothing. This catalogue answers, before an override is written, what is
attached to the markup being replaced.

    extract_override_risk.py --source <vendor/shopware> --out FILE
    extract_override_risk.py --source <vendor/shopware> --count
"""
from __future__ import annotations

import argparse
import collections
import os
import re
import sys

import swsource

JS_SRC = "storefront/Resources/app/storefront/src"

# Where a plugin reaches into the DOM.
QUERY_RE = re.compile(r"""querySelector(?:All)?\(\s*['"`]([^'"`]+)""")
CLOSEST_RE = re.compile(r"""closest\(\s*['"`]([^'"`]+)""")
# Option entries whose name ends in Selector hold a selector as their default.
OPT_SELECTOR_RE = re.compile(r"""(\w*[Ss]elector)\s*:\s*['"]([^'"]+)['"]""")
GET_ELEMENT_RE = re.compile(r"""getElementsByClassName\(\s*['"]([^'"]+)""")

CLASS_RE = re.compile(r"\.([a-zA-Z][\w-]*)")
# Options handed from Twig into a plugin, and the {% set %} that built them.
OPTIONS_ATTR_RE = re.compile(r'data-([a-z0-9-]+)-(options|config)\s*=\s*"([^"]*)"', re.S)
SET_VAR_RE = re.compile(r"\{%-?\s*set\s+(\w+)\s*=\s*(.+?)%\}", re.S)
PLAIN_DATA_RE = re.compile(r'data-([a-z0-9-]+)\s*=\s*"(\{\{[^"]*)"', re.S)
ATTR_RE = re.compile(r"\[(data-[\w-]+)")

# Tokens that are not selectors: option keys parsed out of object literals,
# and framework classes no Shopware template owns.
NOISE = {
    "options", "config", "length", "value", "className", "classList",
    "modal", "offcanvas", "dropdown", "collapse", "active", "show", "fade",
    "form-control", "form-select", "btn", "container", "row", "col",
}


def plugin_label(rel: str) -> str:
    """Turn a source path into the name a reader recognises."""
    name = os.path.basename(rel)
    for suffix in (".plugin.js", ".plugin.ts", ".event.js", ".helper.js", ".util.js", ".js", ".ts"):
        if name.endswith(suffix):
            name = name[: -len(suffix)]
            break
    return "".join(part.capitalize() for part in name.split("-"))


def collect_selectors(source: str):
    """Return {token: {(plugin label, source file)}} for every DOM lookup."""
    root = os.path.join(source, JS_SRC)
    tokens = collections.defaultdict(set)
    raw = collections.defaultdict(set)
    for dirpath, _dirs, files in os.walk(root):
        for name in sorted(files):
            if not name.endswith((".js", ".ts")) or name.endswith((".test.js", ".test.ts")):
                continue
            full = os.path.join(dirpath, name)
            rel = os.path.relpath(full, root).replace(os.sep, "/")
            if rel.startswith("plugin-system/") or "/test/" in rel:
                continue
            with open(full, encoding="utf-8", errors="replace") as handle:
                text = handle.read()
            found = set()
            for pattern in (QUERY_RE, CLOSEST_RE, GET_ELEMENT_RE):
                found.update(pattern.findall(text))
            for _key, value in OPT_SELECTOR_RE.findall(text):
                found.add(value)
            owner = (plugin_label(rel), rel)
            for selector in found:
                for cls in CLASS_RE.findall(selector):
                    if cls in NOISE:
                        continue
                    tokens["." + cls].add(owner)
                    raw["." + cls].add(selector)
                for attr in ATTR_RE.findall(selector):
                    tokens[f"[{attr}]"].add(owner)
                    raw[f"[{attr}]"].add(selector)
                if selector.startswith("data-"):
                    tokens[f"[{selector}]"].add(owner)
    return tokens, raw


def dash_to_plugin(dashed: str) -> str:
    """`quantity-selector` is the attribute form of the plugin name `QuantitySelector`."""
    return "".join(part.capitalize() for part in dashed.split("-"))


def collect_options(source: str):
    """Return rows of (template, block, plugin, kind, expression, origin)."""
    rows = []
    for rel, text in swsource.iter_templates(source):
        at = block_index(text)
        sets = {name: " ".join(expr.split())[:160] for name, expr in SET_VAR_RE.findall(text)}
        for match in OPTIONS_ATTR_RE.finditer(text):
            dashed, kind, expr = match.group(1), match.group(2), match.group(3)
            expr = " ".join(expr.split())
            # A bare variable was usually built by a {% set %} earlier in the file.
            bare = re.fullmatch(r"\{\{\s*(\w+)\s*\|\s*json_encode\s*\}\}", expr)
            origin = sets.get(bare.group(1), "") if bare else ""
            rows.append((rel, at(match.start()), dash_to_plugin(dashed), kind, expr[:160], origin))
        for match in PLAIN_DATA_RE.finditer(text):
            attr, expr = match.group(1), " ".join(match.group(2).split())
            if attr.endswith(("-options", "-config")):
                continue
            rows.append((rel, at(match.start()), f"[data-{attr}]", "value", expr[:160], ""))
    return rows


def block_index(text: str):
    """Return a function mapping a character offset to its innermost block."""
    marks, stack = [], []
    for match in swsource.BLOCK_OR_END_RE.finditer(text):
        token = match.group(1)
        if token.startswith("block"):
            stack.append(token.split()[1])
        elif stack:
            stack.pop()
        marks.append((match.start(), list(stack)))

    def at(pos: int) -> str:
        current: list[str] = []
        for mark_pos, state in marks:
            if mark_pos <= pos:
                current = state
            else:
                break
        return current[-1] if current else "(outside any block)"

    return at


def collect(source: str):
    """Return rows of (template, block, token, owners, occurrences)."""
    tokens, raw = collect_selectors(source)
    rows = []
    for rel, text in swsource.iter_templates(source):
        at = block_index(text)
        for token, owners in tokens.items():
            needle = token[1:-1] if token.startswith("[") else token[1:]
            # A class must match as a whole word; an attribute matches literally.
            pattern = (
                re.compile(re.escape(needle))
                if token.startswith("[")
                else re.compile(r"\b" + re.escape(needle) + r"\b")
            )
            seen_blocks = collections.Counter()
            for match in pattern.finditer(text):
                seen_blocks[at(match.start())] += 1
            for block, count in seen_blocks.items():
                rows.append((rel, block, token, sorted(owners), count, sorted(raw.get(token, []))))
    return rows


def render(source: str) -> list[str]:
    rows = collect(source)
    options = collect_options(source)
    by_template = collections.defaultdict(list)
    for row in rows:
        by_template[row[0]].append(row)

    plugins = {owner for row in rows for owner, _f in [(o[0], o[1]) for o in row[3]]}
    tokens = {row[2] for row in rows}

    lines = [swsource.stamp("extract_override_risk.py", source, JS_SRC), ""]
    lines.append("# Shopware Storefront — what breaks when you override a block")
    lines.append("")
    lines.append(
        "A JavaScript plugin reaches into the markup by selector. Replace the markup without "
        "the selector and the plugin still initialises, finds nothing, and silently does "
        "nothing — no console error, no failed request, just a button that stopped working."
    )
    lines.append("")
    lines.append(
        f"**{len(by_template)} templates carry at least one selector a plugin queries: "
        f"{len(tokens)} distinct selectors across {len(plugins)} plugins, "
        f"{len(rows)} template-block-selector pairs. A further {len(options)} places hand "
        f"options from Twig into a plugin.**"
    )
    lines.append("")
    lines += swsource.toc(
        [
            "How to use this",
            "The rules",
            "Values handed from Twig into a plugin",
            "By template and block",
            "By selector",
            "Selectors the analytics events read",
        ]
    )

    lines.append("## How to use this")
    lines.append("")
    lines.append(
        "Before overriding a block, look the template up below. Every selector listed under the "
        "block you are replacing must still exist in your markup — on the same element, in the "
        "same nesting relationship to its plugin's root element."
    )
    lines.append("")
    lines.append(
        "A selector is listed against the **innermost block** containing it. Overriding a parent "
        "block replaces its children too, so a parent inherits every requirement below it."
    )
    lines.append("")

    lines.append("## The rules")
    lines.append("")
    lines.append(
        "- **`js-` prefixed classes are contracts, not styling.** They exist only so JavaScript "
        "can find the element. Never rename one, and never style against one."
    )
    lines.append(
        "- **`data-*` attributes bind the plugin itself.** Losing the attribute means the plugin "
        "never initialises on that element at all."
    )
    lines.append(
        "- **Nesting matters.** Most plugins query inside `this.el`, so a child selector must stay "
        "a descendant of the element carrying the plugin's own attribute."
    )
    lines.append(
        "- **Keep `{{ parent() }}`** where you only add markup — it is the cheapest way to keep "
        "every selector you did not think about."
    )
    lines.append(
        "- **Test the behaviour, not the layout.** These failures are invisible in a screenshot: "
        "click the button, submit the form, change the quantity."
    )
    lines.append("")

    lines.append("## Values handed from Twig into a plugin")
    lines.append("")
    lines.append(
        "A plugin reads its options from `data-<dash-case-name>-options` (and "
        "`-config`) on its own element, JSON-encoded. These are the values the template "
        "computes and the plugin depends on: remove the attribute, move it to another "
        "element, or drop the variable that feeds it, and the plugin falls back to its "
        "`static options` defaults — usually wrong, always silent."
    )
    lines.append("")
    lines.append(
        "**When overriding a block that carries one of these, keep the attribute on the same "
        "element and keep whatever `{% set %}` produced its value.** If the value comes from "
        "the page struct, it only exists on pages that provide it."
    )
    lines.append("")
    lines.append("| Template | Block | Plugin | Attribute | Expression |")
    lines.append("|---|---|---|---|---|")
    for template, block, plugin, kind, expr, origin in sorted(options):
        cell = expr.replace("|", "\\|")
        lines.append(
            f"| `{template}` | `{block}` | `{plugin}` | `{kind}` | `{cell}` |"
        )
    lines.append("")
    derived = [row for row in options if row[5]]
    if derived:
        lines.append(
            "Where the attribute holds a bare variable, this is the `{% set %}` that built it — "
            "the statement an override must keep or reproduce:"
        )
        lines.append("")
        for template, block, plugin, _k, expr, origin in sorted(derived):
            lines.append(f"- `{template}` → `{plugin}`: `{origin.replace('|', chr(92) + '|')}`")
        lines.append("")

    lines.append("## By template and block")
    lines.append("")
    for template in sorted(by_template):
        entries = by_template[template]
        blocks = collections.defaultdict(list)
        for _t, block, token, owners, count, raws in entries:
            blocks[block].append((token, owners, count, raws))
        lines.append(f"### {template}")
        lines.append("")
        lines.append(f"{len(entries)} selector(s) across {len(blocks)} block(s).")
        lines.append("")
        lines.append("| Block | Selector | Required by | Uses |")
        lines.append("|---|---|---|---|")
        for block in sorted(blocks):
            for token, owners, count, _raws in sorted(blocks[block]):
                names = ", ".join(f"`{label}`" for label, _file in owners)
                lines.append(f"| `{block}` | `{token}` | {names} | {count}× |")
        lines.append("")

    lines.append("## By selector")
    lines.append("")
    lines.append(
        "The reverse lookup: given a class or attribute, which plugin needs it and where it "
        "appears. `Query` shows the full selector the plugin uses, which is what tells you "
        "whether nesting matters."
    )
    lines.append("")
    by_token = collections.defaultdict(list)
    for template, block, token, owners, count, raws in rows:
        by_token[token].append((template, block, owners, raws))
    for token in sorted(by_token):
        entries = by_token[token]
        owners = sorted({(label, file) for _t, _b, os_, _r in entries for label, file in os_})
        raws = sorted({r for _t, _b, _o, rs in entries for r in rs})
        lines.append(f"### {token}")
        lines.append("")
        for label, file in owners:
            lines.append(f"- **`{label}`** — `{file}`")
        if raws:
            lines.append(f"- Query: {', '.join(f'`{r}`' for r in raws[:4])}")
        lines.append("")
        lines.append("Appears in:")
        lines.append("")
        for template, block in sorted({(t, b) for t, b, _o, _r in entries}):
            lines.append(f"- `{template}` → `{block}`")
        lines.append("")

    lines.append("## Selectors the analytics events read")
    lines.append("")
    lines.append(
        "The Google Analytics events read the rendered markup directly to build their payload. "
        "Losing one of these breaks tracking without breaking the page — the most expensive kind "
        "of silent failure, because it is noticed weeks later in a report."
    )
    lines.append("")
    analytics = sorted(
        {
            (token, template, block)
            for template, block, token, owners, _c, _r in rows
            if any("google-analytics" in file for _label, file in owners)
        }
    )
    if analytics:
        lines.append("| Selector | Template | Block |")
        lines.append("|---|---|---|")
        for token, template, block in analytics:
            lines.append(f"| `{token}` | `{template}` | `{block}` |")
    else:
        lines.append("None found.")
    lines.append("")
    return lines


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    swsource.add_source_arg(parser)
    args = parser.parse_args()
    rows = collect(args.source)
    options = collect_options(args.source)
    if args.count:
        print(f"options handed from Twig = {len(options)}")
        templates = {r[0] for r in rows}
        tokens = {r[2] for r in rows}
        plugins = {label for r in rows for label, _f in r[3]}
        print(f"templates with a JS dependency = {len(templates)}")
        print(f"distinct selectors = {len(tokens)}")
        print(f"plugins involved = {len(plugins)}")
        print(f"template-block-selector pairs = {len(rows)}")
        return 0
    swsource.emit(render(args.source), args.out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
