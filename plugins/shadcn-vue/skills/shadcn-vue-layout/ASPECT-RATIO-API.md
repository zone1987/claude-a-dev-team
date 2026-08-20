# AspectRatio — API Reference

The `AspectRatio` component wraps the [`AspectRatio`](https://reka-ui.com/docs/components/aspect-ratio#api-reference) primitive from **reka-ui** and forwards all props.

## Props

| Prop      | Type      | Default | Description                                                              |
|-----------|-----------|---------|--------------------------------------------------------------------------|
| `ratio`   | `number`  | `1`     | The desired aspect ratio. Pass a division expression, e.g. `16 / 9`.    |
| `asChild` | `boolean` | `false` | Merge props and behaviour onto the direct child instead of a wrapper element. |

## Slot

The default slot receives the same `slotProps` forwarded by reka-ui (currently empty for AspectRatio, but kept for future compatibility).

## data-slot

The root element carries `data-slot="aspect-ratio"` which can be used for Tailwind variant targeting:

```css
[data-slot="aspect-ratio"] { /* custom styles */ }
```
