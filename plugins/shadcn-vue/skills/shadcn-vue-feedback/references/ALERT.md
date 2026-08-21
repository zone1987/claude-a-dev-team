# shadcn-vue: Alert

Displays a callout for user attention. Pure Vue component — no reka-ui dependency.
Uses CVA variants for `default` and `destructive` styles. Supports icons (SVG/lucide),
title, description, and optional action slot.

## Sub-Components

- `Alert` — Root container with `role="alert"`, accepts `variant` prop
- `AlertTitle` — Bold heading text (col-start-2 in grid layout)
- `AlertDescription` — Body text with muted color
- `alertVariants` — CVA function exported from index.ts for custom variants

## Key Features

- Grid layout: icon occupies first column, text occupies second
- `has-[>svg]` CSS selector auto-adjusts grid columns when icon present
- Variants: `default` (card background) and `destructive` (text-destructive)
- No reka-ui required — pure div/slot based

## Reference Files

- `ALERT-INSTALLATION.md` — CLI and manual installation
- `ALERT-SOURCE.md` — Complete Vue source code for all files
- `ALERT-API.md` — Props, variants, CVA definition
- `ALERT-EXAMPLES.md` — All demo examples with full code
