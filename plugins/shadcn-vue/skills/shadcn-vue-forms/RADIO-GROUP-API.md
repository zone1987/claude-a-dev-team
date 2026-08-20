# API Reference

## RadioGroup

A thin wrapper around `RadioGroupRoot` from reka-ui. Manages selection state
and provides keyboard navigation across its child `RadioGroupItem` elements.

### Props

Extends all `RadioGroupRootProps` from reka-ui plus the following:

| Prop           | Type                          | Default      | Description                                              |
|----------------|-------------------------------|--------------|----------------------------------------------------------|
| `modelValue`   | `string`                      | —            | The controlled selected value (use with `v-model`).      |
| `defaultValue` | `string`                      | —            | The uncontrolled initial selected value.                 |
| `disabled`     | `boolean`                     | `false`      | Disables all items in the group.                         |
| `orientation`  | `"horizontal" \| "vertical"`  | `"vertical"` | Controls arrow-key navigation direction.                 |
| `dir`          | `"ltr" \| "rtl"`              | `"ltr"`      | Reading direction for the group.                         |
| `loop`         | `boolean`                     | `true`       | Whether keyboard navigation wraps from last to first.    |
| `required`     | `boolean`                     | `false`      | Marks the group as required (`aria-required`).           |
| `class`        | `string`                      | —            | CSS classes merged onto the root via `cn()`.             |

### Emits

| Event               | Payload  | Description                               |
|---------------------|----------|-------------------------------------------|
| `update:modelValue` | `string` | Fired when the user changes the selection.|

### Slot

`default` — receives `RadioGroupRootSlotProps` from reka-ui. Place
`RadioGroupItem` components here.

### Data slot

| Attribute              | Element       | Purpose                   |
|------------------------|---------------|---------------------------|
| `data-slot="radio-group"` | Root `<div>` | Target for CSS overrides. |

---

## RadioGroupItem

A single selectable option within a `RadioGroup`. Wraps `RadioGroupItem` and
`RadioGroupIndicator` from reka-ui.

### Props

Extends all `RadioGroupItemProps` from reka-ui plus the following:

| Prop       | Type      | Default | Description                                             |
|------------|-----------|---------|---------------------------------------------------------|
| `value`    | `string`  | —       | The value this option represents. **Required.**         |
| `disabled` | `boolean` | `false` | Disables this specific item only.                       |
| `class`    | `string`  | —       | CSS classes merged onto the item button via `cn()`.     |

### Slot

`default` — replaces the default `CircleIcon` indicator. The slot content is
rendered inside `RadioGroupIndicator`, which is only mounted when the item is
in the checked state.

### Data slots

| Attribute                        | Element         | Purpose                          |
|----------------------------------|-----------------|----------------------------------|
| `data-slot="radio-group-item"`   | `<button>`      | The clickable item.              |
| `data-slot="radio-group-indicator"` | Inner `<span>` | Wraps the checked indicator.  |

### Invalid state

Set `aria-invalid="true"` on `RadioGroupItem` to activate the
`aria-invalid:border-destructive` and `aria-invalid:ring-destructive/20`
Tailwind variants defined in the component class string.

---

## External API reference

Full reka-ui RadioGroup API:
https://reka-ui.com/docs/components/radio-group#api-reference
