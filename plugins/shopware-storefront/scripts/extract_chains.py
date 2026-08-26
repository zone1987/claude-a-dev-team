#!/usr/bin/env python3
"""Extract the template dependency graph: sw_extends edges and sw_include targets.

sw_extends tells you which template already overrides another, so a change to a
base template propagates to its children. sw_include tells you which partials a
template pulls in, and how widely a partial is reused: editing a target that 43
templates include changes all 43.

    extract_chains.py --source <vendor/shopware> --out FILE
    extract_chains.py --source <vendor/shopware> --count
"""
from __future__ import annotations

import argparse
import collections
import sys

import swsource

PREFIX = "@Storefront/"


def short(path: str) -> str:
    return path[len(PREFIX):] if path.startswith(PREFIX) else path


def collect(source: str):
    extends = []          # (child, parent)
    includes = collections.Counter()
    include_sites = collections.defaultdict(set)
    for rel, text in swsource.iter_templates(source):
        for target in swsource.EXTENDS_RE.findall(text):
            extends.append((rel, short(target)))
        for target in swsource.INCLUDE_RE.findall(text):
            includes[short(target)] += 1
            include_sites[short(target)].add(rel)
    return extends, includes, include_sites


def render(source: str) -> list[str]:
    extends, includes, sites = collect(source)
    children = collections.defaultdict(list)
    for child, parent in extends:
        children[parent].append(child)

    lines = [swsource.stamp("extract_chains.py", source), ""]
    lines.append("# Shopware Storefront — template inheritance and include chains")
    lines.append("")
    lines.append(
        "Which template builds on which, and which partial is reused where. "
        "Read this before changing a template: a base template's blocks reach every "
        "child, and a widely included partial reaches every site that includes it."
    )
    lines.append("")
    lines.append(
        f"**{len(extends)} `sw_extends` edges, {sum(includes.values())} `sw_include` "
        f"calls across {len(includes)} distinct targets.**"
    )
    lines.append("")
    lines += swsource.toc(
        [
            "How the two tags differ",
            "Templates that extend another template",
            "Base templates and what inherits from them",
            "Include targets by reuse",
        ]
    )

    lines.append("## How the two tags differ")
    lines.append("")
    lines.append(
        "- **`sw_extends`** continues a template: the child keeps every block of the parent "
        "and replaces only the ones it redefines. Call `{{ parent() }}` to keep the original "
        "content and add to it. Shopware's variant supports multiple inheritance across "
        "plugins, which Twig's own `extends` does not."
    )
    lines.append(
        "- **`sw_include`** renders another template in place, with the current variables "
        "plus anything passed via `with`. The included template's blocks stay its own — "
        "they are not overridable from the including template."
    )
    lines.append("")

    lines.append("## Templates that extend another template")
    lines.append("")
    lines.append("Each row is one `sw_extends` edge, child first.")
    lines.append("")
    lines.append("| Template | extends |")
    lines.append("|---|---|")
    for child, parent in sorted(extends):
        lines.append(f"| `{child}` | `{parent}` |")
    lines.append("")

    lines.append("## Base templates and what inherits from them")
    lines.append("")
    lines.append(
        "Changing a block here changes every template listed beside it, unless that "
        "template overrides the same block."
    )
    lines.append("")
    for parent in sorted(children, key=lambda p: (-len(children[p]), p)):
        kids = sorted(children[parent])
        lines.append(f"### {parent}")
        lines.append("")
        lines.append(f"{len(kids)} template(s) extend this:")
        lines.append("")
        for kid in kids:
            lines.append(f"- `{kid}`")
        lines.append("")

    lines.append("## Include targets by reuse")
    lines.append("")
    lines.append(
        "Sorted by how many calls reach the target. A high count means a change is "
        "felt widely; the including templates are named so the blast radius is visible."
    )
    lines.append("")
    for target, count in includes.most_common():
        lines.append(f"### {target}")
        lines.append("")
        lines.append(f"{count} call(s), from {len(sites[target])} template(s):")
        lines.append("")
        for site in sorted(sites[target]):
            lines.append(f"- `{site}`")
        lines.append("")
    return lines


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    swsource.add_source_arg(parser)
    args = parser.parse_args()
    extends, includes, _sites = collect(args.source)
    if args.count:
        print(f"sw_extends edges = {len(extends)}")
        print(f"sw_include calls = {sum(includes.values())}")
        print(f"sw_include distinct targets = {len(includes)}")
        return 0
    swsource.emit(render(args.source), args.out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
