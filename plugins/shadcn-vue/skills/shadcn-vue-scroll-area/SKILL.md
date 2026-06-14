---
name: shadcn-vue-scroll-area
description: >
  shadcn-vue ScrollArea component (reka-ui ScrollAreaRoot, custom scrollbar, Tailwind v4 Vue SFC).
  Triggers: "shadcn-vue scroll area", "scroll area vue", "scrollbereich vue",
  "custom scrollbar vue", "scroll area reka-ui", "scrollable container vue shadcn"
---

# shadcn-vue ScrollArea

A custom scrollable container built on reka-ui's ScrollArea primitives with a styled scrollbar overlay.

## References

- [installation.md](references/installation.md) — CLI and manual install
- [source.md](references/source.md) — Full component source (ScrollArea.vue, ScrollBar.vue, index.ts)
- [api.md](references/api.md) — Props and reka-ui API links
- [examples.md](references/examples.md) — Vertical and horizontal scroll examples

## Key Facts

- Built on `reka-ui` ScrollAreaRoot / ScrollAreaViewport / ScrollAreaScrollbar / ScrollAreaThumb
- Two files: `ScrollArea.vue` (root + viewport) and `ScrollBar.vue` (scrollbar + thumb)
- Default scrollbar orientation is `vertical`; pass `orientation="horizontal"` plus `<ScrollBar orientation="horizontal" />` for horizontal scroll
- Uses `reactiveOmit` from `@vueuse/core` to forward props cleanly
- Tailwind v4 utility classes; no extra CSS required
