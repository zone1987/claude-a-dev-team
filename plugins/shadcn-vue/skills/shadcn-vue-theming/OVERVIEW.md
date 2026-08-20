# shadcn-vue: Theming

shadcn-vue empfiehlt CSS-Variablen fuer das Theming. Semantische Token-Namen
(`background`, `foreground`, `primary` etc.) werden in Tailwind-Utilities gemappt:
`bg-background`, `text-foreground`, `border-border`, `ring-ring`.

Dark Mode arbeitet mit denselben Tokens, die im `.dark`-Selektor ueberschrieben werden.

## Reference Files

- `OVERVIEW-DETAIL.md` — Token-Konvention (background/foreground-Paare),
  vollstaendige Token-Tabelle mit Verwendungszweck, Radius-Scale (sm/md/lg/xl/2xl/3xl/4xl),
  neue Tokens hinzufuegen (@theme inline), Base-Colors (Neutral/Gray/Zinc/Stone/Slate),
  vollstaendiges neutrales Theme-CSS, Variante ohne CSS-Variablen (--no-css-variables)
