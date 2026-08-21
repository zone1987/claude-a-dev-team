# Button Group — Base UI vs Radix UI

## ButtonGroupText

| | Radix UI | Base UI |
|---|---|---|
| Polymorphic | `asChild` boolean (`Slot.Root`) | `render` prop (`useRender`) |
| Label example | `<ButtonGroupText asChild><Label htmlFor="x">` | `<ButtonGroupText render={<Label htmlFor="x" />}>` |

## CVA selectors

Radix version targets `:not(:first-child)` / `:not(:last-child)`. Base
version uses `*:data-slot:rounded-r-none` and sibling selector approach.

## Style approach

- Radix: Inline Tailwind CVA
- Base: `cn-button-group-*` CSS tokens

Both export `ButtonGroup`, `ButtonGroupSeparator`, `ButtonGroupText`,
and `buttonGroupVariants`.

---
Sources:
- `/tmp/shadcn-repo/apps/v4/registry/new-york-v4/ui/button-group.tsx`
- `/tmp/shadcn-repo/apps/v4/registry/bases/base/ui/button-group.tsx`
