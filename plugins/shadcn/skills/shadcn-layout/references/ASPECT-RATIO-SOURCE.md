# Aspect Ratio — Component Source

## Radix UI version (`registry/new-york-v4/ui/aspect-ratio.tsx`)

```tsx
"use client"

import { AspectRatio as AspectRatioPrimitive } from "radix-ui"

function AspectRatio({
  ...props
}: React.ComponentProps<typeof AspectRatioPrimitive.Root>) {
  return <AspectRatioPrimitive.Root data-slot="aspect-ratio" {...props} />
}

export { AspectRatio }
```

## Base UI version (`registry/bases/base/ui/aspect-ratio.tsx`)

```tsx
import { cn } from "@/registry/bases/base/lib/utils"

function AspectRatio({
  ratio,
  className,
  ...props
}: React.ComponentProps<"div"> & { ratio: number }) {
  return (
    <div
      data-slot="aspect-ratio"
      style={
        {
          "--ratio": ratio,
        } as React.CSSProperties
      }
      className={cn("relative aspect-(--ratio)", className)}
      {...props}
    />
  )
}

export { AspectRatio }
```

---
Sources:
- `/tmp/shadcn-repo/apps/v4/registry/new-york-v4/ui/aspect-ratio.tsx`
- `/tmp/shadcn-repo/apps/v4/registry/bases/base/ui/aspect-ratio.tsx`
