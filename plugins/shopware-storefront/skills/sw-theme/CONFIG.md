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
