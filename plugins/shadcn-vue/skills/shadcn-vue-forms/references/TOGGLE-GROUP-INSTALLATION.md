# ToggleGroup — Installation

## CLI (recommended)

```bash
npx shadcn-vue@latest add toggle-group
```

This copies `ToggleGroup.vue`, `ToggleGroupItem.vue`, and `index.ts` to `src/components/ui/toggle-group/`.

> Note: `toggle-group` depends on the `toggle` component for `toggleVariants`. The CLI installs both automatically.

## Manual

### 1. Install dependency

```bash
npm install reka-ui
```

Also required:

```bash
npm install class-variance-authority @vueuse/core
```

### 2. Install the Toggle component first

The `ToggleGroupItem` imports `toggleVariants` from `@/components/ui/toggle`. Install toggle first (see shadcn-vue-toggle skill).

### 3. Copy source files

Copy `ToggleGroup.vue`, `ToggleGroupItem.vue`, and `index.ts` from  
`registry/new-york-v4/ui/toggle-group/` into `src/components/ui/toggle-group/`.

### 4. Adjust import paths

Update the `@/registry/new-york-v4/ui/toggle` import in `ToggleGroupItem.vue` to `@/components/ui/toggle`.

## Usage

```vue
<script setup lang="ts">
import { ToggleGroup, ToggleGroupItem } from '@/components/ui/toggle-group'
</script>

<template>
  <ToggleGroup type="multiple">
    <ToggleGroupItem value="a">A</ToggleGroupItem>
    <ToggleGroupItem value="b">B</ToggleGroupItem>
    <ToggleGroupItem value="c">C</ToggleGroupItem>
  </ToggleGroup>
</template>
```
