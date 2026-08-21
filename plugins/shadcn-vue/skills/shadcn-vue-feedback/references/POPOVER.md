# shadcn-vue Popover Component

## Triggers
shadcn-vue popover, popover vue, popover component shadcn, popover reka-ui vue, floating panel vue,
popover trigger vue, popover content vue, popover anchor vue, tooltip panel vue, context popup vue

## Overview

The `Popover` component renders a floating content panel anchored to a trigger element. It is built on reka-ui's `PopoverRoot` and uses `PopoverPortal` to render content in the document body. Supports controlled/uncontrolled open state, all alignment/side options, and optional anchor decoupling.

## Sub-components

| Component | reka-ui Base | Description |
|---|---|---|
| `Popover` | `PopoverRoot` | Root with open state |
| `PopoverTrigger` | `PopoverTrigger` | Element that opens the popover |
| `PopoverContent` | `PopoverContent` + `PopoverPortal` | Floating content panel |
| `PopoverAnchor` | `PopoverAnchor` | Custom anchor (decoupled from trigger) |

## PopoverContent Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `align` | `"start" \| "center" \| "end"` | `"center"` | Horizontal alignment |
| `sideOffset` | `number` | `4` | Gap between trigger and panel (px) |
| `side` | `"top" \| "right" \| "bottom" \| "left"` | `"bottom"` | Preferred side |
| `alignOffset` | `number` | — | Offset along alignment axis |
| `avoidCollisions` | `boolean` | `true` | Flip to avoid viewport edges |
| `class` | `HTMLAttributes["class"]` | — | Additional classes |

## Popover Props (Root)

| Prop | Type | Description |
|---|---|---|
| `open` | `boolean` | Controlled open state |
| `defaultOpen` | `boolean` | Initial open state (uncontrolled) |
| `modal` | `boolean` | Modal mode (traps focus) |

## Emits (Root)

| Event | Type | Description |
|---|---|---|
| `update:open` | `boolean` | Fired on open/close |

## reka-ui Reference
https://reka-ui.com/docs/components/popover

## References
- Source: `POPOVER-SOURCE.md`
- API: `POPOVER-API.md`
- Examples: `POPOVER-EXAMPLES.md`
- Installation: `POPOVER-INSTALLATION.md`
