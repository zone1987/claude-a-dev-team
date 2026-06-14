---
name: shadcn-tooltip
description: >
  shadcn/ui Tooltip component — popup information on hover/focus, TooltipProvider,
  TooltipTrigger, TooltipContent, side position, disabled button tooltip, Tooltip,
  Werkzeughinweis, Hinweisbox, shadcn tooltip, radix tooltip, hover card popup
---

# shadcn/ui Tooltip

A popup that displays information related to an element when the element receives
keyboard focus or the mouse hovers over it. Built on Radix UI Tooltip primitive.
Requires `TooltipProvider` in the app root.

## Quick Reference

- **Install**: `npx shadcn@latest add tooltip`
- **Radix deps**: `radix-ui`
- **Exports**: `Tooltip`, `TooltipTrigger`, `TooltipContent`, `TooltipProvider`
- **Setup**: Add `<TooltipProvider>` to root layout
- **Default delay**: `delayDuration={0}` (no delay)

## Composition

```text
Tooltip
├── TooltipTrigger
└── TooltipContent
```

## Reference files

- [installation.md](references/installation.md) — CLI & manual setup incl. Provider setup
- [source.md](references/source.md) — Complete component source (new-york-v4 + radix base)
- [api.md](references/api.md) — Props tables
- [examples.md](references/examples.md) — All examples
- [base-vs-radix.md](references/base-vs-radix.md) — Styled vs base differences
