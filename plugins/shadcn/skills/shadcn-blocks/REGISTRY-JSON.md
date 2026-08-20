# shadcn-registry-json

Complete schema reference for `registry.json` — the entry point of every
shadcn-compatible registry.

## Schema URL

`https://ui.shadcn.com/schema/registry.json`

## Fields

See [schema-fields.md](`REGISTRY-JSON-SCHEMA-FIELDS.md`) for a full per-field
reference with examples.

## Minimal example

```json
{
  "$schema": "https://ui.shadcn.com/schema/registry.json",
  "name": "acme",
  "homepage": "https://acme.com",
  "items": []
}
```

## Composed example (include)

```json
{
  "$schema": "https://ui.shadcn.com/schema/registry.json",
  "name": "acme",
  "homepage": "https://acme.com",
  "include": [
    "components/ui/registry.json",
    "hooks/registry.json"
  ]
}
```

Root `registry.json` must define `name` and `homepage`.
Included files may omit both.

Source: registry/registry-json.mdx
