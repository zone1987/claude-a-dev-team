# Select — API

## Select (root)

Wraps `SelectRoot`.

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| modelValue | `string` | — | Controlled value (use with `v-model`) |
| defaultValue | `string` | — | Uncontrolled initial value |
| open | `boolean` | — | Controlled open state |
| defaultOpen | `boolean` | — | Uncontrolled initial open state |
| disabled | `boolean` | `false` | Disables the entire select |
| required | `boolean` | `false` | Marks the select as required |
| name | `string` | — | Name for form submission |
| dir | `"ltr" \| "rtl"` | — | Reading direction |

Emits: `update:modelValue`, `update:open`

## SelectTrigger

Wraps `SelectTrigger` + `SelectIcon`.

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| size | `"sm" \| "default"` | `"default"` | Height variant — `h-9` (default) or `h-8` (sm) |
| disabled | `boolean` | `false` | Disables the trigger |
| class | `HTMLAttributes["class"]` | — | Additional CSS classes |

## SelectContent

Wraps `SelectPortal` + `SelectContent` + `SelectViewport` + scroll buttons.

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| position | `"item-aligned" \| "popper"` | `"popper"` | Positioning strategy |
| side | `"top" \| "right" \| "bottom" \| "left"` | `"bottom"` | Preferred side when `position="popper"` |
| sideOffset | `number` | `0` | Distance from the trigger |
| align | `"start" \| "center" \| "end"` | `"start"` | Alignment relative to trigger |
| alignOffset | `number` | `0` | Alignment offset |
| avoidCollisions | `boolean` | `true` | Adjust position to avoid viewport overflow |
| class | `HTMLAttributes["class"]` | — | Additional CSS classes |

## SelectGroup

Wraps items into a logical group. No additional props beyond `SelectGroupProps`.

## SelectLabel

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| class | `HTMLAttributes["class"]` | — | Additional CSS classes |

Renders small muted text as a group label. Typically used inside `SelectGroup`.

## SelectItem

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| value | `string` | **required** | The value emitted on selection |
| disabled | `boolean` | `false` | Prevents selection |
| textValue | `string` | — | Text used for typeahead search |
| class | `HTMLAttributes["class"]` | — | Additional CSS classes |

Named slot `indicator-icon`: replaces the default `Check` icon inside the item indicator.

## SelectItemText

Thin wrapper around reka-ui `SelectItemText`. No additional props. Used inside custom item implementations.

## SelectScrollUpButton / SelectScrollDownButton

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| class | `HTMLAttributes["class"]` | — | Additional CSS classes |

Default slot overrides the chevron icon.

## SelectSeparator

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| class | `HTMLAttributes["class"]` | — | Additional CSS classes |

Renders a 1px horizontal divider between groups.

## SelectValue

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| placeholder | `string` | — | Text shown when no value is selected |

## reka-ui API Reference

https://reka-ui.com/docs/components/select#api-reference
