# shadcn-forms

Build accessible, validated forms with shadcn `<Field />` components and your
choice of form library.

## Supported libraries

| Library            | Validation | Reference                             |
|--------------------|------------|---------------------------------------|
| React Hook Form    | Zod        | [REACT-HOOK-FORM.md](REACT-HOOK-FORM.md) |
| TanStack Form      | Zod        | [TANSTACK-FORM.md](TANSTACK-FORM.md)     |
| Formisch           | Valibot    | [FORMISCH.md](FORMISCH.md)               |
| Next.js Server Actions | Zod   | [NEXT-SERVER-ACTIONS.md](NEXT-SERVER-ACTIONS.md) |

## Key `<Field />` props

| Prop            | Purpose                                      |
|-----------------|----------------------------------------------|
| `data-invalid`  | Triggers error styling on the Field wrapper  |
| `orientation`   | `"vertical"` (default) or `"horizontal"` or `"responsive"` |
| `data-disabled` | Applies disabled styling                     |

Always set `aria-invalid` on the native control (`<Input>`, `<SelectTrigger>`,
`<Checkbox>`, etc.) alongside `data-invalid` on `<Field>` for accessibility.

## Error display pattern (all libraries)

```tsx
{isInvalid && <FieldError errors={[fieldState.error]} />}
```

Source: forms/index.mdx
