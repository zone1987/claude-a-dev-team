# Button — Examples

## Demo

```tsx
import { ArrowUpIcon } from "lucide-react"
import { Button } from "@/registry/new-york-v4/ui/button"

export default function ButtonDemo() {
  return (
    <div className="flex flex-wrap items-center gap-2 md:flex-row">
      <Button variant="outline">Button</Button>
      <Button variant="outline" size="icon" aria-label="Submit">
        <ArrowUpIcon />
      </Button>
    </div>
  )
}
```

## Default

```tsx
<Button>Button</Button>
```

## Outline

```tsx
<Button variant="outline">Outline</Button>
```

## Secondary

```tsx
<Button variant="secondary">Secondary</Button>
```

## Ghost

```tsx
<Button variant="ghost">Ghost</Button>
```

## Destructive

```tsx
<Button variant="destructive">Destructive</Button>
```

## Link

```tsx
<Button variant="link">Link</Button>
```

## Icon button

```tsx
import { CircleFadingArrowUpIcon } from "lucide-react"
<Button variant="outline" size="icon">
  <CircleFadingArrowUpIcon />
</Button>
```

## With icon

```tsx
import { IconGitBranch } from "@tabler/icons-react"
<Button variant="outline" size="sm">
  <IconGitBranch /> New Branch
</Button>
```

## Rounded

```tsx
import { ArrowUpIcon } from "lucide-react"
<Button variant="outline" size="icon" className="rounded-full">
  <ArrowUpIcon />
</Button>
```

## Loading / spinner

```tsx
import { Spinner } from "@/components/ui/spinner"
<Button size="sm" variant="outline" disabled>
  <Spinner />
  Submit
</Button>
```

## Sizes

```tsx
<Button size="sm" variant="outline">Small</Button>
<Button variant="outline">Default</Button>
<Button variant="outline" size="lg">Large</Button>
```

## As child (router link)

```tsx
import Link from "next/link"
<Button asChild>
  <Link href="/login">Login</Link>
</Button>
```

---
Sources:
- `/tmp/shadcn-repo/apps/v4/registry/new-york-v4/examples/button-demo.tsx`
- `/tmp/shadcn-repo/apps/v4/registry/new-york-v4/examples/button-default.tsx`
- `/tmp/shadcn-repo/apps/v4/registry/new-york-v4/examples/button-outline.tsx`
- `/tmp/shadcn-repo/apps/v4/registry/new-york-v4/examples/button-secondary.tsx`
- `/tmp/shadcn-repo/apps/v4/registry/new-york-v4/examples/button-ghost.tsx`
- `/tmp/shadcn-repo/apps/v4/registry/new-york-v4/examples/button-destructive.tsx`
- `/tmp/shadcn-repo/apps/v4/registry/new-york-v4/examples/button-link.tsx`
- `/tmp/shadcn-repo/apps/v4/registry/new-york-v4/examples/button-icon.tsx`
- `/tmp/shadcn-repo/apps/v4/registry/new-york-v4/examples/button-with-icon.tsx`
- `/tmp/shadcn-repo/apps/v4/registry/new-york-v4/examples/button-rounded.tsx`
- `/tmp/shadcn-repo/apps/v4/registry/new-york-v4/examples/button-loading.tsx`
- `/tmp/shadcn-repo/apps/v4/registry/new-york-v4/examples/button-size.tsx`
- `/tmp/shadcn-repo/apps/v4/registry/new-york-v4/examples/button-as-child.tsx`
