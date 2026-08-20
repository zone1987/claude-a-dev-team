# Separator — API

## Separator

Wraps reka-ui `Separator`.

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| orientation | `"horizontal" \| "vertical"` | `"horizontal"` | Orientation of the separator line |
| decorative | `boolean` | `true` | When `true`, renders as `role="none"` (purely visual). Set to `false` for semantic separators (`role="separator"`) |
| class | `HTMLAttributes["class"]` | — | Additional CSS classes |

All `SeparatorProps` from reka-ui are forwarded via `v-bind` (after omitting `class`).

## Styling

The component uses Tailwind data-attribute variants to apply dimensions:

- `data-[orientation=horizontal]:h-px data-[orientation=horizontal]:w-full` — 1px tall, full width
- `data-[orientation=vertical]:h-full data-[orientation=vertical]:w-px` — full height, 1px wide
- `bg-border` — uses the CSS variable `--color-border`

## reka-ui API Reference

https://reka-ui.com/docs/components/separator#api-reference
