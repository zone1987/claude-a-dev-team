# Input — API Reference

## Props

All native `<input>` HTML attributes are forwarded. Key ones:

| Prop           | Type                      | Default  | Description                                                      |
| -------------- | ------------------------- | -------- | ---------------------------------------------------------------- |
| `type`         | `string`                  | `"text"` | Input type (text, email, password, file, number, search, tel, …) |
| `placeholder`  | `string`                  | –        | Placeholder text                                                 |
| `disabled`     | `boolean`                 | `false`  | Disables input, dims with `opacity-50`                           |
| `aria-invalid` | `boolean`                 | –        | Triggers red error styling (border + ring)                       |
| `className`    | `string`                  | –        | Additional CSS classes                                           |
| `value`        | `string`                  | –        | Controlled value                                                 |
| `defaultValue` | `string`                  | –        | Uncontrolled default value                                       |
| `onChange`     | `ChangeEventHandler`      | –        | Change handler                                                   |
| `readOnly`     | `boolean`                 | `false`  | Makes input read-only                                            |
| `required`     | `boolean`                 | `false`  | Marks field as required for form validation                      |
| `autoComplete` | `string`                  | –        | Browser autocomplete hint                                        |

## Styling States

| State         | CSS Approach                                           |
| ------------- | ------------------------------------------------------ |
| Default       | `border-input bg-transparent`                          |
| Focus         | `focus-visible:border-ring focus-visible:ring-[3px]`   |
| Disabled      | `disabled:opacity-50 disabled:cursor-not-allowed`      |
| Invalid       | `aria-invalid:border-destructive aria-invalid:ring-*`  |
| Dark mode     | `dark:bg-input/30`                                     |

## File Input Styling

When `type="file"`, the file picker button is styled with:
- `file:inline-flex file:h-7 file:border-0 file:bg-transparent file:text-sm file:font-medium file:text-foreground`

## Integration with Field

Use `Field` + `FieldLabel` + `FieldError` for full accessible form fields:

```tsx
<Field data-invalid>
  <FieldLabel htmlFor="email">Email</FieldLabel>
  <Input id="email" type="email" aria-invalid />
  <FieldError>Enter a valid email address.</FieldError>
</Field>
```

---

_Source: `apps/v4/registry/new-york-v4/ui/input.tsx`, `apps/v4/content/docs/components/base/input.mdx`_
