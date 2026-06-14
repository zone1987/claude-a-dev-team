# Tooltip — Installation

## CLI (recommended)

```bash
npx shadcn-vue@latest add tooltip
```

This copies `Tooltip.vue`, `TooltipContent.vue`, `TooltipProvider.vue`, `TooltipTrigger.vue`, and `index.ts` to `src/components/ui/tooltip/`.

## Manual

### 1. Install dependency

```bash
npm install reka-ui
```

Also required:

```bash
npm install @vueuse/core
```

### 2. Copy source files

Copy all Vue files and `index.ts` from  
`registry/new-york-v4/ui/tooltip/` into `src/components/ui/tooltip/`.

### 3. Adjust import paths

Replace `@/lib/utils` with the path to your `cn` utility.

## Usage

```vue
<script setup lang="ts">
import {
  Tooltip,
  TooltipContent,
  TooltipProvider,
  TooltipTrigger,
} from '@/components/ui/tooltip'
</script>

<template>
  <TooltipProvider>
    <Tooltip>
      <TooltipTrigger>Hover</TooltipTrigger>
      <TooltipContent>
        <p>Add to library</p>
      </TooltipContent>
    </Tooltip>
  </TooltipProvider>
</template>
```

### App-level provider

Instead of wrapping each Tooltip with `TooltipProvider`, register it once in your app root:

```vue
<!-- App.vue -->
<template>
  <TooltipProvider>
    <RouterView />
  </TooltipProvider>
</template>
```
