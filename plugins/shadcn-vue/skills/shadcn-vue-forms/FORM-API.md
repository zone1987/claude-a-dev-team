# Form — API

vee-validate API: https://vee-validate.logaretm.com/v4/api/
Zod API: https://zod.dev

## Anatomy

```vue
<template>
  <Form>
    <FormField v-slot="{ componentField }" name="fieldName">
      <FormItem>
        <FormLabel />
        <FormControl>
          <!-- Input component or native input -->
        </FormControl>
        <FormDescription />
        <FormMessage />
      </FormItem>
    </FormField>
  </Form>
</template>
```

## Sub-Components

| Component | Origin | Description |
|---|---|---|
| `Form` | vee-validate (re-export) | Form root with validation schema |
| `FormField` | vee-validate `Field` (re-export) | Scoped slot for field context |
| `FormFieldArray` | vee-validate `FieldArray` (re-export) | For arrays of fields |
| `FormItem` | shadcn-vue | Container, provides a unique ID via injection |
| `FormLabel` | shadcn-vue | Label, links itself automatically to the FormItem ID |
| `FormControl` | shadcn-vue | Slot wrapper, sets ARIA attributes automatically |
| `FormDescription` | shadcn-vue | Help text (aria-describedby) |
| `FormMessage` | shadcn-vue | Error message (vee-validate ErrorMessage) |

## FormField — Scoped Slot Props

| Prop | Description |
|---|---|
| `componentField` | v-bind object for shadcn components (modelValue + onChange) |
| `field` | Object for native inputs (value + onInput + onBlur) |
| `value` | Current field value |
| `handleChange` | Change handler function |
| `meta` | Field state (valid, dirty, touched) |
| `errors` | Error list |

## useFormField — Composable

Returns IDs and field state for your own components:

```ts
const {
  id,              // single ID
  name,            // field name
  formItemId,      // `${id}-form-item`
  formDescriptionId, // `${id}-form-item-description`
  formMessageId,   // `${id}-form-item-message`
  error,           // errorMessage from vee-validate
  valid,           // computed boolean
  isDirty,         // computed boolean
  isTouched,       // computed boolean
} = useFormField()
```

Must be used inside `<FormField>` (vee-validate `FieldContextKey`) and `<FormItem>` (FORM_ITEM_INJECTION_KEY).

## FormControl

Uses the reka-ui `<Slot>` to apply ARIA attributes to the first child element:
- `id`: set automatically
- `aria-describedby`: FormDescription ID (+ FormMessage ID if an error is present)
- `aria-invalid`: true if an error is present

## Checkbox Special Case

For checkbox/switch/radio: set `type="checkbox"` on FormField and bind the value via `value` + `handleChange`:

```vue
<FormField v-slot="{ value, handleChange }" type="checkbox" name="accepts">
  <FormItem>
    <FormControl>
      <Checkbox :checked="value" @update:checked="handleChange" />
    </FormControl>
    <FormMessage />
  </FormItem>
</FormField>
```
