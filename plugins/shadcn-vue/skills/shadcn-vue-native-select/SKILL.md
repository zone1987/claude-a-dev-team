---
name: shadcn-vue-native-select
description: >
  shadcn-vue NativeSelect component (Vue-Port von shadcn/ui, nativer <select>, Tailwind v4).
  Triggers: "shadcn-vue native-select", "native select vue", "nativselect vue",
  "native-select component shadcn", "select html vue", "optgroup vue", "native dropdown vue",
  "select ohne reka vue", "accessible native select vue"
---

# shadcn-vue NativeSelect Component

## Triggers
shadcn-vue native-select, native select vue, nativselect vue, native-select component shadcn,
select html vue, optgroup vue, native dropdown vue, select ohne reka vue, accessible native select vue

## Overview

The `NativeSelect` component wraps a native HTML `<select>` element with consistent shadcn-vue styling, a custom chevron icon, and `v-model` support. It does not use reka-ui — it relies purely on the browser's native `<select>` behavior. Use this when you need maximum compatibility or accessibility without a custom dropdown.

## Sub-components

| Component | Element | Description |
|---|---|---|
| `NativeSelect` | `<select>` wrapper div | Root select with chevron icon |
| `NativeSelectOption` | `<option>` | Individual option |
| `NativeSelectOptGroup` | `<optgroup>` | Grouped options with label |

## NativeSelect Props

| Prop | Type | Description |
|---|---|---|
| `modelValue` | `AcceptableValue \| AcceptableValue[]` | v-model binding |
| `class` | `HTMLAttributes["class"]` | Additional classes on `<select>` |
| All native `<select>` attrs | — | Forwarded via `$attrs` |

## v-model
Uses `useVModel` from `@vueuse/core` with `passive: true` and `defaultValue: ""`.

## Disabled State
Parent wrapper applies `has-[select:disabled]:opacity-50` automatically.

## References
- Source: `references/source.md`
- API: `references/api.md`
- Examples: `references/examples.md`
- Installation: `references/installation.md`
