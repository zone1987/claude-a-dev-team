# Scroll Area — API Reference

Full API:
- Radix: https://www.radix-ui.com/docs/primitives/components/scroll-area#api-reference
- Base UI: https://base-ui.com/react/components/scroll-area#api-reference

## ScrollArea

Wraps `ScrollAreaPrimitive.Root`. Accepts all Root props.

| Prop        | Type                            | Default | Description                                   |
| ----------- | ------------------------------- | ------- | --------------------------------------------- |
| `className` | `string`                        | —       | Additional CSS classes                        |
| `children`  | `React.ReactNode`               | —       | Scrollable content                            |
| `type`      | `"auto" \| "always" \| "scroll" \| "hover"` | `"hover"` | Scrollbar visibility strategy (Radix) |
| `scrollHideDelay` | `number`                  | `600`   | Delay before hiding scrollbar in ms (Radix)   |
| `dir`       | `"ltr" \| "rtl"`                | —       | Reading direction                             |

`data-slot="scroll-area"`

Internally renders:
- `data-slot="scroll-area-viewport"` — the scrollable viewport
- `<ScrollBar />` — vertical scrollbar (auto)
- `<Corner />` — corner piece when both scrollbars are visible

## ScrollBar

Wraps `ScrollAreaPrimitive.ScrollAreaScrollbar`.

| Prop          | Type                          | Default      | Description                   |
| ------------- | ----------------------------- | ------------ | ----------------------------- |
| `orientation` | `"vertical" \| "horizontal"` | `"vertical"` | Scrollbar orientation         |
| `className`   | `string`                      | —            | Additional CSS classes        |

`data-slot="scroll-area-scrollbar"`

Internally renders:
- `data-slot="scroll-area-thumb"` — the draggable thumb

## Data attributes

| Attribute       | Values                     | Description                 |
| --------------- | -------------------------- | --------------------------- |
| `data-state`    | `"visible" \| "hidden"`    | Current scrollbar visibility |
| `data-orientation` | `"vertical" \| "horizontal"` | Scrollbar orientation    |

## Source files

- `registry/new-york-v4/ui/scroll-area.tsx`
