# shadcn-vue Installation: Laravel (Inertia + Vue)

## Step 1: Create project

```bash
laravel new my-app --vue
```

This creates a Laravel project with Inertia.js and Vue preconfigured.
The init step is not needed — shadcn-vue detects Laravel+Inertia and configures itself.

## Step 2: Add Components

```bash
npx shadcn-vue@latest add switch
```

Components are installed to `resources/js/components/ui/<component>/`.

Usage:

```vue
<script setup lang="ts">
import { Switch } from '@/Components/ui/switch'
</script>

<template>
  <div>
    <Switch />
  </div>
</template>
```

Note: Laravel uses `@/Components` (capital C) by default for Inertia pages.

Source: `/tmp/shadcn-vue-repo/apps/v4/content/docs/installation/04.laravel.md`
