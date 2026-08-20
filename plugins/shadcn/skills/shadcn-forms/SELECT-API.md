# Select — API Reference

Full API:
- Radix: https://www.radix-ui.com/docs/primitives/components/select#api-reference
- Base UI: https://base-ui.com/react/components/select#api-reference

## Select (Root)

| Prop              | Type                           | Default | Description                              |
| ----------------- | ------------------------------ | ------- | ---------------------------------------- |
| `value`           | `string`                       | —       | Controlled value                         |
| `defaultValue`    | `string`                       | —       | Uncontrolled default value               |
| `onValueChange`   | `(value: string) => void`      | —       | Called when value changes                |
| `open`            | `boolean`                      | —       | Controlled open state                    |
| `defaultOpen`     | `boolean`                      | —       | Uncontrolled open default                |
| `onOpenChange`    | `(open: boolean) => void`      | —       | Called when open state changes           |
| `disabled`        | `boolean`                      | `false` | Disables entire select                   |
| `required`        | `boolean`                      | `false` | Marks as required for forms              |
| `name`            | `string`                       | —       | Name for form submission                 |

`data-slot="select"`

## SelectTrigger

| Prop        | Type                 | Default     | Description                              |
| ----------- | -------------------- | ----------- | ---------------------------------------- |
| `size`      | `"sm" \| "default"` | `"default"` | Height — `h-8` (sm) or `h-9` (default)  |
| `className` | `string`             | —           | Additional CSS classes                   |
| `aria-invalid` | `boolean`         | —           | Shows destructive/invalid styling        |

`data-slot="select-trigger"`, `data-size={size}`

## SelectValue

| Prop          | Type     | Default | Description                              |
| ------------- | -------- | ------- | ---------------------------------------- |
| `placeholder` | `string` | —       | Text shown when no value is selected     |

`data-slot="select-value"`

## SelectContent

| Prop                   | Type                              | Default          | Description                                    |
| ---------------------- | --------------------------------- | ---------------- | ---------------------------------------------- |
| `position`             | `"item-aligned" \| "popper"`      | `"item-aligned"` | How the dropdown is positioned                 |
| `align`                | `"start" \| "center" \| "end"`   | `"center"`       | Alignment relative to trigger                  |
| `sideOffset`           | `number`                          | —                | Distance from trigger (popper mode)            |
| `className`            | `string`                          | —                | Additional CSS classes                         |

`data-slot="select-content"`

Note: `position="item-aligned"` (default) aligns the selected item over the trigger.
`position="popper"` behaves like a standard dropdown aligned to trigger edge.

**Base UI equivalent**: use `alignItemWithTrigger` prop (default `true`) on `SelectContent` instead of `position`.

## SelectGroup

Groups related items visually. Accepts `className`.

`data-slot="select-group"`

## SelectLabel

| Prop        | Type     | Default | Description                       |
| ----------- | -------- | ------- | --------------------------------- |
| `className` | `string` | —       | Additional CSS classes            |

`data-slot="select-label"` — renders `text-xs text-muted-foreground`

## SelectItem

| Prop        | Type      | Default | Description                                    |
| ----------- | --------- | ------- | ---------------------------------------------- |
| `value`     | `string`  | —       | **Required.** The value for this item          |
| `disabled`  | `boolean` | `false` | Disables this item                             |
| `className` | `string`  | —       | Additional CSS classes                         |

`data-slot="select-item"`
Shows a `CheckIcon` when selected via `data-slot="select-item-indicator"`.

## SelectSeparator

Visual horizontal separator between groups.

`data-slot="select-separator"`

## SelectScrollUpButton / SelectScrollDownButton

Rendered automatically inside `SelectContent` for scrollable lists.

`data-slot="select-scroll-up-button"` / `data-slot="select-scroll-down-button"`

## Source files

- `registry/new-york-v4/ui/select.tsx`
