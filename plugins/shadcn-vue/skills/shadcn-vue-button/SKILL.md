---
name: shadcn-vue-button
description: >
  shadcn-vue Button component (Vue-Port von shadcn/ui, reka-ui Primitive, CVA, Tailwind v4, SFC .vue).
  Triggers: "shadcn-vue button", "button vue", "schaltfläche vue", "button komponente vue",
  "button variants vue", "cva button vue", "nuxt button shadcn", "button asChild vue"
---

# shadcn-vue Button Component

## Triggers
shadcn-vue button, button vue, schaltfläche vue, button komponente vue, button variants vue, cva button vue, nuxt button shadcn

## Overview

The `Button` component is a polymorphic, accessible button built on top of reka-ui's `Primitive` and styled with `class-variance-authority` (CVA). It supports 6 visual variants, 6 size presets, and can render as any element or component via the `asChild` / `as` props.

## Variants (6)

| Variant | Description |
|---|---|
| `default` | Solid primary-color background with primary-foreground text |
| `destructive` | Red destructive background, white text; separate ring in dark mode |
| `outline` | Bordered, transparent background; accent hover state |
| `secondary` | Muted secondary background |
| `ghost` | No background; accent hover state |
| `link` | Text-only, underline on hover |

## Sizes (6)

| Size | Height | Notes |
|---|---|---|
| `default` | 36px (h-9) | Standard button |
| `sm` | 32px (h-8) | Smaller gap and padding |
| `lg` | 40px (h-10) | Wider horizontal padding |
| `icon` | 36×36px (size-9) | Square icon-only |
| `icon-sm` | 32×32px (size-8) | Smaller icon-only |
| `icon-lg` | 40×40px (size-10) | Larger icon-only |

## Key Features

- **SVG auto-sizing**: SVGs without an explicit `size-*` class are automatically sized to 16px (1rem) via `[&_svg:not([class*='size-'])]:size-4`.
- **asChild support**: Pass `as-child` to delegate rendering to the direct child element (e.g. `<a>`, `<RouterLink>`), preserving all button styles.
- **aria-invalid**: The component has built-in ring styles for `aria-invalid` state (destructive ring color).
- **data attributes**: Renders `data-slot="button"`, `data-variant`, and `data-size` for CSS targeting.

## Tailwind v4 — Cursor Behavior

Tailwind v4 changed the default cursor for buttons from `pointer` to `default`. To restore the pointer cursor, add to your global CSS:

```css
@layer base {
  button:not(:disabled),
  [role="button"]:not(:disabled) {
    cursor: pointer;
  }
}
```

Alternatively, initialize your project with:
```bash
npx shadcn-vue@latest init --pointer
```

## References

- [Installation](references/installation.md)
- [Source code](references/source.md)
- [API / Props](references/api.md)
- [Examples](references/examples.md)
