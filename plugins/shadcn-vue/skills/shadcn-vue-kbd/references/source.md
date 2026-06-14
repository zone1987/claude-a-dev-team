# Kbd — Vollstandiger Quellcode

## index.ts

```ts
export { default as Kbd } from "./Kbd.vue"
export { default as KbdGroup } from "./KbdGroup.vue"
```

## Kbd.vue

```vue
<script setup lang="ts">
import type { HTMLAttributes } from "vue"
import { cn } from "@/lib/utils"

const props = defineProps<{
  class?: HTMLAttributes["class"]
}>()
</script>

<template>
  <kbd
    :class="cn(
      'bg-muted text-muted-foreground pointer-events-none inline-flex h-5 w-fit min-w-5 items-center justify-center gap-1 rounded-sm px-1 font-sans text-xs font-medium select-none',
      '[&_svg:not([class*=\'size-\'])]:size-3',
      '[[data-slot=tooltip-content]_&]:bg-background/20 [[data-slot=tooltip-content]_&]:text-background dark:[[data-slot=tooltip-content]_&]:bg-background/10',
      props.class,
    )"
  >
    <slot />
  </kbd>
</template>
```

## KbdGroup.vue

```vue
<script setup lang="ts">
import type { HTMLAttributes } from "vue"
import { cn } from "@/lib/utils"

const props = defineProps<{
  class?: HTMLAttributes["class"]
}>()
</script>

<template>
  <kbd
    data-slot="kbd-group"
    :class="cn('inline-flex items-center gap-1', props.class)"
  >
    <slot />
  </kbd>
</template>
```

## Quellen
- `/tmp/shadcn-vue-repo/apps/v4/registry/new-york-v4/ui/kbd/`
