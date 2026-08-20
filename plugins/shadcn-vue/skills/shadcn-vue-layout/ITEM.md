# shadcn-vue Item Component

## Triggers
shadcn-vue item, item vue, item list vue, item group vue, item komponente vue, item component shadcn,
item media vue, item actions vue, item content vue, item title vue, item description vue,
item footer vue, item header vue, item separator vue

## Overview

The `Item` component is a flexible, composable list-item primitive built on reka-ui's `Primitive`. It uses `class-variance-authority` (CVA) for `variant` and `size` styling and is designed for building lists, settings rows, file browsers, or any structured content entry.

## Sub-components

| Component | Description |
|---|---|
| `Item` | Root element, polymorphic via `as`/`asChild` |
| `ItemGroup` | Wrapper list container (`role="list"`) |
| `ItemContent` | Main flexible content column |
| `ItemTitle` | Bold title row inside content |
| `ItemDescription` | Secondary muted text description |
| `ItemMedia` | Icon/image slot left of content |
| `ItemActions` | Action buttons slot right of content |
| `ItemHeader` | Full-width header row (top) |
| `ItemFooter` | Full-width footer row (bottom) |
| `ItemSeparator` | Horizontal separator between items |

## Variants

### itemVariants (on `Item`)

| Variant | Values |
|---|---|
| `variant` | `default` (transparent), `outline` (bordered), `muted` (subtle bg) |
| `size` | `default` (p-4 gap-4), `sm` (py-3 px-4 gap-2.5) |

### itemMediaVariants (on `ItemMedia`)

| Variant | Values |
|---|---|
| `variant` | `default` (transparent), `icon` (8x8 bordered muted bg), `image` (10x10 rounded overflow) |

## References
- Source: `ITEM-SOURCE.md`
- API: `ITEM-API.md`
- Examples: `ITEM-EXAMPLES.md`
- Installation: `ITEM-INSTALLATION.md`
