---
name: sw-theme-assets
description: >
  Assets und Icons in einem Shopware 6 Theme: theme.json asset-Pfade, theme:compile kopiert Assets,
  Twig asset()-Funktion, SCSS-Pfadvariable, custom Icon-Packs (iconSets), sw_icon Twig-Tag.
  Trigger: "Theme Assets", "Bilder im Theme", "custom icons theme", "iconSets theme.json",
  "sw_icon", "asset theme twig", "Theme Fonts", "Theme Bilder einbinden". Shopware 6.7.
---

# Shopware 6 — Theme Assets & Icons

Vollständige Referenz: [references/deep/theme-assets.md](references/deep/theme-assets.md)

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
