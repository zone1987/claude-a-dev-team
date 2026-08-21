# Dialog — API

Reka-UI API reference: https://reka-ui.com/docs/components/dialog#api-reference

## Sub-components

| Component | Description |
|---|---|
| `Dialog` | Root wrapper (DialogRoot from reka-ui) |
| `DialogTrigger` | Button/element that opens the dialog |
| `DialogPortal` | Ports content into `<body>` (used internally) |
| `DialogOverlay` | Semi-transparent overlay behind the dialog |
| `DialogContent` | The actual dialog container with close button |
| `DialogScrollContent` | Scrollable dialog container (the overlay scrolls) |
| `DialogHeader` | Area for title and description |
| `DialogFooter` | Area for action buttons |
| `DialogTitle` | Semantic title (aria-labelledby) |
| `DialogDescription` | Semantic description (aria-describedby) |
| `DialogClose` | Button for closing the dialog |

## Dialog (Root)

Forwards all props/emits to `DialogRoot`.

| Prop | Type | Default | Description |
|---|---|---|---|
| `open` | `boolean` | - | Controlled open state |
| `defaultOpen` | `boolean` | `false` | Uncontrolled initial value |
| `modal` | `boolean` | `true` | Whether the dialog is modal |

| Emit | Payload | Description |
|---|---|---|
| `update:open` | `boolean` | Open state changed |

## DialogContent

| Prop | Type | Default | Description |
|---|---|---|---|
| `class` | `string` | - | Additional CSS classes |
| `showCloseButton` | `boolean` | `true` | Show the X button in the top right |
| All `DialogContentProps` | - | - | Are forwarded to reka-ui |

| Emit | Description |
|---|---|
| `closeAutoFocus` | Focus after closing |
| `escapeKeyDown` | Escape key pressed |
| `interactOutside` | Click outside |
| `openAutoFocus` | Focus on opening |
| `pointerDownOutside` | Pointer event outside |

## DialogFooter

| Prop | Type | Default | Description |
|---|---|---|---|
| `class` | `string` | - | Additional CSS classes |
| `showCloseButton` | `boolean` | `false` | Automatic close button |

## DialogLegend / Label (Header/Footer/Title/Description)

All simple wrapper components accept:

| Prop | Type | Default |
|---|---|---|
| `class` | `string` | - |

## DialogOverlay

Inherits all `DialogOverlayProps` from reka-ui plus `class`.

## Slots

All components use standard default slots (`<slot />`). `Dialog` and `DialogRoot` additionally provide `slotProps` (open state etc.).
