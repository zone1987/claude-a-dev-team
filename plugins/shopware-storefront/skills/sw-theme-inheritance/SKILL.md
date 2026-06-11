---
name: sw-theme-inheritance
description: >
  Theme-Vererbung in Shopware 6: @-Referenzen in theme.json (@Storefront, @ParentTheme), Reihenfolge von views/style/
  script/asset, Bootstrap-Util-Imports. Trigger: "Theme Inheritance", "Theme erben", "@Storefront theme.json",
  "parent theme", "theme vererbung reihenfolge", "extend theme". Shopware 6.7.
---

# Shopware 6 — Theme-Inheritance

Themes erben über `@`-Referenzen in `theme.json`. Die Reihenfolge der Arrays bestimmt Override-Priorität
(spätere Einträge überschreiben frühere).

```json
"style": ["@Storefront", "@ParentTheme", "app/storefront/src/scss/base.scss"]
```

- `@Storefront` = Default-Theme-Basis (immer zuerst), dann ggf. ein Eltern-Theme, zuletzt eigenes SCSS/JS.
- Nur **Bootstrap-Utilities/Variablen** importieren (kein kompiliertes CSS doppelt) — Performance/ADR „atomic theme compilation".
- `views` steuert Twig-Template-Auflösung (Inheritance der Templates, `sw-twig-templates`).

Bei reinem Erweitern eines bestehenden Shops oft besser: Plugin-SCSS/Template-Override statt eigenes Theme.
