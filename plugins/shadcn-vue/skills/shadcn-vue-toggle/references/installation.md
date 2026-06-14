# Toggle — Installation

## CLI (recommended)

```bash
npx shadcn-vue@latest add toggle
```

This copies `Toggle.vue` and `index.ts` to `src/components/ui/toggle/`.

## Manual

### 1. Install dependency

```bash
npm install reka-ui
```

Also required (already present in most shadcn-vue setups):

```bash
npm install class-variance-authority @vueuse/core
```

### 2. Copy source files

Copy `Toggle.vue` and `index.ts` from  
`registry/new-york-v4/ui/toggle/` into your project at `src/components/ui/toggle/`.

### 3. Adjust import paths

Replace `@/lib/utils` with the actual path to your `cn` utility and update any registry-internal imports.

## Usage

```vue
<script setup lang="ts">
import { Toggle } from '@/components/ui/toggle'
</script>

<template>
  <Toggle>Toggle</Toggle>
</template>
```
