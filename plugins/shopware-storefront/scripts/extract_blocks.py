#!/usr/bin/env python3
"""Extract every Twig block of the Storefront, keeping its nesting.

The nesting is the load-bearing part: overriding component_product_box_price
requires knowing it sits inside component_product_box_info, which sits inside
component_product_box_content. A flat list of names cannot answer that.

    extract_blocks.py --source <vendor/shopware> --area component --out FILE
    extract_blocks.py --source <vendor/shopware> --count
"""
from __future__ import annotations

import argparse
import collections
import os
import sys

import swsource

# Which template directories each generated file covers.
AREAS = {
    "component": (["storefront/component"], "Component blocks"),
    "page": (["storefront/page"], "Page blocks"),
    "layout": (["storefront/layout", "storefront/base.html.twig"], "Layout blocks"),
    "cms": (
        ["storefront/element", "storefront/block", "storefront/section"],
        "CMS element, block and section blocks",
    ),
    "utilities": (["storefront/utilities"], "Utility blocks"),
}

INTRO = {
    "component": "Reusable fragments: product cards, forms, addresses, line items, listing filters, reviews.",
    "page": "One directory per page type. These templates are what a controller renders.",
    "layout": "The frame around every page: header, footer, navigation, meta, cookie bar.",
    "cms": "Shopping Experiences. An element renders one slot; a block arranges elements; a section arranges blocks.",
    "utilities": "Small shared helpers included from everywhere: alerts, offcanvas, modals, pagination.",
}


def matches(rel: str, prefixes) -> bool:
    return any(rel == p or rel.startswith(p + "/") for p in prefixes)


def collect(source: str, prefixes):
    """Return [(template, [(depth, name)])] for the templates in this area."""
    out = []
    for rel, text in swsource.iter_templates(source):
        if matches(rel, prefixes):
            out.append((rel, swsource.nested_blocks(text)))
    return out


def render(area: str, source: str) -> list[str]:
    prefixes, title = AREAS[area]
    entries = collect(source, prefixes)
    total = sum(len(b) for _r, b in entries)

    lines = [swsource.stamp("extract_blocks.py", source), ""]
    lines.append(f"# Shopware Storefront — {title}")
    lines.append("")
    lines.append(INTRO[area])
    lines.append("")
    lines.append(
        f"**{len(entries)} templates, {total} blocks.** Indentation is the block nesting: "
        "a nested block only renders when its parent does, and overriding a parent replaces "
        "every child inside it."
    )
    lines.append("")
    lines.append(
        "Paths are relative to `Resources/views/`. Override a template by mirroring its path "
        "under your own `src/Resources/views/` and reaching the block with `{% sw_extends %}`."
    )
    lines.append("")

    # Group by the directory below the area root so the TOC stays navigable.
    groups: dict[str, list] = collections.OrderedDict()
    for rel, blocks in entries:
        parts = rel.split("/")
        key = "/".join(parts[:-1]) if len(parts) > 1 else "/"
        groups.setdefault(key, []).append((rel, blocks))

    lines += swsource.toc(list(groups))

    for key, items in groups.items():
        lines.append(f"## {key}")
        lines.append("")
        for rel, blocks in items:
            name = rel.split("/")[-1]
            lines.append(f"### {name}")
            lines.append("")
            lines.append(f"`{rel}` — {len(blocks)} blocks")
            lines.append("")
            if blocks:
                lines.append("```")
                for depth, block in blocks:
                    lines.append("  " * depth + block)
                lines.append("```")
            else:
                lines.append("No blocks; this template renders directly.")
            lines.append("")
    return lines


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    swsource.add_source_arg(parser)
    parser.add_argument("--area", choices=sorted(AREAS), help="which catalogue to render")
    args = parser.parse_args()

    if args.count:
        grand_t = grand_b = 0
        for area in sorted(AREAS):
            entries = collect(args.source, AREAS[area][0])
            blocks = sum(len(b) for _r, b in entries)
            print(f"{area:12s} templates={len(entries):4d} blocks={blocks:5d}")
            grand_t += len(entries)
            grand_b += blocks
        print(f"{'TOTAL':12s} templates={grand_t:4d} blocks={grand_b:5d}")
        return 0

    if not args.area:
        parser.error("--area is required unless --count is given")
    swsource.emit(render(args.area, args.source), args.out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
