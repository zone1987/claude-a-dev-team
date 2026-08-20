# Tooltip — API Reference

## TooltipProvider

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `delayDuration` | `number` | `0` | Delay before tooltip shows (ms) |
| `skipDelayDuration` | `number` | — | Skip delay when moving between tooltips |
| `disableHoverableContent` | `boolean` | — | Prevents closing when hovering content |

## Tooltip

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `open` | `boolean` | — | Controlled open state |
| `defaultOpen` | `boolean` | — | Uncontrolled default open |
| `onOpenChange` | `(open: boolean) => void` | — | Open state callback |
| `delayDuration` | `number` | — | Override provider delay |

## TooltipTrigger

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `asChild` | `boolean` | `false` | Merge with child element |
| `className` | `string` | — | Additional CSS classes |

## TooltipContent

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `side` | `"top" \| "right" \| "bottom" \| "left"` | `"top"` | Position relative to trigger |
| `sideOffset` | `number` | `0` | Distance from trigger |
| `align` | `"start" \| "center" \| "end"` | `"center"` | Alignment |
| `alignOffset` | `number` | `0` | Alignment offset |
| `avoidCollisions` | `boolean` | `true` | Auto-adjust position to avoid overflow |
| `className` | `string` | — | Additional CSS classes |
