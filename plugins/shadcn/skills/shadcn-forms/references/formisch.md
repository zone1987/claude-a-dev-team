# Formisch + shadcn Field Components

## Setup

```bash
npm install @formisch/react valibot
```

## Full form pattern

```tsx
import { Form, Field as FormischField, useForm } from "@formisch/react"
import type { SubmitHandler } from "@formisch/react"
import * as v from "valibot"

const FormSchema = v.object({
  title: v.pipe(v.string(), v.minLength(5), v.maxLength(32)),
  description: v.pipe(v.string(), v.minLength(20), v.maxLength(100)),
})

export function BugReportForm() {
  const form = useForm({
    schema: FormSchema,
    initialInput: { title: "", description: "" },
  })

  const handleSubmit: SubmitHandler<typeof FormSchema> = (output) => {
    console.log(output)
  }

  return (
    <Form of={form} onSubmit={handleSubmit}>
      <FormischField of={form} path={["title"]}>
        {(field) => (
          <Field data-invalid={field.errors !== null}>
            <FieldLabel htmlFor="form-title">Bug Title</FieldLabel>
            <Input
              {...field.props}
              id="form-title"
              value={field.input}
              aria-invalid={field.errors !== null}
            />
            {field.errors && (
              <FieldError errors={field.errors.map((message) => ({ message }))} />
            )}
          </Field>
        )}
      </FormischField>
      <Button type="submit">Submit</Button>
    </Form>
  )
}
```

NOTE: Import Formisch `Field` as `FormischField` to avoid name clash with
shadcn `Field`.

## Error display pattern

```tsx
{field.errors && (
  <FieldError errors={field.errors.map((message) => ({ message }))} />
)}
```

`field.errors` is `string[] | null`. Must be mapped to `{ message }` objects.

## Validation modes

```tsx
const form = useForm({
  schema: FormSchema,
  validate: "blur",      // "submit" | "blur" | "input" | "initial"
  revalidate: "input",   // "input" | "blur" | "submit"
})
```

## Binding to controls

- **Native inputs** (`<Input>`, `<Textarea>`): spread `field.props` + `value={field.input}`
- **Component controls** (`<Select>`, `<Checkbox>`, etc.): read `field.input`, call `field.onChange(value)`

## Field types

### Input / Textarea

```tsx
<Input {...field.props} id="..." value={field.input} aria-invalid={field.errors !== null} />
```

### Select

```tsx
<Select value={field.input} onValueChange={field.onChange}>
  <SelectTrigger aria-invalid={field.errors !== null}>...</SelectTrigger>
</Select>
```

### Checkbox array

```tsx
<Checkbox
  checked={field.input?.includes(task.id) ?? false}
  onCheckedChange={(checked) => {
    const current = field.input ?? []
    field.onChange(
      checked === true
        ? [...current, task.id]
        : current.filter((v) => v !== task.id)
    )
  }}
  aria-invalid={field.errors !== null}
/>
```

### Switch

```tsx
<Switch
  checked={field.input ?? false}
  onCheckedChange={field.onChange}
  aria-invalid={field.errors !== null}
/>
```

## Array fields (FieldArray)

```tsx
import { FieldArray, insert, remove } from "@formisch/react"

<FieldArray of={form} path={["emails"]}>
  {(fieldArray) => (
    <>
      {fieldArray.items.map((item, index) => (
        <FormischField key={item} of={form} path={["emails", index, "address"]}>
          {(field) => <Input {...field.props} value={field.input} />}
        </FormischField>
      ))}
      <Button onClick={() =>
        insert(form, { path: ["emails"], initialInput: { address: "" } })
      }>
        Add
      </Button>
    </>
  )}
</FieldArray>
```

- `insert(form, { path, initialInput, at? })` — append or insert at index
- `remove(form, { path, at })` — remove at index
- `move(form, { path, from, to })` — reorder
- `swap(form, { path, from, to })` — swap two items

## Form reset

```tsx
import { reset } from "@formisch/react"

// Reset to initial values
reset(form)

// Reset to new values but keep edits
reset(form, { initialInput: serverData, keepInput: true })
```

## Top-level API shape

All methods: first param = form store, second = config.

```ts
getInput(form, { path: ["email"] })
setInput(form, { path: ["email"], value: "..." })
getErrors(form, { path: ["email"] })
submit(form)
validate(form)
focus(form, { path: ["email"] })
```

Source: forms/formisch.mdx
