---
name: shadcn-forms
description: shadcn/ui Formulare — Field/Form-Komponenten mit react-hook-form, TanStack Form, Formisch, Next.js Server Actions und Zod. Trigger: shadcn form, shadcn Formular, react-hook-form shadcn, shadcn zod, shadcn Field, useForm shadcn.
---

# shadcn-forms

Build accessible, validated forms with shadcn `<Field />` components and your
choice of form library.

## Supported libraries

| Library            | Validation | Reference                             |
|--------------------|------------|---------------------------------------|
| React Hook Form    | Zod        | [react-hook-form.md](references/react-hook-form.md) |
| TanStack Form      | Zod        | [tanstack-form.md](references/tanstack-form.md)     |
| Formisch           | Valibot    | [formisch.md](references/formisch.md)               |
| Next.js Server Actions | Zod   | [next-server-actions.md](references/next-server-actions.md) |

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
