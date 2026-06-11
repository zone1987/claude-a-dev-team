---
name: sw-theme-config
description: >
  Theme-Konfiguration in Shopware 6: config-Felder in theme.json (Farben, Fonts, Tabs/Blocks/Sections), als SCSS-Variablen
  & theme_config() nutzbar, Defaults. Trigger: "Theme Config", "theme.json config", "Theme-Farben konfigurierbar",
  "theme_config twig", "sw-color variable", "Theme-Einstellung". Shopware 6.7.
---

# Shopware 6 — Theme-Config

`theme.json` kann konfigurierbare Felder definieren (im Admin unter Themes editierbar), die als SCSS-Variablen und
im Twig via `theme_config()` verfügbar sind.

```json
"config": {
  "fields": {
    "sw-color-brand-primary": { "type": "color", "value": "#0a64bc", "editable": true },
    "ff-show-badge": { "type": "switch", "value": true }
  }
}
```

SCSS: `color: $sw-color-brand-primary;` · Twig: `{{ theme_config('ff-show-badge') }}`. Felder gruppierbar über
`blocks`/`sections`/`tabs`. Plugin ohne eigenes Theme → Variablen per Subscriber (`sw-scss-variables`).
