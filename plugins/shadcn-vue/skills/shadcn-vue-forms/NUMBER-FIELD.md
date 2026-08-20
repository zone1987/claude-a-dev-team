# shadcn-vue NumberField Component

## Triggers
shadcn-vue number-field, number field vue, zahlenfeld vue, number field component shadcn,
number input vue, increment decrement vue, reka-ui number field vue, stepper input vue, numeric input vue

## Overview

The `NumberField` component provides a styled numeric input with increment/decrement buttons. It is built on reka-ui's `NumberFieldRoot` which handles value clamping, step, min/max, and keyboard navigation natively. This is a Vue-specific component (no direct shadcn/ui React equivalent).

## Sub-components

| Component | reka-ui Base | Description |
|---|---|---|
| `NumberField` | `NumberFieldRoot` | Root, provides slot props |
| `NumberFieldContent` | `<div>` | Wrapper that adjusts input padding for buttons |
| `NumberFieldInput` | `NumberFieldInput` | The text input (centered) |
| `NumberFieldDecrement` | `NumberFieldDecrement` | Minus button (absolute left) |
| `NumberFieldIncrement` | `NumberFieldIncrement` | Plus button (absolute right) |

## NumberField Props (forwarded to `NumberFieldRoot`)

| Prop | Type | Description |
|---|---|---|
| `modelValue` / `defaultValue` | `number` | Controlled / uncontrolled value |
| `min` | `number` | Minimum allowed value |
| `max` | `number` | Maximum allowed value |
| `step` | `number` | Step increment |
| `disabled` | `boolean` | Disables the entire field |
| `id` | `string` | For `<Label>` association |
| `class` | `HTMLAttributes["class"]` | Additional CSS |

## Emits

| Event | Type | Description |
|---|---|---|
| `update:modelValue` | `number` | Fired on value change |

## reka-ui Reference
https://reka-ui.com/docs/components/number-field

## References
- Source: `NUMBER-FIELD-SOURCE.md`
- API: `NUMBER-FIELD-API.md`
- Examples: `NUMBER-FIELD-EXAMPLES.md`
- Installation: `NUMBER-FIELD-INSTALLATION.md`
