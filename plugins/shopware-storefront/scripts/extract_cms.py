#!/usr/bin/env python3
"""Map CMS element types to their resolver and their storefront template.

A Shopping Experiences slot has three parts: an administration component, a
DataResolver that loads the data server-side, and a template that renders it.
This maps the type string that ties them together, and reports both directions
of mismatch — a resolver without a template, a template without a resolver.

    extract_cms.py --source <vendor/shopware> --out FILE
    extract_cms.py --source <vendor/shopware> --verify
"""
from __future__ import annotations

import argparse
import os
import re
import sys

import swsource

CORE = "core"
ELEMENT_DIR = "storefront/Resources/views/storefront/element"
BLOCK_DIR = "storefront/Resources/views/storefront/block"
ADMIN_CMS = "administration/Resources/app/administration/src/module/sw-cms"

CLASS_RE = re.compile(r"(?:abstract\s+)?class\s+(\w+)(?:\s+extends\s+(\w+))?")
# getType() returns either a literal or a class constant defined nearby.
TYPE_LITERAL_RE = re.compile(
    r"function getType\(\s*\)\s*:\s*string\s*\{\s*return\s*['\"]([^'\"]+)['\"]", re.S
)
TYPE_CONST_RE = re.compile(
    r"function getType\(\s*\)\s*:\s*string\s*\{\s*return\s*(?:self|static)::(\w+)", re.S
)
CONST_RE = re.compile(r"const\s+(\w+)\s*=\s*['\"]([^'\"]+)['\"]")
COLLECT_RE = re.compile(r"function collect\(")
ENRICH_RE = re.compile(r"function enrich\(")


def find_resolvers(source: str):
    """Every class implementing the CMS element resolver contract."""
    root = os.path.join(source, CORE)
    out = []
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
            if "CmsElementResolverInterface" not in text and "CmsElementResolver" not in text:
                if "TypeDataResolver" not in text:
                    continue
            match = CLASS_RE.search(text)
            if not match:
                continue
            cls, parent = match.group(1), match.group(2) or ""
            if not (
                parent.endswith("CmsElementResolver")
                or parent.endswith("TypeDataResolver")
                or "implements CmsElementResolverInterface" in text
                or cls.endswith("CmsElementResolver")
                or cls.endswith("TypeDataResolver")
            ):
                continue
            consts = dict(CONST_RE.findall(text))
            literal = TYPE_LITERAL_RE.search(text)
            const = TYPE_CONST_RE.search(text)
            type_name = ""
            if literal:
                type_name = literal.group(1)
            elif const:
                type_name = consts.get(const.group(1), "")
            out.append(
                {
                    "class": cls,
                    "parent": parent,
                    "type": type_name,
                    "file": os.path.relpath(full, root).replace(os.sep, "/"),
                    "abstract": text.lstrip().startswith("abstract")
                    or "abstract class" in text[: match.end() + 20],
                    "collect": bool(COLLECT_RE.search(text)),
                    "enrich": bool(ENRICH_RE.search(text)),
                }
            )
    return out


REG_ELEMENT_RE = re.compile(r"registerCmsElement\(\s*\{(.*?)\n\}\s*\)", re.S)
REG_BLOCK_RE = re.compile(r"registerCmsBlock\(\s*\{(.*?)\n\}\s*\)", re.S)
FIELD_RE = re.compile(r"^\s{4}(\w+):\s*['\"]([^'\"]*)['\"]", re.M)
DEFAULT_CFG_RE = re.compile(r"defaultConfig:\s*\{(.*?)\n    \},", re.S)
DEFAULT_CFG_REF_RE = re.compile(r"defaultConfig:\s*(\w+)\s*,")
CONST_DECL_RE = re.compile(r"const\s+(\w+)\s*=\s*\{(.*?)\n\};", re.S)
SPREAD_RE = re.compile(r"\.\.\.(\w+),?")
CFG_KEY_RE = re.compile(r"^\s{4,8}(\w+):\s*\{", re.M)
CFG_FIELD_RE = re.compile(r"^(\s{4,8})(\w+):\s*\{", re.M)
SOURCE_RE = re.compile(r"source:\s*['\"](\w+)['\"]")
VALUE_RE = re.compile(r"value:\s*(.+?)(?:,\s*$|,\s*\n)", re.M)
REQUIRED_RE = re.compile(r"required:\s*(true|false)")
ENTITY_NAME_RE = re.compile(r"entity:\s*\{[^}]*?name:\s*['\"](\w+)['\"]", re.S)


def _value_type(raw: str) -> str:
    """Classify a defaultConfig value literal into the type Twig will see."""
    raw = raw.strip().rstrip(",").strip()
    if raw in ("null", ""):
        return "null"
    if raw in ("true", "false"):
        return "bool"
    if raw.startswith("[") :
        return "array"
    if raw.startswith("{"):
        return "object"
    if raw.startswith(("'", '"', "`")):
        return "string"
    if re.fullmatch(r"-?\d+", raw):
        return "int"
    if re.fullmatch(r"-?\d*\.\d+", raw):
        return "float"
    if raw.startswith("Shopware.Constants"):
        return "constant"
    return "expression"


def parse_config_fields(body: str):
    """Return one entry per configuration field, later spreads overriding earlier ones.

    A field is an object carrying `source`; nested keys such as the `entity` descriptor
    are not fields themselves and are skipped.
    """
    fields = {}
    matches = list(CFG_FIELD_RE.finditer(body))
    for index, match in enumerate(matches):
        name = match.group(2)
        end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
        chunk = body[match.end():end]
        source = SOURCE_RE.search(chunk)
        if not source:
            continue  # not a configuration field, e.g. the nested entity descriptor
        value = VALUE_RE.search(chunk)
        required = REQUIRED_RE.search(chunk)
        entity = ENTITY_NAME_RE.search(chunk)
        raw = value.group(1) if value else ""
        fields[name] = {
            "name": name,
            "source": source.group(1),
            "type": _value_type(raw),
            "default": raw.strip().rstrip(",").strip()[:40],
            "required": bool(required and required.group(1) == "true"),
            "entity": entity.group(1) if entity else "",
        }
    return list(fields.values())
SLOTS_RE = re.compile(r"slots:\s*\{(.*?)\n    \},?", re.S)
SLOT_KEY_RE = re.compile(r"^\s{8}(\w+):\s*(?:\{|['\"](\w[\w-]*)['\"])", re.M)
SLOT_TYPE_RE = re.compile(r"type:\s*['\"]([\w-]+)['\"]")


def _resolve_constants(folder: str, text: str):
    """Collect const objects from this file and any sibling it imports from."""
    consts = dict((n, b) for n, b in CONST_DECL_RE.findall(text))
    # Imports are relative and may reach a sibling element's folder (../image/...).
    for match in re.finditer(r"from\s+['\"](\.[\w./-]+)['\"]", text):
        for suffix in (".ts", ".js", "/index.ts", "/index.js", ""):
            path = os.path.normpath(os.path.join(folder, match.group(1) + suffix))
            if os.path.isfile(path):
                with open(path, encoding="utf-8", errors="replace") as handle:
                    consts.update(dict(CONST_DECL_RE.findall(handle.read())))
                break
    return consts


def _expand(body: str, consts: dict, depth: int = 0) -> str:
    """Inline ...SPREAD references so every field is visible in one body."""
    if depth > 4:
        return body
    def swap(match):
        name = match.group(1)
        return _expand(consts.get(name, ""), consts, depth + 1) if name in consts else ""
    return SPREAD_RE.sub(swap, body)


def admin_elements(source: str):
    """Parse registerCmsElement() calls: name, components, defaultConfig fields."""
    root = os.path.join(source, ADMIN_CMS, "elements")
    out = {}
    if not os.path.isdir(root):
        return out
    for entry in sorted(os.listdir(root)):
        folder = os.path.join(root, entry)
        if not os.path.isdir(folder):
            continue
        for candidate in ("index.ts", "index.js"):
            path = os.path.join(folder, candidate)
            if os.path.isfile(path):
                break
        else:
            continue
        with open(path, encoding="utf-8", errors="replace") as handle:
            text = handle.read()
        block = REG_ELEMENT_RE.search(text)
        if not block:
            continue
        body = block.group(1)
        fields = dict(FIELD_RE.findall(body))
        consts = _resolve_constants(folder, text)
        cfg = DEFAULT_CFG_RE.search(body)
        cfg_body = cfg.group(1) if cfg else ""
        if not cfg_body:
            # defaultConfig may point at an imported constant instead of a literal.
            ref = DEFAULT_CFG_REF_RE.search(body)
            if ref:
                cfg_body = consts.get(ref.group(1), "")
        cfg_body = _expand(cfg_body, consts)
        out[fields.get("name", entry)] = {
            "dir": entry,
            "label": fields.get("label", ""),
            "component": fields.get("component", ""),
            "configComponent": fields.get("configComponent", ""),
            "previewComponent": fields.get("previewComponent", ""),
            "config": [f["name"] for f in parse_config_fields(cfg_body)],
            "fields": parse_config_fields(cfg_body),
        }
    return out


def admin_blocks(source: str):
    """Parse registerCmsBlock() calls: name, category and the slots it declares."""
    root = os.path.join(source, ADMIN_CMS, "blocks")
    out = {}
    if not os.path.isdir(root):
        return out
    for dirpath, _dirs, files in os.walk(root):
        for candidate in ("index.ts", "index.js"):
            if candidate not in files:
                continue
            path = os.path.join(dirpath, candidate)
            with open(path, encoding="utf-8", errors="replace") as handle:
                text = handle.read()
            block = REG_BLOCK_RE.search(text)
            if not block:
                continue
            body = block.group(1)
            fields = dict(FIELD_RE.findall(body))
            slots_m = SLOTS_RE.search(body)
            slots = []
            if slots_m:
                for name, inline in SLOT_KEY_RE.findall(slots_m.group(1)):
                    if inline:
                        slots.append((name, inline))
                    else:
                        after = slots_m.group(1).split(name + ":", 1)[-1]
                        type_m = SLOT_TYPE_RE.search(after[:400])
                        slots.append((name, type_m.group(1) if type_m else "?"))
            name = fields.get("name")
            if name:
                out[name] = {
                    "category": fields.get("category", ""),
                    "label": fields.get("label", ""),
                    "component": fields.get("component", ""),
                    "slots": slots,
                }
    return out


def templates(source: str, subdir: str, prefix: str):
    root = os.path.join(source, subdir)
    found = {}
    if not os.path.isdir(root):
        return found
    for name in sorted(os.listdir(root)):
        if name.startswith(prefix) and name.endswith(".html.twig"):
            found[name[len(prefix): -len(".html.twig")]] = name
    return found


def render(source: str) -> list[str]:
    resolvers = find_resolvers(source)
    concrete = [r for r in resolvers if r["type"]]
    elements = templates(source, ELEMENT_DIR, "cms-element-")
    blocks = templates(source, BLOCK_DIR, "cms-block-")
    by_type = {r["type"]: r for r in concrete}
    admin_el = admin_elements(source)
    admin_bl = admin_blocks(source)

    lines = [swsource.stamp("extract_cms.py", source, ELEMENT_DIR), ""]
    lines.append("# Shopware Storefront — CMS element, resolver and template map")
    lines.append("")
    lines.append(
        "Shopping Experiences render a page from sections, blocks and elements. An element "
        "is the smallest unit and the one that carries data: its resolver runs server-side "
        "and attaches the result, which the template reads as `element.data`."
    )
    lines.append("")
    lines.append(
        f"**{len(admin_el)} administration elements, {len(concrete)} resolvers, "
        f"{len(elements)} element templates; {len(admin_bl)} administration blocks "
        f"and {len(blocks)} block templates.**"
    )
    lines.append("")
    lines += swsource.toc(
        [
            "The four parts of an element",
            "How a slot is rendered",
            "Element type to resolver and template",
            "Element configuration fields",
            "Element templates without a resolver",
            "Blocks and the slots they declare",
            "Abstract resolvers",
        ]
    )

    lines.append("## The four parts of an element")
    lines.append("")
    lines.append(
        "One element type name ties four files together. The name is the join key "
        "everywhere: in `registerCmsElement({name})`, in the resolver's `getType()`, and "
        "in the template filename."
    )
    lines.append("")
    lines.append("| Part | Where | What it does |")
    lines.append("|---|---|---|")
    lines.append(
        "| Registration | `administration/.../sw-cms/elements/<name>/index.ts` | "
        "Declares the element and its `defaultConfig` — the fields the editor can set |"
    )
    lines.append(
        "| Editor components | `component/`, `config/`, `preview/` beside it | "
        "How the element looks while editing, its settings form, its thumbnail |"
    )
    lines.append(
        "| Resolver | `core/.../Cms/<Name>CmsElementResolver.php` | "
        "Loads data server-side; `getType()` returns the same name |"
    )
    lines.append(
        "| Storefront template | `storefront/element/cms-element-<name>.html.twig` | "
        "Renders it, reading `element.config` and `element.data` |"
    )
    lines.append("")
    lines.append(
        "A field in `defaultConfig` becomes `element.config.<field>.value` in Twig. That "
        "is the contract between the two ends: adding a configuration field means adding "
        "it to `defaultConfig` and reading it in the template."
    )
    lines.append("")

    lines.append("## How a slot is rendered")
    lines.append("")
    lines.append("```")
    lines.append("cms_page -> section -> block -> slot")
    lines.append("  slot.type            e.g. 'product-slider'")
    lines.append("  -> resolver          getType() returns the same string")
    lines.append("       collect()       declares the criteria, batched across all slots")
    lines.append("       enrich()        calls $slot->setData(...)")
    lines.append("  -> cms-element-<type>.html.twig")
    lines.append("       element.data    what enrich() attached")
    lines.append("       element.config  what the editor configured in the administration")
    lines.append("```")
    lines.append("")
    lines.append(
        "`collect()` returning `null` means nothing is loaded for that slot. Configuration "
        "is read through `element.config.<field>.value` in Twig, and through "
        "`$slot->getFieldConfig()` in PHP."
    )
    lines.append("")

    lines.append("## Element type to resolver and template")
    lines.append("")
    lines.append("| Type | Admin component | Resolver | collect/enrich | Template |")
    lines.append("|---|---|---|---|---|")
    for type_name in sorted(set(by_type) | set(admin_el) | set(elements)):
        res = by_type.get(type_name)
        tpl = elements.get(type_name)
        adm = admin_el.get(type_name)
        methods = "—"
        if res:
            methods = ", ".join(
                m for m, present in (("collect", res["collect"]), ("enrich", res["enrich"])) if present
            ) or "inherited"
        lines.append(
            f"| `{type_name}` | {'`' + adm['component'] + '`' if adm else '—'} | "
            f"{'`' + res['class'] + '`' if res else '—'} | {methods} | "
            f"{'`storefront/element/' + tpl + '`' if tpl else '—'} |"
        )
    lines.append("")
    lines.append(
        "A dash means that part does not exist for the type: an element with no resolver "
        "gets its data another way, and an element with no template is not rendered by "
        "this bundle."
    )
    lines.append("")
    lines.append("Resolver files are under `vendor/shopware/core/`:")
    lines.append("")
    for type_name in sorted(by_type):
        lines.append(f"- `{by_type[type_name]['class']}` — `{by_type[type_name]['file']}`")
    lines.append("")

    lines.append("## Element configuration fields")
    lines.append("")
    lines.append(
        "What the editor can configure per element, and therefore what the template can "
        "read as `element.config.<field>.value`."
    )
    lines.append("")
    lines.append(
        "Each field is an object, never a bare value. In PHP reach it through "
        "`$slot->getFieldConfig()->get('<field>')`, which returns a `FieldConfig` carrying "
        "`getSource()`, `getValue()`, plus typed accessors such as `getStringValue()` and "
        "`getArrayValue()`."
    )
    lines.append("")
    lines.append("**The four sources** a field can carry, from `FieldConfig`:")
    lines.append("")
    lines.append(
        "- **`static`** — the editor typed a literal value. `getValue()` returns it directly. "
        "This is what every default below declares."
    )
    lines.append(
        "- **`mapped`** — the value is a path into the current entity, such as "
        "`product.name`. Resolve it against the `EntityResolverContext`; the raw value is "
        "the path, not the content."
    )
    lines.append(
        "- **`default`** — a placeholder the element falls back to, typically a demo image."
    )
    lines.append(
        "- **`product_stream`** — the value is a product stream id the resolver turns into "
        "a criteria filter."
    )
    lines.append("")
    lines.append(
        "A field with an `entity` declares that its value is an id of that entity. The "
        "resolver fetches it in `collect()` and attaches the loaded record in `enrich()`, "
        "so the template reads the object from `element.data`, not from `element.config`."
    )
    lines.append("")
    no_config = sorted(n for n, i in admin_el.items() if not i["fields"])
    if no_config:
        lines.append(
            "Elements with no configuration at all: "
            + ", ".join(f"`{n}`" for n in no_config)
            + ". They render from context alone and expose nothing to configure."
        )
        lines.append("")
    for name in sorted(admin_el):
        info = admin_el[name]
        if not info["fields"]:
            continue
        lines.append(f"### {name}")
        lines.append("")
        lines.append(
            f"`administration/.../sw-cms/elements/{info['dir']}/` — "
            f"component `{info['component']}`, config form `{info['configComponent']}`"
        )
        lines.append("")
        lines.append("| Field | Source | Type | Default | Required | Entity |")
        lines.append("|---|---|---|---|---|---|")
        for field in info["fields"]:
            lines.append(
                f"| `{field['name']}` | `{field['source']}` | {field['type']} | "
                f"{'`' + field['default'] + '`' if field['default'] else '—'} | "
                f"{'yes' if field['required'] else '—'} | "
                f"{'`' + field['entity'] + '`' if field['entity'] else '—'} |"
            )
        lines.append("")
        lines.append(
            "In Twig: "
            + ", ".join(f"`element.config.{f['name']}.value`" for f in info["fields"][:3])
            + ("…" if len(info["fields"]) > 3 else "")
        )
        lines.append("")

    lines.append("## Element templates without a resolver")
    lines.append("")
    orphan_tpl = sorted(set(elements) - set(by_type))
    if orphan_tpl:
        lines.append(
            "These render without a server-side resolver. They read another slot's data, "
            "or fetch their own over a route at runtime."
        )
        lines.append("")
        for type_name in orphan_tpl:
            lines.append(f"- `storefront/element/{elements[type_name]}`")
    else:
        lines.append("Every element template has a resolver.")
    lines.append("")

    orphan_res = sorted(t for t in by_type if t not in elements)
    if orphan_res:
        lines.append("Resolvers whose type has no template in this bundle:")
        lines.append("")
        for type_name in orphan_res:
            lines.append(f"- `{type_name}` (`{by_type[type_name]['class']}`)")
        lines.append("")

    lines.append("## Blocks and the slots they declare")
    lines.append("")
    lines.append(
        "A block arranges elements and has no resolver of its own. Its registration names "
        "the slots it offers and the element type each slot takes by default, and its "
        "template includes `cms-element-<type>.html.twig` for each one."
    )
    lines.append("")
    lines.append("| Block | Category | Slots (name: default type) | Template |")
    lines.append("|---|---|---|---|")
    for name in sorted(set(admin_bl) | set(blocks)):
        info = admin_bl.get(name)
        tpl = blocks.get(name)
        slots = (
            ", ".join(f"`{s}`: `{t}`" for s, t in info["slots"])
            if info and info["slots"]
            else "—"
        )
        lines.append(
            f"| `{name}` | {info['category'] if info else '—'} | {slots} | "
            f"{'`storefront/block/' + tpl + '`' if tpl else '—'} |"
        )
    lines.append("")

    lines.append("## Abstract resolvers")
    lines.append("")
    lines.append("Base classes that carry shared behaviour rather than a type of their own.")
    lines.append("")
    for res in sorted(resolvers, key=lambda r: r["class"]):
        if not res["type"]:
            lines.append(f"- `{res['class']}` — `{res['file']}`")
    lines.append("")
    return lines


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    swsource.add_source_arg(parser)
    parser.add_argument("--verify", action="store_true", help="check both directions and exit non-zero on a gap")
    args = parser.parse_args()

    resolvers = find_resolvers(args.source)
    concrete = [r for r in resolvers if r["type"]]
    elements = templates(args.source, ELEMENT_DIR, "cms-element-")

    if args.count or args.verify:
        print(f"resolver classes = {len(resolvers)} ({len(concrete)} with a type)")
        print(f"element templates = {len(elements)}")
        missing_tpl = sorted(r["type"] for r in concrete if r["type"] not in elements)
        missing_res = sorted(set(elements) - {r["type"] for r in concrete})
        print(f"types without template = {missing_tpl or 'none'}")
        print(f"templates without resolver = {missing_res or 'none'}")
        if args.verify and missing_tpl:
            return 1
        return 0
    swsource.emit(render(args.source), args.out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
