# Menubar — Vollstandiger Quellcode

## index.ts

```ts
export { default as Menubar } from "./Menubar.vue"
export { default as MenubarCheckboxItem } from "./MenubarCheckboxItem.vue"
export { default as MenubarContent } from "./MenubarContent.vue"
export { default as MenubarGroup } from "./MenubarGroup.vue"
export { default as MenubarItem } from "./MenubarItem.vue"
export { default as MenubarLabel } from "./MenubarLabel.vue"
export { default as MenubarMenu } from "./MenubarMenu.vue"
export { default as MenubarRadioGroup } from "./MenubarRadioGroup.vue"
export { default as MenubarRadioItem } from "./MenubarRadioItem.vue"
export { default as MenubarSeparator } from "./MenubarSeparator.vue"
export { default as MenubarShortcut } from "./MenubarShortcut.vue"
export { default as MenubarSub } from "./MenubarSub.vue"
export { default as MenubarSubContent } from "./MenubarSubContent.vue"
export { default as MenubarSubTrigger } from "./MenubarSubTrigger.vue"
export { default as MenubarTrigger } from "./MenubarTrigger.vue"
```

## Menubar.vue

```vue
<script setup lang="ts">
import type { MenubarRootEmits, MenubarRootProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import { reactiveOmit } from "@vueuse/core"
import {
  MenubarRoot,
  useForwardPropsEmits,
} from "reka-ui"
import { cn } from "@/lib/utils"

const props = defineProps<MenubarRootProps & { class?: HTMLAttributes["class"] }>()
const emits = defineEmits<MenubarRootEmits>()

const delegatedProps = reactiveOmit(props, "class")

const forwarded = useForwardPropsEmits(delegatedProps, emits)
</script>

<template>
  <MenubarRoot
    v-slot="slotProps"
    data-slot="menubar"
    v-bind="forwarded"
    :class="
      cn(
        'bg-background flex h-9 items-center gap-1 rounded-md border p-1 shadow-xs',
        props.class,
      )
    "
  >
    <slot v-bind="slotProps" />
  </MenubarRoot>
</template>
```

## MenubarCheckboxItem.vue

```vue
<script setup lang="ts">
import type { MenubarCheckboxItemEmits, MenubarCheckboxItemProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import { Check } from "@lucide/vue"
import { reactiveOmit } from "@vueuse/core"
import {
  MenubarCheckboxItem,
  MenubarItemIndicator,
  useForwardPropsEmits,
} from "reka-ui"
import { cn } from "@/lib/utils"

const props = defineProps<MenubarCheckboxItemProps & { class?: HTMLAttributes["class"] }>()
const emits = defineEmits<MenubarCheckboxItemEmits>()

const delegatedProps = reactiveOmit(props, "class")

const forwarded = useForwardPropsEmits(delegatedProps, emits)
</script>

<template>
  <MenubarCheckboxItem
    data-slot="menubar-checkbox-item"
    v-bind="forwarded"
    :class="cn(
      'focus:bg-accent focus:text-accent-foreground relative flex cursor-default items-center gap-2 rounded-xs py-1.5 pr-2 pl-8 text-sm outline-hidden select-none data-[disabled]:pointer-events-none data-[disabled]:opacity-50 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*=\'size-\'])]:size-4',
      props.class,
    )"
  >
    <span class="pointer-events-none absolute left-2 flex size-3.5 items-center justify-center">
      <MenubarItemIndicator>
        <slot name="indicator-icon">
          <Check class="size-4" />
        </slot>
      </MenubarItemIndicator>
    </span>
    <slot />
  </MenubarCheckboxItem>
</template>
```

## MenubarContent.vue

```vue
<script setup lang="ts">
import type { MenubarContentProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import { reactiveOmit } from "@vueuse/core"
import {
  MenubarContent,
  MenubarPortal,
  useForwardProps,
} from "reka-ui"
import { cn } from "@/lib/utils"

defineOptions({
  inheritAttrs: false,
})

const props = withDefaults(
  defineProps<MenubarContentProps & { class?: HTMLAttributes["class"] }>(),
  {
    align: "start",
    alignOffset: -4,
    sideOffset: 8,
  },
)

const delegatedProps = reactiveOmit(props, "class")

const forwardedProps = useForwardProps(delegatedProps)
</script>

<template>
  <MenubarPortal>
    <MenubarContent
      data-slot="menubar-content"
      v-bind="{ ...$attrs, ...forwardedProps }"
      :class="
        cn(
          'bg-popover text-popover-foreground data-[state=open]:animate-in data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2 z-50 min-w-[12rem] origin-(--reka-menubar-content-transform-origin) overflow-hidden rounded-md border p-1 shadow-md',
          props.class,
        )
      "
    >
      <slot />
    </MenubarContent>
  </MenubarPortal>
</template>
```

## MenubarGroup.vue

```vue
<script setup lang="ts">
import type { MenubarGroupProps } from "reka-ui"
import { MenubarGroup } from "reka-ui"

const props = defineProps<MenubarGroupProps>()
</script>

<template>
  <MenubarGroup
    data-slot="menubar-group"
    v-bind="props"
  >
    <slot />
  </MenubarGroup>
</template>
```

## MenubarItem.vue

```vue
<script setup lang="ts">
import type { MenubarItemEmits, MenubarItemProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import { reactiveOmit } from "@vueuse/core"
import {
  MenubarItem,
  useForwardPropsEmits,
} from "reka-ui"
import { cn } from "@/lib/utils"

const props = defineProps<MenubarItemProps & {
  class?: HTMLAttributes["class"]
  inset?: boolean
  variant?: "default" | "destructive"
}>()

const emits = defineEmits<MenubarItemEmits>()

const delegatedProps = reactiveOmit(props, "class", "inset", "variant")
const forwarded = useForwardPropsEmits(delegatedProps, emits)
</script>

<template>
  <MenubarItem
    data-slot="menubar-item"
    :data-inset="inset ? '' : undefined"
    :data-variant="variant"
    v-bind="forwarded"
    :class="cn(
      'focus:bg-accent focus:text-accent-foreground data-[variant=destructive]:text-destructive-foreground data-[variant=destructive]:focus:bg-destructive/10 dark:data-[variant=destructive]:focus:bg-destructive/40 data-[variant=destructive]:focus:text-destructive-foreground data-[variant=destructive]:*:[svg]:!text-destructive-foreground [&_svg:not([class*=\'text-\'])]:text-muted-foreground relative flex cursor-default items-center gap-2 rounded-sm px-2 py-1.5 text-sm outline-hidden select-none data-[disabled]:pointer-events-none data-[disabled]:opacity-50 data-[inset]:pl-8 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*=\'size-\'])]:size-4',
      props.class,
    )"
  >
    <slot />
  </MenubarItem>
</template>
```

## MenubarLabel.vue

```vue
<script setup lang="ts">
import type { MenubarLabelProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import { reactiveOmit } from "@vueuse/core"
import { MenubarLabel } from "reka-ui"
import { cn } from "@/lib/utils"

const props = defineProps<MenubarLabelProps & { class?: HTMLAttributes["class"], inset?: boolean }>()
const delegatedProps = reactiveOmit(props, "class", "inset")
</script>

<template>
  <MenubarLabel
    :data-inset="inset ? '' : undefined"
    v-bind="delegatedProps"
    :class="cn('px-2 py-1.5 text-sm font-medium data-[inset]:pl-8', props.class)"
  >
    <slot />
  </MenubarLabel>
</template>
```

## MenubarMenu.vue

```vue
<script setup lang="ts">
import type { MenubarMenuProps } from "reka-ui"
import { MenubarMenu } from "reka-ui"

const props = defineProps<MenubarMenuProps>()
</script>

<template>
  <MenubarMenu
    data-slot="menubar-menu"
    v-bind="props"
  >
    <slot />
  </MenubarMenu>
</template>
```

## MenubarRadioGroup.vue

```vue
<script setup lang="ts">
import type { MenubarRadioGroupEmits, MenubarRadioGroupProps } from "reka-ui"
import {
  MenubarRadioGroup,
  useForwardPropsEmits,
} from "reka-ui"

const props = defineProps<MenubarRadioGroupProps>()
const emits = defineEmits<MenubarRadioGroupEmits>()

const forwarded = useForwardPropsEmits(props, emits)
</script>

<template>
  <MenubarRadioGroup
    data-slot="menubar-radio-group"
    v-bind="forwarded"
  >
    <slot />
  </MenubarRadioGroup>
</template>
```

## MenubarRadioItem.vue

```vue
<script setup lang="ts">
import type { MenubarRadioItemEmits, MenubarRadioItemProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import { Circle } from "@lucide/vue"
import { reactiveOmit } from "@vueuse/core"
import {
  MenubarItemIndicator,
  MenubarRadioItem,
  useForwardPropsEmits,
} from "reka-ui"
import { cn } from "@/lib/utils"

const props = defineProps<MenubarRadioItemProps & { class?: HTMLAttributes["class"] }>()
const emits = defineEmits<MenubarRadioItemEmits>()

const delegatedProps = reactiveOmit(props, "class")

const forwarded = useForwardPropsEmits(delegatedProps, emits)
</script>

<template>
  <MenubarRadioItem
    data-slot="menubar-radio-item"
    v-bind="forwarded"
    :class="cn(
      'focus:bg-accent focus:text-accent-foreground relative flex cursor-default items-center gap-2 rounded-xs py-1.5 pr-2 pl-8 text-sm outline-hidden select-none data-[disabled]:pointer-events-none data-[disabled]:opacity-50 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*=\'size-\'])]:size-4',
      props.class,
    )"
  >
    <span class="pointer-events-none absolute left-2 flex size-3.5 items-center justify-center">
      <MenubarItemIndicator>
        <slot name="indicator-icon">
          <Circle class="size-2 fill-current" />
        </slot>
      </MenubarItemIndicator>
    </span>
    <slot />
  </MenubarRadioItem>
</template>
```

## MenubarSeparator.vue

```vue
<script setup lang="ts">
import type { MenubarSeparatorProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import { reactiveOmit } from "@vueuse/core"
import { MenubarSeparator, useForwardProps } from "reka-ui"
import { cn } from "@/lib/utils"

const props = defineProps<MenubarSeparatorProps & { class?: HTMLAttributes["class"] }>()

const delegatedProps = reactiveOmit(props, "class")

const forwardedProps = useForwardProps(delegatedProps)
</script>

<template>
  <MenubarSeparator
    data-slot="menubar-separator"
    :class=" cn('bg-border -mx-1 my-1 h-px', props.class)"
    v-bind="forwardedProps"
  />
</template>
```

## MenubarShortcut.vue

```vue
<script setup lang="ts">
import type { HTMLAttributes } from "vue"
import { cn } from "@/lib/utils"

const props = defineProps<{
  class?: HTMLAttributes["class"]
}>()
</script>

<template>
  <span
    data-slot="menubar-shortcut"
    :class="cn('text-muted-foreground ml-auto text-xs tracking-widest', props.class)"
  >
    <slot />
  </span>
</template>
```

## MenubarSub.vue

```vue
<script setup lang="ts">
import type { MenubarSubEmits } from "reka-ui"
import { MenubarSub, useForwardPropsEmits } from "reka-ui"

interface MenubarSubRootProps {
  defaultOpen?: boolean
  open?: boolean
}

const props = defineProps<MenubarSubRootProps>()
const emits = defineEmits<MenubarSubEmits>()

const forwarded = useForwardPropsEmits(props, emits)
</script>

<template>
  <MenubarSub
    v-slot="slotProps"
    data-slot="menubar-sub"
    v-bind="forwarded"
  >
    <slot v-bind="slotProps" />
  </MenubarSub>
</template>
```

## MenubarSubContent.vue

```vue
<script setup lang="ts">
import type { MenubarSubContentEmits, MenubarSubContentProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import { reactiveOmit } from "@vueuse/core"
import {
  MenubarPortal,
  MenubarSubContent,
  useForwardPropsEmits,
} from "reka-ui"
import { cn } from "@/lib/utils"

defineOptions({
  inheritAttrs: false,
})

const props = defineProps<MenubarSubContentProps & { class?: HTMLAttributes["class"] }>()
const emits = defineEmits<MenubarSubContentEmits>()

const delegatedProps = reactiveOmit(props, "class")

const forwarded = useForwardPropsEmits(delegatedProps, emits)
</script>

<template>
  <MenubarPortal>
    <MenubarSubContent
      data-slot="menubar-sub-content"
      v-bind="{ ...$attrs, ...forwarded }"
      :class="
        cn(
          'bg-popover text-popover-foreground data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2 z-50 min-w-[8rem] origin-(--reka-menubar-content-transform-origin) overflow-hidden rounded-md border p-1 shadow-lg',
          props.class,
        )
      "
    >
      <slot />
    </MenubarSubContent>
  </MenubarPortal>
</template>
```

## MenubarSubTrigger.vue

```vue
<script setup lang="ts">
import type { MenubarSubTriggerProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import { ChevronRight } from "@lucide/vue"
import { reactiveOmit } from "@vueuse/core"
import { MenubarSubTrigger, useForwardProps } from "reka-ui"
import { cn } from "@/lib/utils"

const props = defineProps<MenubarSubTriggerProps & { class?: HTMLAttributes["class"], inset?: boolean }>()

const delegatedProps = reactiveOmit(props, "class", "inset")
const forwardedProps = useForwardProps(delegatedProps)
</script>

<template>
  <MenubarSubTrigger
    data-slot="menubar-sub-trigger"
    :data-inset="inset ? '' : undefined"
    v-bind="forwardedProps"
    :class="cn(
      'focus:bg-accent focus:text-accent-foreground data-[state=open]:bg-accent data-[state=open]:text-accent-foreground flex cursor-default items-center rounded-sm px-2 py-1.5 text-sm outline-none select-none data-[inset]:pl-8',
      props.class,
    )"
  >
    <slot />
    <ChevronRight class="ml-auto size-4" />
  </MenubarSubTrigger>
</template>
```

## MenubarTrigger.vue

```vue
<script setup lang="ts">
import type { MenubarTriggerProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import { reactiveOmit } from "@vueuse/core"
import { MenubarTrigger, useForwardProps } from "reka-ui"
import { cn } from "@/lib/utils"

const props = defineProps<MenubarTriggerProps & { class?: HTMLAttributes["class"] }>()

const delegatedProps = reactiveOmit(props, "class")

const forwardedProps = useForwardProps(delegatedProps)
</script>

<template>
  <MenubarTrigger
    data-slot="menubar-trigger"
    v-bind="forwardedProps"
    :class="
      cn(
        'focus:bg-accent focus:text-accent-foreground data-[state=open]:bg-accent data-[state=open]:text-accent-foreground flex items-center rounded-sm px-2 py-1 text-sm font-medium outline-hidden select-none',
        props.class,
      )
    "
  >
    <slot />
  </MenubarTrigger>
</template>
```

## Quellen
- `/tmp/shadcn-vue-repo/apps/v4/registry/new-york-v4/ui/menubar/`
