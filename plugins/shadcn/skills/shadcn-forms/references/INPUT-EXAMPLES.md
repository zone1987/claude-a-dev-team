# Input — Examples

## Example 1 — Demo (Basic)

```tsx
import { Input } from "@/registry/new-york-v4/ui/input"

export default function InputDemo() {
  return <Input type="email" placeholder="Email" />
}
```

## Example 2 — With Label

```tsx
import { Input } from "@/registry/new-york-v4/ui/input"
import { Label } from "@/registry/new-york-v4/ui/label"

export default function InputWithLabel() {
  return (
    <div className="grid w-full max-w-sm items-center gap-3">
      <Label htmlFor="email">Email</Label>
      <Input type="email" id="email" placeholder="Email" />
    </div>
  )
}
```

## Example 3 — With Helper Text

```tsx
import { Input } from "@/registry/new-york-v4/ui/input"
import { Label } from "@/registry/new-york-v4/ui/label"

export default function InputWithText() {
  return (
    <div className="grid w-full max-w-sm items-center gap-3">
      <Label htmlFor="email-2">Email</Label>
      <Input type="email" id="email-2" placeholder="Email" />
      <p className="text-sm text-muted-foreground">Enter your email address.</p>
    </div>
  )
}
```

## Example 4 — With Button

```tsx
import { Button } from "@/registry/new-york-v4/ui/button"
import { Input } from "@/registry/new-york-v4/ui/input"

export default function InputWithButton() {
  return (
    <div className="flex w-full max-w-sm items-center gap-2">
      <Input type="email" placeholder="Email" />
      <Button type="submit" variant="outline">
        Subscribe
      </Button>
    </div>
  )
}
```

## Example 5 — File Input

```tsx
import { Input } from "@/registry/new-york-v4/ui/input"
import { Label } from "@/registry/new-york-v4/ui/label"

export default function InputFile() {
  return (
    <div className="grid w-full max-w-sm items-center gap-3">
      <Label htmlFor="picture">Picture</Label>
      <Input id="picture" type="file" />
    </div>
  )
}
```

## Example 6 — Disabled

```tsx
import { Input } from "@/registry/new-york-v4/ui/input"

export default function InputDisabled() {
  return <Input disabled type="email" placeholder="Email" />
}
```

---

_Source: `apps/v4/registry/new-york-v4/examples/input-demo.tsx`, `apps/v4/registry/new-york-v4/examples/input-with-label.tsx`, `apps/v4/registry/new-york-v4/examples/input-with-text.tsx`, `apps/v4/registry/new-york-v4/examples/input-with-button.tsx`, `apps/v4/registry/new-york-v4/examples/input-file.tsx`, `apps/v4/registry/new-york-v4/examples/input-disabled.tsx`_
