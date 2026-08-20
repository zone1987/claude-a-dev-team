# PinInput — API reference

## PinInput (root)

Based on reka-ui `PinInputRoot`. Generic type `Type extends 'text' | 'number' = 'text'`.

### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `modelValue` | `string[]` | — | Controlled value (one array entry per slot) |
| `defaultValue` | `string[]` | — | Uncontrolled initial value |
| `otp` | `boolean` | `true` | Enable OTP autocomplete |
| `mask` | `boolean` | `false` | Mask the input (password mode) |
| `type` | `"text" \| "number"` | `"text"` | Input type |
| `placeholder` | `string` | — | Placeholder for all slots |
| `disabled` | `boolean` | `false` | Disable all slots |
| `id` | `string` | — | For `<Label>` association |
| `class` | `HTMLAttributes["class"]` | — | Additional CSS classes |

### Emits

| Event | Type | Description |
|---|---|---|
| `update:modelValue` | `string[]` | On change of a slot |
| `complete` | `string[]` | When all slots are filled |

---

## PinInputGroup

Based on reka-ui `Primitive`.

### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `as` | `string \| Component` | `"div"` | HTML element |
| `asChild` | `boolean` | `false` | Render as child element |
| `class` | `HTMLAttributes["class"]` | — | Additional CSS classes |

---

## PinInputSlot

Based on reka-ui `PinInputInput`. Each slot is a standalone input element.

### Props

| Prop | Type | Description |
|---|---|---|
| `index` | `number` | **Required**: 0-based position within the PIN |
| `class` | `HTMLAttributes["class"]` | Additional CSS classes |
| All `PinInputInputProps` | — | Forwarded |

### Styling details
- `first:rounded-l-md first:border-l` — only the first slot has a left border and rounding
- `last:rounded-r-md` — only the last slot has right rounding
- `focus:z-10` — the active slot sits above its neighbors

---

## PinInputSeparator

Based on reka-ui `Primitive`. Default icon: `<Minus>`.

### Props

| Prop | Type | Description |
|---|---|---|
| `as` | `string \| Component` | HTML element (default: `"div"`) |
| `asChild` | `boolean` | Child element mode |

### Slots

| Slot | Description |
|---|---|
| default | Custom separator (default: `<Minus>`) |

---

## reka-ui reference
- https://reka-ui.com/docs/components/pin-input
