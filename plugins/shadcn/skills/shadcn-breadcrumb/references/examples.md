# Breadcrumb — Examples

## Demo (with dropdown for collapsed items)

```tsx
import Link from "next/link"
import {
  Breadcrumb, BreadcrumbEllipsis, BreadcrumbItem, BreadcrumbLink,
  BreadcrumbList, BreadcrumbPage, BreadcrumbSeparator,
} from "@/registry/new-york-v4/ui/breadcrumb"
import {
  DropdownMenu, DropdownMenuContent, DropdownMenuItem, DropdownMenuTrigger,
} from "@/registry/new-york-v4/ui/dropdown-menu"

export default function BreadcrumbDemo() {
  return (
    <Breadcrumb>
      <BreadcrumbList>
        <BreadcrumbItem>
          <BreadcrumbLink asChild>
            <Link href="/">Home</Link>
          </BreadcrumbLink>
        </BreadcrumbItem>
        <BreadcrumbSeparator />
        <BreadcrumbItem>
          <DropdownMenu>
            <DropdownMenuTrigger className="flex items-center gap-1">
              <BreadcrumbEllipsis className="size-4" />
              <span className="sr-only">Toggle menu</span>
            </DropdownMenuTrigger>
            <DropdownMenuContent align="start">
              <DropdownMenuItem>Documentation</DropdownMenuItem>
              <DropdownMenuItem>Themes</DropdownMenuItem>
              <DropdownMenuItem>GitHub</DropdownMenuItem>
            </DropdownMenuContent>
          </DropdownMenu>
        </BreadcrumbItem>
        <BreadcrumbSeparator />
        <BreadcrumbItem>
          <BreadcrumbLink asChild>
            <Link href="/docs/components">Components</Link>
          </BreadcrumbLink>
        </BreadcrumbItem>
        <BreadcrumbSeparator />
        <BreadcrumbItem>
          <BreadcrumbPage>Breadcrumb</BreadcrumbPage>
        </BreadcrumbItem>
      </BreadcrumbList>
    </Breadcrumb>
  )
}
```

## With custom separator (slash)

```tsx
import { SlashIcon } from "lucide-react"

<Breadcrumb>
  <BreadcrumbList>
    <BreadcrumbItem>
      <BreadcrumbLink asChild><Link href="/">Home</Link></BreadcrumbLink>
    </BreadcrumbItem>
    <BreadcrumbSeparator>
      <SlashIcon />
    </BreadcrumbSeparator>
    <BreadcrumbItem>
      <BreadcrumbPage>Page</BreadcrumbPage>
    </BreadcrumbItem>
  </BreadcrumbList>
</Breadcrumb>
```

## Collapsed with ellipsis

```tsx
<BreadcrumbItem>
  <BreadcrumbEllipsis />
</BreadcrumbItem>
<BreadcrumbSeparator />
```

## With dropdown on a segment

```tsx
<BreadcrumbItem>
  <DropdownMenu>
    <DropdownMenuTrigger className="flex items-center gap-1">
      Components
      <ChevronDownIcon className="size-3.5" />
    </DropdownMenuTrigger>
    <DropdownMenuContent align="start">
      <DropdownMenuItem>Documentation</DropdownMenuItem>
      <DropdownMenuItem>GitHub</DropdownMenuItem>
    </DropdownMenuContent>
  </DropdownMenu>
</BreadcrumbItem>
```

---
Sources:
- `/tmp/shadcn-repo/apps/v4/registry/new-york-v4/examples/breadcrumb-demo.tsx`
- `/tmp/shadcn-repo/apps/v4/registry/new-york-v4/examples/breadcrumb-dropdown.tsx`
- `/tmp/shadcn-repo/apps/v4/registry/new-york-v4/examples/breadcrumb-ellipsis.tsx`
- `/tmp/shadcn-repo/apps/v4/registry/new-york-v4/examples/breadcrumb-link.tsx`
- `/tmp/shadcn-repo/apps/v4/registry/new-york-v4/examples/breadcrumb-separator.tsx`
