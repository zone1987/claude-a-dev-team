# Registry Structure

## Requirements

- `registry.json` (or JSON payload) at the root of the registry endpoint
- Must conform to registry.json schema and registry-item.json schema
- Any framework that can serve JSON over HTTP is supported (Next.js, Vite, PHP…)

## Option A: Single registry.json

All items in one file at project root.

```json
{
  "$schema": "https://ui.shadcn.com/schema/registry.json",
  "name": "acme",
  "homepage": "https://acme.com",
  "items": [
    {
      "name": "button",
      "type": "registry:ui",
      "title": "Button",
      "description": "A simple button component.",
      "files": [
        {
          "path": "components/ui/button.tsx",
          "type": "registry:ui"
        }
      ]
    }
  ]
}
```

## Option B: include composition

For large registries, compose from multiple `registry.json` files.

```
registry.json        <- root (name, homepage, include)
components/ui/
  registry.json      <- items with paths relative to this file
  button.tsx
hooks/
  registry.json
  use-toggle.ts
```

Root `registry.json`:

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

Sub-`registry.json` (may omit `name` and `homepage`):

```json
{
  "$schema": "https://ui.shadcn.com/schema/registry.json",
  "items": [
    {
      "name": "button",
      "type": "registry:ui",
      "files": [{ "path": "button.tsx", "type": "registry:ui" }]
    }
  ]
}
```

When using `include`, file `path` values are relative to the declaring
`registry.json`, not the project root.

Item names must be unique across the resolved registry (all included files).

## Item guidelines

- Place source files under `registry/[STYLE]/[NAME]/` (e.g. `registry/default/button/button.tsx`).
- List all registry deps in `registryDependencies` (bare names, `@ns/item`,
  `owner/repo/item`, or full URLs).
- List all npm deps in `dependencies` (use `name@version` for pinning).
- Imports inside registry source files must use `@/registry` path.
- Include a proper `title` and `description` — LLMs use these.

Source: registry/getting-started.mdx
