# TanStack Form + shadcn Field Components

## Setup

```bash
npm install @tanstack/react-form zod
```

## Full form pattern

```tsx
import { useForm } from "@tanstack/react-form"
import * as z from "zod"

const formSchema = z.object({
  title: z.string().min(5).max(32),
  description: z.string().min(20).max(100),
})

export function BugReportForm() {
  const form = useForm({
    defaultValues: { title: "", description: "" },
    validators: { onSubmit: formSchema },
    onSubmit: async ({ value }) => {
      console.log(value)
    },
  })

  return (
    <form onSubmit={(e) => { e.preventDefault(); form.handleSubmit() }}>
      <form.Field
        name="title"
        children={(field) => {
          const isInvalid = field.state.meta.isTouched && !field.state.meta.isValid
          return (
            <Field data-invalid={isInvalid}>
              <FieldLabel htmlFor={field.name}>Bug Title</FieldLabel>
              <Input
                id={field.name}
                name={field.name}
                value={field.state.value}
                onBlur={field.handleBlur}
                onChange={(e) => field.handleChange(e.target.value)}
                aria-invalid={isInvalid}
              />
              {isInvalid && <FieldError errors={field.state.meta.errors} />}
            </Field>
          )
        }}
      />
      <Button type="submit">Submit</Button>
    </form>
  )
}
```

## isInvalid pattern

```tsx
const isInvalid = field.state.meta.isTouched && !field.state.meta.isValid
```

## Validation modes

```tsx
const form = useForm({
  validators: {
    onSubmit: formSchema,     // validate on submit
    onChange: formSchema,     // validate on every change
    onBlur: formSchema,       // validate on blur
  },
})
```

## Field types

### Input

```tsx
<Input
  name={field.name}
  value={field.state.value}
  onBlur={field.handleBlur}
  onChange={(e) => field.handleChange(e.target.value)}
  aria-invalid={isInvalid}
/>
```

### Textarea

```tsx
<Textarea
  name={field.name}
  value={field.state.value}
  onBlur={field.handleBlur}
  onChange={(e) => field.handleChange(e.target.value)}
  aria-invalid={isInvalid}
/>
```

### Select

```tsx
<Select name={field.name} value={field.state.value} onValueChange={field.handleChange}>
  <SelectTrigger aria-invalid={isInvalid}>
    <SelectValue placeholder="Select" />
  </SelectTrigger>
  <SelectContent>...</SelectContent>
</Select>
```

### Checkbox array (mode="array")

```tsx
<form.Field name="tasks" mode="array" children={(field) => (
  <FieldGroup data-slot="checkbox-group">
    {tasks.map((task) => (
      <Checkbox
        key={task.id}
        checked={field.state.value.includes(task.id)}
        onCheckedChange={(checked) => {
          if (checked) {
            field.pushValue(task.id)
          } else {
            const index = field.state.value.indexOf(task.id)
            if (index > -1) field.removeValue(index)
          }
        }}
        aria-invalid={isInvalid}
      />
    ))}
  </FieldGroup>
)} />
```

### Switch

```tsx
<Switch
  name={field.name}
  checked={field.state.value}
  onCheckedChange={field.handleChange}
  aria-invalid={isInvalid}
/>
```

## Array fields (mode="array")

```tsx
<form.Field name="emails" mode="array" children={(field) => (
  <>
    {field.state.value.map((_, index) => (
      <form.Field
        key={index}
        name={`emails[${index}].address`}
        children={(subField) => {
          const isSubInvalid =
            subField.state.meta.isTouched && !subField.state.meta.isValid
          return (
            <Input
              value={subField.state.value}
              onBlur={subField.handleBlur}
              onChange={(e) => subField.handleChange(e.target.value)}
              aria-invalid={isSubInvalid}
            />
          )
        }}
      />
    ))}
    <Button onClick={() => field.pushValue({ address: "" })}>Add</Button>
  </>
)} />
```

- `field.pushValue(item)` — append item
- `field.removeValue(index)` — remove item at index

## Form reset

```tsx
<Button type="button" onClick={() => form.reset()}>Reset</Button>
```

Source: forms/tanstack-form.mdx
