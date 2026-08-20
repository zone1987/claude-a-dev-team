# Sheet — API Reference

Sheet is built on Radix UI Dialog / Base UI Dialog primitives.

Full API:
- Radix: https://www.radix-ui.com/docs/primitives/components/dialog#api-reference
- Base UI: https://base-ui.com/react/components/dialog#api-reference

## Sheet (Root)

| Prop           | Type                      | Default | Description                              |
| -------------- | ------------------------- | ------- | ---------------------------------------- |
| `open`         | `boolean`                 | —       | Controlled open state                    |
| `defaultOpen`  | `boolean`                 | —       | Uncontrolled default open                |
| `onOpenChange` | `(open: boolean) => void` | —       | Called when open state changes           |
| `modal`        | `boolean`                 | `true`  | Whether interaction is modal             |

`data-slot="sheet"`

## SheetTrigger

Renders as button. Accepts `asChild` to replace with a custom element.

`data-slot="sheet-trigger"`

## SheetClose

Renders as button. Accepts `asChild`.

`data-slot="sheet-close"`

## SheetContent

| Prop              | Type                                    | Default   | Description                                          |
| ----------------- | --------------------------------------- | --------- | ---------------------------------------------------- |
| `side`            | `"top" \| "right" \| "bottom" \| "left"` | `"right"` | Which edge of the screen the sheet slides from       |
| `showCloseButton` | `boolean`                               | `true`    | Whether to render the X close button                 |
| `className`       | `string`                                | —         | Additional CSS classes                               |

`data-slot="sheet-content"`

Side-specific widths:
- `right` / `left`: `w-3/4 sm:max-w-sm`
- `top` / `bottom`: `h-auto` (height-based)

## SheetHeader

Plain `div` wrapper. Provides `flex flex-col gap-1.5 p-4` layout.

`data-slot="sheet-header"`

## SheetFooter

Plain `div` wrapper at the bottom. Provides `mt-auto flex flex-col gap-2 p-4` layout.

`data-slot="sheet-footer"`

## SheetTitle

Wraps `SheetPrimitive.Title`. Provides accessible title for the sheet.

`data-slot="sheet-title"`

## SheetDescription

Wraps `SheetPrimitive.Description`. Provides accessible description.

`data-slot="sheet-description"`

## Source files

- `registry/new-york-v4/ui/sheet.tsx`
