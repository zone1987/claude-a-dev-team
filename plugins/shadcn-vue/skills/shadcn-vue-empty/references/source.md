# Empty — Quellcode

Alle Dateien aus `registry/new-york-v4/ui/empty/`.

## Empty.vue

```vue
<script setup lang="ts">
import type { HTMLAttributes } from "vue"
import { cn } from "@/lib/utils"

const props = defineProps<{
  class?: HTMLAttributes["class"]
}>()
</script>

<template>
  <div
    data-slot="empty"
    :class="cn(
      'flex min-w-0 flex-1 flex-col items-center justify-center gap-6 text-balance rounded-lg border-dashed p-6 text-center md:p-12',
      props.class,
    )"
  >
    <slot />
  </div>
</template>
```

## EmptyHeader.vue

```vue
<script setup lang="ts">
import type { HTMLAttributes } from "vue"
import { cn } from "@/lib/utils"

const props = defineProps<{
  class?: HTMLAttributes["class"]
}>()
</script>

<template>
  <div
    data-slot="empty-header"
    :class="cn(
      'flex max-w-sm flex-col items-center gap-2 text-center',
      props.class,
    )"
  >
    <slot />
  </div>
</template>
```

## EmptyMedia.vue

```vue
<script setup lang="ts">
import type { HTMLAttributes } from "vue"
import type { EmptyMediaVariants } from "."
import { cn } from "@/lib/utils"
import { emptyMediaVariants } from "."

const props = defineProps<{
  class?: HTMLAttributes["class"]
  variant?: EmptyMediaVariants["variant"]
}>()
</script>

<template>
  <div
    data-slot="empty-icon"
    :data-variant="variant"
    :class="cn(emptyMediaVariants({ variant }), props.class)"
  >
    <slot />
  </div>
</template>
```

## EmptyTitle.vue

```vue
<script setup lang="ts">
import type { HTMLAttributes } from "vue"
import { cn } from "@/lib/utils"

const props = defineProps<{
  class?: HTMLAttributes["class"]
}>()
</script>

<template>
  <div
    data-slot="empty-title"
    :class="cn('text-lg font-medium tracking-tight', props.class)"
  >
    <slot />
  </div>
</template>
```

## EmptyDescription.vue

```vue
<script setup lang="ts">
import type { HTMLAttributes } from "vue"
import { cn } from "@/lib/utils"

defineProps<{
  class?: HTMLAttributes["class"]
}>()
</script>

<template>
  <p
    data-slot="empty-description"
    :class="cn(
      'text-muted-foreground [&>a:hover]:text-primary text-sm/relaxed [&>a]:underline [&>a]:underline-offset-4',
      $attrs.class ?? '',
    )"
  >
    <slot />
  </p>
</template>
```

## EmptyContent.vue

```vue
<script setup lang="ts">
import type { HTMLAttributes } from "vue"
import { cn } from "@/lib/utils"

const props = defineProps<{
  class?: HTMLAttributes["class"]
}>()
</script>

<template>
  <div
    data-slot="empty-content"
    :class="cn(
      'flex w-full min-w-0 max-w-sm flex-col items-center gap-4 text-balance text-sm',
      props.class,
    )"
  >
    <slot />
  </div>
</template>
```

## index.ts

```ts
import type { VariantProps } from "class-variance-authority"
import { cva } from "class-variance-authority"

export { default as Empty } from "./Empty.vue"
export { default as EmptyContent } from "./EmptyContent.vue"
export { default as EmptyDescription } from "./EmptyDescription.vue"
export { default as EmptyHeader } from "./EmptyHeader.vue"
export { default as EmptyMedia } from "./EmptyMedia.vue"
export { default as EmptyTitle } from "./EmptyTitle.vue"

export const emptyMediaVariants = cva(
  "mb-2 flex shrink-0 items-center justify-center [&_svg]:pointer-events-none [&_svg]:shrink-0",
  {
    variants: {
      variant: {
        default: "bg-transparent",
        icon: "bg-muted text-foreground flex size-10 shrink-0 items-center justify-center rounded-lg [&_svg:not([class*='size-'])]:size-6",
      },
    },
    defaultVariants: {
      variant: "default",
    },
  },
)

export type EmptyMediaVariants = VariantProps<typeof emptyMediaVariants>
```

Quellen:
- `/tmp/shadcn-vue-repo/apps/v4/registry/new-york-v4/ui/empty/`
