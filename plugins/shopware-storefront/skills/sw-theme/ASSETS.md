# Shopware 6 — Theme Assets & Icons

Vollständige Referenz: [ASSETS-DETAIL.md](ASSETS-DETAIL.md)

**Assets einbinden** via `theme.json`:
```json
"asset": ["@Storefront", "app/storefront/src/assets"]
```
Nach `theme:compile` landen Assets in `public/theme/<uuid>/asset/`.

**Verwenden:**
```twig
{# Twig #}
<img src="{{ asset('/assets/your-image.png', 'theme') }}">
```
```scss
// SCSS
body { background-image: url('#{$app-css-relative-asset-path}/your-image.png'); }
```

**Custom Icons** via `iconSets` in theme.json, dann `{% sw_icon 'name' style {'pack': 'custom-icons'} %}`.
