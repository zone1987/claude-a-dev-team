# Skeleton — Source Code

## new-york-v4 (production)

`registry/new-york-v4/ui/skeleton.tsx`

```tsx
import { cn } from "@/lib/utils"

function Skeleton({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="skeleton"
      className={cn("animate-pulse rounded-md bg-accent", className)}
      {...props}
    />
  )
}

export { Skeleton }
```

## Notes

- Pure Tailwind — no external primitive library
- Base and Radix variants are structurally identical (only `cn-skeleton` class prefix differs in base variant)
- Uses `animate-pulse` from Tailwind and `bg-accent` color token
- `rounded-md` is the default — override with `rounded-full` for circles

## Source files

- `registry/new-york-v4/ui/skeleton.tsx`
