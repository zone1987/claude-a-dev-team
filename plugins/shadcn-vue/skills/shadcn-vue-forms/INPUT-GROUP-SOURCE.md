# InputGroup — Quellcode

All files from `registry/new-york-v4/ui/input-group/`.

## Contents

- [InputGroup.vue](#inputgroupvue)
- [InputGroupAddon.vue](#inputgroupaddonvue)
- [InputGroupButton.vue](#inputgroupbuttonvue)
- [InputGroupInput.vue](#inputgroupinputvue)
- [InputGroupText.vue](#inputgrouptextvue)
- [InputGroupTextarea.vue](#inputgrouptextareavue)
- [index.ts](#indexts)

## InputGroup.vue

```vue
<script setup lang="ts">
import type { HTMLAttributes } from "vue"
import { cn } from "@/lib/utils"

const props = defineProps<{
  class?: HTMLAttributes["class"]
}>()
</script>

<template>
  <div
    data-slot="input-group"
    role="group"
    :class="cn(
      'group/input-group border-input dark:bg-input/30 relative flex w-full items-center rounded-md border shadow-xs transition-[color,box-shadow] outline-none',
      'h-9 min-w-0 has-[>textarea]:h-auto',

      // Variants based on alignment.
      'has-[>[data-align=inline-start]]:[&>input]:pl-2',
      'has-[>[data-align=inline-end]]:[&>input]:pr-2',
      'has-[>[data-align=block-start]]:h-auto has-[>[data-align=block-start]]:flex-col has-[>[data-align=block-start]]:[&>input]:pb-3',
      'has-[>[data-align=block-end]]:h-auto has-[>[data-align=block-end]]:flex-col has-[>[data-align=block-end]]:[&>input]:pt-3',

      // Focus state.
      'has-[[data-slot=input-group-control]:focus-visible]:border-ring has-[[data-slot=input-group-control]:focus-visible]:ring-ring/50 has-[[data-slot=input-group-control]:focus-visible]:ring-3',

      // Error state.
      'has-[[data-slot][aria-invalid=true]]:ring-destructive/20 has-[[data-slot][aria-invalid=true]]:border-destructive dark:has-[[data-slot][aria-invalid=true]]:ring-destructive/40',

      props.class,
    )"
  >
    <slot />
  </div>
</template>
```

## InputGroupAddon.vue

```vue
<script setup lang="ts">
import type { HTMLAttributes } from "vue"
import type { InputGroupVariants } from "."
import { cn } from "@/lib/utils"
import { inputGroupAddonVariants } from "."

const props = withDefaults(defineProps<{
  align?: InputGroupVariants["align"]
  class?: HTMLAttributes["class"]
}>(), {
  align: "inline-start",
})

function handleInputGroupAddonClick(e: MouseEvent) {
  const currentTarget = e.currentTarget as HTMLElement | null
  const target = e.target as HTMLElement | null
  if (target && target.closest("button")) {
    return
  }
  if (currentTarget && currentTarget?.parentElement) {
    currentTarget.parentElement?.querySelector("input")?.focus()
  }
}
</script>

<template>
  <div
    role="group"
    data-slot="input-group-addon"
    :data-align="props.align"
    :class="cn(inputGroupAddonVariants({ align: props.align }), props.class)"
    @click="handleInputGroupAddonClick"
  >
    <slot />
  </div>
</template>
```

## InputGroupButton.vue

```vue
<script setup lang="ts">
import type { HTMLAttributes } from "vue"
import type { InputGroupButtonVariants } from "."
import type { ButtonVariants } from "@/registry/new-york-v4/ui/button"
import { cn } from "@/lib/utils"
import { Button } from "@/registry/new-york-v4/ui/button"
import { inputGroupButtonVariants } from "."

interface InputGroupButtonProps {
  variant?: ButtonVariants["variant"]
  size?: InputGroupButtonVariants["size"]
  class?: HTMLAttributes["class"]
}

const props = withDefaults(defineProps<InputGroupButtonProps>(), {
  size: "xs",
  variant: "ghost",
})
</script>

<template>
  <Button
    :data-size="props.size"
    :variant="props.variant"
    :class="cn(inputGroupButtonVariants({ size: props.size }), props.class)"
  >
    <slot />
  </Button>
</template>
```

## InputGroupInput.vue

```vue
<script setup lang="ts">
import type { HTMLAttributes } from "vue"
import { cn } from "@/lib/utils"
import { Input } from "@/registry/new-york-v4/ui/input"

const props = defineProps<{
  class?: HTMLAttributes["class"]
}>()
</script>

<template>
  <Input
    data-slot="input-group-control"
    :class="cn(
      'flex-1 rounded-none border-0 bg-transparent shadow-none focus-visible:ring-0 dark:bg-transparent',
      props.class,
    )"
  />
</template>
```

## InputGroupText.vue

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
    :class="cn(
      'text-muted-foreground flex items-center gap-2 text-sm [&_svg]:pointer-events-none [&_svg:not([class*=\'size-\'])]:size-4',
      props.class,
    )"
  >
    <slot />
  </span>
</template>
```

## InputGroupTextarea.vue

```vue
<script setup lang="ts">
import type { HTMLAttributes } from "vue"
import { cn } from "@/lib/utils"
import { Textarea } from "@/registry/new-york-v4/ui/textarea"

const props = defineProps<{
  class?: HTMLAttributes["class"]
}>()
</script>

<template>
  <Textarea
    data-slot="input-group-control"
    :class="cn(
      'flex-1 resize-none rounded-none border-0 bg-transparent py-3 shadow-none focus-visible:ring-0 dark:bg-transparent',
      props.class,
    )"
  />
</template>
```

## index.ts

```ts
import type { VariantProps } from "class-variance-authority"
import { cva } from "class-variance-authority"

export { default as InputGroup } from "./InputGroup.vue"
export { default as InputGroupAddon } from "./InputGroupAddon.vue"
export { default as InputGroupButton } from "./InputGroupButton.vue"
export { default as InputGroupInput } from "./InputGroupInput.vue"
export { default as InputGroupText } from "./InputGroupText.vue"
export { default as InputGroupTextarea } from "./InputGroupTextarea.vue"

export const inputGroupAddonVariants = cva(
  "text-muted-foreground flex h-auto cursor-text items-center justify-center gap-2 py-1.5 text-sm font-medium select-none [&>svg:not([class*='size-'])]:size-4 [&>kbd]:rounded-[calc(var(--radius)-5px)] group-data-[disabled=true]/input-group:opacity-50",
  {
    variants: {
      align: {
        "inline-start":
          "order-first pl-3 has-[>button]:ml-[-0.45rem] has-[>kbd]:ml-[-0.35rem]",
        "inline-end":
          "order-last pr-3 has-[>button]:mr-[-0.45rem] has-[>kbd]:mr-[-0.35rem]",
        "block-start":
          "order-first w-full justify-start px-3 pt-3 [.border-b]:pb-3 group-has-[>input]/input-group:pt-2.5",
        "block-end":
          "order-last w-full justify-start px-3 pb-3 [.border-t]:pt-3 group-has-[>input]/input-group:pb-2.5",
      },
    },
    defaultVariants: {
      align: "inline-start",
    },
  },
)

export type InputGroupVariants = VariantProps<typeof inputGroupAddonVariants>

export const inputGroupButtonVariants = cva(
  "text-sm shadow-none flex gap-2 items-center",
  {
    variants: {
      size: {
        "xs": "h-6 gap-1 px-2 rounded-[calc(var(--radius)-5px)] [&>svg:not([class*='size-'])]:size-3.5 has-[>svg]:px-2",
        "sm": "h-8 px-2.5 gap-1.5 rounded-md has-[>svg]:px-2.5",
        "icon-xs": "size-6 rounded-[calc(var(--radius)-5px)] p-0 has-[>svg]:p-0",
        "icon-sm": "size-8 p-0 has-[>svg]:p-0",
      },
    },
    defaultVariants: {
      size: "xs",
    },
  },
)

export type InputGroupButtonVariants = VariantProps<typeof inputGroupButtonVariants>
```

Sources:
- `/tmp/shadcn-vue-repo/apps/v4/registry/new-york-v4/ui/input-group/`
