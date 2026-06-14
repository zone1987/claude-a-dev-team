# Drawer — Quellcode

Alle Dateien aus `registry/new-york-v4/ui/drawer/`.

## Drawer.vue

```vue
<script lang="ts" setup>
import type { DrawerRootEmits, DrawerRootProps } from "vaul-vue"
import { useForwardPropsEmits } from "reka-ui"
import { DrawerRoot } from "vaul-vue"

const props = withDefaults(defineProps<DrawerRootProps>(), {
  shouldScaleBackground: true,
})

const emits = defineEmits<DrawerRootEmits>()

const forwarded = useForwardPropsEmits(props, emits)
</script>

<template>
  <DrawerRoot
    v-slot="slotProps"
    data-slot="drawer"
    v-bind="forwarded"
  >
    <slot v-bind="slotProps" />
  </DrawerRoot>
</template>
```

## DrawerClose.vue

```vue
<script lang="ts" setup>
import type { DrawerCloseProps } from "vaul-vue"
import { DrawerClose } from "vaul-vue"

const props = defineProps<DrawerCloseProps>()
</script>

<template>
  <DrawerClose
    data-slot="drawer-close"
    v-bind="props"
  >
    <slot />
  </DrawerClose>
</template>
```

## DrawerContent.vue

```vue
<script lang="ts" setup>
import type { DialogContentEmits, DialogContentProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import { useForwardPropsEmits } from "reka-ui"
import { DrawerContent, DrawerPortal } from "vaul-vue"
import { cn } from "@/lib/utils"
import DrawerOverlay from "./DrawerOverlay.vue"

defineOptions({
  inheritAttrs: false,
})

const props = defineProps<DialogContentProps & { class?: HTMLAttributes["class"] }>()
const emits = defineEmits<DialogContentEmits>()

const forwarded = useForwardPropsEmits(props, emits)
</script>

<template>
  <DrawerPortal>
    <DrawerOverlay />
    <DrawerContent
      data-slot="drawer-content"
      v-bind="{ ...$attrs, ...forwarded }"
      :class="cn(
        'group/drawer-content bg-background fixed z-50 flex h-auto flex-col',
        'data-[vaul-drawer-direction=top]:inset-x-0 data-[vaul-drawer-direction=top]:top-0 data-[vaul-drawer-direction=top]:mb-24 data-[vaul-drawer-direction=top]:max-h-[80vh] data-[vaul-drawer-direction=top]:rounded-b-lg',
        'data-[vaul-drawer-direction=bottom]:inset-x-0 data-[vaul-drawer-direction=bottom]:bottom-0 data-[vaul-drawer-direction=bottom]:mt-24 data-[vaul-drawer-direction=bottom]:max-h-[80vh] data-[vaul-drawer-direction=bottom]:rounded-t-lg',
        'data-[vaul-drawer-direction=right]:inset-y-0 data-[vaul-drawer-direction=right]:right-0 data-[vaul-drawer-direction=right]:w-3/4 data-[vaul-drawer-direction=right]:sm:max-w-sm',
        'data-[vaul-drawer-direction=left]:inset-y-0 data-[vaul-drawer-direction=left]:left-0 data-[vaul-drawer-direction=left]:w-3/4 data-[vaul-drawer-direction=left]:sm:max-w-sm',
        props.class,
      )"
    >
      <div class="bg-muted mx-auto mt-4 hidden h-2 w-[100px] shrink-0 rounded-full group-data-[vaul-drawer-direction=bottom]/drawer-content:block" />
      <slot />
    </DrawerContent>
  </DrawerPortal>
</template>
```

## DrawerDescription.vue

```vue
<script lang="ts" setup>
import type { DrawerDescriptionProps } from "vaul-vue"
import type { HTMLAttributes } from "vue"
import { reactiveOmit } from "@vueuse/core"
import { DrawerDescription } from "vaul-vue"
import { cn } from "@/lib/utils"

const props = defineProps<DrawerDescriptionProps & { class?: HTMLAttributes["class"] }>()

const delegatedProps = reactiveOmit(props, "class")
</script>

<template>
  <DrawerDescription
    data-slot="drawer-description"
    v-bind="delegatedProps"
    :class="cn('text-muted-foreground text-sm', props.class)"
  >
    <slot />
  </DrawerDescription>
</template>
```

## DrawerFooter.vue

```vue
<script lang="ts" setup>
import type { HTMLAttributes } from "vue"
import { cn } from "@/lib/utils"

const props = defineProps<{
  class?: HTMLAttributes["class"]
}>()
</script>

<template>
  <div
    data-slot="drawer-footer"
    :class="cn('mt-auto flex flex-col gap-2 p-4', props.class)"
  >
    <slot />
  </div>
</template>
```

## DrawerHeader.vue

```vue
<script lang="ts" setup>
import type { HTMLAttributes } from "vue"
import { cn } from "@/lib/utils"

const props = defineProps<{
  class?: HTMLAttributes["class"]
}>()
</script>

<template>
  <div
    data-slot="drawer-header"
    :class="cn('flex flex-col gap-1.5 p-4', props.class)"
  >
    <slot />
  </div>
</template>
```

## DrawerOverlay.vue

```vue
<script lang="ts" setup>
import type { DialogOverlayProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import { reactiveOmit } from "@vueuse/core"
import { DrawerOverlay } from "vaul-vue"
import { cn } from "@/lib/utils"

const props = defineProps<DialogOverlayProps & { class?: HTMLAttributes["class"] }>()

const delegatedProps = reactiveOmit(props, "class")
</script>

<template>
  <DrawerOverlay
    data-slot="drawer-overlay"
    v-bind="delegatedProps"
    :class="cn('data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 fixed inset-0 z-50 bg-black/80', props.class)"
  />
</template>
```

## DrawerTitle.vue

```vue
<script lang="ts" setup>
import type { DrawerTitleProps } from "vaul-vue"
import type { HTMLAttributes } from "vue"
import { reactiveOmit } from "@vueuse/core"
import { DrawerTitle } from "vaul-vue"
import { cn } from "@/lib/utils"

const props = defineProps<DrawerTitleProps & { class?: HTMLAttributes["class"] }>()

const delegatedProps = reactiveOmit(props, "class")
</script>

<template>
  <DrawerTitle
    data-slot="drawer-title"
    v-bind="delegatedProps"
    :class="cn('text-foreground font-semibold', props.class)"
  >
    <slot />
  </DrawerTitle>
</template>
```

## DrawerTrigger.vue

```vue
<script lang="ts" setup>
import type { DrawerTriggerProps } from "vaul-vue"
import { DrawerTrigger } from "vaul-vue"

const props = defineProps<DrawerTriggerProps>()
</script>

<template>
  <DrawerTrigger
    data-slot="drawer-trigger"
    v-bind="props"
  >
    <slot />
  </DrawerTrigger>
</template>
```

## index.ts

```ts
export { default as Drawer } from "./Drawer.vue"
export { default as DrawerClose } from "./DrawerClose.vue"
export { default as DrawerContent } from "./DrawerContent.vue"
export { default as DrawerDescription } from "./DrawerDescription.vue"
export { default as DrawerFooter } from "./DrawerFooter.vue"
export { default as DrawerHeader } from "./DrawerHeader.vue"
export { default as DrawerOverlay } from "./DrawerOverlay.vue"
export { default as DrawerTitle } from "./DrawerTitle.vue"
export { default as DrawerTrigger } from "./DrawerTrigger.vue"
```

Quellen:
- `/tmp/shadcn-vue-repo/apps/v4/registry/new-york-v4/ui/drawer/`
