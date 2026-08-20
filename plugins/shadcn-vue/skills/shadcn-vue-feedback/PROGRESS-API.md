# API Reference

## Progress

A thin wrapper around `ProgressRoot` from reka-ui. Renders a horizontal
progress bar with an animated inner indicator.

### Props

Extends all `ProgressRootProps` from reka-ui plus the following:

| Prop            | Type                                      | Default | Description                                               |
|-----------------|-------------------------------------------|---------|-----------------------------------------------------------|
| `modelValue`    | `number`                                  | `0`     | Current progress value between `0` and `max`.             |
| `max`           | `number`                                  | `100`   | Maximum value. Determines the full-width threshold.       |
| `getValueLabel` | `(value: number, max: number) => string`  | —       | Returns a human-readable accessibility label for the value.|
| `class`         | `string`                                  | —       | CSS classes merged onto the root element via `cn()`.      |

All other `ProgressRootProps` (e.g. `asChild`) are forwarded verbatim to
`ProgressRoot` via `reactiveOmit` / `v-bind`.

### Data slots

| Slot attribute              | Element                 | Purpose                       |
|-----------------------------|-------------------------|-------------------------------|
| `data-slot="progress"`      | Root `<div>`            | Target for CSS overrides.     |
| `data-slot="progress-indicator"` | Inner `<div>`      | The moving bar element.       |

### Indicator positioning

The indicator width is always `100%`. Its visible position is driven by:

```
transform: translateX(-{{ 100 - (modelValue ?? 0) }}%)
```

When `modelValue` is `0`, the indicator is fully hidden (shifted left by
100%). When `modelValue` equals `max` (default `100`), `translateX(0%)` shows
it in full.

### Accessibility

- Renders with `role="progressbar"`.
- `aria-valuemin="0"`, `aria-valuemax` bound to `max`,
  `aria-valuenow` bound to `modelValue`.
- Provide `getValueLabel` to give screen readers a meaningful text, e.g.
  `"66 of 100 steps complete"`.

## External API reference

Full reka-ui ProgressRoot API:
https://reka-ui.com/docs/components/progress#api-reference
