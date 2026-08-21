# Source Code

## Contents

- [Stepper.vue](#steppervue)
- [StepperDescription.vue](#stepperdescriptionvue)
- [StepperIndicator.vue](#stepperindicatorvue)
- [StepperItem.vue](#stepperitemvue)
- [StepperSeparator.vue](#stepperseparatorvue)
- [StepperTitle.vue](#steppertitlevue)
- [StepperTrigger.vue](#steppertriggervue)
- [index.ts](#indexts)

## Stepper.vue

```vue
<script lang="ts" setup>
import type { StepperRootEmits, StepperRootProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import { reactiveOmit } from "@vueuse/core"
import { StepperRoot, useForwardPropsEmits } from "reka-ui"
import { cn } from "@/lib/utils"

const props = defineProps<StepperRootProps & { class?: HTMLAttributes["class"] }>()
const emits = defineEmits<StepperRootEmits>()

const delegatedProps = reactiveOmit(props, "class")

const forwarded = useForwardPropsEmits(delegatedProps, emits)
</script>

<template>
  <StepperRoot
    v-slot="slotProps"
    :class="cn(
      'flex gap-2',
      props.class,
    )"
    v-bind="forwarded"
  >
    <slot v-bind="slotProps" />
  </StepperRoot>
</template>
```

## StepperDescription.vue

```vue
<script lang="ts" setup>
import type { StepperDescriptionProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import { reactiveOmit } from "@vueuse/core"
import { StepperDescription, useForwardProps } from "reka-ui"
import { cn } from "@/lib/utils"

const props = defineProps<StepperDescriptionProps & { class?: HTMLAttributes["class"] }>()

const delegatedProps = reactiveOmit(props, "class")

const forwarded = useForwardProps(delegatedProps)
</script>

<template>
  <StepperDescription v-slot="slotProps" v-bind="forwarded" :class="cn('text-xs text-muted-foreground', props.class)">
    <slot v-bind="slotProps" />
  </StepperDescription>
</template>
```

## StepperIndicator.vue

```vue
<script lang="ts" setup>
import type { StepperIndicatorProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import { reactiveOmit } from "@vueuse/core"
import { StepperIndicator, useForwardProps } from "reka-ui"
import { cn } from "@/lib/utils"

const props = defineProps<StepperIndicatorProps & { class?: HTMLAttributes["class"] }>()

const delegatedProps = reactiveOmit(props, "class")

const forwarded = useForwardProps(delegatedProps)
</script>

<template>
  <StepperIndicator
    v-slot="slotProps"
    v-bind="forwarded"
    :class="cn(
      'inline-flex items-center justify-center rounded-full text-muted-foreground/50 w-8 h-8',
      // Disabled
      'group-data-[disabled]:text-muted-foreground group-data-[disabled]:opacity-50',
      // Active
      'group-data-[state=active]:bg-primary group-data-[state=active]:text-primary-foreground',
      // Completed
      'group-data-[state=completed]:bg-accent group-data-[state=completed]:text-accent-foreground',
      props.class,
    )"
  >
    <slot v-bind="slotProps" />
  </StepperIndicator>
</template>
```

## StepperItem.vue

```vue
<script lang="ts" setup>
import type { StepperItemProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import { reactiveOmit } from "@vueuse/core"
import { StepperItem, useForwardProps } from "reka-ui"
import { cn } from "@/lib/utils"

const props = defineProps<StepperItemProps & { class?: HTMLAttributes["class"] }>()

const delegatedProps = reactiveOmit(props, "class")

const forwarded = useForwardProps(delegatedProps)
</script>

<template>
  <StepperItem
    v-slot="slotProps"
    v-bind="forwarded"
    :class="cn('flex items-center gap-2 group data-[disabled]:pointer-events-none', props.class)"
  >
    <slot v-bind="slotProps" />
  </StepperItem>
</template>
```

## StepperSeparator.vue

```vue
<script lang="ts" setup>
import type { StepperSeparatorProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import { reactiveOmit } from "@vueuse/core"
import { StepperSeparator, useForwardProps } from "reka-ui"
import { cn } from "@/lib/utils"

const props = defineProps<StepperSeparatorProps & { class?: HTMLAttributes["class"] }>()

const delegatedProps = reactiveOmit(props, "class")

const forwarded = useForwardProps(delegatedProps)
</script>

<template>
  <StepperSeparator
    v-bind="forwarded"
    :class="cn(
      'bg-muted',
      // Disabled
      'group-data-[disabled]:bg-muted group-data-[disabled]:opacity-50',
      // Completed
      'group-data-[state=completed]:bg-accent',
      props.class,
    )"
  />
</template>
```

## StepperTitle.vue

```vue
<script lang="ts" setup>
import type { StepperTitleProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import { reactiveOmit } from "@vueuse/core"
import { StepperTitle, useForwardProps } from "reka-ui"
import { cn } from "@/lib/utils"

const props = defineProps<StepperTitleProps & { class?: HTMLAttributes["class"] }>()

const delegatedProps = reactiveOmit(props, "class")

const forwarded = useForwardProps(delegatedProps)
</script>

<template>
  <StepperTitle v-bind="forwarded" :class="cn('text-md font-semibold whitespace-nowrap', props.class)">
    <slot />
  </StepperTitle>
</template>
```

## StepperTrigger.vue

```vue
<script lang="ts" setup>
import type { StepperTriggerProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import { reactiveOmit } from "@vueuse/core"
import { StepperTrigger, useForwardProps } from "reka-ui"
import { cn } from "@/lib/utils"

const props = defineProps<StepperTriggerProps & { class?: HTMLAttributes["class"] }>()

const delegatedProps = reactiveOmit(props, "class")

const forwarded = useForwardProps(delegatedProps)
</script>

<template>
  <StepperTrigger
    v-bind="forwarded"
    :class="cn('p-1 flex flex-col items-center text-center gap-1 rounded-md', props.class)"
  >
    <slot />
  </StepperTrigger>
</template>
```

## index.ts

```ts
export { default as Stepper } from "./Stepper.vue"
export { default as StepperDescription } from "./StepperDescription.vue"
export { default as StepperIndicator } from "./StepperIndicator.vue"
export { default as StepperItem } from "./StepperItem.vue"
export { default as StepperSeparator } from "./StepperSeparator.vue"
export { default as StepperTitle } from "./StepperTitle.vue"
export { default as StepperTrigger } from "./StepperTrigger.vue"
```

Sources:
- `registry/new-york-v4/ui/stepper/Stepper.vue`
- `registry/new-york-v4/ui/stepper/StepperDescription.vue`
- `registry/new-york-v4/ui/stepper/StepperIndicator.vue`
- `registry/new-york-v4/ui/stepper/StepperItem.vue`
- `registry/new-york-v4/ui/stepper/StepperSeparator.vue`
- `registry/new-york-v4/ui/stepper/StepperTitle.vue`
- `registry/new-york-v4/ui/stepper/StepperTrigger.vue`
- `registry/new-york-v4/ui/stepper/index.ts`
