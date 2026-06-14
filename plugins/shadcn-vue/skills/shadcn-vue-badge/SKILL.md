---
name: shadcn-vue-badge
description: >
  Use this skill when working with shadcn-vue Badge components. Triggers:
  "shadcn-vue badge", "badge vue", "badge nuxt", "tag vue", "label badge vue",
  "status badge vue", "chip vue", "badge component shadcn", "badge variant vue".
references:
  - references/installation.md
  - references/source.md
  - references/api.md
  - references/examples.md
---

# shadcn-vue Badge

The Badge component renders small, inline labels for statuses, categories, counts, or any short metadata. It is built on top of `reka-ui`'s `Primitive` component, which means it supports the **`as` / `asChild`** pattern to render as any HTML element or custom component without losing styling.

## Variants (CVA)

Variants are defined with `class-variance-authority` (CVA) and live in `index.ts`:

| Variant | Description |
|---|---|
| `default` | Primary-colored filled badge |
| `secondary` | Secondary-colored filled badge |
| `destructive` | Red/destructive filled badge (with reduced opacity in dark mode) |
| `outline` | Transparent background, foreground border |

Default variant is `default`.

## Key characteristics

- **CVA-powered** — all variants and the base classes are in `badgeVariants()`, fully composable and overridable via `cn()`.
- **reka-ui Primitive** — renders as a `<div>` by default; swap the tag with `:as="'span'"` or use `as-child` to merge props onto a child element (e.g. `<a>` links).
- **Icon support** — SVG children are automatically sized to `size-3` via `[&>svg]:size-3` and spaced with `gap-1`.
- **Accessibility** — `focus-visible` ring styles and `aria-invalid` state styles are baked in.
- **Composable** — export `badgeVariants` separately to apply Badge styles to any element without the Vue wrapper.

## References

- `references/installation.md` — CLI and manual installation steps
- `references/source.md` — Full source of `index.ts` and `Badge.vue`
- `references/api.md` — Props, variants, inherited Primitive props
- `references/examples.md` — Practical code examples
