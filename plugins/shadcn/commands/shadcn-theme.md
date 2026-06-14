---
name: shadcn-theme
description: Erzeugt/ändert ein shadcn/ui-Theme — setzt die semantischen CSS-Variablen-Tokens (Light + Dark) konsistent, mappt sie via Tailwind-v4 @theme (oklch), passt --radius und --chart-Tokens an und prüft Kontrast/A11y.
argument-hint: [--base-color neutral|zinc|slate|stone|gray] [--primary "<farbe>"] [--radius 0.5rem] [--dark]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /shadcn-theme

Theme bauen/anpassen. Skills: `shadcn-theming`, `shadcn-colors`, `shadcn-tailwind-v4`, bei `--dark` `shadcn-dark-mode`.

## Ablauf
1. Basisfarbe/Primary/Radius aus `$ARGUMENTS`.
2. **Tokens setzen:** in `globals.css` `:root` UND `.dark` alle Theme-Variablen konsistent (`--background`,
   `--foreground`, `--primary`(+`-foreground`), `--secondary`, `--muted`, `--accent`, `--destructive`, `--border`,
   `--input`, `--ring`, `--card`, `--popover`, `--sidebar*`, `--chart-1..5`, `--radius`) — Werte aus `shadcn-colors`.
3. **Tailwind v4:** `@theme inline`-Mapping der Variablen; Farbraum oklch.
4. Kontrast/A11y prüfen (Light + Dark); fehlende Tokens ergänzen.

Token-Namen/Werte gegen `shadcn-theming`/`shadcn-colors` prüfen — keine festen Farben in Komponenten. Vorlage: `utils/globals.css`.
