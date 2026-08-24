---
name: shadcn-vue-theme
description: Creates or changes a shadcn-vue theme — sets the semantic CSS variable tokens consistently for light and dark, maps them through Tailwind v4 @theme (oklch), adjusts --radius and the --chart tokens, and checks contrast.
argument-hint: [--base-color neutral|zinc|slate|stone|gray] [--primary "<colour>"] [--radius 0.5rem] [--dark]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /shadcn-vue-theme

Build or change a theme. Skill: `shadcn-vue-theming`.

## Steps
1. Base colour and options from `$ARGUMENTS`.
2. Set every semantic token in `:root` and `.dark`: `--background`, `--foreground`, `--primary`,
   `--secondary`, `--muted`, `--accent`, `--destructive`, `--border`, `--ring`, `--card`,
   `--popover`, `--sidebar`, `--chart-1` to `--chart-5`.
3. Map them through Tailwind v4 `@theme inline`, in oklch.
4. `--radius` and the chart tokens follow the same palette, so a chart matches the surface it sits on.
5. Check the contrast of every foreground-on-background pair, in both modes.

Never define a colour only inside `.dark`: a token missing from `:root` falls back to nothing. Use
the documented token names only (source: `shadcn-vue-theming`).
