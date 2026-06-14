# Avatar — Base UI vs Radix UI

## Dependency

| | Radix UI | Base UI |
|---|---|---|
| Package | `radix-ui` | `@base-ui/react` |
| Import | `from "radix-ui"` | `from "@base-ui/react/avatar"` |

## Component type differences

| | Radix UI | Base UI |
|---|---|---|
| Root props | `React.ComponentProps<AvatarPrimitive.Root>` | `AvatarPrimitive.Root.Props` |
| Image props | `AvatarPrimitive.Image` | `AvatarPrimitive.Image.Props` |
| Fallback props | `AvatarPrimitive.Fallback` | `AvatarPrimitive.Fallback.Props` |

## Style differences

- Radix: `overflow-hidden rounded-full` sizing via data-size
- Base: `cn-avatar-*` tokens + `after:` pseudo-element border overlay with
  `mix-blend-darken/lighten` for dark mode

## AvatarGroupCount size inheritance

Both use container query pattern via group selectors, but Base uses
`cn-avatar-group-count` CSS tokens vs direct Tailwind in Radix version.

---
Sources:
- `/tmp/shadcn-repo/apps/v4/registry/new-york-v4/ui/avatar.tsx`
- `/tmp/shadcn-repo/apps/v4/registry/bases/base/ui/avatar.tsx`
