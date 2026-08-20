# PinInput — Vollstandiger Quellcode

## Contents

- [index.ts](#indexts)
- [PinInput.vue](#pininputvue)
- [PinInputGroup.vue](#pininputgroupvue)
- [PinInputSeparator.vue](#pininputseparatorvue)
- [PinInputSlot.vue](#pininputslotvue)
- [Quellen](#quellen)

## index.ts

```ts
export { default as PinInput } from "./PinInput.vue"
export { default as PinInputGroup } from "./PinInputGroup.vue"
export { default as PinInputSeparator } from "./PinInputSeparator.vue"
export { default as PinInputSlot } from "./PinInputSlot.vue"
```

## PinInput.vue

```vue
<script setup lang="ts" generic="Type extends 'text' | 'number' = 'text'">
import type { PinInputRootEmits, PinInputRootProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import { reactiveOmit } from "@vueuse/core"
import { PinInputRoot, useForwardPropsEmits } from "reka-ui"
import { cn } from "@/lib/utils"

const props = withDefaults(defineProps<PinInputRootProps<Type> & { class?: HTMLAttributes["class"] }>(), {
  otp: true,
})
const emits = defineEmits<PinInputRootEmits<Type>>()

const delegatedProps = reactiveOmit(props, "class")

const forwarded = useForwardPropsEmits(delegatedProps, emits)
</script>

<template>
  <PinInputRoot
    :otp="props.otp"
    data-slot="pin-input"
    v-bind="forwarded" :class="cn('flex items-center gap-2 has-disabled:opacity-50 disabled:cursor-not-allowed', props.class)"
  >
    <slot />
  </PinInputRoot>
</template>
```

## PinInputGroup.vue

```vue
<script setup lang="ts">
import type { PrimitiveProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import { reactiveOmit } from "@vueuse/core"
import { Primitive, useForwardProps } from "reka-ui"
import { cn } from "@/lib/utils"

const props = defineProps<PrimitiveProps & { class?: HTMLAttributes["class"] }>()
const delegatedProps = reactiveOmit(props, "class")
const forwardedProps = useForwardProps(delegatedProps)
</script>

<template>
  <Primitive
    data-slot="pin-input-group"
    v-bind="forwardedProps"
    :class="cn('flex items-center', props.class)"
  >
    <slot />
  </Primitive>
</template>
```

## PinInputSeparator.vue

```vue
<script setup lang="ts">
import type { PrimitiveProps } from "reka-ui"
import { Minus } from "@lucide/vue"
import { Primitive, useForwardProps } from "reka-ui"

const props = defineProps<PrimitiveProps>()
const forwardedProps = useForwardProps(props)
</script>

<template>
  <Primitive
    data-slot="pin-input-separator"
    v-bind="forwardedProps"
  >
    <slot>
      <Minus />
    </slot>
  </Primitive>
</template>
```

## PinInputSlot.vue

```vue
<script setup lang="ts">
import type { PinInputInputProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import { reactiveOmit } from "@vueuse/core"
import { PinInputInput, useForwardProps } from "reka-ui"
import { cn } from "@/lib/utils"

const props = defineProps<PinInputInputProps & { class?: HTMLAttributes["class"] }>()

const delegatedProps = reactiveOmit(props, "class")

const forwardedProps = useForwardProps(delegatedProps)
</script>

<template>
  <PinInputInput
    data-slot="pin-input-slot"
    v-bind="forwardedProps"
    :class="cn('border-input focus:border-ring focus:ring-ring/50 focus:aria-invalid:ring-destructive/20 dark:bg-input/30 dark:focus:aria-invalid:ring-destructive/40 aria-invalid:border-destructive focus:aria-invalid:border-destructive relative flex h-9 w-9 items-center justify-center border-y border-r text-sm shadow-xs transition-all outline-none text-center first:rounded-l-md first:border-l last:rounded-r-md focus:z-10 focus:ring-3', props.class)"
  />
</template>
```

## Quellen
- `/tmp/shadcn-vue-repo/apps/v4/registry/new-york-v4/ui/pin-input/`
