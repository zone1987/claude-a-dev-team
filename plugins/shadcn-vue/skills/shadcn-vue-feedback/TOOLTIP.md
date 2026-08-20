# shadcn-vue Tooltip

## Overview

The Tooltip component displays contextual information on hover or keyboard focus. It is built on reka-ui's Tooltip primitives and consists of four composable parts: `TooltipProvider` (app-level wrapper), `Tooltip` (root), `TooltipTrigger` (the element that activates the tooltip), and `TooltipContent` (the floating panel). `TooltipContent` is automatically rendered inside a `TooltipPortal` and includes an animated arrow.

## Architecture

```
TooltipProvider (wrap once at app level, delayDuration=0)
  Tooltip (open/closed state)
    TooltipTrigger (hover/focus target)
    TooltipContent (portal + arrow, side-aware animations)
```

## Animation

`TooltipContent` uses Tailwind's `animate-in / animate-out` with zoom + fade and directional slide based on `data-[side]`:

- `data-[side=top]`: `slide-in-from-bottom-2`
- `data-[side=bottom]`: `slide-in-from-top-2`
- `data-[side=left]`: `slide-in-from-right-2`
- `data-[side=right]`: `slide-in-from-left-2`

## Tooltip on disabled elements

Disabled HTML elements don't fire pointer events. Wrap the disabled element in a `<span>` to receive events:

```vue
<TooltipTrigger :as-child="true">
  <span class="inline-block">
    <Button disabled>Disabled</Button>
  </span>
</TooltipTrigger>
```

## References

- [TOOLTIP-INSTALLATION.md](TOOLTIP-INSTALLATION.md)
- [TOOLTIP-SOURCE.md](TOOLTIP-SOURCE.md)
- [TOOLTIP-API.md](TOOLTIP-API.md)
- [TOOLTIP-EXAMPLES.md](TOOLTIP-EXAMPLES.md)
