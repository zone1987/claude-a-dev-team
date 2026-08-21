# Shopware 6 — Theme assets & icons

Full reference: [ASSETS-DETAIL.md](ASSETS-DETAIL.md)

**Include assets** via `theme.json`:
```json
"asset": ["@Storefront", "app/storefront/src/assets"]
```
After `theme:compile` the assets end up in `public/theme/<uuid>/asset/`.

**Usage:**
```twig
{# Twig #}
<img src="{{ asset('/assets/your-image.png', 'theme') }}">
```
```scss
// SCSS
body { background-image: url('#{$app-css-relative-asset-path}/your-image.png'); }
```

**Custom icons** via `iconSets` in theme.json, then `{% sw_icon 'name' style {'pack': 'custom-icons'} %}`.
