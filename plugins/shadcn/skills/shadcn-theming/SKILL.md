---
name: shadcn-theming
description: shadcn/ui theming: CSS variable tokens, colour palettes, light and dark mode, Tailwind v4 @theme, RTL and direction. Use when the request names shadcn theming, colors or dark mode.
---

# shadcn/ui theming

Colour, radius and typography come from CSS variable tokens rather than component props. Change a token and every component follows.

## Reference map

- **[COLORS.md](COLORS.md)**: shadcn/ui uses OKLCH for all color values in Tailwind v4. [COLORS-NEUTRAL-PALETTE](COLORS-NEUTRAL-PALETTE.md), [COLORS-THEME-VARIABLE-MAPPING](COLORS-THEME-VARIABLE-MAPPING.md).
- **[DARK-MODE.md](DARK-MODE.md)**: Dark mode works by toggling the `.dark` class on the `<html>` element. [DARK-MODE-ASTRO](DARK-MODE-ASTRO.md), [DARK-MODE-NEXT](DARK-MODE-NEXT.md), [DARK-MODE-REMIX](DARK-MODE-REMIX.md), [DARK-MODE-TANSTACK-START](DARK-MODE-TANSTACK-START.md), [DARK-MODE-VITE](DARK-MODE-VITE.md).
- **[DIRECTION.md](DIRECTION.md)**: The `DirectionProvider` sets text direction for shadcn/ui components. [DIRECTION-API](DIRECTION-API.md), [DIRECTION-INSTALLATION](DIRECTION-INSTALLATION.md), [DIRECTION-SOURCE](DIRECTION-SOURCE.md).
- **[FULL-THEME.md](FULL-THEME.md)**: Complete default `neutral` theme scaffold for `app/globals.css`:. [FULL-THEME-2](FULL-THEME-2.md).
- **[OVERVIEW.md](OVERVIEW.md)**: shadcn/ui uses CSS variables for theming by default.
- **[RTL.md](RTL.md)**: First-class RTL support for shadcn/ui: Arabic, Hebrew, Persian and any other RTL language. [RTL-CONCEPTS](RTL-CONCEPTS.md), [RTL-NEXT](RTL-NEXT.md), [RTL-START](RTL-START.md), [RTL-VITE](RTL-VITE.md).
- **[TOKENS.md](TOKENS.md)**: `--radius` is the base radius token. [TOKENS-2](TOKENS-2.md).
- **[TYPOGRAPHY.md](TYPOGRAPHY.md)**: Utility class patterns for styling headings, paragraphs, lists, blockquotes, tables, and other text elements. [TYPOGRAPHY-CLASSES](TYPOGRAPHY-CLASSES.md), [TYPOGRAPHY-EXAMPLES](TYPOGRAPHY-EXAMPLES.md).

## Source

Distilled from [ui.shadcn.com](https://ui.shadcn.com) and the [shadcn-ui repository](https://github.com/shadcn-ui/ui), retrieved 2026-08-20. Components are React source you copy into your project, styled with Tailwind and built on Radix UI or Base UI.
