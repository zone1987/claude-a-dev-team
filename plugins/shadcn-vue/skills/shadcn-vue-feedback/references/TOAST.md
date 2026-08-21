# shadcn-vue Toast Component (Deprecated)

The `toast` component from shadcn-vue v3 has been **deprecated** in v4.

Use the `sonner` component instead:
- Skill: `shadcn-vue-sonner`
- Docs: https://www.shadcn-vue.com/docs/components/sonner
- Library: `vue-sonner` (https://vue-sonner.vercel.app/)

The old v3 toast documentation is still available at:
https://v3.shadcn-vue.com/docs/components/toast

## Migration to Sonner

### 1. Install

```bash
npx shadcn-vue@latest add sonner
```

### 2. Add Toaster to root layout

```vue
<script setup lang="ts">
import 'vue-sonner/style.css'
import { Toaster } from '@/components/ui/sonner'
</script>

<template>
  <div>
    <main><!-- content --></main>
    <Toaster />
  </div>
</template>
```

### 3. Show toasts

```vue
<script setup lang="ts">
import { toast } from 'vue-sonner'
</script>

<template>
  <button @click="() => toast('Hello!')">Show Toast</button>
</template>
```

See the `shadcn-vue-sonner` skill for full API and examples.
