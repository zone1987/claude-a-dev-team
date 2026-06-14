# Next.js Server Actions + shadcn Field Components

## Setup

Uses built-in React/Next.js primitives. No extra form library needed.

```bash
# next/form is built into Next.js 15+
```

## Full pattern

### schema.ts

```ts
import { z } from "zod"

export const formSchema = z.object({
  title: z.string().min(5, "Min 5 chars.").max(32, "Max 32 chars."),
  description: z.string().min(20, "Min 20 chars.").max(100, "Max 100 chars."),
})

export type FormState = {
  values?: z.infer<typeof formSchema>
  errors: null | Partial<Record<keyof z.infer<typeof formSchema>, string[]>>
  success: boolean
}
```

### actions.ts

```ts
"use server"
import { formSchema, type FormState } from "./schema"

export async function bugReportFormAction(
  _prevState: FormState,
  formData: FormData
): Promise<FormState> {
  const values = {
    title: formData.get("title") as string,
    description: formData.get("description") as string,
  }

  const result = formSchema.safeParse(values)

  if (!result.success) {
    return {
      values, // return values to preserve user input on error
      success: false,
      errors: result.error.flatten().fieldErrors,
    }
  }

  // call your API / database here

  // omit values to reset form on success
  return { errors: null, success: true }
}
```

### form.tsx (client component)

```tsx
"use client"

import * as React from "react"
import Form from "next/form"
import { bugReportFormAction } from "./actions"
import type { FormState } from "./schema"

export function BugReportForm() {
  const [formState, formAction, pending] = React.useActionState(
    bugReportFormAction,
    { errors: null, success: false }
  )

  return (
    <Form action={formAction}>
      <Field data-invalid={!!formState.errors?.title?.length}>
        <FieldLabel htmlFor="title">Bug Title</FieldLabel>
        <Input
          id="title"
          name="title"
          defaultValue={formState.values?.title}
          disabled={pending}
          aria-invalid={!!formState.errors?.title?.length}
        />
        {formState.errors?.title && (
          <FieldError>{formState.errors.title[0]}</FieldError>
        )}
      </Field>

      <Button type="submit" disabled={pending}>
        {pending && <Spinner />} Submit
      </Button>
    </Form>
  )
}
```

## Key patterns

### Error display

```tsx
<Field data-invalid={!!formState.errors?.fieldName?.length}>
  <Input aria-invalid={!!formState.errors?.fieldName?.length} />
  {formState.errors?.fieldName && (
    <FieldError>{formState.errors.fieldName[0]}</FieldError>
  )}
</Field>
```

### Pending state

```tsx
<Field data-disabled={pending}>
  <Input disabled={pending} />
</Field>
<Button type="submit" disabled={pending}>
  {pending && <Spinner />} Submit
</Button>
```

### Preserve values on error, reset on success

- On **error**: return `values` so `defaultValue` repopulates the field.
- On **success**: omit `values` so React resets the native form.

### Business logic validation (server side)

```ts
if (await db.user.findUnique({ where: { email: result.data.email } })) {
  return {
    values,
    success: false,
    errors: { email: ["This email is already registered"] },
  }
}
```

Source: forms/next.mdx
