# Badge — Examples

## Demo

```tsx
import { AlertCircleIcon, BadgeCheckIcon, CheckIcon } from "lucide-react"
import { Badge } from "@/registry/new-york-v4/ui/badge"

export default function BadgeDemo() {
  return (
    <div className="flex flex-col items-center gap-2">
      <div className="flex w-full flex-wrap gap-2">
        <Badge>Badge</Badge>
        <Badge variant="secondary">Secondary</Badge>
        <Badge variant="destructive">Destructive</Badge>
        <Badge variant="outline">Outline</Badge>
      </div>
      <div className="flex w-full flex-wrap gap-2">
        <Badge
          variant="secondary"
          className="bg-blue-500 text-white dark:bg-blue-600"
        >
          <BadgeCheckIcon />
          Verified
        </Badge>
        <Badge className="h-5 min-w-5 rounded-full px-1 font-mono tabular-nums">
          8
        </Badge>
        <Badge
          className="h-5 min-w-5 rounded-full px-1 font-mono tabular-nums"
          variant="destructive"
        >
          99
        </Badge>
        <Badge
          className="h-5 min-w-5 rounded-full px-1 font-mono tabular-nums"
          variant="outline"
        >
          20+
        </Badge>
      </div>
    </div>
  )
}
```

## Destructive

```tsx
import { Badge } from "@/components/ui/badge"
<Badge variant="destructive">Destructive</Badge>
```

## Outline

```tsx
<Badge variant="outline">Outline</Badge>
```

## Secondary

```tsx
<Badge variant="secondary">Secondary</Badge>
```

## Notification count (pill)

```tsx
<Badge className="h-5 min-w-5 rounded-full px-1 font-mono tabular-nums">
  99
</Badge>
```

## As a link (asChild)

```tsx
<Badge asChild>
  <a href="/docs">Documentation</a>
</Badge>
```

---
Sources:
- `/tmp/shadcn-repo/apps/v4/registry/new-york-v4/examples/badge-demo.tsx`
- `/tmp/shadcn-repo/apps/v4/registry/new-york-v4/examples/badge-destructive.tsx`
- `/tmp/shadcn-repo/apps/v4/registry/new-york-v4/examples/badge-outline.tsx`
- `/tmp/shadcn-repo/apps/v4/registry/new-york-v4/examples/badge-secondary.tsx`
