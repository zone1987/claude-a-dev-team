---
name: shadcn-vue-button-group
description: >
  shadcn-vue ButtonGroup component (Vue-Port von shadcn/ui, Tailwind v4, SFC .vue).
  Triggers: "shadcn-vue button-group", "button group vue", "buttongroup vue",
  "grouped buttons vue", "toolbar buttons vue", "split button vue",
  "button-group shadcn", "vue button cluster"
---

# shadcn-vue ButtonGroup Component

## Triggers
shadcn-vue button-group, button group vue, buttongroup vue, grouped buttons vue, toolbar buttons vue, split button vue, button-group shadcn, vue button cluster

## Overview

`ButtonGroup` is a layout wrapper that visually merges adjacent buttons (and other form controls) into a single cohesive unit by removing inner border-radii and collapsing duplicate borders. It is built entirely from CSS via `class-variance-authority` — no JavaScript state is involved.

The component suite ships three sub-components:

| Component | Purpose |
|---|---|
| `ButtonGroup` | Outer wrapper — applies the shared CVA variants and exposes `role="group"` |
| `ButtonGroupSeparator` | Visual divider between items (recommended for non-outline button variants where the missing border is not visible) |
| `ButtonGroupText` | Inline label or icon text inside a group (styled as a muted pill with a border) |

## Sub-components

### ButtonGroup
Renders a `<div role="group">` with `data-slot="button-group"` and `data-orientation`. Accepts any children — `<Button>`, `<Input>`, `<Select>`, nested `<ButtonGroup>`, etc.

### ButtonGroupSeparator
Thin divider line built on top of the shadcn-vue `Separator` (reka-ui). Defaults to `orientation="vertical"`. Use when buttons carry a solid background so the implicit border merging alone is not enough to distinguish items.

### ButtonGroupText
A styled `<div>` (or any element via `as`/`asChild`) that displays a short label or icon inside a group. Uses the `bg-muted` background and a small border to match the group's form-control aesthetic.

## Orientation

| Value | Layout | Border adjustment |
|---|---|---|
| `horizontal` (default) | `flex-row` | Removes left radius + left border from non-first items; removes right radius from non-last items |
| `vertical` | `flex-col` | Removes top radius + top border from non-first items; removes bottom radius from non-last items |

## ButtonGroup vs ToggleGroup

Use `ButtonGroup` for **action buttons** (submit, copy, navigate) that need a compact grouped visual — there is no selected/active state involved.  
Use `ToggleGroup` (reka-ui) when you need mutually exclusive or multi-select **toggle state** — e.g. text alignment, view switchers.

## Accessibility

- `ButtonGroup` renders `role="group"` automatically.
- Always add an `aria-label` to `ButtonGroup` when the group purpose is not clear from surrounding context.
- Each individual `<Button>` inside the group should still carry its own accessible label (`aria-label` or visible text).

## Nesting

Nested `ButtonGroup` elements are supported. The outer wrapper applies a `gap-2` between any inner `[data-slot=button-group]` children so nested groups visually separate slightly from each other.

## References

- [Installation](references/installation.md)
- [Source code](references/source.md)
- [API / Props](references/api.md)
- [Examples](references/examples.md)
