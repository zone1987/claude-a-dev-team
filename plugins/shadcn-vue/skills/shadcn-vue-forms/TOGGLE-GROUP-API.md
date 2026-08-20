# ToggleGroup — API Reference

## Sub-components

| Export | Description |
|---|---|
| `ToggleGroup` | Root container — sets type, variant, size, spacing context |
| `ToggleGroupItem` | Individual toggle item inside a group |

## ToggleGroup Props

Extends all reka-ui `ToggleGroupRootProps` plus:

| Prop | Type | Default | Description |
|---|---|---|---|
| `class` | `HTMLAttributes["class"]` | `undefined` | Additional CSS classes |
| `type` | `"single" \| "multiple"` | required | Single or multiple selection mode |
| `variant` | `"default" \| "outline"` | `undefined` | Shared visual variant (passed to items via context) |
| `size` | `"sm" \| "default" \| "lg"` | `undefined` | Shared size preset |
| `spacing` | `number` | `0` | Gap between items in Tailwind spacing units |
| `defaultValue` | `string \| string[]` | `undefined` | Uncontrolled initial value |
| `modelValue` | `string \| string[]` | `undefined` | Controlled value (v-model) |
| `disabled` | `boolean` | `false` | Disables all items |
| `orientation` | `"horizontal" \| "vertical"` | `"horizontal"` | Layout direction |
| `loop` | `boolean` | `true` | Keyboard navigation loops around |
| `as` | `AsTag \| Component` | `"div"` | Root element |
| `asChild` | `boolean` | `false` | Merge onto child |

## ToggleGroup Emits

| Event | Payload | Description |
|---|---|---|
| `update:modelValue` | `string \| string[]` | Fires when selection changes |

## ToggleGroup Slots

| Slot | Slot Props | Description |
|---|---|---|
| `default` | `{ modelValue: string \| string[] }` | Items container |

## ToggleGroupItem Props

Extends all reka-ui `ToggleGroupItemProps` plus:

| Prop | Type | Default | Description |
|---|---|---|---|
| `value` | `string` | required | Unique value for this item |
| `class` | `HTMLAttributes["class"]` | `undefined` | Additional CSS classes |
| `variant` | `"default" \| "outline"` | inherited from context | Override parent variant |
| `size` | `"sm" \| "default" \| "lg"` | inherited from context | Override parent size |
| `disabled` | `boolean` | `false` | Disables this item |
| `as` | `AsTag \| Component` | `"button"` | Rendered element |
| `asChild` | `boolean` | `false` | Merge onto child |

## ToggleGroupItem Slots

| Slot | Slot Props | Description |
|---|---|---|
| `default` | `{ pressed: boolean }` | Item content |

## Data Attributes

| Element | Attribute | Values | Description |
|---|---|---|---|
| ToggleGroup | `data-slot` | `"toggle-group"` | CSS targeting |
| ToggleGroup | `data-variant` | `"default" \| "outline"` | Current variant |
| ToggleGroup | `data-size` | `"sm" \| "default" \| "lg"` | Current size |
| ToggleGroup | `data-spacing` | number | Current spacing value |
| ToggleGroupItem | `data-slot` | `"toggle-group-item"` | CSS targeting |
| ToggleGroupItem | `data-state` | `"on" \| "off"` | Pressed state |
| ToggleGroupItem | `data-disabled` | `""` | Present when disabled |

## reka-ui API Reference

https://reka-ui.com/docs/components/toggle-group#api-reference
