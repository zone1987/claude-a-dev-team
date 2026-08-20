# API Reference

## Textarea Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `modelValue` | `string \| number` | — | Controlled value (v-model) |
| `defaultValue` | `string \| number` | — | Uncontrolled initial value |
| `placeholder` | `string` | — | Placeholder text (native attr) |
| `disabled` | `boolean` | `false` | Disables the textarea |
| `rows` | `number` | — | Initial visible row count |
| `maxLength` | `number` | — | Maximum character count |
| `readonly` | `boolean` | `false` | Read-only mode |
| `required` | `boolean` | `false` | Form validation required |
| `name` | `string` | — | Form field name |
| `aria-invalid` | `boolean` | — | Triggers destructive ring styling |
| `class` | `string` | — | Additional Tailwind CSS classes |

## Emits

| Event | Payload | Description |
|-------|---------|-------------|
| `update:modelValue` | `string \| number` | Emitted on input changes |

## CSS Notes

- `field-sizing-content`: Auto-grows the textarea to fit its content
  (modern browser feature; adds to `min-h-16` baseline).
- `aria-invalid="true"`: Applies `ring-destructive` border highlight for
  form validation feedback.

## Compose with Field

For accessible labels and descriptions, use the `Field` component family:

```vue
<script setup lang="ts">
import { Field, FieldDescription, FieldLabel } from "@/components/ui/field"
import { Textarea } from "@/components/ui/textarea"
</script>

<template>
  <Field>
    <FieldLabel html-for="message">Message</FieldLabel>
    <Textarea id="message" placeholder="Type here..." :rows="4" />
    <FieldDescription>Press enter to send.</FieldDescription>
  </Field>
</template>
```
