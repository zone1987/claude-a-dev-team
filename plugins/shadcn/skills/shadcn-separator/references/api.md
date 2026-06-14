# Separator — API Reference

Full API:
- Radix: https://www.radix-ui.com/docs/primitives/components/separator#api-reference
- Base UI: https://base-ui.com/react/components/separator#api-reference

## Separator

| Prop          | Type                          | Default        | Description                                           |
| ------------- | ----------------------------- | -------------- | ----------------------------------------------------- |
| `orientation` | `"horizontal" \| "vertical"` | `"horizontal"` | Direction of the separator line                       |
| `decorative`  | `boolean`                     | `true`         | When true, hides from a11y tree (Radix only)         |
| `className`   | `string`                      | —              | Additional CSS classes                                |

`data-slot="separator"`

## Data attributes

| Attribute         | Values                        | Set by          |
| ----------------- | ----------------------------- | --------------- |
| `data-orientation` | `"horizontal" \| "vertical"` | Radix primitive |
| `data-horizontal`  | present                       | Base UI variant |
| `data-vertical`    | present                       | Base UI variant |

## Visual output

- `horizontal`: `h-px w-full` — a full-width 1px line
- `vertical`: `h-full w-px` — a 1px vertical line (requires parent with set height)

## Source files

- `registry/new-york-v4/ui/separator.tsx`
