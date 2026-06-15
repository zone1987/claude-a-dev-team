# shadcn-vue: components.json Reference

The `components.json` file holds configuration for your project. It is only required
if you use the CLI. Generate it with:

```bash
npx shadcn-vue@latest init
```

## $schema

```json
{
  "$schema": "https://shadcn-vue.com/schema.json"
}
```

JSON Schema URL: https://shadcn-vue.com/schema.json

## style

The visual style for your components. **Cannot be changed after initialization.**

```json
{
  "style": "new-york"
}
```

The `default` style is deprecated. Use `new-york` for new projects.

## typescript

Choose between TypeScript or JavaScript components.
Setting `false` generates `.vue` files without TypeScript.

```json
{
  "typescript": true
}
```

```json
{
  "typescript": false
}
```

## tailwind

### tailwind.config

Path to your `tailwind.config.js` or `tailwind.config.ts` file.
**For Tailwind CSS v4, leave this blank (`""`).**

```json
{
  "tailwind": {
    "config": "tailwind.config.js"
  }
}
```

```json
{
  "tailwind": {
    "config": ""
  }
}
```

### tailwind.css

Path to the CSS file that imports Tailwind CSS into your project.

```json
{
  "tailwind": {
    "css": "styles/global.css"
  }
}
```

### tailwind.baseColor

Controls the default color palette generated for your components.
**Cannot be changed after initialization.**

```json
{
  "tailwind": {
    "baseColor": "neutral"
  }
}
```

Available values: `"gray"` | `"neutral"` | `"slate"` | `"stone"` | `"zinc"`

### tailwind.cssVariables

Controls theming approach: CSS variables (`true`) or Tailwind utility classes (`false`).

```json
{
  "tailwind": {
    "cssVariables": true
  }
}
```

**Cannot be changed after initialization.** To switch, delete and re-install components.

To initialize without CSS variables:

```bash
npx shadcn-vue@latest init --no-css-variables
```

### tailwind.prefix

Prefix for all Tailwind CSS utility classes. Components are added with this prefix.

```json
{
  "tailwind": {
    "prefix": "tw-"
  }
}
```

## aliases

The CLI uses these values together with the `paths` config in `tsconfig.json` or
`jsconfig.json` to place generated components in the correct location.

**Important:** If you use the `src` directory, it must be included under `paths` in
`tsconfig.json` or `jsconfig.json`.

### aliases.utils

Import alias for utility functions.

```json
{
  "aliases": {
    "utils": "@/lib/utils"
  }
}
```

### aliases.components

Import alias for components.

```json
{
  "aliases": {
    "components": "@/components"
  }
}
```

### aliases.ui

Import alias for `ui` components. Controls where the CLI places `ui` components.

```json
{
  "aliases": {
    "ui": "@/app/ui"
  }
}
```

### aliases.lib

Import alias for `lib` functions such as `cn` or `valueUpdater`.

```json
{
  "aliases": {
    "lib": "@/lib"
  }
}
```

### aliases.composables

Import alias for composables such as `useMediaQuery` or `useToast`.

```json
{
  "aliases": {
    "composables": "@/composables"
  }
}
```

## iconLibrary

The icon library to use for components. Set during `init` via `--icon-library`.

Available values: `"lucide"` | `"tabler"` | `"hugeicons"` | `"phosphor"` | `"remixicon"`

```json
{
  "iconLibrary": "lucide"
}
```

## pointer

Enable pointer cursor for buttons (adds `cursor-pointer`).

```json
{
  "pointer": false
}
```

Set via `--pointer` / `--no-pointer` during init.

## rtl

Enable RTL (right-to-left) support.

```json
{
  "rtl": false
}
```

Set via `--rtl` / `--no-rtl` during init. Can be migrated later via:

```bash
npx shadcn-vue@latest migrate rtl
```

## Complete Example (from manual installation)

```json
{
  "$schema": "https://shadcn-vue.com/schema.json",
  "style": "new-york",
  "typescript": true,
  "tailwind": {
    "config": "",
    "css": "src/styles/globals.css",
    "baseColor": "neutral",
    "cssVariables": true,
    "prefix": ""
  },
  "aliases": {
    "components": "@/components",
    "composables": "@/composables",
    "utils": "@/lib/utils",
    "ui": "@/components/ui",
    "lib": "@/lib"
  },
  "iconLibrary": "lucide",
  "pointer": false,
  "rtl": false
}
```

Source: `/tmp/shadcn-vue-repo/apps/v4/content/docs/03.components-json.md`
and `/tmp/shadcn-vue-repo/apps/v4/content/docs/installation/05.manual.md`
