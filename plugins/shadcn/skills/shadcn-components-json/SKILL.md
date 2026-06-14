---
name: shadcn-components-json
description: >
  shadcn/ui components.json configuration — all fields: $schema, style, rsc,
  tsx, tailwind.config, tailwind.css, tailwind.baseColor, tailwind.cssVariables,
  tailwind.prefix, aliases.components, aliases.utils, aliases.ui, aliases.lib,
  aliases.hooks, iconLibrary, registries. Use when asked about components.json,
  shadcn config file, aliases setup, private registry configuration.
---

# shadcn/ui — components.json

`components.json` holds project configuration used by the CLI to generate
components customised for your project.

It is optional — only required when using the CLI to add components.
Copy-and-paste users do not need it.

Create it: `npx shadcn@latest init`

## Complete field reference

```json
{
  "$schema": "https://ui.shadcn.com/schema.json",
  "style": "new-york",
  "rsc": true,
  "tsx": true,
  "tailwind": {
    "config": "",
    "css": "app/globals.css",
    "baseColor": "neutral",
    "cssVariables": true,
    "prefix": ""
  },
  "iconLibrary": "lucide",
  "aliases": {
    "components": "@/components",
    "utils": "@/lib/utils",
    "ui": "@/components/ui",
    "lib": "@/lib",
    "hooks": "@/hooks"
  },
  "registries": {
    "@v0": "https://v0.dev/chat/b/{name}",
    "@acme": {
      "url": "https://registry.acme.com/{name}.json",
      "headers": {
        "Authorization": "Bearer ${REGISTRY_TOKEN}"
      },
      "params": {
        "version": "latest"
      }
    }
  }
}
```

## Reference files

- [references/fields.md](references/fields.md)
- [references/registries.md](references/registries.md)

Source: `/tmp/shadcn-repo/apps/v4/content/docs/(root)/components-json.mdx`
