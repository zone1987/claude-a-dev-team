# shadcn-vue Select

A fully accessible dropdown select built on reka-ui's Select primitives, composed from 11 sub-components.

## References

- [SELECT-INSTALLATION.md](SELECT-INSTALLATION.md) — CLI and manual install
- [SELECT-SOURCE.md](SELECT-SOURCE.md) — Full source for all 11 components + index.ts
- [SELECT-API.md](SELECT-API.md) — Props, emits and reka-ui API links for all sub-components
- [SELECT-EXAMPLES.md](SELECT-EXAMPLES.md) — Basic, grouped, sizes, with field, disabled examples

## Key Facts

- 11 sub-components: Select, SelectContent, SelectGroup, SelectItem, SelectItemText, SelectLabel, SelectScrollDownButton, SelectScrollUpButton, SelectSeparator, SelectTrigger, SelectValue
- Root `Select` forwards `modelValue`/`update:modelValue` for v-model usage
- `SelectTrigger` supports `size="sm"` and `size="default"` (default)
- `SelectContent` defaults to `position="popper"` with CSS variable-driven sizing
- `SelectItem` exposes a named slot `indicator-icon` to replace the default Check icon
- Built on `reka-ui`; uses `reactiveOmit` + `useForwardPropsEmits` for clean prop delegation
- Tailwind v4 utility classes; animations via data-state attributes
