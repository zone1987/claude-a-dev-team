#!/usr/bin/env python3
"""Extract the request chain: Route -> Controller method -> Twig template.

This is what turns a URL into a template. Given a page in a design, it names the
controller to look at and the template to override; given a template, it names
the route that reaches it.

    extract_routes.py --source <vendor/shopware> --out FILE
    extract_routes.py --source <vendor/shopware> --count
"""
from __future__ import annotations

import argparse
import os
import re
import sys

import swsource

CONTROLLERS = "storefront/Controller"

ROUTE_RE = re.compile(r"#\[Route\((.*?)\)\]", re.S)
PATH_RE = re.compile(r"""["']([^"']*/[^"']*|/)["']""")
NAME_RE = re.compile(r"""name:\s*["']([^"']+)["']""")
METHODS_RE = re.compile(r"""methods:\s*\[([^\]]*)\]""")
DEFAULTS_RE = re.compile(r"defaults:\s*\[(.*?)\]", re.S)
FUNC_RE = re.compile(r"public function\s+(\w+)\s*\(")
RENDER_RE = re.compile(r"renderStorefront\(\s*['\"]([^'\"]+)['\"]")
PAGE_LOAD_RE = re.compile(r"(\w*(?:Page|Pagelet))Loader->load\(|\$this->(\w+Loader)->load\(")


def parse_controller(path: str):
    """Walk a controller file, pairing each method with its route and renders."""
    with open(path, encoding="utf-8", errors="replace") as handle:
        text = handle.read()

    # Index every method start so a render can be attributed to its method.
    methods = [(m.start(), m.group(1)) for m in FUNC_RE.finditer(text)]
    routes = {}
    for match in ROUTE_RE.finditer(text):
        body = match.group(1)
        after = text[match.end():]
        fn = FUNC_RE.search(after)
        if not fn:
            continue
        name = NAME_RE.search(body)
        path_m = PATH_RE.search(body)
        methods_m = METHODS_RE.search(body)
        defaults = DEFAULTS_RE.search(body)
        routes[fn.group(1)] = {
            "path": path_m.group(1) if path_m else "",
            "name": name.group(1) if name else "",
            "methods": (
                ", ".join(v.strip().strip("'\"") for v in methods_m.group(1).split(","))
                if methods_m
                else ""
            ),
            "defaults": " ".join(defaults.group(1).split()) if defaults else "",
        }

    def method_at(pos: int) -> str:
        current = ""
        for start, name in methods:
            if start <= pos:
                current = name
            else:
                break
        return current

    rows = []
    for match in RENDER_RE.finditer(text):
        fn = method_at(match.start())
        info = routes.get(fn, {})
        rows.append(
            {
                "method": fn,
                "template": match.group(1),
                "path": info.get("path", ""),
                "name": info.get("name", ""),
                "methods": info.get("methods", ""),
                "defaults": info.get("defaults", ""),
            }
        )
    return rows


def collect(source: str):
    root = os.path.join(source, CONTROLLERS)
    out = []
    if not os.path.isdir(root):
        return out
    for name in sorted(os.listdir(root)):
        if not name.endswith(".php"):
            continue
        for row in parse_controller(os.path.join(root, name)):
            row["controller"] = name[:-4]
            out.append(row)
    return out


def render(source: str) -> list[str]:
    rows = collect(source)
    lines = [swsource.stamp("extract_routes.py", source, CONTROLLERS), ""]
    lines.append("# Shopware Storefront — route, controller and template map")
    lines.append("")
    lines.append(
        "How a URL becomes HTML. The controller loads a Page through its PageLoader and "
        "hands it to `renderStorefront()`, which resolves the template through the theme "
        "inheritance chain — so your own template at the same path wins over the core one."
    )
    lines.append("")
    lines.append(f"**{len(rows)} `renderStorefront()` calls across "
                 f"{len({r['controller'] for r in rows})} controllers.**")
    lines.append("")
    lines += swsource.toc(
        ["The chain", "Route to template", "Templates by route", "Controllers without a route attribute"]
    )

    lines.append("## The chain")
    lines.append("")
    lines.append("```")
    lines.append("HTTP request")
    lines.append("  -> Route            #[Route(path, name, methods, defaults)]")
    lines.append("  -> Controller       a method on a *Controller class")
    lines.append("  -> PageLoader       builds the Page struct, dispatches PageLoadedEvent")
    lines.append("  -> renderStorefront('@Storefront/storefront/...')")
    lines.append("  -> Twig template    resolved through theme inheritance")
    lines.append("```")
    lines.append("")
    lines.append(
        "To add data to an existing page, subscribe to its `*PageLoadedEvent` and call "
        "`addExtension()` — no controller override is needed. To change markup, override "
        "the template. Reach for a controller override only for genuinely new routes."
    )
    lines.append("")

    lines.append("## Route to template")
    lines.append("")
    lines.append("| Controller::method | Path | Route name | Methods | Template |")
    lines.append("|---|---|---|---|---|")
    for row in sorted(rows, key=lambda r: (r["controller"], r["method"])):
        tpl = row["template"]
        tpl = tpl[len("@Storefront/"):] if tpl.startswith("@Storefront/") else tpl
        lines.append(
            f"| `{row['controller']}::{row['method']}` | "
            f"{'`' + row['path'] + '`' if row['path'] else '—'} | "
            f"{'`' + row['name'] + '`' if row['name'] else '—'} | "
            f"{row['methods'] or '—'} | `{tpl}` |"
        )
    lines.append("")

    lines.append("## Templates by route")
    lines.append("")
    lines.append("The same lookup from the template side: which route reaches this file.")
    lines.append("")
    by_tpl: dict[str, list] = {}
    for row in rows:
        tpl = row["template"]
        tpl = tpl[len("@Storefront/"):] if tpl.startswith("@Storefront/") else tpl
        by_tpl.setdefault(tpl, []).append(row)
    lines.append("| Template | Reached by |")
    lines.append("|---|---|")
    for tpl in sorted(by_tpl):
        reach = "<br>".join(
            f"`{r['controller']}::{r['method']}`" + (f" ({r['name']})" if r["name"] else "")
            for r in sorted(by_tpl[tpl], key=lambda r: r["method"])
        )
        lines.append(f"| `{tpl}` | {reach} |")
    lines.append("")

    lines.append("## Controllers without a route attribute")
    lines.append("")
    orphans = [r for r in rows if not r["path"] and not r["name"]]
    if orphans:
        lines.append(
            "These render a template without an adjacent `#[Route]`. They are reached "
            "through exception handling, an ESI include or a parent route rather than "
            "directly by URL."
        )
        lines.append("")
        for row in sorted(orphans, key=lambda r: (r["controller"], r["method"])):
            tpl = row["template"]
            tpl = tpl[len("@Storefront/"):] if tpl.startswith("@Storefront/") else tpl
            lines.append(f"- `{row['controller']}::{row['method']}` renders `{tpl}`")
    else:
        lines.append("Every `renderStorefront()` call sits under a route attribute.")
    lines.append("")
    return lines


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    swsource.add_source_arg(parser)
    args = parser.parse_args()
    rows = collect(args.source)
    if args.count:
        print(f"renderStorefront calls = {len(rows)}")
        print(f"controllers = {len({r['controller'] for r in rows})}")
        print(f"with route = {len([r for r in rows if r['name'] or r['path']])}")
        return 0
    swsource.emit(render(args.source), args.out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
