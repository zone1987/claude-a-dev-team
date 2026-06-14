# Examples

## Basic

Plain textarea with placeholder.

```vue
<!-- TextareaBasic.vue -->
<script setup lang="ts">
import { Textarea } from "@/components/ui/textarea"
</script>

<template>
  <Textarea placeholder="Type your message here." />
</template>
```

## Invalid State

Textarea with `aria-invalid` for form error display.

```vue
<!-- TextareaInvalid.vue -->
<script setup lang="ts">
import { Textarea } from "@/components/ui/textarea"
</script>

<template>
  <Textarea placeholder="Type your message here." :aria-invalid="true" />
</template>
```

## With Label

Textarea inside a `Field` with `FieldLabel`.

```vue
<!-- TextareaWithLabel.vue -->
<script setup lang="ts">
import { Field, FieldLabel } from "@/components/ui/field"
import { Textarea } from "@/components/ui/textarea"
</script>

<template>
  <Field>
    <FieldLabel html-for="textarea-demo-message">
      Message
    </FieldLabel>
    <Textarea
      id="textarea-demo-message"
      placeholder="Type your message here."
      :rows="6"
    />
  </Field>
</template>
```

## With Description

Textarea with label and helper description text.

```vue
<!-- TextareaWithDescription.vue -->
<script setup lang="ts">
import { Field, FieldDescription, FieldLabel } from "@/components/ui/field"
import { Textarea } from "@/components/ui/textarea"
</script>

<template>
  <Field>
    <FieldLabel html-for="textarea-demo-message-2">
      Message
    </FieldLabel>
    <Textarea
      id="textarea-demo-message-2"
      placeholder="Type your message here."
      :rows="6"
    />
    <FieldDescription>
      Type your message and press enter to send.
    </FieldDescription>
  </Field>
</template>
```

## Disabled

Textarea in disabled state.

```vue
<!-- TextareaDisabled.vue -->
<script setup lang="ts">
import { Field, FieldLabel } from "@/components/ui/field"
import { Textarea } from "@/components/ui/textarea"
</script>

<template>
  <Field>
    <FieldLabel html-for="textarea-demo-disabled">
      Message
    </FieldLabel>
    <Textarea
      id="textarea-demo-disabled"
      placeholder="Type your message here."
      :disabled="true"
    />
  </Field>
</template>
```

Sources:
- `registry/bases/reka/examples/textarea/TextareaBasic.vue`
- `registry/bases/reka/examples/textarea/TextareaInvalid.vue`
- `registry/bases/reka/examples/textarea/TextareaWithLabel.vue`
- `registry/bases/reka/examples/textarea/TextareaWithDescription.vue`
- `registry/bases/reka/examples/textarea/TextareaDisabled.vue`
