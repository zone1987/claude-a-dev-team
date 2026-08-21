# shadcn-vue RadioGroup

The RadioGroup component provides a set of mutually exclusive options where
only one item can be selected at a time. It is built on top of
`RadioGroupRoot`, `RadioGroupItem`, and `RadioGroupIndicator` from reka-ui
and styled with Tailwind v4.

## Contents

- [Sub-components](#sub-components)
- [Props](#props)
- [Emits](#emits)
- [Slots](#slots)
- [Usage patterns](#usage-patterns)
- [Styling](#styling)
- [Accessibility](#accessibility)
- [Files](#files)
- [References](#references)

## Sub-components

### RadioGroup (RadioGroupRoot wrapper)

The container that manages selection state and keyboard navigation. Renders
as a `<div role="radiogroup">`. Forwards all `RadioGroupRootProps` from
reka-ui and exposes an `update:modelValue` emit for two-way binding.

### RadioGroupItem (RadioGroupItem wrapper)

An individual selectable option. Renders as a `<button role="radio">`.
Inside it, `RadioGroupIndicator` renders only when the item is checked,
displaying the default `CircleIcon` (from `@lucide/vue`) or a custom icon
provided via the default slot.

## Props

### RadioGroup

| Prop             | Type                        | Default  | Description                                |
|------------------|-----------------------------|----------|--------------------------------------------|
| `modelValue`     | `string`                    | —        | The controlled selected value.             |
| `defaultValue`   | `string`                    | —        | The uncontrolled default selected value.   |
| `disabled`       | `boolean`                   | `false`  | Disables all items in the group.           |
| `orientation`    | `"horizontal" \| "vertical"` | `"vertical"` | Keyboard navigation direction.        |
| `dir`            | `"ltr" \| "rtl"`            | `"ltr"`  | Reading direction.                         |
| `loop`           | `boolean`                   | `true`   | Whether keyboard navigation wraps.         |
| `required`       | `boolean`                   | `false`  | Marks the group as required for forms.     |
| `class`          | `string`                    | —        | Additional CSS classes on the root.        |

### RadioGroupItem

| Prop       | Type      | Default | Description                                      |
|------------|-----------|---------|--------------------------------------------------|
| `value`    | `string`  | —       | The value this item represents. **Required.**    |
| `disabled` | `boolean` | `false` | Disables this individual item.                   |
| `class`    | `string`  | —       | Additional CSS classes on the item button.       |

## Emits

### RadioGroup

| Event              | Payload  | Description                          |
|--------------------|----------|--------------------------------------|
| `update:modelValue`| `string` | Fired when the selected value changes.|

## Slots

### RadioGroup default slot

Receives `RadioGroupRootSlotProps` from reka-ui. Use it to render
`RadioGroupItem` instances (and accompanying labels).

### RadioGroupItem default slot

Replaces the default `CircleIcon` indicator with a custom icon or element.
Rendered only when the item is in the checked state.

## Usage patterns

### Uncontrolled (default value)

```vue
<template>
  <RadioGroup default-value="comfortable">
    <Field orientation="horizontal">
      <RadioGroupItem id="r1" value="default" />
      <FieldLabel html-for="r1" class="font-normal">Default</FieldLabel>
    </Field>
    <Field orientation="horizontal">
      <RadioGroupItem id="r2" value="comfortable" />
      <FieldLabel html-for="r2" class="font-normal">Comfortable</FieldLabel>
    </Field>
  </RadioGroup>
</template>
```

### Controlled with v-model

```vue
<script setup lang="ts">
import { ref } from "vue"
const plan = ref("plus")
</script>

<template>
  <RadioGroup v-model="plan">
    <Field orientation="horizontal">
      <RadioGroupItem id="plus" value="plus" />
      <FieldLabel html-for="plus">Plus</FieldLabel>
    </Field>
    <Field orientation="horizontal">
      <RadioGroupItem id="pro" value="pro" />
      <FieldLabel html-for="pro">Pro</FieldLabel>
    </Field>
  </RadioGroup>
</template>
```

### Disabled group

Pass `:disabled="true"` on the root to disable all items simultaneously.
Individual items can also be disabled via their own `disabled` prop.

### Custom indicator icon

```vue
<RadioGroupItem value="star">
  <StarIcon class="size-2 fill-primary" />
</RadioGroupItem>
```

## Styling

- `RadioGroupRoot` carries `data-slot="radio-group"`.
- `RadioGroupItem` carries `data-slot="radio-group-item"`.
- `RadioGroupIndicator` carries `data-slot="radio-group-indicator"`.

Invalid state is indicated via `aria-invalid` on `RadioGroupItem`, which
triggers the `aria-invalid:border-destructive` and
`aria-invalid:ring-destructive/20` Tailwind variants baked into the component.

## Accessibility

- `role="radiogroup"` on the container.
- `role="radio"` and `aria-checked` on each item (managed by reka-ui).
- Arrow-key navigation between items (direction controlled by `orientation`).
- `required` on the root sets `aria-required`.
- Use `<FieldSet>` + `<FieldLegend>` to provide a group label for screen readers.

## Files

- `src/components/ui/radio-group/RadioGroup.vue` — root component
- `src/components/ui/radio-group/RadioGroupItem.vue` — item component
- `src/components/ui/radio-group/index.ts` — barrel export

## References

- Installation: `RADIO-GROUP-INSTALLATION.md`
- Source code: `RADIO-GROUP-SOURCE.md`
- API reference: `RADIO-GROUP-API.md`
- Usage examples: `RADIO-GROUP-EXAMPLES.md`
- reka-ui docs: https://reka-ui.com/docs/components/radio-group
