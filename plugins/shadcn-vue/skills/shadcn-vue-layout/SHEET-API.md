# API Reference

reka-ui Documentation: https://reka-ui.com/docs/components/dialog#api-reference

## Sheet (DialogRoot)

| Prop | Type | Default | Description |
|---|---|---|---|
| open | boolean | — | Controlled open state |
| defaultOpen | boolean | false | Uncontrolled initial open state |
| modal | boolean | true | Whether to block interaction outside |

| Emit | Payload | Description |
|---|---|---|
| update:open | boolean | Fired when open state changes |

## SheetTrigger (DialogTrigger)

| Prop | Type | Default | Description |
|---|---|---|---|
| asChild | boolean | false | Render as child element |

## SheetContent (DialogContent)

| Prop | Type | Default | Description |
|---|---|---|---|
| side | "top" \| "right" \| "bottom" \| "left" | "right" | Slide direction |
| class | string | — | Additional CSS classes |
| forceMount | boolean | — | Force mount even when closed |
| trapFocus | boolean | true | Trap focus inside content |

The content includes an automatic close button (X icon) in the top-right corner.

## SheetClose (DialogClose)

| Prop | Type | Default | Description |
|---|---|---|---|
| asChild | boolean | false | Render as child element |

## SheetOverlay (DialogOverlay)

| Prop | Type | Default | Description |
|---|---|---|---|
| class | string | — | Additional CSS classes |
| forceMount | boolean | — | Force mount even when closed |

## SheetHeader

| Prop | Type | Default | Description |
|---|---|---|---|
| class | string | — | Additional CSS classes |

Pure layout div (`flex flex-col gap-1.5 p-4`).

## SheetFooter

| Prop | Type | Default | Description |
|---|---|---|---|
| class | string | — | Additional CSS classes |

Pure layout div (`mt-auto flex flex-col gap-2 p-4`).

## SheetTitle (DialogTitle)

| Prop | Type | Default | Description |
|---|---|---|---|
| class | string | — | Additional CSS classes |

## SheetDescription (DialogDescription)

| Prop | Type | Default | Description |
|---|---|---|---|
| class | string | — | Additional CSS classes |

## data-slot Attributes

| Component | data-slot value |
|---|---|
| Sheet | sheet |
| SheetTrigger | sheet-trigger |
| SheetContent | sheet-content |
| SheetOverlay | sheet-overlay |
| SheetClose | sheet-close |
| SheetHeader | sheet-header |
| SheetFooter | sheet-footer |
| SheetTitle | sheet-title |
| SheetDescription | sheet-description |
