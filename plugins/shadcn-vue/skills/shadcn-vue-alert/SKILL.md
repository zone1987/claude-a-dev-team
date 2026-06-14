---
name: shadcn-vue-alert
description: >
  shadcn-vue Alert component (Vue-Port von shadcn/ui, Tailwind v4, SFC .vue, keine reka-ui-Abhängigkeit).
  Triggers: "shadcn-vue alert", "shadcn vue alert", "alert vue", "alert nuxt", "alert komponente vue",
  "hinweis box vue", "callout vue", "notification box vue", "alert destructive vue"
---

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

- `references/installation.md` — CLI and manual installation
- `references/source.md` — Complete Vue source code for all files
- `references/api.md` — Props, variants, CVA definition
- `references/examples.md` — All demo examples with full code
