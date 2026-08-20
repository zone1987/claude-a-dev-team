# Shopware 6 — Theme config

`theme.json` can define configurable fields (editable in the admin under Themes) that are available as SCSS variables and
in Twig via `theme_config()`.

```json
"config": {
  "fields": {
    "sw-color-brand-primary": { "type": "color", "value": "#0a64bc", "editable": true },
    "ff-show-badge": { "type": "switch", "value": true }
  }
}
```

SCSS: `color: $sw-color-brand-primary;` · Twig: `{{ theme_config('ff-show-badge') }}`. Group fields via
`blocks`/`sections`/`tabs`. Plugin without its own theme → provide variables via a subscriber (`sw-scss-variables`).
