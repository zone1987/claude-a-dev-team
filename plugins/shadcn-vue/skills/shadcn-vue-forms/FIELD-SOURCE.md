# Field — Quellcode

Alle Dateien aus `registry/new-york-v4/ui/field/`.

## Contents

- [Field.vue](#fieldvue)
- [FieldContent.vue](#fieldcontentvue)
- [FieldDescription.vue](#fielddescriptionvue)
- [FieldError.vue](#fielderrorvue)
- [FieldGroup.vue](#fieldgroupvue)
- [FieldLabel.vue](#fieldlabelvue)
- [FieldLegend.vue](#fieldlegendvue)
- [FieldSeparator.vue](#fieldseparatorvue)
- [FieldSet.vue](#fieldsetvue)
- [FieldTitle.vue](#fieldtitlevue)
- [index.ts](#indexts)

## Field.vue

```vue
<script setup lang="ts">
import type { HTMLAttributes } from "vue"
import type { FieldVariants } from "."
import { cn } from "@/lib/utils"
import { fieldVariants } from "."

const props = defineProps<{
  class?: HTMLAttributes["class"]
  orientation?: FieldVariants["orientation"]
}>()
</script>

<template>
  <div
    role="group"
    data-slot="field"
    :data-orientation="orientation"
    :class="cn(
      fieldVariants({ orientation }),
      props.class,
    )"
  >
    <slot />
  </div>
</template>
```

## FieldContent.vue

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
    data-slot="field-content"
    :class="cn(
      'group/field-content flex flex-1 flex-col gap-1.5 leading-snug',
      props.class,
    )"
  >
    <slot />
  </div>
</template>
```

## FieldDescription.vue

```vue
<script setup lang="ts">
import type { HTMLAttributes } from "vue"
import { cn } from "@/lib/utils"

const props = defineProps<{
  class?: HTMLAttributes["class"]
}>()
</script>

<template>
  <p
    data-slot="field-description"
    :class="cn(
      'text-muted-foreground text-sm leading-normal font-normal group-has-[[data-orientation=horizontal]]/field:text-balance',
      'last:mt-0 nth-last-2:-mt-1 [[data-variant=legend]+&]:-mt-1.5',
      '[&>a:hover]:text-primary [&>a]:underline [&>a]:underline-offset-4',
      props.class,
    )"
  >
    <slot />
  </p>
</template>
```

## FieldError.vue

```vue
<script setup lang="ts">
import type { HTMLAttributes } from "vue"
import { computed } from "vue"
import { cn } from "@/lib/utils"

const props = defineProps<{
  class?: HTMLAttributes["class"]
  errors?: Array<string | { message: string | undefined } | undefined>
}>()

const content = computed(() => {
  if (!props.errors || props.errors.length === 0)
    return null

  const uniqueErrors = [
    ...new Map(
      props.errors
        .filter(Boolean)
        .map((error) => {
          const message = typeof error === "string" ? error : error?.message
          return [message, error]
        }),
    ).values(),
  ]

  if (uniqueErrors.length === 1 && uniqueErrors[0]) {
    return typeof uniqueErrors[0] === "string" ? uniqueErrors[0] : uniqueErrors[0].message
  }

  return uniqueErrors.map(error => typeof error === "string" ? error : error?.message)
})
</script>

<template>
  <div
    v-if="$slots.default || content"
    role="alert"
    data-slot="field-error"
    :class="cn('text-destructive text-sm font-normal', props.class)"
  >
    <slot v-if="$slots.default" />

    <template v-else-if="typeof content === 'string'">
      {{ content }}
    </template>

    <ul v-else-if="Array.isArray(content)" class="ml-4 flex list-disc flex-col gap-1">
      <li v-for="(error, index) in content" :key="index">
        {{ error }}
      </li>
    </ul>
  </div>
</template>
```

## FieldGroup.vue

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
    data-slot="field-group"
    :class="cn(
      'group/field-group @container/field-group flex w-full flex-col gap-7 data-[slot=checkbox-group]:gap-3 [&>[data-slot=field-group]]:gap-4',
      props.class,
    )"
  >
    <slot />
  </div>
</template>
```

## FieldLabel.vue

```vue
<script setup lang="ts">
import type { HTMLAttributes } from "vue"
import { cn } from "@/lib/utils"
import { Label } from "@/registry/new-york-v4/ui/label"

const props = defineProps<{
  class?: HTMLAttributes["class"]
}>()
</script>

<template>
  <Label
    data-slot="field-label"
    :class="cn(
      'group/field-label peer/field-label flex w-fit gap-2 leading-snug group-data-[disabled=true]/field:opacity-50',
      'has-[>[data-slot=field]]:w-full has-[>[data-slot=field]]:flex-col has-[>[data-slot=field]]:rounded-md has-[>[data-slot=field]]:border [&>*]:data-[slot=field]:p-4',
      'has-data-[state=checked]:bg-primary/5 has-data-[state=checked]:border-primary dark:has-data-[state=checked]:bg-primary/10',
      props.class,
    )"
  >
    <slot />
  </Label>
</template>
```

## FieldLegend.vue

```vue
<script setup lang="ts">
import type { HTMLAttributes } from "vue"
import { cn } from "@/lib/utils"

const props = defineProps<{
  class?: HTMLAttributes["class"]
  variant?: "legend" | "label"
}>()
</script>

<template>
  <legend
    data-slot="field-legend"
    :data-variant="variant"
    :class="cn(
      'mb-3 font-medium',
      'data-[variant=legend]:text-base',
      'data-[variant=label]:text-sm',
      props.class,
    )"
  >
    <slot />
  </legend>
</template>
```

## FieldSeparator.vue

```vue
<script setup lang="ts">
import type { HTMLAttributes } from "vue"
import { cn } from "@/lib/utils"
import { Separator } from "@/registry/new-york-v4/ui/separator"

const props = defineProps<{
  class?: HTMLAttributes["class"]
}>()
</script>

<template>
  <div
    data-slot="field-separator"
    :data-content="!!$slots.default"
    :class="cn(
      'relative -my-2 h-5 text-sm group-data-[variant=outline]/field-group:-mb-2',
      props.class,
    )"
  >
    <Separator class="absolute inset-0 top-1/2" />
    <span
      v-if="$slots.default"
      class="bg-background text-muted-foreground relative mx-auto block w-fit px-2"
      data-slot="field-separator-content"
    >
      <slot />
    </span>
  </div>
</template>
```

## FieldSet.vue

```vue
<script setup lang="ts">
import type { HTMLAttributes } from "vue"
import { cn } from "@/lib/utils"

const props = defineProps<{
  class?: HTMLAttributes["class"]
}>()
</script>

<template>
  <fieldset
    data-slot="field-set"
    :class="cn(
      'flex flex-col gap-6',
      'has-[>[data-slot=checkbox-group]]:gap-3 has-[>[data-slot=radio-group]]:gap-3',
      props.class,
    )"
  >
    <slot />
  </fieldset>
</template>
```

## FieldTitle.vue

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
    data-slot="field-label"
    :class="cn(
      'flex w-fit items-center gap-2 text-sm leading-snug font-medium group-data-[disabled=true]/field:opacity-50',
      props.class,
    )"
  >
    <slot />
  </div>
</template>
```

## index.ts

```ts
import type { VariantProps } from "class-variance-authority"
import { cva } from "class-variance-authority"

export const fieldVariants = cva(
  "group/field flex w-full gap-3 data-[invalid=true]:text-destructive",
  {
    variants: {
      orientation: {
        vertical: ["flex-col [&>*]:w-full [&>.sr-only]:w-auto"],
        horizontal: [
          "flex-row items-center",
          "[&>[data-slot=field-label]]:flex-auto",
          "has-[>[data-slot=field-content]]:items-start has-[>[data-slot=field-content]]:[&>[role=checkbox],[role=radio]]:mt-px",
        ],
        responsive: [
          "flex-col [&>*]:w-full [&>.sr-only]:w-auto @md/field-group:flex-row @md/field-group:items-center @md/field-group:[&>*]:w-auto",
          "@md/field-group:[&>[data-slot=field-label]]:flex-auto",
          "@md/field-group:has-[>[data-slot=field-content]]:items-start @md/field-group:has-[>[data-slot=field-content]]:[&>[role=checkbox],[role=radio]]:mt-px",
        ],
      },
    },
    defaultVariants: {
      orientation: "vertical",
    },
  },
)

export type FieldVariants = VariantProps<typeof fieldVariants>

export { default as Field } from "./Field.vue"
export { default as FieldContent } from "./FieldContent.vue"
export { default as FieldDescription } from "./FieldDescription.vue"
export { default as FieldError } from "./FieldError.vue"
export { default as FieldGroup } from "./FieldGroup.vue"
export { default as FieldLabel } from "./FieldLabel.vue"
export { default as FieldLegend } from "./FieldLegend.vue"
export { default as FieldSeparator } from "./FieldSeparator.vue"
export { default as FieldSet } from "./FieldSet.vue"
export { default as FieldTitle } from "./FieldTitle.vue"
```

Quellen:
- `/tmp/shadcn-vue-repo/apps/v4/registry/new-york-v4/ui/field/`
