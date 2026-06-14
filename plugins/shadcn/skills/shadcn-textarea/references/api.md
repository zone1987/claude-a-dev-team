# Textarea — API

`Textarea` extends all native HTML `<textarea>` props (`React.ComponentProps<"textarea">`).

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `className` | `string` | — | Additional CSS classes |
| `disabled` | `boolean` | `false` | Disables the textarea |
| `placeholder` | `string` | — | Placeholder text |
| `value` | `string` | — | Controlled value |
| `defaultValue` | `string` | — | Uncontrolled default value |
| `onChange` | `React.ChangeEventHandler<HTMLTextAreaElement>` | — | Change handler |
| `rows` | `number` | — | Number of visible rows |
| `cols` | `number` | — | Number of columns |
| `aria-invalid` | `boolean \| "true" \| "false"` | — | Marks textarea as invalid (adds destructive styling) |
| `required` | `boolean` | `false` | Marks as required |
| `readOnly` | `boolean` | `false` | Makes textarea read-only |
| `maxLength` | `number` | — | Maximum character length |

## Notes

- `field-sizing-content` CSS property enables auto-resize based on content.
- Use `aria-invalid` for validation error state (triggers red border + ring).
- `data-disabled` on a parent `Field` component enables field-level disabled styling.
