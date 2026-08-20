# shadcn-registry-item-json

Complete schema reference for `registry-item.json` — defines a single
installable item in any shadcn registry.

## Schema URL

`https://ui.shadcn.com/schema/registry-item.json`

## References

- [fields.md](`REGISTRY-ITEM-JSON-FIELDS.md`) — Every top-level field documented
- [types.md](`REGISTRY-ITEM-JSON-TYPES.md`) — All `registry:*` type values
- [files.md](`REGISTRY-ITEM-JSON-FILES.md`) — `files[]` object: path, type, target, placeholders
- [cssvars-css.md](`REGISTRY-ITEM-JSON-CSSVARS-CSS.md`) — `cssVars`, `css`, animations
- [advanced.md](`REGISTRY-ITEM-JSON-ADVANCED.md`) — `font`, `envVars`, `tailwind`, `meta`, `categories`, `docs`, `extends`, `config`

## Minimal example

```json
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "button",
  "type": "registry:ui",
  "files": [{ "path": "components/ui/button.tsx", "type": "registry:ui" }]
}
```

Source: registry/registry-item-json.mdx
