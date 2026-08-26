#!/usr/bin/env python3
"""Map JavaScript plugins to their selector, options, events and templates.

A Storefront JS plugin is bound to a CSS selector, almost always a data-attribute.
Knowing which selector a plugin listens on is what connects a template change to
the behaviour attached to it: remove the attribute and the plugin stops running.

    extract_js.py --source <vendor/shopware> --out FILE
    extract_js.py --source <vendor/shopware> --count
"""
from __future__ import annotations

import argparse
import collections
import os
import re
import sys

import swsource

MAIN = "storefront/Resources/app/storefront/src/main.js"
SRC = "storefront/Resources/app/storefront/src"

REGISTER_CALL_RE = re.compile(r"PluginManager\.register\(")
OPTIONS_RE = re.compile(r"static options\s*=\s*\{(.*?)\n    \};", re.S)
OPTION_KEY_RE = re.compile(r"^\s{8}(\w+):", re.M)
CLASS_RE = re.compile(r"export default class (\w+) extends (\w+)")
PUBLISH_RE = re.compile(r"\$?emitter\.publish\(\s*['\"]([^'\"]+)['\"]")


def parse_main(source: str):
    """Return [(plugin, selector, async)] from main.js, in registration order."""
    path = os.path.join(source, MAIN)
    if not os.path.isfile(path):
        return []
    with open(path, encoding="utf-8", errors="replace") as handle:
        text = handle.read()
    out = []
    for call in REGISTER_CALL_RE.finditer(text):
        args = _split_args(text, call.end())
        if not args:
            continue
        name = args[0].strip().strip("'\"")
        body = args[1] if len(args) > 1 else ""
        selector = args[2].strip().strip("'\"") if len(args) > 2 else ""
        out.append({"plugin": name, "selector": selector, "async": "import(" in body})
    return out


def _split_args(text: str, start: int):
    """Split a call's arguments at depth-0 commas, respecting quotes."""
    args, buf, depth = [], [], 0
    quote = None
    i = start
    while i < len(text):
        ch = text[i]
        if quote:
            buf.append(ch)
            if ch == quote and text[i - 1] != "\\":
                quote = None
        elif ch in "'\"`":
            quote = ch
            buf.append(ch)
        elif ch in "([{":
            depth += 1
            buf.append(ch)
        elif ch in ")]}":
            if ch == ")" and depth == 0:
                args.append("".join(buf))
                return args
            depth -= 1
            buf.append(ch)
        elif ch == "," and depth == 0:
            args.append("".join(buf))
            buf = []
        else:
            buf.append(ch)
        i += 1
    return args


def parse_plugins(source: str):
    """Return {class: {file, extends, options[]}} for every plugin class."""
    root = os.path.join(source, SRC)
    found = {}
    for dirpath, _dirs, files in os.walk(root):
        for name in sorted(files):
            if not (name.endswith(".plugin.js") or name.endswith(".plugin.ts")):
                continue
            full = os.path.join(dirpath, name)
            with open(full, encoding="utf-8", errors="replace") as handle:
                text = handle.read()
            match = CLASS_RE.search(text)
            if not match:
                continue
            block = OPTIONS_RE.search(text)
            found[match.group(1)] = {
                "file": os.path.relpath(full, root).replace(os.sep, "/"),
                "extends": match.group(2),
                "options": OPTION_KEY_RE.findall(block.group(1)) if block else [],
            }
    return found


def parse_events(source: str):
    """Return {event: [files]} for every published emitter event."""
    root = os.path.join(source, SRC)
    events = collections.defaultdict(set)
    for dirpath, _dirs, files in os.walk(root):
        for name in sorted(files):
            if not name.endswith((".js", ".ts")):
                continue
            full = os.path.join(dirpath, name)
            rel = os.path.relpath(full, root).replace(os.sep, "/")
            if rel.startswith("helper/emitter"):
                continue  # documentation examples, not real events
            with open(full, encoding="utf-8", errors="replace") as handle:
                text = handle.read()
            for event in PUBLISH_RE.findall(text):
                events[event].add(rel)
    return events


def template_hits(source: str):
    """Count data-attribute occurrences across all templates."""
    counts = collections.Counter()
    sites = collections.defaultdict(set)
    attr_re = re.compile(r"data-[a-z][a-z0-9-]*")
    for rel, text in swsource.iter_templates(source):
        for attr in attr_re.findall(text):
            counts[attr] += 1
            sites[attr].add(rel)
    return counts, sites


def render(source: str) -> list[str]:
    registrations = parse_main(source)
    plugins = parse_plugins(source)
    events = parse_events(source)
    counts, sites = template_hits(source)

    lines = [swsource.stamp("extract_js.py", source, SRC), ""]
    lines.append("# Shopware Storefront — JavaScript plugins, selectors and events")
    lines.append("")
    lines.append(
        "Every Storefront behaviour is a plugin class bound to a selector. `PluginManager` "
        "scans the DOM after load, instantiates each plugin on every matching element, and "
        "re-runs the scan when markup is replaced by AJAX."
    )
    lines.append("")
    lines.append(
        f"**{len(registrations)} registrations, {len(plugins)} plugin classes, "
        f"{len(events)} distinct published events.**"
    )
    lines.append("")
    lines += swsource.toc(
        [
            "Keeping a plugin alive through a template change",
            "Registrations",
            "Plugin options",
            "Published events",
            "Data attributes in templates",
        ]
    )

    lines.append("## Keeping a plugin alive through a template change")
    lines.append("")
    lines.append(
        "The selector is the contract between markup and behaviour. Keep the attribute on "
        "the element when you restructure a template, and keep the child selectors the "
        "plugin's options name — those default to class or attribute lookups inside the "
        "plugin's own element."
    )
    lines.append("")
    lines.append(
        "Override a plugin with `PluginManager.override('Name', MyClass, selector)` to "
        "replace it, or `extend` to inherit and change part of it. Registering a second "
        "plugin on the same selector is fine; both run."
    )
    lines.append("")

    lines.append("## Registrations")
    lines.append("")
    lines.append(
        "In `main.js` order. Async plugins load their code on first match, so an unused "
        "plugin costs nothing."
    )
    lines.append("")
    lines.append("| Plugin | Selector | Loading | In templates | Class file |")
    lines.append("|---|---|---|---|---|")
    for reg in registrations:
        selector = reg["selector"]
        attr = selector.strip("[]").split("=")[0] if selector.startswith("[") else ""
        hits = counts.get(attr, 0) if attr else 0
        info = plugins.get(reg["plugin"], {})
        lines.append(
            f"| `{reg['plugin']}` | {'`' + selector + '`' if selector else '—'} | "
            f"{'async' if reg['async'] else 'sync'} | {hits if attr else '—'} | "
            f"{'`' + info['file'] + '`' if info else '—'} |"
        )
    lines.append("")

    lines.append("## Plugin options")
    lines.append("")
    lines.append(
        "Options are overridable per element with a JSON `data-<plugin-name>-options` "
        "attribute, and globally when registering the plugin."
    )
    lines.append("")
    for name in sorted(plugins):
        info = plugins[name]
        if not info["options"]:
            continue
        keys = ", ".join(f"`{k}`" for k in info["options"])
        lines.append(f"### {name}")
        lines.append("")
        lines.append(f"`{info['file']}` — extends `{info['extends']}`")
        lines.append("")
        lines.append(f"{len(info['options'])} options: {keys}")
        lines.append("")

    lines.append("## Published events")
    lines.append("")
    lines.append(
        "Subscribe with `document.$emitter.subscribe('name', callback)`, or on one plugin "
        "instance with `this.$emitter.subscribe(...)`. Use these to react to core behaviour "
        "instead of overriding the plugin that owns it."
    )
    lines.append("")
    lines.append("| Event | Published in |")
    lines.append("|---|---|")
    for event in sorted(events):
        where = ", ".join(f"`{f}`" for f in sorted(events[event]))
        lines.append(f"| `{event}` | {where} |")
    lines.append("")

    lines.append("## Data attributes in templates")
    lines.append("")
    lines.append(
        "Every `data-*` attribute the templates carry, by frequency. `data-bs-*` belongs to "
        "Bootstrap, not to a Storefront plugin."
    )
    lines.append("")
    lines.append("| Attribute | Occurrences | Templates |")
    lines.append("|---|---:|---:|")
    for attr, count in counts.most_common():
        lines.append(f"| `{attr}` | {count} | {len(sites[attr])} |")
    lines.append("")
    return lines


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    swsource.add_source_arg(parser)
    args = parser.parse_args()
    registrations = parse_main(args.source)
    plugins = parse_plugins(args.source)
    events = parse_events(args.source)
    if args.count:
        print(f"registrations = {len(registrations)}")
        print(f"plugin classes = {len(plugins)}")
        print(f"classes with options = {len([p for p in plugins.values() if p['options']])}")
        print(f"distinct events = {len(events)}")
        missing = [r["plugin"] for r in registrations if not r["selector"]]
        print(f"registrations without selector = {missing or 'none'}")
        return 0
    swsource.emit(render(args.source), args.out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
