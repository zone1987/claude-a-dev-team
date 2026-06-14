# Label — Base vs Radix

Both variants export the same `Label` component and API. The only difference is the underlying primitive.

## Radix variant (default `new-york-v4`)

Uses `@radix-ui/react-label` via the `radix-ui` umbrella package. This provides the same accessibility semantics as the native `<label>` plus some additional handling via Radix.

```tsx
import { Label as LabelPrimitive } from "radix-ui"

function Label({ className, ...props }: React.ComponentProps<typeof LabelPrimitive.Root>) {
  return (
    <LabelPrimitive.Root
      data-slot="label"
      className={cn(
        "flex items-center gap-2 text-sm leading-none font-medium select-none group-data-[disabled=true]:pointer-events-none group-data-[disabled=true]:opacity-50 peer-disabled:cursor-not-allowed peer-disabled:opacity-50",
        className
      )}
      {...props}
    />
  )
}
```

## Base UI variant

Uses `@base-ui/react` Label primitive. Structurally identical but without the Radix dependency.

```tsx
import * as React from "react"
import { cn } from "@/lib/utils"

function Label({ className, ...props }: React.ComponentProps<"label">) {
  return (
    <label
      data-slot="label"
      className={cn(
        "cn-label flex items-center select-none group-data-[disabled=true]:pointer-events-none peer-disabled:cursor-not-allowed",
        className
      )}
      {...props}
    />
  )
}
```

**Choose Radix** if you use other Radix primitives in your project.
**Choose Base UI** if you use `@base-ui/react` throughout.

---
Source: `registry/bases/base/ui/label.tsx`, `registry/bases/radix/ui/label.tsx`
