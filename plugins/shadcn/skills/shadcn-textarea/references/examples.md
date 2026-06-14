# Textarea — Examples

## Basic (textarea-demo.tsx)

```tsx
import { Textarea } from "@/registry/new-york-v4/ui/textarea"

export default function TextareaDemo() {
  return <Textarea placeholder="Type your message here." />
}
```

## Disabled (textarea-disabled.tsx)

```tsx
import { Textarea } from "@/registry/new-york-v4/ui/textarea"

export default function TextareaDisabled() {
  return <Textarea placeholder="Type your message here." disabled />
}
```

## With Button (textarea-with-button.tsx)

```tsx
import { Button } from "@/registry/new-york-v4/ui/button"
import { Textarea } from "@/registry/new-york-v4/ui/textarea"

export default function TextareaWithButton() {
  return (
    <div className="grid w-full gap-2">
      <Textarea placeholder="Type your message here." />
      <Button>Send message</Button>
    </div>
  )
}
```

## With Label (textarea-with-label.tsx)

```tsx
import { Label } from "@/registry/new-york-v4/ui/label"
import { Textarea } from "@/registry/new-york-v4/ui/textarea"

export default function TextareaWithLabel() {
  return (
    <div className="grid w-full gap-3">
      <Label htmlFor="message">Your message</Label>
      <Textarea placeholder="Type your message here." id="message" />
    </div>
  )
}
```

## With Label and Helper Text (textarea-with-text.tsx)

```tsx
import { Label } from "@/registry/new-york-v4/ui/label"
import { Textarea } from "@/registry/new-york-v4/ui/textarea"

export default function TextareaWithText() {
  return (
    <div className="grid w-full gap-3">
      <Label htmlFor="message-2">Your Message</Label>
      <Textarea placeholder="Type your message here." id="message-2" />
      <p className="text-sm text-muted-foreground">
        Your message will be copied to the support team.
      </p>
    </div>
  )
}
```

## With Field (label + description via Field components)

Use `Field`, `FieldLabel`, and `FieldDescription` from the shadcn `field` component
to compose a fully accessible labeled textarea with helper text.

```tsx
import { Field, FieldDescription, FieldLabel } from "@/components/ui/field"
import { Textarea } from "@/components/ui/textarea"

export default function TextareaWithField() {
  return (
    <Field>
      <FieldLabel>Bio</FieldLabel>
      <Textarea placeholder="Tell us about yourself." />
      <FieldDescription>A short bio displayed on your profile.</FieldDescription>
    </Field>
  )
}
```

## Invalid / Validation Error

Set `aria-invalid` on the `Textarea` to apply destructive (red) border and ring.
When used inside a `Field`, also set `data-invalid` on the `Field` to propagate
error styling to the label.

```tsx
import { Field, FieldLabel } from "@/components/ui/field"
import { Textarea } from "@/components/ui/textarea"

export default function TextareaInvalid() {
  return (
    <Field data-invalid>
      <FieldLabel>Message</FieldLabel>
      <Textarea aria-invalid placeholder="Type your message here." />
    </Field>
  )
}
```
