#!/usr/bin/env python3
"""Shared parsing of the Ventrata OCTO OpenAPI specification.

Every fact in this plugin is derived here, so extraction and verification cannot drift
apart: extract_spec.py renders what this module reports, verify_spec.py checks the shipped
files against the same report.
"""
from __future__ import annotations

import re
from typing import Any

import yaml

CAP_RE = re.compile(r"^From capability `octo/([a-z][a-z-]*)`\.?\s*(.*)$", re.S)
REF_RE = re.compile(r"#/components/schemas/(\w+)")
HTTP_METHODS = ("get", "post", "patch", "put", "delete")


def load(path: str) -> dict[str, Any]:
    with open(path, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def schemas(spec: dict) -> dict[str, Any]:
    return spec.get("components", {}).get("schemas", {}) or {}


def type_of(prop: dict) -> str:
    """Render a property's type the way a reader needs it, refs included."""
    if not isinstance(prop, dict):
        return "unknown"
    if "$ref" in prop:
        m = REF_RE.search(prop["$ref"])
        return m.group(1) if m else "object"
    for key in ("oneOf", "anyOf", "allOf"):
        if key in prop:
            parts = [type_of(p) for p in prop[key] if isinstance(p, dict)]
            uniq = [p for i, p in enumerate(parts) if p not in parts[:i]]
            return " | ".join(uniq) or "object"
    t = prop.get("type")
    if t == "array":
        return f"{type_of(prop.get('items') or {})}[]"
    if prop.get("format"):
        return f"{t} ({prop['format']})"
    return t or "object"


def split_fields(schema: dict) -> tuple[dict[str, dict], dict[str, dict[str, dict]]]:
    """Split a schema's properties into base fields and capability-gated fields.

    Capability attribution is machine-readable: such descriptions start with
    "From capability `octo/<name>`".
    """
    base: dict[str, dict] = {}
    caps: dict[str, dict[str, dict]] = {}
    required = set(schema.get("required") or [])
    for name, prop in (schema.get("properties") or {}).items():
        prop = prop if isinstance(prop, dict) else {}
        desc = (prop.get("description") or "").strip()
        ex = prop.get("example")
        if ex is None:
            ex = (prop.get("items") or {}).get("example")
        info = {
            "type": type_of(prop),
            "required": name in required,
            "nullable": bool(prop.get("nullable")),
            "enum": prop.get("enum") or (prop.get("items") or {}).get("enum") or [],
            "description": desc,
            "example": ex,
            "default": prop.get("default"),
        }
        m = CAP_RE.match(desc)
        if m:
            info["description"] = m.group(2).strip()
            caps.setdefault(f"octo/{m.group(1)}", {})[name] = info
        else:
            base[name] = info
    return base, caps


def closure(spec: dict, roots: list[str]) -> list[str]:
    """All schema names reachable from roots, so no referenced sub-schema is missed."""
    sch = schemas(spec)
    seen: list[str] = []
    queue = list(roots)
    while queue:
        name = queue.pop(0)
        if name in seen or name not in sch:
            continue
        seen.append(name)
        queue.extend(REF_RE.findall(yaml.safe_dump(sch[name], allow_unicode=True)))
    return seen


def operations(spec: dict, path_filter=None) -> list[dict]:
    """Flatten paths into operations, merging path-level and operation-level parameters."""
    out = []
    for path, item in (spec.get("paths") or {}).items():
        if path_filter and not path_filter(path):
            continue
        shared = item.get("parameters") or []
        for method, op in item.items():
            if method.lower() not in HTTP_METHODS or not isinstance(op, dict):
                continue
            params = []
            for p in shared + (op.get("parameters") or []):
                if not isinstance(p, dict):
                    continue
                sub = p.get("schema") or {}
                ex = p.get("example")
                if ex is None:
                    ex = sub.get("example")
                params.append(
                    {
                        "name": p.get("name", ""),
                        "in": p.get("in", ""),
                        "required": bool(p.get("required")),
                        "type": type_of(sub),
                        "enum": sub.get("enum") or (sub.get("items") or {}).get("enum") or [],
                        "description": (p.get("description") or "").strip(),
                        "example": ex,
                        "default": sub.get("default"),
                    }
                )
            body = op.get("requestBody") or {}
            body_ref = ""
            if body:
                for m in REF_RE.findall(yaml.safe_dump(body, allow_unicode=True)):
                    body_ref = m
                    break
            # Which schema each status code returns. A bare list of codes tells an
            # integrator nothing about what to parse.
            responses = {}
            for code, r in (op.get("responses") or {}).items():
                refs = REF_RE.findall(yaml.safe_dump(r or {}, allow_unicode=True))
                responses[str(code)] = {
                    "description": ((r or {}).get("description") or "").strip(),
                    "schema": refs[0] if refs else "",
                }
            out.append(
                {
                    "path": path,
                    "method": method.upper(),
                    "summary": (op.get("summary") or "").strip(),
                    "description": (op.get("description") or "").strip(),
                    "tags": op.get("tags") or [],
                    "params": params,
                    "requestBody": body_ref,
                    "responses": sorted(str(k) for k in (op.get("responses") or {})),
                    "responseDetail": responses,
                }
            )
    return out


def capability_index(spec: dict) -> dict[str, dict[str, list[str]]]:
    """capability -> schema -> fields, across every schema in the spec."""
    idx: dict[str, dict[str, list[str]]] = {}
    for name, schema in schemas(spec).items():
        _, caps = split_fields(schema)
        for cap, fields in caps.items():
            idx.setdefault(cap, {})[name] = sorted(fields)
    return idx


def schema_capability(schema: dict) -> str:
    """A capability declared on the schema itself, not on its fields.

    Some schemas exist only under a capability (Waitlist, Webhook) and say so in their own
    description rather than per field. Missing this hides whole response types.
    """
    m = CAP_RE.match((schema.get("description") or "").strip())
    return f"octo/{m.group(1)}" if m else ""


def response_schemas(spec: dict) -> dict[str, list[str]]:
    """Schema name -> the operations that return it.

    Response bodies are what an integrator parses, so every one of them has to be documented
    somewhere. Array wrappers are resolved to the item schema as well as recorded themselves.
    """
    out: dict[str, list[str]] = {}
    sch = schemas(spec)
    for path, item in (spec.get("paths") or {}).items():
        for method, op in (item or {}).items():
            if method.lower() not in HTTP_METHODS or not isinstance(op, dict):
                continue
            label = f"{method.upper()} {path}"
            for code, resp in (op.get("responses") or {}).items():
                for name in REF_RE.findall(yaml.safe_dump(resp, allow_unicode=True)):
                    out.setdefault(name, []).append(label)
                    items = (sch.get(name) or {}).get("items") or {}
                    for inner in REF_RE.findall(yaml.safe_dump(items, allow_unicode=True)):
                        out.setdefault(inner, []).append(label)
    return {k: sorted(set(v)) for k, v in out.items()}


def is_array(schema: dict) -> bool:
    return (schema or {}).get("type") == "array"


def array_item(schema: dict) -> str:
    m = REF_RE.search(yaml.safe_dump((schema or {}).get("items") or {}, allow_unicode=True))
    return m.group(1) if m else ""


def enum_registry(spec: dict) -> dict[str, list[list[str]]]:
    """field name -> the distinct enum value sets the specification declares for it.

    Many fields carry a value set on one schema and only an example on another
    (`Booking.status` is an enum, `BookingUnitItem.status` is a bare string). The registry
    lets a renderer state the values in both places instead of leaving the reader guessing.
    """
    reg: dict[str, list[list[str]]] = {}
    for schema in schemas(spec).values():
        base, caps = split_fields(schema)
        for f, i in list(base.items()) + [(k, v) for d in caps.values() for k, v in d.items()]:
            if i["enum"] and i["enum"] not in reg.setdefault(f, []):
                reg[f].append(list(i["enum"]))
    for path, item in (spec.get("paths") or {}).items():
        for method, op in (item or {}).items():
            if method.lower() not in HTTP_METHODS or not isinstance(op, dict):
                continue
            for p in (item.get("parameters") or []) + (op.get("parameters") or []):
                if not isinstance(p, dict):
                    continue
                sub = p.get("schema") or {}
                en = sub.get("enum") or (sub.get("items") or {}).get("enum")
                name = p.get("name", "")
                if en and en not in reg.setdefault(name, []):
                    reg[name].append(list(en))
    return {k: v for k, v in reg.items() if v}


def inferred_enum(registry: dict, field: str, example) -> list[str]:
    """The value set a field belongs to, chosen by which set contains its example.

    Only returns a set when the example makes the choice unambiguous: with two candidate
    sets and no example, guessing would be worse than staying silent.
    """
    sets = registry.get(field) or []
    if not sets:
        return []
    if len(sets) == 1:
        return sets[0]
    hits = [s for s in sets if example is not None and str(example) in s]
    return hits[0] if len(hits) == 1 else []


def counts(spec: dict) -> dict[str, int]:
    sch = schemas(spec)
    ops = len(operations(spec))
    cap_fields = sum(
        len(f) for s in sch.values() for f in split_fields(s)[1].values()
    )
    return {
        "paths": len(spec.get("paths") or {}),
        "operations": ops,
        "schemas": len(sch),
        "capabilityFields": cap_fields,
    }
