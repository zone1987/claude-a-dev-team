---
name: shadcn-vue-kbd
description: >
  shadcn-vue Kbd component (Vue-Port von shadcn/ui, native <kbd>, Tailwind v4).
  Triggers: "shadcn-vue kbd", "kbd vue", "keyboard shortcut vue", "tastaturkuerzel vue",
  "kbd component shadcn", "kbd group vue", "keyboard key vue", "shortcut display vue"
---

# shadcn-vue Kbd Component

## Triggers
shadcn-vue kbd, kbd vue, keyboard shortcut vue, tastaturkuerzel vue, kbd component shadcn,
kbd group vue, keyboard key vue, shortcut display vue

## Overview

The `Kbd` component renders keyboard keys as styled `<kbd>` HTML elements. `KbdGroup` wraps multiple `Kbd` components into a compound shortcut. No reka-ui primitive is used — these are pure presentational wrappers using Tailwind v4.

## Sub-components

| Component | Element | Description |
|---|---|---|
| `Kbd` | `<kbd>` | Single keyboard key |
| `KbdGroup` | `<kbd>` | Groups multiple keys for compound shortcuts |

## Styling Notes
- `Kbd` applies `bg-muted`, `text-muted-foreground`, rounded, inline-flex with `h-5`, `min-w-5`
- Inside `[data-slot=tooltip-content]` the background adapts for dark tooltip contrast
- SVG children inside `Kbd` are auto-sized to `size-3`

## References
- Source: `references/source.md`
- API: `references/api.md`
- Examples: `references/examples.md`
- Installation: `references/installation.md`
