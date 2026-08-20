# Input — API

## Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `modelValue` | `string \| number` | - | v-model binding |
| `defaultValue` | `string \| number` | - | Uncontrolled initial value |
| `class` | `string` | - | Additional CSS classes |
| All native `<input>` attributes | - | - | e.g. `type`, `placeholder`, `disabled`, `required`, `aria-invalid` |

## Emits

| Event | Payload | Description |
|---|---|---|
| `update:modelValue` | `string \| number` | On input |

## Important native attributes

| Attribute | Description |
|---|---|
| `type` | `text`, `email`, `password`, `number`, `tel`, `url`, `search`, `date`, `time`, `file`, etc. |
| `disabled` | Disables the field (opacity-50, cursor-not-allowed) |
| `aria-invalid` | Enables error styling (red border + ring) |
| `placeholder` | Placeholder text |

## CSS classes (states)

- **Focus**: `focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:ring-3`
- **Error**: `aria-invalid:ring-destructive/20 aria-invalid:border-destructive`
- **Disabled**: `disabled:pointer-events-none disabled:cursor-not-allowed disabled:opacity-50`
