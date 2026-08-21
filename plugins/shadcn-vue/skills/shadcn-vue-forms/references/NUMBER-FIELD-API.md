# NumberField — API Reference

## Contents

- [NumberField (Root)](#numberfield-root)
- [NumberFieldContent](#numberfieldcontent)
- [NumberFieldInput](#numberfieldinput)
- [NumberFieldDecrement](#numberfielddecrement)
- [NumberFieldIncrement](#numberfieldincrement)
- [reka-ui Reference](#reka-ui-reference)

## NumberField (Root)

Based on reka-ui `NumberFieldRoot`. Manages value, min/max, step and disabled state.

### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `modelValue` | `number` | — | Controlled value |
| `defaultValue` | `number` | — | Uncontrolled initial value |
| `min` | `number` | — | Minimum value |
| `max` | `number` | — | Maximum value |
| `step` | `number` | `1` | Step size |
| `disabled` | `boolean` | `false` | Disables the entire field |
| `id` | `string` | — | For `<Label>` association |
| `locale` | `string` | — | Locale for number formatting |
| `formatOptions` | `Intl.NumberFormatOptions` | — | Number formatting |
| `class` | `HTMLAttributes["class"]` | — | Additional CSS classes |

### Emits

| Event | Type | Description |
|---|---|---|
| `update:modelValue` | `number` | Fires on value change |

### Slot Props

```ts
// v-slot="{ modelValue, ... }"
```

---

## NumberFieldContent

Positioning wrapper for input + buttons.

### Props

| Prop | Type | Description |
|---|---|---|
| `class` | `HTMLAttributes["class"]` | Additional CSS classes |

### Behavior
Automatically adjusts the input padding when decrement/increment is present (`has-[[data-slot=increment]]`, `has-[[data-slot=decrement]]`).

---

## NumberFieldInput

Based on reka-ui `NumberFieldInput`. No own `v-model` — state is managed by `NumberFieldRoot`.

### Props

| Prop | Type | Description |
|---|---|---|
| `class` | `HTMLAttributes["class"]` | Additional CSS classes |

---

## NumberFieldDecrement

Minus button (absolutely positioned on the left).

### Props

| Prop | Type | Description |
|---|---|---|
| `class` | `HTMLAttributes["class"]` | Additional CSS classes |
| All `NumberFieldDecrementProps` | — | Forwarded |

### Slots

| Slot | Description |
|---|---|
| default | Custom icon (default: `<Minus>`) |

---

## NumberFieldIncrement

Plus button (absolutely positioned on the right).

### Props

| Prop | Type | Description |
|---|---|---|
| `class` | `HTMLAttributes["class"]` | Additional CSS classes |
| All `NumberFieldIncrementProps` | — | Forwarded |

### Slots

| Slot | Description |
|---|---|
| default | Custom icon (default: `<Plus>`) |

---

## reka-ui Reference
- https://reka-ui.com/docs/components/number-field
