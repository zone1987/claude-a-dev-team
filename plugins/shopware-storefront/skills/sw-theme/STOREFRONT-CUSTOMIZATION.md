# Shopware 6 — Storefront customization in the theme

Full reference: [STOREFRONT-CUSTOMIZATION-CUSTOMIZATION.md](STOREFRONT-CUSTOMIZATION-CUSTOMIZATION.md)

**Override Bootstrap variables** in `overrides.scss` (must come **before** `@Storefront`):
```scss
// overrides.scss — variables ONLY, no CSS
$border-radius: 0;
$sw-color-brand-primary: #ff0000;
```

**Responsive breakpoints** (as of 6.7.8.0) via theme.json:
```json
"config": { "fields": { "sw-breakpoint-lg": { "value": 1024 } } }
```

**Without the Shopware skin** (Bootstrap only):
```json
"style": ["@StorefrontBootstrap", "@Plugins", "app/storefront/src/scss/base.scss"]
```
