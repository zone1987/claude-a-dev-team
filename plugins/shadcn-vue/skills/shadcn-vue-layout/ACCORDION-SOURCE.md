# Accordion — Complete Source Code

## Contents

- [index.ts](#indexts)
- [Accordion.vue](#accordionvue)
- [AccordionContent.vue](#accordioncontentvue)
- [AccordionItem.vue](#accordionitemvue)
- [AccordionTrigger.vue](#accordiontriggervue)

## index.ts

```ts
export { default as Accordion } from "./Accordion.vue"
export { default as AccordionContent } from "./AccordionContent.vue"
export { default as AccordionItem } from "./AccordionItem.vue"
export { default as AccordionTrigger } from "./AccordionTrigger.vue"
```

## Accordion.vue

```vue
<script setup lang="ts">
import type { AccordionRootEmits, AccordionRootProps } from "reka-ui"
import {
  AccordionRoot,
  useForwardPropsEmits,
} from "reka-ui"

const props = defineProps<AccordionRootProps>()
const emits = defineEmits<AccordionRootEmits>()

const forwarded = useForwardPropsEmits(props, emits)
</script>

<template>
  <AccordionRoot v-slot="slotProps" data-slot="accordion" v-bind="forwarded">
    <slot v-bind="slotProps" />
  </AccordionRoot>
</template>
```

## AccordionContent.vue

```vue
<script setup lang="ts">
import type { AccordionContentProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import { reactiveOmit } from "@vueuse/core"
import { AccordionContent } from "reka-ui"
import { cn } from "@/lib/utils"

const props = defineProps<AccordionContentProps & { class?: HTMLAttributes["class"] }>()

const delegatedProps = reactiveOmit(props, "class")
</script>

<template>
  <AccordionContent
    data-slot="accordion-content"
    v-bind="delegatedProps"
    class="data-[state=closed]:animate-accordion-up data-[state=open]:animate-accordion-down overflow-hidden text-sm"
  >
    <div :class="cn('pt-0 pb-4', props.class)">
      <slot />
    </div>
  </AccordionContent>
</template>
```

## AccordionItem.vue

```vue
<script setup lang="ts">
import type { AccordionItemProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import { reactiveOmit } from "@vueuse/core"
import { AccordionItem, useForwardProps } from "reka-ui"
import { cn } from "@/lib/utils"

const props = defineProps<AccordionItemProps & { class?: HTMLAttributes["class"] }>()

const delegatedProps = reactiveOmit(props, "class")

const forwardedProps = useForwardProps(delegatedProps)
</script>

<template>
  <AccordionItem
    v-slot="slotProps"
    data-slot="accordion-item"
    v-bind="forwardedProps"
    :class="cn('border-b last:border-b-0', props.class)"
  >
    <slot v-bind="slotProps" />
  </AccordionItem>
</template>
```

## AccordionTrigger.vue

```vue
<script setup lang="ts">
import type { AccordionTriggerProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import { ChevronDown } from "@lucide/vue"
import { reactiveOmit } from "@vueuse/core"
import {
  AccordionHeader,
  AccordionTrigger,
} from "reka-ui"
import { cn } from "@/lib/utils"

const props = defineProps<AccordionTriggerProps & { class?: HTMLAttributes["class"] }>()

const delegatedProps = reactiveOmit(props, "class")
</script>

<template>
  <AccordionHeader class="flex">
    <AccordionTrigger
      data-slot="accordion-trigger"
      v-bind="delegatedProps"
      :class="
        cn(
          'focus-visible:border-ring focus-visible:ring-ring/50 flex flex-1 items-start justify-between gap-4 rounded-md py-4 text-left text-sm font-medium transition-all outline-none hover:underline focus-visible:ring-3 disabled:pointer-events-none disabled:opacity-50 [&[data-state=open]>svg]:rotate-180',
          props.class,
        )
      "
    >
      <slot />
      <slot name="icon">
        <ChevronDown
          class="text-muted-foreground pointer-events-none size-4 shrink-0 translate-y-0.5 transition-transform duration-200"
        />
      </slot>
    </AccordionTrigger>
  </AccordionHeader>
</template>
```

---
Source: `/tmp/shadcn-vue-repo/apps/v4/registry/new-york-v4/ui/accordion/`
