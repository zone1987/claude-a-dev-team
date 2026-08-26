#!/usr/bin/env python3
"""Track where a template's variables come from.

A template can only read what something put there. Four things do:
the controller, the global Twig extensions, an including template's `with`,
and the template's own `{% set %}`. Overriding a block without knowing which
of the four supplies a variable is how a template breaks in one context and
works in another.

    extract_variables.py --source <vendor/shopware> --out FILE
    extract_variables.py --source <vendor/shopware> --count
"""
from __future__ import annotations

import argparse
import collections
import os
import re
import sys

import swsource

CONTROLLERS = "storefront/Controller"
TWIG_EXT = "storefront/Framework/Twig"
CORE = "core"
STOREFRONT = "storefront"

RENDER_VARS_RE = re.compile(
    r"renderStorefront\(\s*['\"]([^'\"]+)['\"]\s*,\s*\[(.*?)\]\s*\)", re.S
)
VAR_KEY_RE = re.compile(r"['\"](\w+)['\"]\s*=>")
SET_RE = re.compile(r"\{%-?\s*set\s+(\w+)\s*=")
WITH_RE = re.compile(
    r"sw_include\s*\(?\s*['\"]([^'\"]+)['\"]\s*(?:\)\s*)?with\s*\{(.*?)\}", re.S
)
WITH_KEY_RE = re.compile(r"(\w+)\s*:")
FOR_RE = re.compile(r"\{%-?\s*for\s+([\w\s,]+)\s+in\s")
GLOBAL_RE = re.compile(r"^ {12}'(\w+)'\s*=>", re.M)
TWIG_FN_RE = re.compile(r"new TwigFunction\(\s*'([^']+)'")
TWIG_FL_RE = re.compile(r"new TwigFilter\(\s*'([^']+)'")

# What each global carries. The names are read from the source; the meaning is not
# in the code, so it is stated here once and checked against the array below.
GLOBAL_MEANING = {
    "shopware": "config bag: `dateFormat`, `navigation` (active and root id), `minSearchLength`, `showStagingBanner`",
    "themeId": "id of the resolved theme; read by `theme_config()` rather than directly",
    "controllerName": "the controller without its suffix, e.g. `Product` — used for body classes",
    "controllerAction": "the method that handled the request, e.g. `index`",
    "context": "the `SalesChannelContext`: customer, currency, tax state, payment and shipping method",
    "activeRoute": "the matched route name; navigation templates compare against it",
    "formViolations": "validation errors of the previous request, for re-rendering a failed form",
    "jsonLdFlags": "the `json_encode` flags used for structured data output",
}


def twig_extensions(source: str):
    """Return [(class, path, functions, filters)] for every Twig extension."""
    found = []
    for area in (CORE, STOREFRONT):
        root = os.path.join(source, area)
        for dirpath, _dirs, files in os.walk(root):
            if os.sep + "Test" in dirpath:
                continue
            for name in sorted(files):
                if not name.endswith(".php"):
                    continue
                full = os.path.join(dirpath, name)
                try:
                    with open(full, encoding="utf-8", errors="replace") as handle:
                        text = handle.read()
                except OSError:
                    continue
                if "extends AbstractExtension" not in text:
                    continue
                functions = sorted(set(TWIG_FN_RE.findall(text)))
                filters = sorted(set(TWIG_FL_RE.findall(text)))
                if not functions and not filters:
                    continue
                found.append(
                    (name[:-4], os.path.relpath(full, source).replace(os.sep, "/"),
                     functions, filters)
                )
    return sorted(found)


def controller_vars(source: str):
    """Return {template: {variable: {controller}}} from renderStorefront calls."""
    root = os.path.join(source, CONTROLLERS)
    out = collections.defaultdict(lambda: collections.defaultdict(set))
    if not os.path.isdir(root):
        return out
    for name in sorted(os.listdir(root)):
        if not name.endswith(".php"):
            continue
        with open(os.path.join(root, name), encoding="utf-8", errors="replace") as handle:
            text = handle.read()
        for match in RENDER_VARS_RE.finditer(text):
            template = match.group(1)
            template = template[len("@Storefront/"):] if template.startswith("@Storefront/") else template
            for key in VAR_KEY_RE.findall(match.group(2)):
                out[template][key].add(name[:-4])
    return out


def global_vars(source: str):
    """Return the variables the Twig extensions add to every template."""
    path = os.path.join(source, TWIG_EXT, "TemplateDataExtension.php")
    if not os.path.isfile(path):
        return []
    with open(path, encoding="utf-8", errors="replace") as handle:
        text = handle.read()
    # Only the top-level keys of the returned array; nested keys sit deeper.
    match = re.search(r"function getGlobals\(\).*?\n        return \[(.*?)\n        \];", text, re.S)
    body = match.group(1) if match else text
    return sorted(set(GLOBAL_RE.findall(body)))


def template_vars(source: str):
    """Return per template: what it sets, what it loops, what it passes on."""
    sets = {}
    passes = collections.defaultdict(lambda: collections.defaultdict(set))
    receives = collections.defaultdict(lambda: collections.defaultdict(set))
    for rel, text in swsource.iter_templates(source):
        local = sorted(set(SET_RE.findall(text)))
        loops: set[str] = set()
        for group in FOR_RE.findall(text):
            for name in group.split(","):
                if name.strip():
                    loops.add(name.strip())
        sets[rel] = {"set": local, "for": sorted(loops)}
        for match in WITH_RE.finditer(text):
            target = match.group(1)
            target = target[len("@Storefront/"):] if target.startswith("@Storefront/") else target
            for key in WITH_KEY_RE.findall(match.group(2)):
                passes[rel][target].add(key)
                receives[target][key].add(rel)
    return sets, passes, receives


def render(source: str) -> list[str]:
    ctrl = controller_vars(source)
    globals_ = global_vars(source)
    extensions = twig_extensions(source)
    sets, passes, receives = template_vars(source)

    total_set = sum(len(v["set"]) for v in sets.values())
    with_pairs = sum(len(t) for t in passes.values())

    lines = [swsource.stamp("extract_variables.py", source, CONTROLLERS), ""]
    lines.append("# Shopware Storefront — where template variables come from")
    lines.append("")
    lines.append(
        "A template reads only what something put in scope. Four sources do that, and knowing "
        "which one supplies a variable decides whether an override works in every context or "
        "only in the one you tested."
    )
    lines.append("")
    lines.append(
        f"**{len(globals_)} global variables from {len(extensions)} Twig extensions, "
        f"{len(ctrl)} templates receiving controller variables, {with_pairs} include "
        f"hand-offs, {total_set} local assignments.**"
    )
    lines.append("")
    lines += swsource.toc(
        [
            "The four sources",
            "Global variables and where they come from",
            "Functions and filters, and which extension provides them",
            "Variables a controller passes",
            "Variables passed between templates",
            "Variables a template defines itself",
        ]
    )

    lines.append("## The four sources")
    lines.append("")
    lines.append(
        "1. **Global** — added by a Twig extension to every template. Always available, "
        "including in a partial reached through several includes."
    )
    lines.append(
        "2. **Controller** — the array handed to `renderStorefront()`. Almost always just "
        "`page`, which carries everything else on the page struct."
    )
    lines.append(
        "3. **Include** — `sw_include ... with {...}` puts named values in the included "
        "template's scope. Without `only`, the including scope stays visible too, which is why "
        "a partial can silently depend on a variable nobody passed it."
    )
    lines.append(
        "4. **Local** — `{% set %}` and the loop variable of `{% for %}`, visible from that "
        "point to the end of the enclosing block."
    )
    lines.append("")
    lines.append(
        "**The trap when overriding.** A `{% set %}` in a parent block is not visible to a "
        "child block you override in your own template: blocks resolve in their own scope. "
        "Re-derive the value, or override the block that holds the `{% set %}` instead."
    )
    lines.append("")

    lines.append("## Global variables and where they come from")
    lines.append("")
    lines.append(
        "`Storefront/Framework/Twig/TemplateDataExtension.php` implements `GlobalsInterface` "
        "and its `getGlobals()` runs once per request, reading the current request from the "
        "`RequestStack`."
    )
    lines.append("")
    lines.append(
        "**It returns an empty array when there is no current request, or when the request "
        "carries no `SalesChannelContext`.** So in a context outside a sales channel — a "
        "rendered mail template, a generated document — none of these exist. Guard with "
        "`{% if context is defined %}` in a template that both paths reach."
    )
    lines.append("")
    lines.append("| Variable | Carries |")
    lines.append("|---|---|")
    for name in globals_:
        lines.append(f"| `{name}` | {GLOBAL_MEANING.get(name, 'see the extension source')} |")
    lines.append("")
    lines.append(
        "The navigation ids inside `shopware.navigation` are resolved in a fixed order: the "
        "route's `navigationId` attribute first, then the request parameter, then the category "
        "of a landing page, and finally the sales channel's root category. That is why a "
        "landing page still highlights the right navigation entry."
    )
    lines.append("")

    lines.append("## Functions and filters, and which extension provides them")
    lines.append("")
    lines.append(
        "Not variables, but the other half of what a template can reach. Each is registered by "
        "one extension class; the path says whether it comes from the core or the Storefront."
    )
    lines.append("")
    lines.append("| Extension | Functions | Filters |")
    lines.append("|---|---|---|")
    for cls, path, functions, filters in extensions:
        fn = ", ".join(f"`{f}()`" for f in functions) or "—"
        fl = ", ".join(f"`{f}`" for f in filters) or "—"
        lines.append(f"| `{cls}`<br><sub>`{path}`</sub> | {fn} | {fl} |")
    lines.append("")
    lines.append(
        "`sw_extends`, `sw_include`, `sw_block` and `sw_source` come from "
        "`TwigFeaturesWithInheritanceExtension`: they are the multi-inheritance aware "
        "replacements for Twig's own tags, which is why a plugin template can extend a "
        "template another plugin already extended."
    )
    lines.append("")

    lines.append("## Variables a controller passes")
    lines.append("")
    lines.append("| Template | Variables | From |")
    lines.append("|---|---|---|")
    for template in sorted(ctrl):
        entries = ctrl[template]
        names = ", ".join(f"`{v}`" for v in sorted(entries))
        sources = ", ".join(
            f"`{c}`" for c in sorted({c for s in entries.values() for c in s})
        )
        lines.append(f"| `{template}` | {names} | {sources} |")
    lines.append("")

    lines.append("## Variables passed between templates")
    lines.append("")
    lines.append(
        "Each row is one `sw_include ... with`. Read it from the receiving side: these are the "
        "names the partial can count on, whoever includes it."
    )
    lines.append("")
    for target in sorted(receives):
        lines.append(f"### {target}")
        lines.append("")
        for key in sorted(receives[target]):
            senders = ", ".join(f"`{s}`" for s in sorted(receives[target][key]))
            lines.append(f"- `{key}` — from {senders}")
        lines.append("")

    lines.append("## Variables a template defines itself")
    lines.append("")
    lines.append(
        "`{% set %}` assignments and `{% for %}` loop variables, per template. A block you "
        "override cannot see these unless it sits inside the block that defines them."
    )
    lines.append("")
    for rel in sorted(sets):
        info = sets[rel]
        if not info["set"] and not info["for"]:
            continue
        parts = []
        if info["set"]:
            parts.append("sets " + ", ".join(f"`{v}`" for v in info["set"]))
        if info["for"]:
            parts.append("loops " + ", ".join(f"`{v}`" for v in info["for"]))
        lines.append(f"- `{rel}` — {'; '.join(parts)}")
    lines.append("")
    return lines


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    swsource.add_source_arg(parser)
    args = parser.parse_args()
    ctrl = controller_vars(args.source)
    globals_ = global_vars(args.source)
    sets, passes, _receives = template_vars(args.source)
    if args.count:
        print(f"global variables = {len(globals_)}")
        print(f"templates with controller variables = {len(ctrl)}")
        print(f"include hand-offs = {sum(len(t) for t in passes.values())}")
        print(f"local assignments = {sum(len(v['set']) for v in sets.values())}")
        return 0
    swsource.emit(render(args.source), args.out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
