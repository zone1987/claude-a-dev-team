# Combobox — Complete Source Code

## Contents

- [index.ts](#indexts)
- [Combobox.vue](#comboboxvue)
- [ComboboxAnchor.vue](#comboboxanchorvue)
- [ComboboxEmpty.vue](#comboboxemptyvue)
- [ComboboxGroup.vue](#comboboxgroupvue)
- [ComboboxInput.vue](#comboboxinputvue)
- [ComboboxItem.vue](#comboboxitemvue)
- [ComboboxItemIndicator.vue](#comboboxitemindicatorvue)
- [ComboboxList.vue](#comboboxlistvue)
- [ComboboxSeparator.vue](#comboboxseparatorvue)
- [ComboboxTrigger.vue](#comboboxtriggervue)
- [ComboboxViewport.vue](#comboboxviewportvue)

## index.ts

```ts
export { default as Combobox } from "./Combobox.vue"
export { default as ComboboxAnchor } from "./ComboboxAnchor.vue"
export { default as ComboboxEmpty } from "./ComboboxEmpty.vue"
export { default as ComboboxGroup } from "./ComboboxGroup.vue"
export { default as ComboboxInput } from "./ComboboxInput.vue"
export { default as ComboboxItem } from "./ComboboxItem.vue"
export { default as ComboboxItemIndicator } from "./ComboboxItemIndicator.vue"
export { default as ComboboxList } from "./ComboboxList.vue"
export { default as ComboboxSeparator } from "./ComboboxSeparator.vue"
export { default as ComboboxTrigger } from "./ComboboxTrigger.vue"
export { default as ComboboxViewport } from "./ComboboxViewport.vue"

export { ComboboxCancel } from "reka-ui"
```

## Combobox.vue

```vue
<script setup lang="ts">
import type { ComboboxRootEmits, ComboboxRootProps } from "reka-ui"
import { ComboboxRoot, useForwardPropsEmits } from "reka-ui"

const props = defineProps<ComboboxRootProps>()
const emits = defineEmits<ComboboxRootEmits>()

const forwarded = useForwardPropsEmits(props, emits)
</script>

<template>
  <ComboboxRoot
    v-slot="slotProps"
    data-slot="combobox"
    v-bind="forwarded"
  >
    <slot v-bind="slotProps" />
  </ComboboxRoot>
</template>
```

## ComboboxAnchor.vue

```vue
<script setup lang="ts">
import type { ComboboxAnchorProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import { reactiveOmit } from "@vueuse/core"
import { ComboboxAnchor, useForwardProps } from "reka-ui"
import { cn } from "@/lib/utils"

const props = defineProps<ComboboxAnchorProps & { class?: HTMLAttributes["class"] }>()

const delegatedProps = reactiveOmit(props, "class")

const forwarded = useForwardProps(delegatedProps)
</script>

<template>
  <ComboboxAnchor
    data-slot="combobox-anchor"
    v-bind="forwarded"
    :class="cn('w-[200px]', props.class)"
  >
    <slot />
  </ComboboxAnchor>
</template>
```

## ComboboxEmpty.vue

```vue
<script setup lang="ts">
import type { ComboboxEmptyProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import { reactiveOmit } from "@vueuse/core"
import { ComboboxEmpty } from "reka-ui"
import { cn } from "@/lib/utils"

const props = defineProps<ComboboxEmptyProps & { class?: HTMLAttributes["class"] }>()

const delegatedProps = reactiveOmit(props, "class")
</script>

<template>
  <ComboboxEmpty
    data-slot="combobox-empty"
    v-bind="delegatedProps"
    :class="cn('py-6 text-center text-sm', props.class)"
  >
    <slot />
  </ComboboxEmpty>
</template>
```

## ComboboxGroup.vue

```vue
<script setup lang="ts">
import type { ComboboxGroupProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import { reactiveOmit } from "@vueuse/core"
import { ComboboxGroup, ComboboxLabel } from "reka-ui"
import { cn } from "@/lib/utils"

const props = defineProps<ComboboxGroupProps & {
  class?: HTMLAttributes["class"]
  heading?: string
}>()

const delegatedProps = reactiveOmit(props, "class")
</script>

<template>
  <ComboboxGroup
    data-slot="combobox-group"
    v-bind="delegatedProps"
    :class="cn('overflow-hidden p-1 text-foreground', props.class)"
  >
    <ComboboxLabel v-if="heading" class="px-2 py-1.5 text-xs font-medium text-muted-foreground">
      {{ heading }}
    </ComboboxLabel>
    <slot />
  </ComboboxGroup>
</template>
```

## ComboboxInput.vue

```vue
<script setup lang="ts">
import type { ComboboxInputEmits, ComboboxInputProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import { SearchIcon } from "@lucide/vue"
import { reactiveOmit } from "@vueuse/core"
import { ComboboxInput, useForwardPropsEmits } from "reka-ui"
import { cn } from "@/lib/utils"

defineOptions({
  inheritAttrs: false,
})

const props = defineProps<ComboboxInputProps & {
  class?: HTMLAttributes["class"]
}>()

const emits = defineEmits<ComboboxInputEmits>()

const delegatedProps = reactiveOmit(props, "class")

const forwarded = useForwardPropsEmits(delegatedProps, emits)
</script>

<template>
  <div
    data-slot="command-input-wrapper"
    class="flex h-9 items-center gap-2 border-b px-3"
  >
    <SearchIcon class="size-4 shrink-0 opacity-50" />
    <ComboboxInput
      data-slot="command-input"
      :class="cn(
        'placeholder:text-muted-foreground flex h-10 w-full rounded-md bg-transparent py-3 text-sm outline-hidden disabled:cursor-not-allowed disabled:opacity-50',
        props.class,
      )"
      v-bind="{ ...$attrs, ...forwarded }"
    >
      <slot />
    </ComboboxInput>
  </div>
</template>
```

## ComboboxItem.vue

```vue
<script setup lang="ts">
import type { ComboboxItemEmits, ComboboxItemProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import { reactiveOmit } from "@vueuse/core"
import { ComboboxItem, useForwardPropsEmits } from "reka-ui"
import { cn } from "@/lib/utils"

const props = defineProps<ComboboxItemProps & { class?: HTMLAttributes["class"] }>()
const emits = defineEmits<ComboboxItemEmits>()

const delegatedProps = reactiveOmit(props, "class")

const forwarded = useForwardPropsEmits(delegatedProps, emits)
</script>

<template>
  <ComboboxItem
    data-slot="combobox-item"
    v-bind="forwarded"
    :class="cn('data-[highlighted]:bg-accent data-[highlighted]:text-accent-foreground [&_svg:not([class*=\'text-\'])]:text-muted-foreground relative flex cursor-default items-center gap-2 rounded-sm px-2 py-1.5 text-sm outline-hidden select-none data-[disabled]:pointer-events-none data-[disabled]:opacity-50 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*=\'size-\'])]:size-4', props.class)"
  >
    <slot />
  </ComboboxItem>
</template>
```

## ComboboxItemIndicator.vue

```vue
<script setup lang="ts">
import type { ComboboxItemIndicatorProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import { reactiveOmit } from "@vueuse/core"
import { ComboboxItemIndicator, useForwardProps } from "reka-ui"
import { cn } from "@/lib/utils"

const props = defineProps<ComboboxItemIndicatorProps & { class?: HTMLAttributes["class"] }>()

const delegatedProps = reactiveOmit(props, "class")

const forwarded = useForwardProps(delegatedProps)
</script>

<template>
  <ComboboxItemIndicator
    data-slot="combobox-item-indicator"
    v-bind="forwarded"
    :class="cn('ml-auto', props.class)"
  >
    <slot />
  </ComboboxItemIndicator>
</template>
```

## ComboboxList.vue

```vue
<script setup lang="ts">
import type { ComboboxContentEmits, ComboboxContentProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import { reactiveOmit } from "@vueuse/core"
import { ComboboxContent, ComboboxPortal, useForwardPropsEmits } from "reka-ui"
import { cn } from "@/lib/utils"

defineOptions({
  inheritAttrs: false,
})

const props = withDefaults(defineProps<ComboboxContentProps & { class?: HTMLAttributes["class"] }>(), {
  position: "popper",
  align: "center",
  sideOffset: 4,
})
const emits = defineEmits<ComboboxContentEmits>()

const delegatedProps = reactiveOmit(props, "class")
const forwarded = useForwardPropsEmits(delegatedProps, emits)
</script>

<template>
  <ComboboxPortal>
    <ComboboxContent
      data-slot="combobox-list"
      v-bind="{ ...$attrs, ...forwarded }"
      :class="cn('z-50 w-[200px] rounded-md border bg-popover text-popover-foreground origin-(--reka-combobox-content-transform-origin) overflow-hidden shadow-md outline-none data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2', props.class)"
    >
      <slot />
    </ComboboxContent>
  </ComboboxPortal>
</template>
```

## ComboboxSeparator.vue

```vue
<script setup lang="ts">
import type { ComboboxSeparatorProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import { reactiveOmit } from "@vueuse/core"
import { ComboboxSeparator } from "reka-ui"
import { cn } from "@/lib/utils"

const props = defineProps<ComboboxSeparatorProps & { class?: HTMLAttributes["class"] }>()

const delegatedProps = reactiveOmit(props, "class")
</script>

<template>
  <ComboboxSeparator
    data-slot="combobox-separator"
    v-bind="delegatedProps"
    :class="cn('bg-border -mx-1 h-px', props.class)"
  >
    <slot />
  </ComboboxSeparator>
</template>
```

## ComboboxTrigger.vue

```vue
<script setup lang="ts">
import type { ComboboxTriggerProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import { reactiveOmit } from "@vueuse/core"
import { ComboboxTrigger, useForwardProps } from "reka-ui"
import { cn } from "@/lib/utils"

const props = defineProps<ComboboxTriggerProps & { class?: HTMLAttributes["class"] }>()

const delegatedProps = reactiveOmit(props, "class")

const forwarded = useForwardProps(delegatedProps)
</script>

<template>
  <ComboboxTrigger
    data-slot="combobox-trigger"
    v-bind="forwarded"
    :class="cn('', props.class)"
    tabindex="0"
  >
    <slot />
  </ComboboxTrigger>
</template>
```

## ComboboxViewport.vue

```vue
<script setup lang="ts">
import type { ComboboxViewportProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import { reactiveOmit } from "@vueuse/core"
import { ComboboxViewport, useForwardProps } from "reka-ui"
import { cn } from "@/lib/utils"

const props = defineProps<ComboboxViewportProps & { class?: HTMLAttributes["class"] }>()

const delegatedProps = reactiveOmit(props, "class")

const forwarded = useForwardProps(delegatedProps)
</script>

<template>
  <ComboboxViewport
    data-slot="combobox-viewport"
    v-bind="forwarded"
    :class="cn('max-h-[300px] scroll-py-1 overflow-x-hidden overflow-y-auto', props.class)"
  >
    <slot />
  </ComboboxViewport>
</template>
```

---
Source: `registry/new-york-v4/ui/combobox/`, `registry/bases/reka/ui/combobox/`
