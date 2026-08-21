---
name: shadcn-theming
description: shadcn/ui theming: CSS variable tokens, colour palettes, light and dark mode, Tailwind v4 @theme, RTL and direction. Use when the request names shadcn theming, colors or dark mode.
---

# shadcn/ui theming

Colour, radius and typography come from CSS variable tokens rather than component props. Change a token and every component follows.

## Reference map

- **[COLORS.md](references/COLORS.md)**: shadcn/ui uses OKLCH for all color values in Tailwind v4. [COLORS-NEUTRAL-PALETTE](references/COLORS-NEUTRAL-PALETTE.md), [COLORS-THEME-VARIABLE-MAPPING](references/COLORS-THEME-VARIABLE-MAPPING.md).
- **[DARK-MODE.md](references/DARK-MODE.md)**: Dark mode works by toggling the `.dark` class on the `<html>` element. [DARK-MODE-ASTRO](references/DARK-MODE-ASTRO.md), [DARK-MODE-NEXT](references/DARK-MODE-NEXT.md), [DARK-MODE-REMIX](references/DARK-MODE-REMIX.md), [DARK-MODE-TANSTACK-START](references/DARK-MODE-TANSTACK-START.md), [DARK-MODE-VITE](references/DARK-MODE-VITE.md).
- **[DIRECTION.md](references/DIRECTION.md)**: The `DirectionProvider` sets text direction for shadcn/ui components. [DIRECTION-API](references/DIRECTION-API.md), [DIRECTION-INSTALLATION](references/DIRECTION-INSTALLATION.md), [DIRECTION-SOURCE](references/DIRECTION-SOURCE.md).
- **[FULL-THEME.md](references/FULL-THEME.md)**: Complete default `neutral` theme scaffold for `app/globals.css`:. [FULL-THEME-2](references/FULL-THEME-2.md).
- **[OVERVIEW.md](references/OVERVIEW.md)**: shadcn/ui uses CSS variables for theming by default.
- **[RTL.md](references/RTL.md)**: First-class RTL support for shadcn/ui: Arabic, Hebrew, Persian and any other RTL language. [RTL-CONCEPTS](references/RTL-CONCEPTS.md), [RTL-NEXT](references/RTL-NEXT.md), [RTL-START](references/RTL-START.md), [RTL-VITE](references/RTL-VITE.md).
- **[TOKENS.md](references/TOKENS.md)**: `--radius` is the base radius token. [TOKENS-2](references/TOKENS-2.md).
- **[TYPOGRAPHY.md](references/TYPOGRAPHY.md)**: Utility class patterns for styling headings, paragraphs, lists, blockquotes, tables, and other text elements. [TYPOGRAPHY-CLASSES](references/TYPOGRAPHY-CLASSES.md), [TYPOGRAPHY-EXAMPLES](references/TYPOGRAPHY-EXAMPLES.md).

## Source

Distilled from [ui.shadcn.com](https://ui.shadcn.com) and the [shadcn-ui repository](https://github.com/shadcn-ui/ui), retrieved 2026-08-20. Components are React source you copy into your project, styled with Tailwind and built on Radix UI or Base UI.
