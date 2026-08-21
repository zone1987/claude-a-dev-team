# Popover — API Reference

## Composition

```text
Popover
├── PopoverTrigger
├── PopoverAnchor   (optional, for custom positioning)
└── PopoverContent
    └── PopoverHeader
        ├── PopoverTitle
        └── PopoverDescription
```

## Popover

Root component that manages open/close state.

Inherits `PopoverPrimitive.Root` props from `@radix-ui/react-popover`:

| Prop             | Type                      | Description                               |
| ---------------- | ------------------------- | ----------------------------------------- |
| `open`           | `boolean`                 | Controlled open state                     |
| `defaultOpen`    | `boolean`                 | Initial open state (uncontrolled)         |
| `onOpenChange`   | `(open: boolean) => void` | Callback when open state changes          |
| `modal`          | `boolean`                 | Makes popover modal (default `false`)     |

## PopoverTrigger

Button that opens/closes the popover. Use `asChild` to render as a custom element:

```tsx
<PopoverTrigger asChild>
  <Button variant="outline">Open</Button>
</PopoverTrigger>
```

## PopoverContent

The floating panel rendered in a Portal. Defaults: `align="center"`, `sideOffset=4`.

| Prop          | Type                                     | Default    | Description                        |
| ------------- | ---------------------------------------- | ---------- | ---------------------------------- |
| `align`       | `"start" \| "center" \| "end"`           | `"center"` | Horizontal alignment to trigger    |
| `side`        | `"top" \| "right" \| "bottom" \| "left"` | `"bottom"` | Which side to render on            |
| `sideOffset`  | `number`                                 | `4`        | Gap from trigger in pixels         |
| `className`   | `string`                                 |            | Override/extend default `w-72 p-4` |

## PopoverAnchor

Optional anchor for positioning the popover relative to a different element than the trigger.

## PopoverHeader

Flex column container for title and description. `flex flex-col gap-1 text-sm`.

## PopoverTitle

Heading element inside the header. `font-medium`.

## PopoverDescription

Muted description below the title. `text-muted-foreground`.

---
Source: `content/docs/components/base/popover.mdx`
