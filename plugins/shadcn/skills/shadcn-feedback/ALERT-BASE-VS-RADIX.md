# Alert — Base UI vs Radix UI

## Key differences

| | Radix UI | Base UI |
|---|---|---|
| `AlertAction` | Not in default export | Exported, absolute positioned in corner |
| Layout | CSS grid `grid-cols-[0_1fr]` with icon col | `cn-alert-*` CSS tokens |
| Variants | Inline Tailwind classes | `cn-alert-variant-*` CSS tokens |
| Icon sizing | `[&>svg]:size-4` | Theme-controlled via CSS |

## AlertAction (Base UI only in default registry)

The Radix version of `alert.tsx` does not export `AlertAction`. If you need
an action button inside an alert using Radix, add it manually or import from
the Base UI version.

## Style customization

Radix version: override directly with `className`.

Base version: uses `cn-alert-*` CSS custom tokens that map to theme
variables, allowing theme-level customization without component changes.

---
Sources:
- `/tmp/shadcn-repo/apps/v4/registry/new-york-v4/ui/alert.tsx`
- `/tmp/shadcn-repo/apps/v4/registry/bases/base/ui/alert.tsx`
