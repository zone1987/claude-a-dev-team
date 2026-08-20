# shadcn-vue ScrollArea

A custom scrollable container built on reka-ui's ScrollArea primitives with a styled scrollbar overlay.

## References

- [installation.md](`SCROLL-AREA-INSTALLATION.md`) — CLI and manual install
- [source.md](`SCROLL-AREA-SOURCE.md`) — Full component source (ScrollArea.vue, ScrollBar.vue, index.ts)
- [api.md](`SCROLL-AREA-API.md`) — Props and reka-ui API links
- [examples.md](`SCROLL-AREA-EXAMPLES.md`) — Vertical and horizontal scroll examples

## Key Facts

- Built on `reka-ui` ScrollAreaRoot / ScrollAreaViewport / ScrollAreaScrollbar / ScrollAreaThumb
- Two files: `ScrollArea.vue` (root + viewport) and `ScrollBar.vue` (scrollbar + thumb)
- Default scrollbar orientation is `vertical`; pass `orientation="horizontal"` plus `<ScrollBar orientation="horizontal" />` for horizontal scroll
- Uses `reactiveOmit` from `@vueuse/core` to forward props cleanly
- Tailwind v4 utility classes; no extra CSS required
