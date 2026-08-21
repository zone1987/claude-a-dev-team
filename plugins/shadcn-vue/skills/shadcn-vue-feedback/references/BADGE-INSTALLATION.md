# Badge — Installation

## CLI (recommended)

```bash
npx shadcn-vue@latest add badge
```

This adds two files to your project:

- `components/ui/badge/index.ts` — CVA variants + type exports
- `components/ui/badge/Badge.vue` — the Vue component

## Manual installation

### 1. Install dependencies

The Badge component depends on `reka-ui` (for the `Primitive` component) and `class-variance-authority`:

```bash
npm install reka-ui class-variance-authority
```

> Note: `reka-ui` is used for the `Primitive` building block that enables the `as`/`asChild` pattern. It is not listed as a direct peer in all shadcn-vue docs versions, but it is a required runtime dependency.

You also need `@vueuse/core` for `reactiveOmit`:

```bash
npm install @vueuse/core
```

And `clsx` + `tailwind-merge` if you haven't already set up the `cn` utility:

```bash
npm install clsx tailwind-merge
```

### 2. Add the `cn` utility

Create `lib/utils.ts` if it doesn't exist:

```ts
import { clsx, type ClassValue } from "clsx"
import { twMerge } from "tailwind-merge"

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}
```

### 3. Copy the component files

Create `components/ui/badge/index.ts` and `components/ui/badge/Badge.vue` — see `references/source.md` for the full source.

### 4. Configure path alias

Make sure your `tsconfig.json` / `vite.config.ts` includes the `@` alias pointing to `src/` (or wherever your project root is):

```ts
// vite.config.ts
import { fileURLToPath, URL } from "node:url"
import { defineConfig } from "vite"

export default defineConfig({
  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", import.meta.url)),
    },
  },
})
```

### 5. Usage

```vue
<script setup lang="ts">
import { Badge } from "@/components/ui/badge"
</script>

<template>
  <Badge>New</Badge>
</template>
```
