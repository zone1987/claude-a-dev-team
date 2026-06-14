---
name: shadcn-javascript
description: >
  shadcn/ui with JavaScript (no TypeScript) — tsx: false in components.json,
  .jsx file extension, jsconfig.json paths alias. Use when asked about shadcn
  JavaScript, no TypeScript, shadcn JS, tsx false, jsx components.
---

# shadcn/ui — JavaScript

shadcn/ui is written in TypeScript, but provides JavaScript components via
the CLI.

## Enable JavaScript mode

Set `tsx` to `false` in `components.json`:

```json
{
  "style": "new-york",
  "rsc": false,
  "tsx": false,
  "tailwind": {
    "config": "",
    "css": "src/app/globals.css",
    "baseColor": "zinc",
    "cssVariables": true
  },
  "iconLibrary": "lucide",
  "aliases": {
    "components": "@/components",
    "utils": "@/lib/utils",
    "ui": "@/components/ui",
    "lib": "@/lib",
    "hooks": "@/hooks"
  }
}
```

Components will be added with `.jsx` extension.

## Configure import aliases (jsconfig.json)

```json
{
  "compilerOptions": {
    "paths": {
      "@/*": ["./*"]
    }
  }
}
```

Source: `/tmp/shadcn-repo/apps/v4/content/docs/(root)/javascript.mdx`
