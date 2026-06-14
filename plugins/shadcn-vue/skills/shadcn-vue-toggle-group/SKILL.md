---
name: shadcn-vue-toggle-group
description: >
  shadcn-vue ToggleGroup-Komponente (Vue-Port von shadcn/ui, reka-ui ToggleGroupRoot, CVA, Tailwind v4).
  Triggers: "shadcn-vue toggle group", "toggle group vue", "toggle gruppe vue", "mehrere toggles vue",
  "toggle group single multiple vue", "reka-ui toggle group", "toggle group orientation vue"
---

# shadcn-vue ToggleGroup

## Overview

`ToggleGroup` is a container for related `ToggleGroupItem` elements. It wraps reka-ui's `ToggleGroupRoot` and provides shared `variant`, `size`, and `spacing` context to all child items. Supports `type="single"` (only one item active) and `type="multiple"` (multiple items active), plus `orientation="horizontal"` (default) / `"vertical"`.

## Spacing

The `spacing` prop (number, default `0`) controls the gap between items via a CSS custom property `--gap`. When `spacing=0` the items are fused into a segmented control (connected borders), when `spacing > 0` items are separated.

| Spacing | Visual effect |
|---|---|
| `0` | Fused/connected — first item rounded-l, last rounded-r; outline borders merged |
| `1`–`n` | Tailwind spacing unit gap between items; each item individually rounded |

## Variants / Sizes

Inherits the same CVA variants as `Toggle`:

| Variant | Description |
|---|---|
| `default` | No background; accent fill on active |
| `outline` | Bordered, accent hover |

| Size | Height |
|---|---|
| `sm` | `h-8` |
| `default` | `h-9` |
| `lg` | `h-10` |

## Context injection

`ToggleGroup` provides `variant`, `size`, and `spacing` to all child `ToggleGroupItem` components via Vue's `provide`/`inject`. Item-level props override context.

## References

- [Installation](references/installation.md)
- [Source code](references/source.md)
- [API / Props](references/api.md)
- [Examples](references/examples.md)
