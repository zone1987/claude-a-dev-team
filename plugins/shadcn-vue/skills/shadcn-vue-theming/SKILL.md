---
name: shadcn-vue-theming
description: >
  shadcn-vue Theming: CSS-Variablen vs. Utility-Klassen, alle Theme-Tokens (background,
  foreground, card, popover, primary, secondary, muted, accent, destructive, border,
  input, ring, chart-1..5, sidebar-*), Radius-Scale, neue Tokens hinzufuegen,
  Base-Colors, vollstaendiges neutral Theme CSS.
  Triggers: "shadcn vue theming", "shadcn vue css variablen", "theme tokens shadcn",
  "shadcn vue farben anpassen", "css variables shadcn vue", "dark mode tokens",
  "background foreground shadcn", "primary shadcn vue", "radius shadcn",
  "shadcn vue oklch", "theming shadcn vue", "custom theme shadcn"
---

# shadcn-vue: Theming

shadcn-vue empfiehlt CSS-Variablen fuer das Theming. Semantische Token-Namen
(`background`, `foreground`, `primary` etc.) werden in Tailwind-Utilities gemappt:
`bg-background`, `text-foreground`, `border-border`, `ring-ring`.

Dark Mode arbeitet mit denselben Tokens, die im `.dark`-Selektor ueberschrieben werden.

## Reference Files

- `references/theming.md` — Token-Konvention (background/foreground-Paare),
  vollstaendige Token-Tabelle mit Verwendungszweck, Radius-Scale (sm/md/lg/xl/2xl/3xl/4xl),
  neue Tokens hinzufuegen (@theme inline), Base-Colors (Neutral/Gray/Zinc/Stone/Slate),
  vollstaendiges neutrales Theme-CSS, Variante ohne CSS-Variablen (--no-css-variables)
