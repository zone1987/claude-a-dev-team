# Installation

## CLI (recommended)

```bash
npx shadcn-vue@latest add sonner
```

## Manual

### Dependencies

```bash
npm install vue-sonner
```

Copy the source from GitHub into `src/components/ui/sonner/`:
https://github.com/unovue/shadcn-vue/tree/dev/apps/v4/registry/new-york-v4/ui/sonner

Update import paths to match your project (e.g. `@/lib/utils`).

### Set Up the Root Layout

Add `<Toaster />` and the required CSS to your root layout:

```vue
<script setup lang="ts">
import 'vue-sonner/style.css'
import { Toaster } from '@/components/ui/sonner'
</script>

<template>
  <div>
    <main><!-- Your app content --></main>
    <Toaster />
  </div>
</template>
```
