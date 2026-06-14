# Switch — Examples

## Basic demo

```tsx
import { Label } from "@/components/ui/label"
import { Switch } from "@/components/ui/switch"

export default function SwitchDemo() {
  return (
    <div className="flex items-center space-x-2">
      <Switch id="airplane-mode" />
      <Label htmlFor="airplane-mode">Airplane Mode</Label>
    </div>
  )
}
```

## Controlled

```tsx
"use client"

import * as React from "react"
import { Label } from "@/components/ui/label"
import { Switch } from "@/components/ui/switch"

export default function SwitchControlled() {
  const [checked, setChecked] = React.useState(false)

  return (
    <div className="flex items-center space-x-2">
      <Switch
        id="notifications"
        checked={checked}
        onCheckedChange={setChecked}
      />
      <Label htmlFor="notifications">Enable notifications</Label>
    </div>
  )
}
```

## With description (Field + FieldLabel + FieldDescription)

Wrap the switch inside a `Field` component to connect a label and description via `aria-describedby`.

```tsx
import { Field, FieldDescription, FieldLabel } from "@/components/ui/field"
import { Switch } from "@/components/ui/switch"

export default function SwitchWithDescription() {
  return (
    <Field className="flex items-center justify-between gap-4">
      <div className="space-y-1">
        <FieldLabel htmlFor="marketing-emails">Marketing emails</FieldLabel>
        <FieldDescription>
          Receive emails about new products, features, and more.
        </FieldDescription>
      </div>
      <Switch id="marketing-emails" />
    </Field>
  )
}
```

## Disabled

```tsx
import { Label } from "@/components/ui/label"
import { Switch } from "@/components/ui/switch"

export default function SwitchDisabled() {
  return (
    <div className="flex items-center space-x-2">
      <Switch id="disable-demo" disabled />
      <Label htmlFor="disable-demo" className="opacity-50">
        Disabled switch
      </Label>
    </div>
  )
}
```

## Invalid / error state

Use `aria-invalid` to communicate a validation error. Pair with a Field and error message.

```tsx
import { Field, FieldDescription, FieldLabel } from "@/components/ui/field"
import { Switch } from "@/components/ui/switch"

export default function SwitchInvalid() {
  return (
    <Field data-invalid className="flex items-start justify-between gap-4">
      <div className="space-y-1">
        <FieldLabel htmlFor="terms-switch">Accept terms</FieldLabel>
        <FieldDescription className="text-destructive">
          You must accept the terms to continue.
        </FieldDescription>
      </div>
      <Switch id="terms-switch" aria-invalid />
    </Field>
  )
}
```

## Sizes

```tsx
import { Label } from "@/components/ui/label"
import { Switch } from "@/components/ui/switch"

export default function SwitchSizes() {
  return (
    <div className="flex flex-col gap-4">
      <div className="flex items-center space-x-2">
        <Switch id="size-default" size="default" />
        <Label htmlFor="size-default">Default (1.15rem × 2rem)</Label>
      </div>
      <div className="flex items-center space-x-2">
        <Switch id="size-sm" size="sm" />
        <Label htmlFor="size-sm">Small (0.875rem × 1.5rem)</Label>
      </div>
    </div>
  )
}
```

## Choice card (Card-style toggle)

Wrap the switch in a card-like label so the entire card is clickable.

```tsx
import { Card } from "@/components/ui/card"
import { Field, FieldDescription, FieldLabel } from "@/components/ui/field"
import { Switch } from "@/components/ui/switch"

export default function SwitchChoiceCard() {
  return (
    <Card className="p-4">
      <Field className="flex items-center justify-between gap-4">
        <div className="space-y-1">
          <FieldLabel htmlFor="card-switch" className="text-base font-medium">
            Dark mode
          </FieldLabel>
          <FieldDescription>
            Switch between light and dark theme.
          </FieldDescription>
        </div>
        <Switch id="card-switch" />
      </Field>
    </Card>
  )
}
```

## RTL support

Set `dir="rtl"` on a wrapping element or use a direction context. The switch thumb translation is handled by CSS logical properties internally.

```tsx
import { Label } from "@/components/ui/label"
import { Switch } from "@/components/ui/switch"

export default function SwitchRTL() {
  return (
    <div dir="rtl" className="flex items-center space-x-2">
      <Label htmlFor="rtl-switch">وضع الطيران</Label>
      <Switch id="rtl-switch" />
    </div>
  )
}
```

## In a form

```tsx
"use client"

import * as React from "react"
import { Label } from "@/components/ui/label"
import { Switch } from "@/components/ui/switch"
import { Button } from "@/components/ui/button"

export default function SwitchForm() {
  function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault()
    const data = new FormData(e.currentTarget)
    console.log("marketing:", data.get("marketing"))
  }

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <div className="flex items-center space-x-2">
        <Switch id="marketing" name="marketing" value="yes" />
        <Label htmlFor="marketing">Receive marketing emails</Label>
      </div>
      <Button type="submit">Save preferences</Button>
    </form>
  )
}
```
