# Breadcrumb — Base UI vs Radix UI

## BreadcrumbLink

| | Radix UI | Base UI |
|---|---|---|
| Router link | `asChild` boolean | `render` prop |
| Example | `<BreadcrumbLink asChild><Link href="/" />` | `<BreadcrumbLink render={<Link href="/" />}>` |

## Separator icon

- Radix: `ChevronRight` from `lucide-react`
- Base: `IconPlaceholder` supporting multiple icon libraries

## Style approach

- Radix: Direct Tailwind classes
- Base: `cn-breadcrumb-*` CSS tokens

---
Sources:
- `/tmp/shadcn-repo/apps/v4/registry/new-york-v4/ui/breadcrumb.tsx`
- `/tmp/shadcn-repo/apps/v4/registry/bases/base/ui/breadcrumb.tsx`
