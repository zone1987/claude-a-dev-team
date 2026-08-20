# Breadcrumb — Source Code

## Contents

- [index.ts](#indexts)
- [Breadcrumb.vue](#breadcrumbvue)
- [BreadcrumbList.vue](#breadcrumblistvue)
- [BreadcrumbItem.vue](#breadcrumbitemvue)
- [BreadcrumbLink.vue](#breadcrumblinkvue)
- [BreadcrumbPage.vue](#breadcrumbpagevue)
- [BreadcrumbSeparator.vue](#breadcrumbseparatorvue)
- [BreadcrumbEllipsis.vue](#breadcrumbellipsisvue)

## index.ts

```ts
export { default as Breadcrumb } from "./Breadcrumb.vue"
export { default as BreadcrumbEllipsis } from "./BreadcrumbEllipsis.vue"
export { default as BreadcrumbItem } from "./BreadcrumbItem.vue"
export { default as BreadcrumbLink } from "./BreadcrumbLink.vue"
export { default as BreadcrumbList } from "./BreadcrumbList.vue"
export { default as BreadcrumbPage } from "./BreadcrumbPage.vue"
export { default as BreadcrumbSeparator } from "./BreadcrumbSeparator.vue"
```

## Breadcrumb.vue

```vue
<script lang="ts" setup>
import type { HTMLAttributes } from "vue"

const props = defineProps<{
  class?: HTMLAttributes["class"]
}>()
</script>

<template>
  <nav
    aria-label="breadcrumb"
    data-slot="breadcrumb"
    :class="props.class"
  >
    <slot />
  </nav>
</template>
```

## BreadcrumbList.vue

```vue
<script lang="ts" setup>
import type { HTMLAttributes } from "vue"
import { cn } from "@/lib/utils"

const props = defineProps<{
  class?: HTMLAttributes["class"]
}>()
</script>

<template>
  <ol
    data-slot="breadcrumb-list"
    :class="cn('text-muted-foreground flex flex-wrap items-center gap-1.5 text-sm break-words sm:gap-2.5', props.class)"
  >
    <slot />
  </ol>
</template>
```

## BreadcrumbItem.vue

```vue
<script lang="ts" setup>
import type { HTMLAttributes } from "vue"
import { cn } from "@/lib/utils"

const props = defineProps<{
  class?: HTMLAttributes["class"]
}>()
</script>

<template>
  <li
    data-slot="breadcrumb-item"
    :class="cn('inline-flex items-center gap-1.5', props.class)"
  >
    <slot />
  </li>
</template>
```

## BreadcrumbLink.vue

```vue
<script lang="ts" setup>
import type { PrimitiveProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import { Primitive } from "reka-ui"
import { cn } from "@/lib/utils"

const props = withDefaults(defineProps<PrimitiveProps & { class?: HTMLAttributes["class"] }>(), {
  as: "a",
})
</script>

<template>
  <Primitive
    data-slot="breadcrumb-link"
    :as="as"
    :as-child="asChild"
    :class="cn('hover:text-foreground transition-colors', props.class)"
  >
    <slot />
  </Primitive>
</template>
```

## BreadcrumbPage.vue

```vue
<script lang="ts" setup>
import type { HTMLAttributes } from "vue"
import { cn } from "@/lib/utils"

const props = defineProps<{
  class?: HTMLAttributes["class"]
}>()
</script>

<template>
  <span
    data-slot="breadcrumb-page"
    role="link"
    aria-disabled="true"
    aria-current="page"
    :class="cn('text-foreground font-normal', props.class)"
  >
    <slot />
  </span>
</template>
```

## BreadcrumbSeparator.vue

```vue
<script lang="ts" setup>
import type { HTMLAttributes } from "vue"
import { ChevronRight } from "@lucide/vue"
import { cn } from "@/lib/utils"

const props = defineProps<{
  class?: HTMLAttributes["class"]
}>()
</script>

<template>
  <li
    data-slot="breadcrumb-separator"
    role="presentation"
    aria-hidden="true"
    :class="cn('[&>svg]:size-3.5', props.class)"
  >
    <slot>
      <ChevronRight />
    </slot>
  </li>
</template>
```

## BreadcrumbEllipsis.vue

```vue
<script lang="ts" setup>
import type { HTMLAttributes } from "vue"
import { MoreHorizontal } from "@lucide/vue"
import { cn } from "@/lib/utils"

const props = defineProps<{
  class?: HTMLAttributes["class"]
}>()
</script>

<template>
  <span
    data-slot="breadcrumb-ellipsis"
    role="presentation"
    aria-hidden="true"
    :class="cn('flex size-9 items-center justify-center', props.class)"
  >
    <slot>
      <MoreHorizontal class="size-4" />
    </slot>
    <span class="sr-only">More</span>
  </span>
</template>
```

---
Source: shadcn-vue breadcrumb component
