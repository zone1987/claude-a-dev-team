# shadcn-vue Toggle

## Overview

The `Toggle` component is a two-state button (on/off) built on reka-ui's `Toggle` primitive and styled with `class-variance-authority` (CVA). It provides `variant` (default/outline) and `size` (sm/default/lg) props, exposes the pressed state via `data-[state=on]`, and forwards all reka-ui Toggle props/emits.

## Variants

| Variant | Class | Description |
|---|---|---|
| `default` | `bg-transparent` | No background; accent fill on active state |
| `outline` | `border border-input bg-transparent shadow-xs hover:bg-accent hover:text-accent-foreground` | Bordered, accent hover |

## Sizes

| Size | Height | Min-width | Padding |
|---|---|---|---|
| `sm` | `h-8` | `min-w-8` | `px-1.5` |
| `default` | `h-9` | `min-w-9` | `px-2` |
| `lg` | `h-10` | `min-w-10` | `px-2.5` |

## Key Features

- Pressed state via `data-[state=on]` attribute — style active state with `data-[state=on]:bg-accent data-[state=on]:text-accent-foreground`
- SVG auto-sizing: `[&_svg:not([class*='size-'])]:size-4`
- `aria-label` required for icon-only toggles
- Group usage: use inside `ToggleGroup` for related toggles
- `data-slot="toggle"` for CSS targeting

## References

- [Installation](`TOGGLE-INSTALLATION.md`)
- [Source code](`TOGGLE-SOURCE.md`)
- [API / Props](`TOGGLE-API.md`)
- [Examples](`TOGGLE-EXAMPLES.md`)
