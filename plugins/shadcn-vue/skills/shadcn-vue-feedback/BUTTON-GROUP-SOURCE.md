# ButtonGroup — Source Code

## Contents

- [index.ts](#indexts)
- [ButtonGroup.vue](#buttongroupvue)
- [ButtonGroupSeparator.vue](#buttongroupseparatorvue)
- [ButtonGroupText.vue](#buttongrouptextvue)

## index.ts

```ts
import type { VariantProps } from "class-variance-authority"
import { cva } from "class-variance-authority"

export { default as ButtonGroup } from "./ButtonGroup.vue"
export { default as ButtonGroupSeparator } from "./ButtonGroupSeparator.vue"
export { default as ButtonGroupText } from "./ButtonGroupText.vue"

export const buttonGroupVariants = cva(
  "flex w-fit items-stretch [&>*]:focus-visible:z-10 [&>*]:focus-visible:relative [&>[data-slot=select-trigger]:not([class*='w-'])]:w-fit [&>input]:flex-1 has-[select[aria-hidden=true]:last-child]:[&>[data-slot=select-trigger]:last-of-type]:rounded-r-md has-[>[data-slot=button-group]]:gap-2",
  {
    variants: {
      orientation: {
        horizontal:
          "[&>*:not(:first-child)]:rounded-l-none [&>*:not(:first-child)]:border-l-0 [&>*:not(:last-child)]:rounded-r-none",
        vertical:
          "flex-col [&>*:not(:first-child)]:rounded-t-none [&>*:not(:first-child)]:border-t-0 [&>*:not(:last-child)]:rounded-b-none",
      },
    },
    defaultVariants: {
      orientation: "horizontal",
    },
  },
)

export type ButtonGroupVariants = VariantProps<typeof buttonGroupVariants>
```

## ButtonGroup.vue

```vue
<script setup lang="ts">
import type { HTMLAttributes } from "vue"
import type { ButtonGroupVariants } from "."
import { cn } from "@/lib/utils"
import { buttonGroupVariants } from "."

const props = defineProps<{
  class?: HTMLAttributes["class"]
  orientation?: ButtonGroupVariants["orientation"]
}>()
</script>

<template>
  <div
    role="group"
    data-slot="button-group"
    :data-orientation="props.orientation"
    :class="cn(buttonGroupVariants({ orientation: props.orientation }), props.class)"
  >
    <slot />
  </div>
</template>
```

## ButtonGroupSeparator.vue

```vue
<script setup lang="ts">
import type { SeparatorProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import { reactiveOmit } from "@vueuse/core"
import { cn } from "@/lib/utils"
import { Separator } from "@/components/ui/separator"

const props = withDefaults(defineProps<SeparatorProps & { class?: HTMLAttributes["class"] }>(), {
  orientation: "vertical",
})
const delegatedProps = reactiveOmit(props, "class")
</script>

<template>
  <Separator
    data-slot="button-group-separator"
    v-bind="delegatedProps"
    :orientation="props.orientation"
    :class="cn(
      'bg-input relative !m-0 self-stretch data-[orientation=vertical]:h-auto',
      props.class,
    )"
  />
</template>
```

> **Note:** The import path for `Separator` is `@/components/ui/separator` (standard shadcn-vue path). In the shadcn registry the path may appear as `@/registry/new-york-v4/ui/separator` — adjust to match your project.

## ButtonGroupText.vue

```vue
<script setup lang="ts">
import type { PrimitiveProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import type { ButtonGroupVariants } from "."
import { Primitive } from "reka-ui"
import { cn } from "@/lib/utils"

interface Props extends PrimitiveProps {
  class?: HTMLAttributes["class"]
  orientation?: ButtonGroupVariants["orientation"]
}

const props = withDefaults(defineProps<Props>(), {
  as: "div",
})
</script>

<template>
  <Primitive
    role="group"
    :data-orientation="props.orientation"
    :as="as"
    :as-child="asChild"
    :class="cn(
      'bg-muted flex items-center gap-2 rounded-md border px-4 text-sm font-medium shadow-xs [&_svg]:pointer-events-none [&_svg:not([class*=\'size-\'])]:size-4',
      props.class,
    )"
  >
    <slot />
  </Primitive>
</template>
```
