# components.json — Field Reference

## $schema

JSON Schema URL for validation.
```json
{ "$schema": "https://ui.shadcn.com/schema.json" }
```

## style

Component style variant. **Cannot be changed after initialisation.**
```json
{ "style": "new-york" }
```
Note: `default` style is deprecated. Use `new-york`.

## rsc

Enable React Server Components support.
When `true`, the CLI automatically adds `"use client"` directive to client
components.
```json
{ "rsc": true }
```

## tsx

Use TypeScript (`.tsx`) or JavaScript (`.jsx`) components.
```json
{ "tsx": true }   // TypeScript (default)
{ "tsx": false }  // JavaScript
```

## tailwind

### tailwind.config

Path to `tailwind.config.js` or `tailwind.config.ts`.
**For Tailwind CSS v4, leave this blank.**
```json
{ "tailwind": { "config": "tailwind.config.js" } }
{ "tailwind": { "config": "" } }  // Tailwind v4
```

### tailwind.css

Path to the CSS file that imports Tailwind CSS.
```json
{ "tailwind": { "css": "app/globals.css" } }
{ "tailwind": { "css": "src/index.css" } }
```

### tailwind.baseColor

Controls the default theme token values generated on `init`.
**Cannot be changed after initialisation.**

Available values: `neutral` | `stone` | `zinc` | `mauve` | `olive` | `mist` | `taupe`
```json
{ "tailwind": { "baseColor": "neutral" } }
```

### tailwind.cssVariables

`true` (recommended): generates semantic CSS variable tokens (`bg-background`,
`text-foreground`, etc.).
`false`: generates inline Tailwind color utilities (`bg-zinc-950`, etc.).
**Cannot be changed after initialisation.** Switching requires deleting and
re-installing all components.
```json
{ "tailwind": { "cssVariables": true } }
```

Initialise without CSS variables:
```bash
npx shadcn@latest init --no-css-variables
```

### tailwind.prefix

Prefix for all Tailwind utility classes. Components will be added using this
prefix.
```json
{ "tailwind": { "prefix": "tw-" } }
```

## aliases

The CLI uses aliases to place generated components and rewrite imports.

Backed by either:
1. `compilerOptions.paths` in `tsconfig.json` / `jsconfig.json`
2. `package.json#imports` with `moduleResolution: "bundler"` and
   `resolvePackageJsonImports: true`

### aliases.components
```json
{ "aliases": { "components": "@/components" } }
```

### aliases.utils
```json
{ "aliases": { "utils": "@/lib/utils" } }
```

### aliases.ui

Determines where the CLI installs UI components.
```json
{ "aliases": { "ui": "@/components/ui" } }
// Custom location:
{ "aliases": { "ui": "@/app/ui" } }
```

### aliases.lib

Alias for lib functions (format-date, generate-id, etc.).
```json
{ "aliases": { "lib": "@/lib" } }
```

### aliases.hooks

Alias for hooks (use-media-query, use-toast, etc.).
```json
{ "aliases": { "hooks": "@/hooks" } }
```

## iconLibrary

Icon library to use in components.
```json
{ "iconLibrary": "lucide" }
```

Source: `/tmp/shadcn-repo/apps/v4/content/docs/(root)/components-json.mdx`
