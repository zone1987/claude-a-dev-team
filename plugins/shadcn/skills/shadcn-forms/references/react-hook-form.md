# React Hook Form + shadcn Field Components

## Setup

```bash
npm install react-hook-form @hookform/resolvers zod
```

## Full form pattern

```tsx
import { zodResolver } from "@hookform/resolvers/zod"
import { useForm, Controller } from "react-hook-form"
import * as z from "zod"

const formSchema = z.object({
  title: z.string().min(5).max(32),
  description: z.string().min(20).max(100),
})

export function BugReportForm() {
  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
    defaultValues: { title: "", description: "" },
  })

  function onSubmit(data: z.infer<typeof formSchema>) {
    console.log(data)
  }

  return (
    <form onSubmit={form.handleSubmit(onSubmit)}>
      <Controller
        name="title"
        control={form.control}
        render={({ field, fieldState }) => (
          <Field data-invalid={fieldState.invalid}>
            <FieldLabel htmlFor={field.name}>Bug Title</FieldLabel>
            <Input
              {...field}
              id={field.name}
              aria-invalid={fieldState.invalid}
            />
            <FieldDescription>Concise title for your bug report.</FieldDescription>
            {fieldState.invalid && <FieldError errors={[fieldState.error]} />}
          </Field>
        )}
      />
      <Button type="submit">Submit</Button>
    </form>
  )
}
```

## Validation modes

```tsx
const form = useForm({
  resolver: zodResolver(formSchema),
  mode: "onChange", // "onChange" | "onBlur" | "onSubmit" | "onTouched" | "all"
})
```

## Error display pattern

```tsx
<Field data-invalid={fieldState.invalid}>
  <Input {...field} aria-invalid={fieldState.invalid} />
  {fieldState.invalid && <FieldError errors={[fieldState.error]} />}
</Field>
```

Always set BOTH `data-invalid` on `<Field>` AND `aria-invalid` on the control.

## Field types

### Textarea

```tsx
<Textarea {...field} id={field.name} aria-invalid={fieldState.invalid} />
```

### Select

```tsx
<Select name={field.name} value={field.value} onValueChange={field.onChange}>
  <SelectTrigger id={field.name} aria-invalid={fieldState.invalid}>
    <SelectValue placeholder="Select" />
  </SelectTrigger>
  <SelectContent>...</SelectContent>
</Select>
```

### Checkbox (array)

```tsx
<Checkbox
  checked={field.value.includes(item.id)}
  onCheckedChange={(checked) => {
    const newValue = checked
      ? [...field.value, item.id]
      : field.value.filter((v) => v !== item.id)
    field.onChange(newValue)
  }}
  aria-invalid={fieldState.invalid}
/>
```

Add `data-slot="checkbox-group"` to `<FieldGroup>` for spacing.

### Radio group

```tsx
<RadioGroup name={field.name} value={field.value} onValueChange={field.onChange}>
  <RadioGroupItem value={item.id} aria-invalid={fieldState.invalid} />
</RadioGroup>
```

### Switch

```tsx
<Switch
  name={field.name}
  checked={field.value}
  onCheckedChange={field.onChange}
  aria-invalid={fieldState.invalid}
/>
```

## Array fields (useFieldArray)

```tsx
import { useFieldArray } from "react-hook-form"

const { fields, append, remove } = useFieldArray({
  control: form.control,
  name: "emails",
})

// Add item
append({ address: "" })

// Remove item
remove(index)

// Render — always use field.id as key
fields.map((field, index) => (
  <Controller
    key={field.id}
    name={`emails.${index}.address`}
    control={form.control}
    render={({ field: controllerField, fieldState }) => (
      <Input {...controllerField} aria-invalid={fieldState.invalid} />
    )}
  />
))
```

## Form reset

```tsx
<Button type="button" onClick={() => form.reset()}>Reset</Button>
```

Source: forms/react-hook-form.mdx
