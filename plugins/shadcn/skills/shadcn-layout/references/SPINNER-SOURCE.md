# Spinner — Source Code

## new-york-v4 (production)

`registry/new-york-v4/ui/spinner.tsx`

```tsx
import { Loader2Icon } from "lucide-react"

import { cn } from "@/lib/utils"

function Spinner({ className, ...props }: React.ComponentProps<"svg">) {
  return (
    <Loader2Icon
      role="status"
      aria-label="Loading"
      className={cn("size-4 animate-spin", className)}
      {...props}
    />
  )
}

export { Spinner }
```

## Custom variant (from docs)

Replace `Loader2Icon` with any icon:

```tsx
import { LoaderIcon } from "lucide-react"

import { cn } from "@/lib/utils"

function Spinner({ className, ...props }: React.ComponentProps<"svg">) {
  return (
    <LoaderIcon
      role="status"
      aria-label="Loading"
      className={cn("size-4 animate-spin", className)}
      {...props}
    />
  )
}

export { Spinner }
```

## Notes

- No external dependency (uses lucide-react which is already a shadcn/ui dep)
- Pure `animate-spin` Tailwind animation
- `role="status"` and `aria-label="Loading"` for accessibility
- Default size `size-4` (1rem) — override with `size-*` classes

## Source files

- `registry/new-york-v4/ui/spinner.tsx`
- `registry/new-york-v4/examples/spinner-custom.tsx`
