---
name: shadcn-vue-separator
description: >
  shadcn-vue Separator component (reka-ui Separator, horizontal/vertical, Tailwind v4 Vue SFC).
  Triggers: "shadcn-vue separator", "trennlinie vue", "separator component vue",
  "divider vue", "horizontal divider vue", "reka-ui separator shadcn"
---

# shadcn-vue Separator

A thin visual divider built on reka-ui's Separator primitive, supporting horizontal and vertical orientations.

## References

- [installation.md](references/installation.md) — CLI and manual install
- [source.md](references/source.md) — Full component source (Separator.vue, index.ts)
- [api.md](references/api.md) — Props and reka-ui API link
- [examples.md](references/examples.md) — Horizontal, vertical, vertical menu, in-list examples

## Key Facts

- Single component `Separator.vue` wrapping reka-ui's `Separator`
- Default orientation is `horizontal`; pass `orientation="vertical"` for vertical use
- Default `decorative` is `true` (hidden from the accessibility tree via `role="none"`)
- Set `decorative="false"` when the separator conveys semantic meaning (`role="separator"`)
- Uses `data-[orientation=horizontal]` and `data-[orientation=vertical]` Tailwind variants
- Tailwind v4 utility classes; no extra CSS required
