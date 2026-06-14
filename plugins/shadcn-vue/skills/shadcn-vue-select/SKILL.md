---
name: shadcn-vue-select
description: >
  shadcn-vue Select component (reka-ui SelectRoot, Tailwind v4 Vue SFC).
  Triggers: "shadcn-vue select", "select component vue", "dropdown vue",
  "auswahlfeld vue", "select reka-ui", "select dropdown vue shadcn"
---

# shadcn-vue Select

A fully accessible dropdown select built on reka-ui's Select primitives, composed from 11 sub-components.

## References

- [installation.md](references/installation.md) — CLI and manual install
- [source.md](references/source.md) — Full source for all 11 components + index.ts
- [api.md](references/api.md) — Props, emits and reka-ui API links for all sub-components
- [examples.md](references/examples.md) — Basic, grouped, sizes, with field, disabled examples

## Key Facts

- 11 sub-components: Select, SelectContent, SelectGroup, SelectItem, SelectItemText, SelectLabel, SelectScrollDownButton, SelectScrollUpButton, SelectSeparator, SelectTrigger, SelectValue
- Root `Select` forwards `modelValue`/`update:modelValue` for v-model usage
- `SelectTrigger` supports `size="sm"` and `size="default"` (default)
- `SelectContent` defaults to `position="popper"` with CSS variable-driven sizing
- `SelectItem` exposes a named slot `indicator-icon` to replace the default Check icon
- Built on `reka-ui`; uses `reactiveOmit` + `useForwardPropsEmits` for clean prop delegation
- Tailwind v4 utility classes; animations via data-state attributes
