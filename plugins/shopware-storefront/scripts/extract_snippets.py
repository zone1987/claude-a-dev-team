#!/usr/bin/env python3
"""Catalogue the Storefront snippets and where each one is used.

Every visible string in the Storefront is a snippet key. Rebuilding a template
means carrying the keys across, and a key that no longer resolves renders as the
key itself — visible to customers, and easy to miss in a language you do not read.

    extract_snippets.py --source <vendor/shopware> --out FILE
    extract_snippets.py --source <vendor/shopware> --count
"""
from __future__ import annotations

import argparse
import collections
import json
import os
import re
import sys

import swsource

SNIPPETS = "storefront/Resources/snippet"
CORE_SNIPPETS = "core/Framework/Resources/snippet"
TRANS_RE = re.compile(r"['\"]([a-zA-Z][\w.]*\.[\w.]+)['\"]\s*\|\s*trans")
TRANS_FN_RE = re.compile(r"\btrans\s*\(\s*['\"]([a-zA-Z][\w.]*\.[\w.]+)['\"]")


def flatten(data, prefix=""):
    """Turn the nested JSON into dotted keys."""
    out = {}
    for key, value in data.items():
        path = f"{prefix}.{key}" if prefix else key
        if isinstance(value, dict):
            out.update(flatten(value, path))
        else:
            out[path] = value
    return out


def load_snippets(source: str, subpath: str = SNIPPETS):
    """Return {locale: {dotted key: text}}."""
    root = os.path.join(source, subpath)
    found = {}
    if not os.path.isdir(root):
        return found
    for dirpath, _dirs, files in os.walk(root):
        for name in sorted(files):
            if not name.endswith(".json"):
                continue
            # storefront.en.json and messages.en.base.json both carry the locale second.
            match = re.match(r"(.+?)\.([a-zA-Z-]+?)(?:\.base)?\.json$", name)
            locale = match.group(2) if match else name
            with open(os.path.join(dirpath, name), encoding="utf-8") as handle:
                found[locale] = flatten(json.load(handle))
    return found


def usage(source: str):
    """Return {snippet key: {templates}}."""
    out = collections.defaultdict(set)
    for rel, text in swsource.iter_templates(source):
        for pattern in (TRANS_RE, TRANS_FN_RE):
            for key in pattern.findall(text):
                out[key].add(rel)
    return out


def render(source: str) -> list[str]:
    snippets = load_snippets(source)
    core = load_snippets(source, CORE_SNIPPETS)
    used = usage(source)
    base = snippets.get("en") or (next(iter(snippets.values())) if snippets else {})
    core_base = core.get("en", {})
    # A template may use a key the core bundle defines; both resolve at render time.
    resolvable = dict(core_base)
    resolvable.update(base)

    namespaces = collections.defaultdict(list)
    for key in base:
        namespaces[key.split(".")[0]].append(key)

    missing = sorted(k for k in used if k not in resolvable)
    from_core = sorted(k for k in used if k not in base and k in core_base)
    unused = sorted(k for k in base if k not in used)

    lines = [swsource.stamp("extract_snippets.py", source, SNIPPETS), ""]
    lines.append("# Shopware Storefront — snippets")
    lines.append("")
    lines.append(
        "Every visible string is a snippet key resolved at render time. A key that does not "
        "resolve is printed literally, so a customer sees `checkout.cartHeaderProduct` instead of "
        "a heading — which is why a template rewrite has to carry its keys across."
    )
    lines.append("")
    lines.append(
        f"**{len(base)} Storefront keys in {len(namespaces)} namespaces, "
        f"{len(core_base)} core keys, {len(snippets)} shipped locales, "
        f"{len(used)} keys referenced by templates.**"
    )
    lines.append("")
    lines += swsource.toc(
        [
            "Where snippets live",
            "Using a snippet",
            "Overriding and adding",
            "Namespaces",
            "Keys that come from the core bundle",
            "Keys referenced but not defined",
            "Keys defined but unused",
            "All keys",
        ]
    )

    lines.append("## Where snippets live")
    lines.append("")
    lines.append(
        "`Resources/snippet/<name>.<locale>.json`. The Storefront ships "
        + ", ".join(f"`storefront.{locale}.json`" for locale in sorted(snippets))
        + ". A plugin or theme adds its own file at the same path in its own bundle, and the "
        "files are merged — a key defined in several bundles resolves to the one with the "
        "highest priority, which is what makes overriding work."
    )
    lines.append("")
    lines.append(
        "The file name carries the locale, and the JSON is nested; the nesting flattens into the "
        "dotted keys used in templates, so `{\"checkout\": {\"cartHeader\": \"…\"}}` becomes "
        "`checkout.cartHeader`."
    )
    lines.append("")

    lines.append("## Using a snippet")
    lines.append("")
    lines.append("```twig")
    lines.append("{{ 'checkout.cartHeaderProduct'|trans }}")
    lines.append("{{ 'checkout.cartHeaderProduct'|trans|sw_sanitize }}")
    lines.append("{{ 'account.orderItemCount'|trans({'%count%': items|length}) }}")
    lines.append("<button title=\"{{ 'general.close'|trans|striptags }}\">")
    lines.append("```")
    lines.append("")
    lines.append(
        "- **`|sw_sanitize`** when the text may contain markup a shop owner edited — it strips "
        "everything unsafe and keeps basic HTML."
    )
    lines.append(
        "- **`|striptags`** in an attribute, where markup would break the HTML."
    )
    lines.append(
        "- **Placeholders** are `%name%` and are passed as a hash. A missing placeholder renders "
        "literally rather than failing."
    )
    lines.append(
        "- **In JavaScript**, pass the text in through a data attribute from the template; there "
        "is no client-side translation function."
    )
    lines.append("")

    lines.append("## Overriding and adding")
    lines.append("")
    lines.append(
        "Create `<your-plugin>/src/Resources/snippet/storefront.en.json` with only the keys you "
        "change. The nesting must match the core file, since the merge happens per resolved key."
    )
    lines.append("")
    lines.append(
        "Snippets are also editable per sales channel in the administration, and that value wins "
        "over every file. A key that looks wrong in the shop but right in the file has usually "
        "been edited there."
    )
    lines.append("")
    lines.append(
        "Add a new key under your own namespace rather than extending a core one, so a core "
        "update cannot collide with it."
    )
    lines.append("")

    lines.append("## Namespaces")
    lines.append("")
    lines.append("| Namespace | Keys | Covers |")
    lines.append("|---|---:|---|")
    meaning = {
        "account": "customer account, addresses, orders, profile",
        "address": "address forms and formatting",
        "captcha": "captcha labels and errors",
        "checkout": "cart, confirm, finish, line items",
        "component": "shared components: filters, reviews, sliders",
        "contact": "the contact form",
        "cookie": "cookie consent dialogue",
        "detail": "product detail page",
        "ellipsis": "truncation markers",
        "error": "error pages and messages",
        "footer": "footer columns and service menu",
        "general": "shared labels: close, back, submit",
        "global": "sitewide notices",
        "header": "header, search, widgets",
        "listing": "product listing, sorting, pagination",
        "newsletter": "newsletter subscription",
        "revocationRequest": "the revocation form",
        "search": "search results",
        "spatial": "3D and AR viewers",
        "theme": "theme-level strings",
        "wishlist": "wishlist",
    }
    for namespace in sorted(namespaces):
        lines.append(
            f"| `{namespace}` | {len(namespaces[namespace])} | {meaning.get(namespace, '—')} |"
        )
    lines.append("")

    lines.append("## Keys that come from the core bundle")
    lines.append("")
    lines.append(
        "Used by a Storefront template but defined in `core/Framework/Resources/snippet/`. They "
        "resolve normally; override them in a file matching the core path, not the Storefront one."
    )
    lines.append("")
    if from_core:
        for key in from_core:
            sites = ", ".join(f"`{t}`" for t in sorted(used[key])[:2])
            lines.append(f"- `{key}` — {core_base[key]} — used in {sites}")
    else:
        lines.append("None.")
    lines.append("")

    lines.append("## Keys referenced but not defined")
    lines.append("")
    if missing:
        lines.append(
            "Referenced by a template but present in neither the Storefront nor the core snippet "
            "file at this version. Each renders as the key itself unless a plugin or the "
            "administration supplies it. Verify before relying on one, and define it in your own "
            "snippet file if you keep the template that uses it."
        )
        lines.append("")
        for key in missing:
            sites = ", ".join(f"`{t}`" for t in sorted(used[key]))
            lines.append(f"- `{key}` — used in {sites}")
    else:
        lines.append("Every referenced key resolves.")
    lines.append("")

    lines.append("## Keys defined but unused")
    lines.append("")
    lines.append(
        f"{len(unused)} keys are defined but never referenced from a Storefront template. They "
        "are reached from PHP, from the administration, or from another bundle's templates — do "
        "not treat them as removable."
    )
    lines.append("")

    lines.append("## All keys")
    lines.append("")
    lines.append("Grouped by namespace, with the English text and where it is used.")
    lines.append("")
    for namespace in sorted(namespaces):
        lines.append(f"### {namespace}")
        lines.append("")
        lines.append("| Key | English | Used in |")
        lines.append("|---|---|---|")
        for key in sorted(namespaces[namespace]):
            text = str(base[key]).replace("|", "\\|")[:60]
            sites = sorted(used.get(key, []))
            cell = f"`{sites[0]}`" if sites else "—"
            if len(sites) > 1:
                cell += f" +{len(sites) - 1}"
            lines.append(f"| `{key}` | {text} | {cell} |")
        lines.append("")
    return lines


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    swsource.add_source_arg(parser)
    args = parser.parse_args()
    snippets = load_snippets(args.source)
    core = load_snippets(args.source, CORE_SNIPPETS)
    used = usage(args.source)
    if args.count:
        base = snippets.get("en") or (next(iter(snippets.values())) if snippets else {})
        resolvable = dict(core.get("en", {}))
        resolvable.update(base)
        print(f"locales = {sorted(snippets)}")
        print(f"storefront keys = {len(base)}")
        print(f"core keys = {len(core.get('en', {}))}")
        print(f"referenced in templates = {len(used)}")
        print(f"resolved from core = {len([k for k in used if k not in base and k in resolvable])}")
        print(f"referenced but undefined = {sorted(k for k in used if k not in resolvable)}")
        return 0
    swsource.emit(render(args.source), args.out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
