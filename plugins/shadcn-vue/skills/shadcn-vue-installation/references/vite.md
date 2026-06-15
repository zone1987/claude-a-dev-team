# shadcn-vue Installation: Vite

## Step 1: Create project

```bash
npm create vite@latest my-vue-app --template vue-ts
```

## Step 2: Add Tailwind CSS

```bash
npm install tailwindcss @tailwindcss/vite
```

Replace everything in `src/style.css`:

```css
@import "tailwindcss";
```

## Step 3: Edit tsconfig.json

Add `baseUrl` and `paths` to `compilerOptions` in both `tsconfig.json` and `tsconfig.app.json`:

```json
{
  "files": [],
  "references": [
    { "path": "./tsconfig.app.json" },
    { "path": "./tsconfig.node.json" }
  ],
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["./src/*"]
    }
  }
}
```

## Step 4: Edit tsconfig.app.json

```json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["./src/*"]
    }
  }
}
```

## Step 5: Update vite.config.ts

### Option A: resolve alias

```bash
npm install -D @types/node
```

```typescript
import path from 'node:path'
import { defineConfig } from 'vite'
import tailwindcss from '@tailwindcss/vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue(), tailwindcss()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },
})
```

### Option B: vite-tsconfig-paths

```bash
npm install -D vite-tsconfig-paths
```

```typescript
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import tailwindcss from '@tailwindcss/vite'
import tsconfigPaths from 'vite-tsconfig-paths'

export default defineConfig({
  plugins: [vue(), tailwindcss(), tsconfigPaths()],
})
```

## Step 6: Run the CLI

```bash
npx shadcn-vue@latest init
# Which color would you like to use as base color? › Neutral
```

## Step 7: Add Components

```bash
npx shadcn-vue@latest add button
```

Usage:

```vue
<script setup lang="ts">
import { Button } from '@/components/ui/button'
</script>

<template>
  <div>
    <Button>Click me</Button>
  </div>
</template>
```

Source: `/tmp/shadcn-vue-repo/apps/v4/content/docs/installation/01.vite.md`
