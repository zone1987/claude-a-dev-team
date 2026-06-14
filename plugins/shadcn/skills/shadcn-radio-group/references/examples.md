# RadioGroup — Examples

## Demo

Basic radio group with three options.

```tsx
import { Label } from "@/components/ui/label"
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group"

export default function RadioGroupDemo() {
  return (
    <RadioGroup defaultValue="comfortable">
      <div className="flex items-center gap-3">
        <RadioGroupItem value="default" id="r1" />
        <Label htmlFor="r1">Default</Label>
      </div>
      <div className="flex items-center gap-3">
        <RadioGroupItem value="comfortable" id="r2" />
        <Label htmlFor="r2">Comfortable</Label>
      </div>
      <div className="flex items-center gap-3">
        <RadioGroupItem value="compact" id="r3" />
        <Label htmlFor="r3">Compact</Label>
      </div>
    </RadioGroup>
  )
}
```

## With Description

Radio group items with a description using the `Field` component.

```tsx
import { Field, FieldDescription, FieldLabel } from "@/components/ui/field"
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group"

export default function RadioGroupDescription() {
  return (
    <RadioGroup defaultValue="comfortable" className="gap-4">
      <Field className="flex flex-row items-start gap-3">
        <RadioGroupItem value="default" id="desc-r1" className="mt-0.5" />
        <div>
          <FieldLabel htmlFor="desc-r1">Default</FieldLabel>
          <FieldDescription>Standard spacing for most use cases.</FieldDescription>
        </div>
      </Field>
      <Field className="flex flex-row items-start gap-3">
        <RadioGroupItem value="comfortable" id="desc-r2" className="mt-0.5" />
        <div>
          <FieldLabel htmlFor="desc-r2">Comfortable</FieldLabel>
          <FieldDescription>More padding for a relaxed layout.</FieldDescription>
        </div>
      </Field>
    </RadioGroup>
  )
}
```

## Choice Card

Full-clickable card style selection using `FieldLabel` wrapping the entire `Field`.

```tsx
import { Field, FieldLabel } from "@/components/ui/field"
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group"

export default function RadioGroupChoiceCard() {
  return (
    <RadioGroup defaultValue="starter" className="gap-3">
      {[
        { value: "starter", label: "Starter", description: "For individuals and small teams." },
        { value: "pro", label: "Pro", description: "For growing teams with more needs." },
        { value: "enterprise", label: "Enterprise", description: "For large organizations." },
      ].map((plan) => (
        <Field key={plan.value} className="flex cursor-pointer items-center gap-3 rounded-md border p-3">
          <FieldLabel className="flex w-full cursor-pointer items-center gap-3">
            <RadioGroupItem value={plan.value} id={`card-${plan.value}`} />
            <div>
              <div className="font-medium">{plan.label}</div>
              <div className="text-sm text-muted-foreground">{plan.description}</div>
            </div>
          </FieldLabel>
        </Field>
      ))}
    </RadioGroup>
  )
}
```

## Disabled

Use the `disabled` prop on `RadioGroup` to disable all items at once.

```tsx
import { Label } from "@/components/ui/label"
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group"

export default function RadioGroupDisabled() {
  return (
    <RadioGroup defaultValue="option-one" disabled>
      <div className="flex items-center gap-3">
        <RadioGroupItem value="option-one" id="dis-r1" />
        <Label htmlFor="dis-r1">Option One</Label>
      </div>
      <div className="flex items-center gap-3">
        <RadioGroupItem value="option-two" id="dis-r2" />
        <Label htmlFor="dis-r2">Option Two</Label>
      </div>
    </RadioGroup>
  )
}
```

## Invalid (validation error)

Use `aria-invalid` on `RadioGroupItem` to show destructive border/ring for validation errors.

```tsx
import { Label } from "@/components/ui/label"
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group"

export default function RadioGroupInvalid() {
  return (
    <RadioGroup>
      <div className="flex items-center gap-3">
        <RadioGroupItem value="option-one" id="inv-r1" aria-invalid="true" />
        <Label htmlFor="inv-r1">Option One</Label>
      </div>
      <div className="flex items-center gap-3">
        <RadioGroupItem value="option-two" id="inv-r2" aria-invalid="true" />
        <Label htmlFor="inv-r2">Option Two</Label>
      </div>
    </RadioGroup>
  )
}
```

---
Source: `registry/new-york-v4/examples/radio-group-demo.tsx`, `content/docs/components/base/radio-group.mdx`
