---
name: shadcn-registry-item-json
description: Schema von registry-item.json — alle Felder: name, type (registry:ui/block/lib/hook/page/file/theme/style), title, description, files[], dependencies, registryDependencies, cssVars, css, tailwind, envVars, meta, docs. Trigger: registry-item.json, shadcn item schema, registry:ui type.
---

# shadcn-registry-item-json

Complete schema reference for `registry-item.json` — defines a single
installable item in any shadcn registry.

## Schema URL

`https://ui.shadcn.com/schema/registry-item.json`

## References

- [fields.md](references/fields.md) — Every top-level field documented
- [types.md](references/types.md) — All `registry:*` type values
- [files.md](references/files.md) — `files[]` object: path, type, target, placeholders
- [cssvars-css.md](references/cssvars-css.md) — `cssVars`, `css`, animations
- [advanced.md](references/advanced.md) — `font`, `envVars`, `tailwind`, `meta`, `categories`, `docs`, `extends`, `config`

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
