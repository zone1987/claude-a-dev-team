# Label — Examples

## Demo

Label paired with a Checkbox using `htmlFor` / `id`.

```tsx
import { Checkbox } from "@/components/ui/checkbox"
import { Label } from "@/components/ui/label"

export default function LabelDemo() {
  return (
    <div>
      <div className="flex items-center space-x-2">
        <Checkbox id="terms" />
        <Label htmlFor="terms">Accept terms and conditions</Label>
      </div>
    </div>
  )
}
```

## With Input

Standard label + input pairing.

```tsx
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"

export default function LabelInput() {
  return (
    <div className="grid w-full max-w-sm items-center gap-1.5">
      <Label htmlFor="email">Email</Label>
      <Input type="email" id="email" placeholder="Email" />
    </div>
  )
}
```

---
Source: `registry/new-york-v4/examples/label-demo.tsx`
