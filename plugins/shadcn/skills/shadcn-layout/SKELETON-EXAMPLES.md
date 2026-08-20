# Skeleton — Examples

## Demo (avatar + text lines)

`registry/new-york-v4/examples/skeleton-demo.tsx`

```tsx
import { Skeleton } from "@/registry/new-york-v4/ui/skeleton"

export default function SkeletonDemo() {
  return (
    <div className="flex items-center space-x-4">
      <Skeleton className="h-12 w-12 rounded-full" />
      <div className="space-y-2">
        <Skeleton className="h-4 w-[250px]" />
        <Skeleton className="h-4 w-[200px]" />
      </div>
    </div>
  )
}
```

## Card

`registry/new-york-v4/examples/skeleton-card.tsx`

```tsx
import { Skeleton } from "@/registry/new-york-v4/ui/skeleton"

export default function SkeletonCard() {
  return (
    <div className="flex flex-col space-y-3">
      <Skeleton className="h-[125px] w-[250px] rounded-xl" />
      <div className="space-y-2">
        <Skeleton className="h-4 w-[250px]" />
        <Skeleton className="h-4 w-[200px]" />
      </div>
    </div>
  )
}
```

## Source files

- `registry/new-york-v4/examples/skeleton-demo.tsx`
- `registry/new-york-v4/examples/skeleton-card.tsx`
