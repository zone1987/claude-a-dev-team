---
name: shadcn-direction
description: >
  shadcn/ui Direction component — DirectionProvider and useDirection hook for RTL/LTR support.
  Triggers: "shadcn direction", "shadcn DirectionProvider", "shadcn RTL", "shadcn rtl support",
  "shadcn/ui right to left", "shadcn direction provider", "shadcn useDirection",
  "shadcn arabisch rtl", "rtl layout shadcn", "shadcn ltr rtl switching".
  Exports: DirectionProvider, useDirection.
---

# shadcn-direction

The `DirectionProvider` sets text direction (`ltr` or `rtl`) for shadcn/ui components. Wraps the Radix UI `Direction.DirectionProvider` (new-york-v4) or re-exports from `@base-ui/react/direction-provider` (Base UI). Essential for RTL languages (Arabic, Hebrew, Persian).

## Exports

- `DirectionProvider` — context provider, accepts `direction` or `dir` prop
- `useDirection` — hook to read the current direction in child components

## Quick start

```bash
npx shadcn@latest add direction
```

## References

- `references/installation.md` — CLI + manual install
- `references/source.md` — complete source code for both variants
- `references/api.md` — props and hook usage
