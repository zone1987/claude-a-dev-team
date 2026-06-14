---
name: shadcn-toggle-group
description: >
  shadcn/ui ToggleGroup component — set of toggle buttons, single multiple selection,
  ToggleGroup, ToggleGroupItem, spacing, outline variant, vertical horizontal orientation,
  Schaltergruppe, shadcn toggle group, radix toggle group, button group toggle
---

# shadcn/ui ToggleGroup

A set of two-state buttons that can be toggled on or off. Supports `single` and `multiple`
selection modes. Built on Radix UI ToggleGroup primitive with Context-based variant/size propagation.

## Quick Reference

- **Install**: `npx shadcn@latest add toggle-group`
- **Radix deps**: `radix-ui`
- **Exports**: `ToggleGroup`, `ToggleGroupItem`
- **Variants**: `default` | `outline`
- **Sizes**: `default` | `sm` | `lg`
- **Spacing**: `spacing` prop (0 = connected, 2 = default gap)
- **Breaking change 2026-05-17**: Default spacing changed from `0` to `2`

## Composition

```text
ToggleGroup
├── ToggleGroupItem
└── ToggleGroupItem
```

## Reference files

- [installation.md](references/installation.md) — CLI & manual setup
- [source.md](references/source.md) — Complete component source (new-york-v4 + radix base)
- [api.md](references/api.md) — Props tables
- [examples.md](references/examples.md) — All examples
- [base-vs-radix.md](references/base-vs-radix.md) — Differences between variants
