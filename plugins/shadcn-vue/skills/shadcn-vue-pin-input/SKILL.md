---
name: shadcn-vue-pin-input
description: >
  shadcn-vue PinInput component (Vue-Port von shadcn/ui, reka-ui PinInputRoot, Tailwind v4).
  Triggers: "shadcn-vue pin-input", "pin input vue", "otp input vue", "pin eingabe vue",
  "pin input component shadcn", "reka-ui pin input vue", "otp field vue", "verification code vue",
  "masked pin input vue", "pin input separator vue"
---

# shadcn-vue PinInput Component

## Triggers
shadcn-vue pin-input, pin input vue, otp input vue, pin eingabe vue, pin input component shadcn,
reka-ui pin input vue, otp field vue, verification code vue, masked pin input vue, pin input separator vue

## Overview

The `PinInput` component provides a styled one-time password / PIN entry field. It is built on reka-ui's `PinInputRoot` which handles focus management, value tracking across slots, and OTP auto-fill. This is a Vue-specific component.

## Sub-components

| Component | reka-ui Base | Description |
|---|---|---|
| `PinInput` | `PinInputRoot` | Root, manages all slot values |
| `PinInputGroup` | `Primitive` | Visual grouping of adjacent slots |
| `PinInputSlot` | `PinInputInput` | Individual character input cell |
| `PinInputSeparator` | `Primitive` | Visual separator between groups |

## PinInput Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `modelValue` | `string[]` | — | Controlled value array |
| `otp` | `boolean` | `true` | Enable OTP autocomplete |
| `mask` | `boolean` | `false` | Mask input as password |
| `type` | `"text" \| "number"` | `"text"` | Input type (generic) |
| `disabled` | `boolean` | — | Disable all slots |
| `placeholder` | `string` | — | Placeholder per slot |

## PinInputSlot Props

| Prop | Type | Description |
|---|---|---|
| `index` | `number` | Required: 0-based position of this slot |
| `class` | `HTMLAttributes["class"]` | Additional classes |

## Emits

| Event | Type | Description |
|---|---|---|
| `update:modelValue` | `string[]` | Fired on any slot change |
| `complete` | `string[]` | Fired when all slots are filled |

## reka-ui Reference
https://reka-ui.com/docs/components/pin-input

## References
- Source: `references/source.md`
- API: `references/api.md`
- Examples: `references/examples.md`
- Installation: `references/installation.md`
