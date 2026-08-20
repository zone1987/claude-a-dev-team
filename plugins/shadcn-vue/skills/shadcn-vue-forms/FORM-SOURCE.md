# Form — Quellcode

Alle Dateien aus `registry/new-york-v4/ui/form/`.

## Contents

- [FormControl.vue](#formcontrolvue)
- [FormDescription.vue](#formdescriptionvue)
- [FormItem.vue](#formitemvue)
- [FormLabel.vue](#formlabelvue)
- [FormMessage.vue](#formmessagevue)
- [injectionKeys.ts](#injectionkeysts)
- [useFormField.ts](#useformfieldts)
- [index.ts](#indexts)

## FormControl.vue

```vue
<script lang="ts" setup>
import { Slot } from "reka-ui"
import { useFormField } from "./useFormField"

const { error, formItemId, formDescriptionId, formMessageId } = useFormField()
</script>

<template>
  <Slot
    :id="formItemId"
    data-slot="form-control"
    :aria-describedby="!error ? `${formDescriptionId}` : `${formDescriptionId} ${formMessageId}`"
    :aria-invalid="!!error"
  >
    <slot />
  </Slot>
</template>
```

## FormDescription.vue

```vue
<script lang="ts" setup>
import type { HTMLAttributes } from "vue"
import { cn } from "@/lib/utils"
import { useFormField } from "./useFormField"

const props = defineProps<{
  class?: HTMLAttributes["class"]
}>()

const { formDescriptionId } = useFormField()
</script>

<template>
  <p
    :id="formDescriptionId"
    data-slot="form-description"
    :class="cn('text-muted-foreground text-sm', props.class)"
  >
    <slot />
  </p>
</template>
```

## FormItem.vue

```vue
<script lang="ts" setup>
import type { HTMLAttributes } from "vue"
import { useId } from "reka-ui"
import { provide } from "vue"
import { cn } from "@/lib/utils"
import { FORM_ITEM_INJECTION_KEY } from "./injectionKeys"

const props = defineProps<{
  class?: HTMLAttributes["class"]
}>()

const id = useId()
provide(FORM_ITEM_INJECTION_KEY, id)
</script>

<template>
  <div
    data-slot="form-item"
    :class="cn('grid gap-2', props.class)"
  >
    <slot />
  </div>
</template>
```

## FormLabel.vue

```vue
<script lang="ts" setup>
import type { LabelProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import { cn } from "@/lib/utils"
import { Label } from "@/registry/new-york-v4/ui/label"
import { useFormField } from "./useFormField"

const props = defineProps<LabelProps & { class?: HTMLAttributes["class"] }>()

const { error, formItemId } = useFormField()
</script>

<template>
  <Label
    data-slot="form-label"
    :data-error="!!error"
    :class="cn(
      'data-[error=true]:text-destructive',
      props.class,
    )"
    :for="formItemId"
  >
    <slot />
  </Label>
</template>
```

## FormMessage.vue

```vue
<script lang="ts" setup>
import type { HTMLAttributes } from "vue"
import { ErrorMessage } from "vee-validate"
import { toValue } from "vue"
import { cn } from "@/lib/utils"
import { useFormField } from "./useFormField"

const props = defineProps<{
  class?: HTMLAttributes["class"]
}>()

const { name, formMessageId } = useFormField()
</script>

<template>
  <ErrorMessage
    :id="formMessageId"
    data-slot="form-message"
    as="p"
    :name="toValue(name)"
    :class="cn('text-destructive text-sm', props.class)"
  />
</template>
```

## injectionKeys.ts

```ts
import type { InjectionKey } from "vue"

export const FORM_ITEM_INJECTION_KEY
  = Symbol() as InjectionKey<string>
```

## useFormField.ts

```ts
import { FieldContextKey } from "vee-validate"
import { computed, inject } from "vue"
import { FORM_ITEM_INJECTION_KEY } from "./injectionKeys"

export function useFormField() {
  const fieldContext = inject(FieldContextKey)
  const fieldItemContext = inject(FORM_ITEM_INJECTION_KEY)

  if (!fieldContext)
    throw new Error("useFormField should be used within <FormField>")

  const { name, errorMessage: error, meta } = fieldContext
  const id = fieldItemContext

  const fieldState = {
    valid: computed(() => meta.valid),
    isDirty: computed(() => meta.dirty),
    isTouched: computed(() => meta.touched),
    error,
  }

  return {
    id,
    name,
    formItemId: `${id}-form-item`,
    formDescriptionId: `${id}-form-item-description`,
    formMessageId: `${id}-form-item-message`,
    ...fieldState,
  }
}
```

## index.ts

```ts
export { default as FormControl } from "./FormControl.vue"
export { default as FormDescription } from "./FormDescription.vue"
export { default as FormItem } from "./FormItem.vue"
export { default as FormLabel } from "./FormLabel.vue"
export { default as FormMessage } from "./FormMessage.vue"
export { FORM_ITEM_INJECTION_KEY } from "./injectionKeys"
export { Form, Field as FormField, FieldArray as FormFieldArray } from "vee-validate"
```

Quellen:
- `/tmp/shadcn-vue-repo/apps/v4/registry/new-york-v4/ui/form/`
