# AlertDialog — Source Code

## index.ts

```ts
export { default as AlertDialog } from "./AlertDialog.vue"
export { default as AlertDialogAction } from "./AlertDialogAction.vue"
export { default as AlertDialogCancel } from "./AlertDialogCancel.vue"
export { default as AlertDialogContent } from "./AlertDialogContent.vue"
export { default as AlertDialogDescription } from "./AlertDialogDescription.vue"
export { default as AlertDialogFooter } from "./AlertDialogFooter.vue"
export { default as AlertDialogHeader } from "./AlertDialogHeader.vue"
export { default as AlertDialogTitle } from "./AlertDialogTitle.vue"
export { default as AlertDialogTrigger } from "./AlertDialogTrigger.vue"
```

## AlertDialog.vue

Root component. Forwards all props and emits to reka-ui `AlertDialogRoot`.

```vue
<script setup lang="ts">
import type { AlertDialogEmits, AlertDialogProps } from "reka-ui"
import { AlertDialogRoot, useForwardPropsEmits } from "reka-ui"

const props = defineProps<AlertDialogProps>()
const emits = defineEmits<AlertDialogEmits>()

const forwarded = useForwardPropsEmits(props, emits)
</script>

<template>
  <AlertDialogRoot v-slot="slotProps" data-slot="alert-dialog" v-bind="forwarded">
    <slot v-bind="slotProps" />
  </AlertDialogRoot>
</template>
```

## AlertDialogTrigger.vue

Renders the trigger element that opens the dialog.

```vue
<script setup lang="ts">
import type { AlertDialogTriggerProps } from "reka-ui"
import { AlertDialogTrigger } from "reka-ui"

const props = defineProps<AlertDialogTriggerProps>()
</script>

<template>
  <AlertDialogTrigger data-slot="alert-dialog-trigger" v-bind="props">
    <slot />
  </AlertDialogTrigger>
</template>
```

## AlertDialogContent.vue

Portal + overlay + animated modal panel. Strips the `class` prop before forwarding to reka-ui.

```vue
<script setup lang="ts">
import type { AlertDialogContentEmits, AlertDialogContentProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import { reactiveOmit } from "@vueuse/core"
import {
  AlertDialogContent,
  AlertDialogOverlay,
  AlertDialogPortal,
  useForwardPropsEmits,
} from "reka-ui"
import { cn } from "@/lib/utils"

defineOptions({
  inheritAttrs: false,
})

const props = defineProps<AlertDialogContentProps & { class?: HTMLAttributes["class"] }>()
const emits = defineEmits<AlertDialogContentEmits>()

const delegatedProps = reactiveOmit(props, "class")

const forwarded = useForwardPropsEmits(delegatedProps, emits)
</script>

<template>
  <AlertDialogPortal>
    <AlertDialogOverlay
      data-slot="alert-dialog-overlay"
      class="data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 fixed inset-0 z-50 bg-black/80"
    />
    <AlertDialogContent
      data-slot="alert-dialog-content"
      v-bind="{ ...$attrs, ...forwarded }"
      :class="
        cn(
          'bg-background data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 fixed top-[50%] left-[50%] z-50 grid w-full max-w-[calc(100%-2rem)] translate-x-[-50%] translate-y-[-50%] gap-4 rounded-lg border p-6 shadow-lg duration-200 sm:max-w-lg',
          props.class,
        )
      "
    >
      <slot />
    </AlertDialogContent>
  </AlertDialogPortal>
</template>
```

## AlertDialogHeader.vue

Layout wrapper for title + description. Centered on mobile, left-aligned on `sm:`.

```vue
<script setup lang="ts">
import type { HTMLAttributes } from "vue"
import { cn } from "@/lib/utils"

const props = defineProps<{ class?: HTMLAttributes["class"] }>()
</script>

<template>
  <div data-slot="alert-dialog-header" :class="cn('flex flex-col gap-2 text-center sm:text-left', props.class)">
    <slot />
  </div>
</template>
```

## AlertDialogFooter.vue

Layout wrapper for action buttons. Stacked (reverse) on mobile, row (justify-end) on `sm:`.

```vue
<script setup lang="ts">
import type { HTMLAttributes } from "vue"
import { cn } from "@/lib/utils"

const props = defineProps<{ class?: HTMLAttributes["class"] }>()
</script>

<template>
  <div data-slot="alert-dialog-footer" :class="cn('flex flex-col-reverse gap-2 sm:flex-row sm:justify-end', props.class)">
    <slot />
  </div>
</template>
```

## AlertDialogTitle.vue

Heading rendered via reka-ui `AlertDialogTitle`. Styled `text-lg font-semibold`.

```vue
<script setup lang="ts">
import type { AlertDialogTitleProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import { reactiveOmit } from "@vueuse/core"
import { AlertDialogTitle } from "reka-ui"
import { cn } from "@/lib/utils"

const props = defineProps<AlertDialogTitleProps & { class?: HTMLAttributes["class"] }>()
const delegatedProps = reactiveOmit(props, "class")
</script>

<template>
  <AlertDialogTitle data-slot="alert-dialog-title" v-bind="delegatedProps" :class="cn('text-lg font-semibold', props.class)">
    <slot />
  </AlertDialogTitle>
</template>
```

## AlertDialogDescription.vue

Descriptive text rendered via reka-ui `AlertDialogDescription`. Styled `text-muted-foreground text-sm`.

```vue
<script setup lang="ts">
import type { AlertDialogDescriptionProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import { reactiveOmit } from "@vueuse/core"
import { AlertDialogDescription } from "reka-ui"
import { cn } from "@/lib/utils"

const props = defineProps<AlertDialogDescriptionProps & { class?: HTMLAttributes["class"] }>()
const delegatedProps = reactiveOmit(props, "class")
</script>

<template>
  <AlertDialogDescription data-slot="alert-dialog-description" v-bind="delegatedProps" :class="cn('text-muted-foreground text-sm', props.class)">
    <slot />
  </AlertDialogDescription>
</template>
```

## AlertDialogAction.vue

Confirmation button. Uses `buttonVariants()` (default variant) from the Button component.

```vue
<script setup lang="ts">
import type { AlertDialogActionProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import { reactiveOmit } from "@vueuse/core"
import { AlertDialogAction } from "reka-ui"
import { cn } from "@/lib/utils"
import { buttonVariants } from "@/components/ui/button"

const props = defineProps<AlertDialogActionProps & { class?: HTMLAttributes["class"] }>()
const delegatedProps = reactiveOmit(props, "class")
</script>

<template>
  <AlertDialogAction v-bind="delegatedProps" :class="cn(buttonVariants(), props.class)">
    <slot />
  </AlertDialogAction>
</template>
```

## AlertDialogCancel.vue

Dismiss button. Uses `buttonVariants({ variant: "outline" })` from the Button component, with `mt-2 sm:mt-0` for footer spacing.

```vue
<script setup lang="ts">
import type { AlertDialogCancelProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import { reactiveOmit } from "@vueuse/core"
import { AlertDialogCancel } from "reka-ui"
import { cn } from "@/lib/utils"
import { buttonVariants } from "@/components/ui/button"

const props = defineProps<AlertDialogCancelProps & { class?: HTMLAttributes["class"] }>()
const delegatedProps = reactiveOmit(props, "class")
</script>

<template>
  <AlertDialogCancel v-bind="delegatedProps" :class="cn(buttonVariants({ variant: 'outline' }), 'mt-2 sm:mt-0', props.class)">
    <slot />
  </AlertDialogCancel>
</template>
```
