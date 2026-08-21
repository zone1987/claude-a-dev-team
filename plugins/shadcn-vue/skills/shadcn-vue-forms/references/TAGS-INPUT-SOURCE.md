# Source Code

## Contents

- [TagsInput.vue](#tagsinputvue)
- [TagsInputInput.vue](#tagsinputinputvue)
- [TagsInputItem.vue](#tagsinputitemvue)
- [TagsInputItemDelete.vue](#tagsinputitemdeletevue)
- [TagsInputItemText.vue](#tagsinputitemtextvue)
- [index.ts](#indexts)

## TagsInput.vue

```vue
<script setup lang="ts">
import type { TagsInputRootEmits, TagsInputRootProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import { reactiveOmit } from "@vueuse/core"
import { TagsInputRoot, useForwardPropsEmits } from "reka-ui"
import { cn } from "@/lib/utils"

const props = defineProps<TagsInputRootProps & { class?: HTMLAttributes["class"] }>()
const emits = defineEmits<TagsInputRootEmits>()

const delegatedProps = reactiveOmit(props, "class")

const forwarded = useForwardPropsEmits(delegatedProps, emits)
</script>

<template>
  <TagsInputRoot
    v-slot="slotProps" v-bind="forwarded" :class="cn(
      'flex flex-wrap gap-2 items-center rounded-md border border-input bg-background px-2 py-1 text-sm shadow-xs transition-[color,box-shadow] outline-none',
      'focus-within:border-ring focus-within:ring-ring/50 focus-within:ring-3',
      'aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive',
      props.class)"
  >
    <slot v-bind="slotProps" />
  </TagsInputRoot>
</template>
```

## TagsInputInput.vue

```vue
<script setup lang="ts">
import type { TagsInputInputProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import { reactiveOmit } from "@vueuse/core"
import { TagsInputInput, useForwardProps } from "reka-ui"
import { cn } from "@/lib/utils"

const props = defineProps<TagsInputInputProps & { class?: HTMLAttributes["class"] }>()

const delegatedProps = reactiveOmit(props, "class")

const forwardedProps = useForwardProps(delegatedProps)
</script>

<template>
  <TagsInputInput v-bind="forwardedProps" :class="cn('text-sm min-h-5 focus:outline-none flex-1 bg-transparent px-1', props.class)" />
</template>
```

## TagsInputItem.vue

```vue
<script setup lang="ts">
import type { TagsInputItemProps } from "reka-ui"
import type { HTMLAttributes } from "vue"

import { reactiveOmit } from "@vueuse/core"
import { TagsInputItem, useForwardProps } from "reka-ui"
import { cn } from "@/lib/utils"

const props = defineProps<TagsInputItemProps & { class?: HTMLAttributes["class"] }>()

const delegatedProps = reactiveOmit(props, "class")

const forwardedProps = useForwardProps(delegatedProps)
</script>

<template>
  <TagsInputItem v-bind="forwardedProps" :class="cn('flex h-5 items-center rounded-md bg-secondary data-[state=active]:ring-ring data-[state=active]:ring-2 data-[state=active]:ring-offset-2 ring-offset-background', props.class)">
    <slot />
  </TagsInputItem>
</template>
```

## TagsInputItemDelete.vue

```vue
<script setup lang="ts">
import type { TagsInputItemDeleteProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import { X } from "@lucide/vue"
import { reactiveOmit } from "@vueuse/core"
import { TagsInputItemDelete, useForwardProps } from "reka-ui"
import { cn } from "@/lib/utils"

const props = defineProps<TagsInputItemDeleteProps & { class?: HTMLAttributes["class"] }>()

const delegatedProps = reactiveOmit(props, "class")

const forwardedProps = useForwardProps(delegatedProps)
</script>

<template>
  <TagsInputItemDelete v-bind="forwardedProps" :class="cn('flex rounded bg-transparent mr-1', props.class)">
    <slot>
      <X class="w-4 h-4" />
    </slot>
  </TagsInputItemDelete>
</template>
```

## TagsInputItemText.vue

```vue
<script setup lang="ts">
import type { TagsInputItemTextProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import { reactiveOmit } from "@vueuse/core"
import { TagsInputItemText, useForwardProps } from "reka-ui"
import { cn } from "@/lib/utils"

const props = defineProps<TagsInputItemTextProps & { class?: HTMLAttributes["class"] }>()

const delegatedProps = reactiveOmit(props, "class")

const forwardedProps = useForwardProps(delegatedProps)
</script>

<template>
  <TagsInputItemText v-bind="forwardedProps" :class="cn('py-0.5 px-2 text-sm rounded bg-transparent', props.class)">
    <slot />
  </TagsInputItemText>
</template>
```

## index.ts

```ts
export { default as TagsInput } from "./TagsInput.vue"
export { default as TagsInputInput } from "./TagsInputInput.vue"
export { default as TagsInputItem } from "./TagsInputItem.vue"
export { default as TagsInputItemDelete } from "./TagsInputItemDelete.vue"
export { default as TagsInputItemText } from "./TagsInputItemText.vue"
```

Sources:
- `registry/new-york-v4/ui/tags-input/TagsInput.vue`
- `registry/new-york-v4/ui/tags-input/TagsInputInput.vue`
- `registry/new-york-v4/ui/tags-input/TagsInputItem.vue`
- `registry/new-york-v4/ui/tags-input/TagsInputItemDelete.vue`
- `registry/new-york-v4/ui/tags-input/TagsInputItemText.vue`
- `registry/new-york-v4/ui/tags-input/index.ts`
