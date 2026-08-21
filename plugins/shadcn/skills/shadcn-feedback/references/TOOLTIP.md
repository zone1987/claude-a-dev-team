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

- [TOOLTIP-INSTALLATION.md](TOOLTIP-INSTALLATION.md) — CLI & manual setup incl. Provider setup
- [TOOLTIP-SOURCE.md](TOOLTIP-SOURCE.md) — Complete component source (new-york-v4 + radix base)
- [TOOLTIP-API.md](TOOLTIP-API.md) — Props tables
- [TOOLTIP-EXAMPLES.md](TOOLTIP-EXAMPLES.md) — All examples
- [TOOLTIP-BASE-VS-RADIX.md](TOOLTIP-BASE-VS-RADIX.md) — Styled vs base differences
