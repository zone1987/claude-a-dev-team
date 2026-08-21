# Toggle — Source Code

## `index.ts`

```ts
import type { VariantProps } from "class-variance-authority"
import { cva } from "class-variance-authority"

export { default as Toggle } from "./Toggle.vue"

export const toggleVariants = cva(
  "inline-flex items-center justify-center gap-2 rounded-md text-sm font-medium hover:bg-muted hover:text-muted-foreground disabled:pointer-events-none disabled:opacity-50 data-[state=on]:bg-accent data-[state=on]:text-accent-foreground [&_svg]:pointer-events-none [&_svg:not([class*='size-'])]:size-4 [&_svg]:shrink-0 focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:ring-3 outline-none transition-[color,box-shadow] aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive whitespace-nowrap",
  {
    variants: {
      variant: {
        default: "bg-transparent",
        outline:
          "border border-input bg-transparent shadow-xs hover:bg-accent hover:text-accent-foreground",
      },
      size: {
        default: "h-9 px-2 min-w-9",
        sm: "h-8 px-1.5 min-w-8",
        lg: "h-10 px-2.5 min-w-10",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  },
)

export type ToggleVariants = VariantProps<typeof toggleVariants>
```

## `Toggle.vue`

```vue
<script setup lang="ts">
import type { ToggleEmits, ToggleProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import type { ToggleVariants } from "."
import { reactiveOmit } from "@vueuse/core"
import { Toggle, useForwardPropsEmits } from "reka-ui"
import { cn } from "@/lib/utils"
import { toggleVariants } from "."

const props = withDefaults(defineProps<ToggleProps & {
  class?: HTMLAttributes["class"]
  variant?: ToggleVariants["variant"]
  size?: ToggleVariants["size"]
}>(), {
  variant: "default",
  size: "default",
  disabled: false,
})

const emits = defineEmits<ToggleEmits>()

const delegatedProps = reactiveOmit(props, "class", "size", "variant")
const forwarded = useForwardPropsEmits(delegatedProps, emits)
</script>

<template>
  <Toggle
    v-slot="slotProps"
    data-slot="toggle"
    v-bind="forwarded"
    :class="cn(toggleVariants({ variant, size }), props.class)"
  >
    <slot v-bind="slotProps" />
  </Toggle>
</template>
```

**Source:** `registry/new-york-v4/ui/toggle/Toggle.vue`, `registry/new-york-v4/ui/toggle/index.ts`
