---
name: reui-theming
description: ReUI extended theme tokens beyond shadcn/ui: --success, --info, --warning, --invert and their foreground pairs. Use when theming ReUI or an @reui block shows wrong state colours.
---

# Theming ReUI

ReUI uses the shadcn/ui theming system unchanged and **adds semantic tokens for states shadcn/ui
does not name**. Blocks and components reference those tokens, so a project that never defines them
renders state colours wrong — a success alert falling back to a default surface, for example.

## What ReUI adds

Nine tokens beyond the shadcn/ui palette, each with a light and a dark value:

| Token | Used for |
|---|---|
| `--destructive-foreground` | foreground on destructive actions |
| `--success`, `--success-foreground` | positive outcomes |
| `--info`, `--info-foreground` | informational states |
| `--warning`, `--warning-foreground` | cautionary states |
| `--invert`, `--invert-foreground` | inverted surfaces |

Each needs a matching `--color-*` entry in `@theme inline` to become a Tailwind utility. The exact
values, and the `@theme inline`, `:root` and `.dark` blocks verbatim, are in
**[TOKENS.md](references/TOKENS.md)**.

## What upstream does not define

ReUI documents only these extended tokens and defers everything else — base palette, radius,
custom colours, switching between utilities and variables — to the shadcn/ui documentation. There is
no separate ReUI theme system, no theme picker and no preset list. Do not invent one.

Premium blocks adapt to whatever theme is active through these semantic tokens: change the theme and
every block follows. That is also why restyling an installed block with raw colour utilities is the
wrong move — it breaks the adaptation the block was built for.

## Source

[Styling](https://reui.io/docs/styling), mirrored 2026-09-04. Token values cross-checked against the
`cssVars` block that `registry.json` ships with `@reui/alert`.
