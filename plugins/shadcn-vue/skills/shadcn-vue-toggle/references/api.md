# Toggle — API Reference

## Sub-components

| Export | Description |
|---|---|
| `Toggle` | The single toggle button component |
| `toggleVariants` | CVA function — use directly for custom styling |
| `ToggleVariants` | TypeScript type for variant/size props |

## Props (Toggle)

Extends all reka-ui `ToggleProps` plus:

| Prop | Type | Default | Description |
|---|---|---|---|
| `class` | `HTMLAttributes["class"]` | `undefined` | Additional CSS classes merged via `cn()` |
| `variant` | `"default" \| "outline"` | `"default"` | Visual style variant |
| `size` | `"sm" \| "default" \| "lg"` | `"default"` | Button size preset |
| `defaultPressed` | `boolean` | `false` | Uncontrolled initial pressed state |
| `pressed` | `boolean` | `undefined` | Controlled pressed state |
| `disabled` | `boolean` | `false` | Disables interaction |
| `as` | `AsTag \| Component` | `"button"` | Rendered element or component |
| `asChild` | `boolean` | `false` | Merges props onto child element |

## Emits (Toggle)

| Event | Payload | Description |
|---|---|---|
| `update:pressed` | `boolean` | Fired when pressed state changes |

## Slots (Toggle)

| Slot | Slot Props | Description |
|---|---|---|
| `default` | `{ pressed: boolean }` | Toggle content; receives pressed state |

## Data Attributes

| Attribute | Values | Description |
|---|---|---|
| `data-slot` | `"toggle"` | Always present for CSS targeting |
| `data-state` | `"on" \| "off"` | Current pressed state |
| `data-disabled` | `""` | Present when disabled |

## reka-ui API Reference

https://reka-ui.com/docs/components/toggle#api-reference
