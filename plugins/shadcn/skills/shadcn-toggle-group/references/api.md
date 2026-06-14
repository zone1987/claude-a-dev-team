# ToggleGroup — API Reference

## ToggleGroup

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `type` | `"single" \| "multiple"` | required | Selection mode |
| `value` | `string \| string[]` | — | Controlled value |
| `defaultValue` | `string \| string[]` | — | Uncontrolled default |
| `onValueChange` | `(value: string \| string[]) => void` | — | Change callback |
| `variant` | `"default" \| "outline"` | `"default"` | Visual style (propagates to items) |
| `size` | `"default" \| "sm" \| "lg"` | `"default"` | Size (propagates to items) |
| `spacing` | `number` | `2` (radix base) / `0` (new-york-v4) | Gap between items (0 = connected) |
| `orientation` | `"horizontal" \| "vertical"` | `"horizontal"` | Layout (radix base only) |
| `disabled` | `boolean` | `false` | Disables all items |
| `className` | `string` | — | Additional CSS classes |

## ToggleGroupItem

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `value` | `string` | required | Item identifier |
| `variant` | `"default" \| "outline"` | — | Override context variant |
| `size` | `"default" \| "sm" \| "lg"` | — | Override context size |
| `disabled` | `boolean` | `false` | Disables this item |
| `aria-label` | `string` | — | Required for icon-only items |
| `className` | `string` | — | Additional CSS classes |
