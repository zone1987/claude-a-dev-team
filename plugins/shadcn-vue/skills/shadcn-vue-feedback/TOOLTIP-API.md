# Tooltip — API Reference

## Sub-components

| Export | Description |
|---|---|
| `TooltipProvider` | App-level provider; manages delay and open state globally |
| `Tooltip` | Root for a single tooltip; manages open/closed state |
| `TooltipTrigger` | The element that triggers the tooltip on hover/focus |
| `TooltipContent` | The floating content panel (rendered in a portal) |

## TooltipProvider Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `delayDuration` | `number` | `0` | Milliseconds before tooltip appears |
| `skipDelayDuration` | `number` | `300` | Delay skipped when moving between tooltips |
| `disableHoverableContent` | `boolean` | `false` | Prevents hovering tooltip content from keeping it open |
| `disableClosingTrigger` | `boolean` | `false` | Prevents trigger click from closing tooltip |
| `ignoreNonKeyboardFocus` | `boolean` | `false` | Only show tooltip on keyboard focus |

## Tooltip Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `open` | `boolean` | `undefined` | Controlled open state |
| `defaultOpen` | `boolean` | `false` | Uncontrolled initial open state |
| `delayDuration` | `number` | inherited | Per-tooltip delay override |
| `disableHoverableContent` | `boolean` | inherited | Per-tooltip override |
| `disableClosingTrigger` | `boolean` | inherited | Per-tooltip override |
| `ignoreNonKeyboardFocus` | `boolean` | inherited | Per-tooltip override |

## Tooltip Emits

| Event | Payload | Description |
|---|---|---|
| `update:open` | `boolean` | Fires when open state changes |

## TooltipTrigger Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `as` | `AsTag \| Component` | `"button"` | Rendered element |
| `asChild` | `boolean` | `false` | Merge props onto child element |

## TooltipContent Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `class` | `HTMLAttributes["class"]` | `undefined` | Additional CSS classes |
| `side` | `"top" \| "right" \| "bottom" \| "left"` | `"top"` | Preferred side of the trigger |
| `sideOffset` | `number` | `4` | Distance in px from trigger |
| `align` | `"start" \| "center" \| "end"` | `"center"` | Alignment along trigger axis |
| `alignOffset` | `number` | `0` | Offset along alignment axis |
| `avoidCollisions` | `boolean` | `true` | Flip side when near viewport edge |
| `collisionBoundary` | `Element \| null \| Array<...>` | `[]` | Boundary elements for collision detection |
| `collisionPadding` | `number \| Partial<Record<Side, number>>` | `0` | Padding for collision detection |
| `arrowPadding` | `number` | `0` | Padding from edges for arrow |
| `sticky` | `"partial" \| "always"` | `"partial"` | Sticky behavior at boundary edges |
| `hideWhenDetached` | `boolean` | `false` | Hide when trigger is fully obscured |
| `as` | `AsTag \| Component` | `"div"` | Rendered element |
| `asChild` | `boolean` | `false` | Merge onto child |

## TooltipContent Emits

| Event | Payload | Description |
|---|---|---|
| `escapeKeyDown` | `KeyboardEvent` | Fires on Escape key |
| `pointerDownOutside` | `PointerDownOutsideEvent` | Fires on outside pointer down |

## Data Attributes

| Element | Attribute | Values | Description |
|---|---|---|---|
| Tooltip | `data-slot` | `"tooltip"` | CSS targeting |
| TooltipTrigger | `data-slot` | `"tooltip-trigger"` | CSS targeting |
| TooltipContent | `data-slot` | `"tooltip-content"` | CSS targeting |
| TooltipContent | `data-state` | `"delayed-open" \| "instant-open" \| "closed"` | Current state |
| TooltipContent | `data-side` | `"top" \| "right" \| "bottom" \| "left"` | Resolved side |
| TooltipContent | `data-align` | `"start" \| "center" \| "end"` | Resolved alignment |

## reka-ui API Reference

https://reka-ui.com/docs/components/tooltip#api-reference
