# Label — API Reference

## Label

| Prop        | Type                                              | Default | Description                                 |
| ----------- | ------------------------------------------------- | ------- | ------------------------------------------- |
| `htmlFor`   | `string`                                          |         | ID of the associated form control           |
| `className` | `string`                                          | `""`    | Additional CSS classes                      |
| `children`  | `React.ReactNode`                                 |         | Label text / content                        |

Inherits all props from `@radix-ui/react-label` Root (or native `<label>` in base variant).

### Peer / group states

The label automatically:
- Shows `cursor-not-allowed opacity-50` when a `peer` sibling is `disabled`
- Shows `pointer-events-none opacity-50` when a parent has `data-disabled="true"`

### Usage with Field

For complete form fields use the `Field` component which provides built-in `FieldLabel`, `FieldDescription`, and `FieldError`:

```tsx
import { Field, FieldLabel } from "@/components/ui/field"
import { Input } from "@/components/ui/input"

<Field>
  <FieldLabel htmlFor="email">Your email address</FieldLabel>
  <Input id="email" />
</Field>
```

---
Source: `content/docs/components/base/label.mdx`
