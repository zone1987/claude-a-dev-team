# Tooltip — new-york-v4 vs Radix base

Both variants expose the same four components (`Tooltip`, `TooltipTrigger`,
`TooltipContent`, `TooltipProvider`) with identical structure and `data-slot`
attributes. Both render `TooltipContent` into a Portal. The difference is purely
in styling responsibility.

## TooltipContent className

| Aspect | new-york-v4 | radix base |
|--------|-------------|------------|
| Animations | Full Tailwind animate-in/out (`animate-in`, `fade-in-0`, `zoom-in-95`, directional `slide-in-from-*`, `data-[state=closed]:animate-out`, `data-[state=closed]:fade-out-0`, `data-[state=closed]:zoom-out-95`) | None — left to design system |
| Shape | `rounded-md px-3 py-1.5 text-xs` | No shape classes |
| Text | `text-balance` included | Not included |
| Max width | No explicit max-width | `max-w-xs` |
| Marker classes | None | `cn-tooltip-content` (hook for design system CSS) |

## Arrow className

| Aspect | new-york-v4 | radix base |
|--------|-------------|------------|
| Size | `size-2.5` | No explicit size |
| Shape | `rotate-45 rounded-[2px]` | No shape |
| Marker class | None | `cn-tooltip-arrow` (hook for design system CSS) |

## Summary

- Use **new-york-v4** for projects that rely on Tailwind utility classes for all
  component styling. The component is self-contained and requires no additional CSS.
- Use **radix base** when your design system provides its own CSS (e.g. via
  `.cn-tooltip-content` and `.cn-tooltip-arrow` selectors). The base variant
  intentionally carries minimal Tailwind classes so the design system retains full
  control over appearance and animation.
