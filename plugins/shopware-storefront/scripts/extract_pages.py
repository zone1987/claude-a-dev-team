#!/usr/bin/env python3
"""Extract the Page/Pagelet layer: structs, loaders and their loaded events.

A controller never assembles data itself; a PageLoader does, and publishes a
*PageLoadedEvent when it is done. That event is the extension point: subscribe
to it and call addExtension() instead of overriding the controller.

    extract_pages.py --source <vendor/shopware> --out FILE
    extract_pages.py --source <vendor/shopware> --count
"""
from __future__ import annotations

import argparse
import collections
import os
import re
import sys

import swsource

PAGE_DIR = "storefront/Page"
PAGELET_DIR = "storefront/Pagelet"

CLASS_RE = re.compile(r"(?:final\s+)?class\s+(\w+)(?:\s+extends\s+([\w\\]+))?")
GETTER_RE = re.compile(r"public function (get\w+)\(\s*\)\s*:\s*\??([\w\\|]+)")


def scan(source: str, subdir: str):
    """Return {relative_dir: [(class, parent, file, [getters])]}."""
    root = os.path.join(source, subdir)
    found = collections.defaultdict(list)
    if not os.path.isdir(root):
        return found
    for dirpath, _dirs, files in os.walk(root):
        for name in sorted(files):
            if not name.endswith(".php"):
                continue
            full = os.path.join(dirpath, name)
            with open(full, encoding="utf-8", errors="replace") as handle:
                text = handle.read()
            match = CLASS_RE.search(text)
            if not match:
                continue
            parent = (match.group(2) or "").split("\\")[-1]
            getters = [g for g, _t in GETTER_RE.findall(text)]
            rel = os.path.relpath(dirpath, root).replace(os.sep, "/")
            found[rel if rel != "." else "/"].append(
                (match.group(1), parent, name, getters)
            )
    return found


def classify(name: str) -> str:
    if name.endswith("LoadedEvent"):
        return "event"
    if name.endswith("LoadedHook"):
        return "hook"
    if name.endswith("Loader") or name.endswith("LoaderInterface"):
        return "loader"
    if name.endswith("Pagelet"):
        return "pagelet"
    if name.endswith("Page"):
        return "page"
    return "other"


def render(source: str) -> list[str]:
    pages = scan(source, PAGE_DIR)
    pagelets = scan(source, PAGELET_DIR)

    all_classes = [c for items in pages.values() for c in items]
    page_structs = [c for c in all_classes if classify(c[0]) == "page"]

    lines = [swsource.stamp("extract_pages.py", source, PAGE_DIR), ""]
    lines.append("# Shopware Storefront — Page and Pagelet classes")
    lines.append("")
    lines.append(
        "Every Storefront page is a struct filled by a loader. The loader builds the "
        "generic page first (header, footer, meta), adds its own data, then dispatches "
        "its loaded event."
    )
    lines.append("")
    lines.append(
        f"**{len(pages)} page domains, {len(page_structs)} page structs, "
        f"{len(pagelets)} pagelet domains.**"
    )
    lines.append("")
    lines += swsource.toc(
        ["How to extend a page", "Page domains", "Pagelet domains", "What a Page always carries"]
    )

    lines.append("## How to extend a page")
    lines.append("")
    lines.append(
        "Subscribe to the domain's `*PageLoadedEvent` and attach your data as an extension:"
    )
    lines.append("")
    lines.append("```php")
    lines.append("public static function getSubscribedEvents(): array")
    lines.append("{")
    lines.append("    return [ProductPageLoadedEvent::class => 'onProductPageLoaded'];")
    lines.append("}")
    lines.append("")
    lines.append("public function onProductPageLoaded(ProductPageLoadedEvent $event): void")
    lines.append("{")
    lines.append("    $event->getPage()->addExtension('myData', new ArrayStruct([...]));")
    lines.append("}")
    lines.append("```")
    lines.append("")
    lines.append(
        "In Twig the extension is reachable as `page.extensions.myData`. Decorating the "
        "PageLoader also works and is the choice when the data must exist before other "
        "subscribers run; overriding the controller is almost never right."
    )
    lines.append("")

    for title, data, anchor in (
        ("Page domains", pages, "page"),
        ("Pagelet domains", pagelets, "pagelet"),
    ):
        lines.append(f"## {title}")
        lines.append("")
        if not data:
            lines.append("None in this bundle.")
            lines.append("")
            continue
        for rel in sorted(data):
            items = sorted(data[rel])
            lines.append(f"### {rel}")
            lines.append("")
            lines.append("| Class | Kind | Extends |")
            lines.append("|---|---|---|")
            for cls, parent, _file, _getters in items:
                lines.append(
                    f"| `{cls}` | {classify(cls)} | {'`' + parent + '`' if parent else '—'} |"
                )
            lines.append("")
            # Show what the page struct exposes: that is what Twig can read.
            for cls, _parent, _file, getters in items:
                if classify(cls) in ("page", "pagelet") and getters:
                    shown = ", ".join(f"`{g}()`" for g in sorted(getters))
                    lines.append(f"`{cls}` exposes: {shown}")
                    lines.append("")

    lines.append("## What a Page always carries")
    lines.append("")
    lines.append(
        "`GenericPageLoader` fills these before any domain loader runs, so they are "
        "available in every template that receives a `page`:"
    )
    lines.append("")
    lines.append("- **`page.header`** — navigation tree, active language and currency, the cart widget.")
    lines.append("- **`page.footer`** — footer columns and service menu.")
    lines.append("- **`page.metaInformation`** — title, description, canonical URL, robots directives.")
    lines.append("- **`page.salesChannelContext`** — customer, currency, tax state, payment and shipping method.")
    lines.append("- **`page.extensions`** — anything a subscriber attached via `addExtension()`.")
    lines.append("")
    return lines


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    swsource.add_source_arg(parser)
    args = parser.parse_args()
    pages = scan(args.source, PAGE_DIR)
    pagelets = scan(args.source, PAGELET_DIR)
    if args.count:
        flat = [c for items in pages.values() for c in items]
        kinds = collections.Counter(classify(c[0]) for c in flat)
        print(f"page domains = {len(pages)}, pagelet domains = {len(pagelets)}")
        print(f"classes under Page/ = {len(flat)}")
        for kind, count in sorted(kinds.items()):
            print(f"  {kind:10s} {count}")
        return 0
    swsource.emit(render(args.source), args.out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
