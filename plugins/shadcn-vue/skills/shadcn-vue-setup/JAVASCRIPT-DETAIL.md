# shadcn-vue: JavaScript (Non-TypeScript) Usage

shadcn-vue is written in TypeScript but provides JavaScript versions of components.
To opt out of TypeScript, set `"typescript": false` in `components.json`.

## components.json with TypeScript disabled

```json
{
  "style": "default",
  "tailwind": {
    "config": "tailwind.config.js",
    "css": "src/app/globals.css",
    "baseColor": "zinc",
    "cssVariables": true
  },
  "typescript": false,
  "aliases": {
    "utils": "~/lib/utils",
    "components": "~/components"
  }
}
```

With `"typescript": false`, the CLI adds components as JavaScript `.vue` files
(without `<script setup lang="ts">` annotations).

## jsconfig.json for path aliases

When not using TypeScript, configure path aliases in `jsconfig.json`:

```json
{
  "compilerOptions": {
    "paths": {
      "@/*": ["./*"]
    }
  }
}
```

## CLI behavior

The CLI reads `typescript` from `components.json` and generates appropriate files.
No extra flags are needed when adding components — the project setting is applied
automatically.

Source: `/tmp/shadcn-vue-repo/apps/v4/content/docs/07.javascript.md`
