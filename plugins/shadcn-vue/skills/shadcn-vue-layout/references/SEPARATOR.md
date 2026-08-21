# shadcn-vue Separator

A thin visual divider built on reka-ui's Separator primitive, supporting horizontal and vertical orientations.

## References

- [SEPARATOR-INSTALLATION.md](SEPARATOR-INSTALLATION.md) — CLI and manual install
- [SEPARATOR-SOURCE.md](SEPARATOR-SOURCE.md) — Full component source (Separator.vue, index.ts)
- [SEPARATOR-API.md](SEPARATOR-API.md) — Props and reka-ui API link
- [SEPARATOR-EXAMPLES.md](SEPARATOR-EXAMPLES.md) — Horizontal, vertical, vertical menu, in-list examples

## Key Facts

- Single component `Separator.vue` wrapping reka-ui's `Separator`
- Default orientation is `horizontal`; pass `orientation="vertical"` for vertical use
- Default `decorative` is `true` (hidden from the accessibility tree via `role="none"`)
- Set `decorative="false"` when the separator conveys semantic meaning (`role="separator"`)
- Uses `data-[orientation=horizontal]` and `data-[orientation=vertical]` Tailwind variants
- Tailwind v4 utility classes; no extra CSS required
