# ToggleGroup — Source Code

## `index.ts`

```ts
export { default as ToggleGroup } from "./ToggleGroup.vue"
export { default as ToggleGroupItem } from "./ToggleGroupItem.vue"
```

## `ToggleGroup.vue`

```vue
<script setup lang="ts">
import type { VariantProps } from "class-variance-authority"
import type { ToggleGroupRootEmits, ToggleGroupRootProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import type { toggleVariants } from "@/registry/new-york-v4/ui/toggle"
import { reactiveOmit } from "@vueuse/core"
import { ToggleGroupRoot, useForwardPropsEmits } from "reka-ui"
import { provide } from "vue"
import { cn } from "@/lib/utils"

type ToggleGroupVariants = VariantProps<typeof toggleVariants>

const props = withDefaults(defineProps<ToggleGroupRootProps & {
  class?: HTMLAttributes["class"]
  variant?: ToggleGroupVariants["variant"]
  size?: ToggleGroupVariants["size"]
  spacing?: number
}>(), {
  spacing: 0,
})

const emits = defineEmits<ToggleGroupRootEmits>()

provide("toggleGroup", {
  variant: props.variant,
  size: props.size,
  spacing: props.spacing,
})

const delegatedProps = reactiveOmit(props, "class", "size", "variant")
const forwarded = useForwardPropsEmits(delegatedProps, emits)
</script>

<template>
  <ToggleGroupRoot
    v-slot="slotProps"
    data-slot="toggle-group"
    :data-size="size"
    :data-variant="variant"
    :data-spacing="spacing"
    :style="{
      '--gap': spacing,
    }"
    v-bind="forwarded"
    :class="cn('group/toggle-group flex w-fit items-center gap-[--spacing(var(--gap))] rounded-md data-[spacing=default]:data-[variant=outline]:shadow-xs', props.class)"
  >
    <slot v-bind="slotProps" />
  </ToggleGroupRoot>
</template>
```

## `ToggleGroupItem.vue`

```vue
<script setup lang="ts">
import type { VariantProps } from "class-variance-authority"
import type { ToggleGroupItemProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import { reactiveOmit } from "@vueuse/core"
import { ToggleGroupItem, useForwardProps } from "reka-ui"
import { inject } from "vue"
import { cn } from "@/lib/utils"
import { toggleVariants } from "@/registry/new-york-v4/ui/toggle"

type ToggleGroupVariants = VariantProps<typeof toggleVariants> & {
  spacing?: number
}

const props = defineProps<ToggleGroupItemProps & {
  class?: HTMLAttributes["class"]
  variant?: ToggleGroupVariants["variant"]
  size?: ToggleGroupVariants["size"]
}>()

const context = inject<ToggleGroupVariants>("toggleGroup")

const delegatedProps = reactiveOmit(props, "class", "size", "variant")
const forwardedProps = useForwardProps(delegatedProps)
</script>

<template>
  <ToggleGroupItem
    v-slot="slotProps"
    data-slot="toggle-group-item"
    :data-variant="context?.variant || variant"
    :data-size="context?.size || size"
    :data-spacing="context?.spacing"
    v-bind="forwardedProps"
    :class="cn(
      toggleVariants({
        variant: context?.variant || variant,
        size: context?.size || size,
      }),
      'w-auto min-w-0 shrink-0 px-3 focus:z-10 focus-visible:z-10',
      'data-[spacing=0]:rounded-none data-[spacing=0]:shadow-none data-[spacing=0]:first:rounded-l-md data-[spacing=0]:last:rounded-r-md data-[spacing=0]:data-[variant=outline]:border-l-0 data-[spacing=0]:data-[variant=outline]:first:border-l',
      props.class)"
  >
    <slot v-bind="slotProps" />
  </ToggleGroupItem>
</template>
```

**Source:** `registry/new-york-v4/ui/toggle-group/ToggleGroup.vue`, `registry/new-york-v4/ui/toggle-group/ToggleGroupItem.vue`, `registry/new-york-v4/ui/toggle-group/index.ts`
