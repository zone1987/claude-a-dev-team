---
name: sw-theme
description: >
  Ein Storefront-Theme in Shopware 6 erstellen: ThemePlugin (extends ThemeInterface/Plugin), theme.json, Struktur,
  Theme aktivieren/kompilieren. Trigger: "Theme erstellen", "theme.json", "ThemeInterface", "eigenes Theme",
  "theme:compile", "storefront theme plugin", "Theme aktivieren". Shopware 6.7. Scaffolder: /sw-theme.
---

# Shopware 6 — Theme

Ein Theme ist ein Plugin, dessen Klasse `ThemeInterface` implementiert; Kern ist die `theme.json` unter
`src/Resources/`.

```json
{
  "name": "FfTheme",
  "author": "forty-four",
  "views": ["@Storefront", "@Plugins", "@FfTheme"],
  "style": ["@Storefront", "app/storefront/src/scss/base.scss"],
  "script": ["@Storefront", "app/storefront/dist/storefront/js/ff-theme.js"],
  "asset": ["@Storefront", "app/storefront/src/assets"]
}
```

`theme.json` definiert View-/Style-/Script-/Asset-Reihenfolge und Config-Felder (`sw-theme-config`).
Aktivieren: `bin/console theme:change`; kompilieren: `theme:compile`. Vererbung über `@`-Referenzen
(`sw-theme-inheritance`). Reines Styling ohne eigenes Theme geht auch als Plugin-SCSS (`sw-storefront-scss`).
