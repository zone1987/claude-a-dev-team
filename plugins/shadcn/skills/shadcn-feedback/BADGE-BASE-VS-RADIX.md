# Badge — Base UI vs Radix UI

## Render prop vs asChild

| | Radix UI | Base UI |
|---|---|---|
| Polymorphic | `asChild` boolean | `render` prop |
| Pattern | `<Badge asChild><a href="...">` | `<Badge render={<a href="..." />}>` |

## Style approach

| | Radix UI | Base UI |
|---|---|---|
| Variants | Inline Tailwind CVA classes | `cn-badge-variant-*` CSS tokens |
| Base classes | Full Tailwind string | Minimal `cn-badge` + tokens |

## Export

Both export `Badge` and `badgeVariants` identically.

---
Sources:
- `/tmp/shadcn-repo/apps/v4/registry/new-york-v4/ui/badge.tsx`
- `/tmp/shadcn-repo/apps/v4/registry/bases/base/ui/badge.tsx`
