---
name: sw-theme-storefront-customization
description: >
  Storefront im Theme anpassen: SCSS/JS hinzufügen, Bootstrap-Variablen überschreiben (overrides.scss),
  responsive Breakpoints customizen (sw-breakpoint-*), @StorefrontBootstrap (ohne Shopware-Skin).
  Trigger: "Bootstrap Variablen überschreiben Theme", "overrides.scss", "border-radius Theme",
  "Breakpoints anpassen Theme", "StorefrontBootstrap", "ohne Shopware Skin", "SCSS Theme anpassen",
  "JS Theme hinzufügen". Shopware 6.7.
---

# Shopware 6 — Storefront-Customization im Theme

Vollständige Referenz: [references/deep/theme-customization.md](references/deep/theme-customization.md)

**Bootstrap-Variablen** überschreiben in `overrides.scss` (muss **vor** `@Storefront` stehen):
```scss
// overrides.scss — NUR Variablen, kein CSS
$border-radius: 0;
$sw-color-brand-primary: #ff0000;
```

**Responsive Breakpoints** (ab 6.7.8.0) via theme.json:
```json
"config": { "fields": { "sw-breakpoint-lg": { "value": 1024 } } }
```

**Ohne Shopware-Skin** (nur Bootstrap):
```json
"style": ["@StorefrontBootstrap", "@Plugins", "app/storefront/src/scss/base.scss"]
```
