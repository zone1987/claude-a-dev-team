# shadcn-vue Dark Mode: Vitepress

## Step 1: Install Dependencies

```bash
npm install @vueuse/core
```

Optional (icons):

```bash
npm install -D @iconify/vue @iconify-json/radix-icons
```

## Step 2: Add a mode toggle

We use [`useToggle`](https://vueuse.org/shared/useToggle/) from `@vueuse/core` (a boolean
switcher with utility functions) and `useData` from vitepress.

`components/ModeToggle.vue`:

```vue
<script setup lang="ts">
import { useToggle } from '@vueuse/core'
import { useData } from 'vitepress'
import { Button } from '@/registry/default/ui/button'

const { frontmatter, isDark } = useData()
const toggleDark = useToggle(isDark)
</script>

<template>
  <Button variant="outline" @click="toggleDark()">
    <Icon
      icon="radix-icons:moon"
      class="h-[1.2rem] w-[1.2rem] rotate-0 scale-100 transition-all dark:-rotate-90 dark:scale-0"
    />
    <Icon
      icon="radix-icons:sun"
      class="absolute h-[1.2rem] w-[1.2rem] rotate-90 scale-0 transition-all dark:rotate-0 dark:scale-100"
    />
    <span class="sr-only">Toggle theme</span>
  </Button>
</template>
```

Note: Vitepress uses `useData().isDark` as the reactive boolean, toggled via `useToggle`.

Source: `/tmp/shadcn-vue-repo/apps/v4/content/docs/dark-mode/03.vitepress.md`
