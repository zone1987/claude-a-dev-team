# Shopware 6 — Theme Assets & Icons: Complete Reference

Sources: `guides/plugins/themes/assets/add-assets-to-theme.md`,
`guides/plugins/themes/assets/add-icons.md`

---

## Contents

- [Including assets in a theme](#including-assets-in-a-theme)
- [Linking assets](#linking-assets)
- [Custom Icons](#custom-icons)
- [Quick reference: paths](#quick-reference-paths)

## Including assets in a theme

There are two methods:

### Method 1: theme.json (recommended for themes)

Configure the asset path in `theme.json`:

```json
{
  "asset": [
    "app/storefront/src/assets"
  ]
}
```

With the storefront default theme:
```json
{
  "asset": [
    "@Storefront",
    "app/storefront/src/assets"
  ]
}
```

**How it works:** The command `bin/console theme:compile` copies all assets from the
configured path to `<shopware-root>/public/theme/<theme-asset-uuid>/asset/`.

```text
public/
└── theme/
    ├── <theme-uuid>/
    │   ├── css/
    │   │   └── all.css
    │   └── js/
    │       └── all.js
    └── <theme-asset-uuid>/
        └── asset/
            └── your-image.png   ← copied here
```

### Method 2: plugin approach (standard assets)

Works like normal plugin assets via `<plugin>/src/Resources/public/`.
Details: `guides/plugins/storefront/styling/add-custom-assets.md`

---

## Linking assets

### In Twig templates

```twig
<img src="{{ asset('/assets/your-image.png', 'theme') }}">
```

The second parameter `'theme'` specifies the asset package name.

### In SCSS

```scss
body {
    background-image: url('#{$app-css-relative-asset-path}/your-image.png');
}
```

The SCSS variable `$app-css-relative-asset-path` is set automatically by Shopware and
points to the theme asset directory.

---

## Custom Icons

### Default icon system

Shopware uses SVG icons. Default icons are located in:
```
<shopware-root>/src/Storefront/Resources/app/storefront/dist/assets/icon/
├── default/    ← default pack
└── solid/      ← solid pack
```

### Using an icon in Twig

```twig
{% sw_icon 'done-outline-24px' style {
    'size': 'lg',
    'namespace': 'TestPlugin',
    'pack': 'solid'
} %}
```

**`sw_icon` configuration parameters:**

| Parameter | Description |
|---|---|
| `size` | Size of the icon |
| `namespace` | Plugin/theme name in which the icon is looked up — **important for custom icons** |
| `pack` | Icon pack name (default: `default`) |
| `color` | Color (Bootstrap variants or any CSS color) |
| `class` | Additional CSS class |

> **Caution:** Without a `namespace` configuration, Shopware shows the default storefront icons.

### Placing your own icons (classic)

Icons in the plugin/theme under:
```
<YourPlugin>/src/Resources/app/storefront/dist/assets/icon/default/
```

For your own icon packs, create a folder with the pack name:
```
<YourPlugin>/src/Resources/app/storefront/dist/assets/icon/<pack-name>/
```

> **Caution:** Icons are **not** part of theme inheritance. Custom icons must be placed in your
> own theme namespace and referenced explicitly via `namespace`.

### iconSets in theme.json (as of Shopware 6.4.1.0) — MANDATORY for apps

For app themes and as the preferred method:

```json
{
  "iconSets": {
    "custom-icons": "app/storefront/src/assets/icon-pack/custom-icons"
  }
}
```

Usage in Twig:
```twig
{% sw_icon 'done-outline-24px' style {
    'pack': 'custom-icons'
} %}
```

> **Note:** For app themes, `iconSets` is **mandatory**, since icons cannot be loaded otherwise.

---

## Quick reference: paths

| Purpose | Path |
|---|---|
| Assets in the theme | `src/Resources/app/storefront/src/assets/` |
| Default icons | `dist/assets/icon/default/` |
| Custom icon pack | `dist/assets/icon/<pack-name>/` |
| Compiled assets (public) | `public/theme/<theme-asset-uuid>/asset/` |
