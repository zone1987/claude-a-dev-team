# HoverCard — API

Reka-UI API reference: https://reka-ui.com/docs/components/hover-card#api-reference

## Sub-components

| Component | Description |
|---|---|
| `HoverCard` | Root wrapper (HoverCardRoot) |
| `HoverCardTrigger` | Element that opens the card on hover |
| `HoverCardContent` | Content of the card (w-64, p-4, rounded-md) |

## HoverCard (Root)

| Prop | Type | Default | Description |
|---|---|---|---|
| `open` | `boolean` | - | Controlled state |
| `defaultOpen` | `boolean` | `false` | - |
| `openDelay` | `number` | `700` | Delay before opening (ms) |
| `closeDelay` | `number` | `300` | Delay before closing (ms) |

| Emit | Payload | Description |
|---|---|---|
| `update:open` | `boolean` | State changed |

## HoverCardContent

| Prop | Type | Default | Description |
|---|---|---|---|
| `side` | `"top" \| "right" \| "bottom" \| "left"` | `"bottom"` | Display side |
| `sideOffset` | `number` | `4` | Distance from the trigger |
| `align` | `"start" \| "center" \| "end"` | `"center"` | Alignment |
| `alignOffset` | `number` | `0` | Offset relative to the alignment |
| `class` | `string` | - | - |

## Slots

All components use default slots. `HoverCard` provides slotProps (open state).
