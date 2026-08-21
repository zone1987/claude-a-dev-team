# Shopware 6 — Storefront customization in the theme: full reference

Sources: `guides/plugins/themes/styling/add-css-js-to-theme.md`,
`guides/plugins/themes/styling/override-bootstrap-variables-in-a-theme.md`,
`guides/plugins/themes/styling/override-theme-breakpoints.md`,
`guides/plugins/themes/inheritance/add-theme-inheritance-without-resources.md`

---

## Contents

- [Including SCSS in a theme](#including-scss-in-a-theme)
- [Overriding Bootstrap variables](#overriding-bootstrap-variables)
- [Adjusting responsive breakpoints](#adjusting-responsive-breakpoints)
- [Including JavaScript in a theme](#including-javascript-in-a-theme)
- [Theme without the Shopware skin (Bootstrap only)](#theme-without-the-shopware-skin-bootstrap-only)
- [Namespace references in theme.json](#namespace-references-in-themejson)
- [Quick reference: Shopware SCSS variables](#quick-reference-shopware-scss-variables)

## Including SCSS in a theme

The PHP SASS compiler processes SCSS. Entry points are defined in `theme.json`:

```json
{
  "style": [
    "app/storefront/src/scss/overrides.scss",
    "@Storefront",
    "app/storefront/src/scss/base.scss"
  ]
}
```

**The order is decisive:**
1. `overrides.scss` — **before** `@Storefront` for variable overrides
2. `@Storefront` — the default Shopware theme
3. `base.scss` — your own SCSS (after Storefront → can override classes)

### base.scss — your own CSS/SCSS

```
src/Resources/app/storefront/src/scss/base.scss
```

Example:
```scss
body {
    background-color: blue;
}

.custom-header {
    font-size: 2rem;
    color: $sw-color-brand-primary; // use a theme variable
}
```

After changes: `bin/console theme:compile`

---

## Overriding Bootstrap variables

Bootstrap 4/5 uses `!default` for variables. Overrides must be declared **before** the import.

The `overrides.scss` entry point in `theme.json` is deliberately placed **before** `@Storefront`:

```json
"style": [
    "app/storefront/src/scss/overrides.scss",  ← HERE: before @Storefront
    "@Storefront",
    "app/storefront/src/scss/base.scss"
]
```

### overrides.scss

```scss
// src/Resources/app/storefront/src/scss/overrides.scss
/*
Override variable defaults
==================================================
This file is used to override default SCSS variables from the Shopware Storefront or Bootstrap.
Because of the !default flags, theme variable overrides have to be declared beforehand.
https://getbootstrap.com/docs/4.0/getting-started/theming/#variable-defaults
*/

$border-radius: 0;

// Further override examples
$icon-base-color: #f00;
$modal-backdrop-bg: rgba(255, 0, 0, 0.5);
$disabled-btn-bg: #f00;
$disabled-btn-border-color: #fc8;
$font-weight-semibold: 300;
```

> **Important:** **Only** variable overrides in `overrides.scss`. No CSS like `.container { background: #f00 }`.
> In watch mode (`storefront-watch`) variables are injected dynamically — CSS selectors
> in `overrides.scss` may appear more than once in the build.

---

## Adjusting responsive breakpoints

As of Shopware **6.7.8.0** there are six theme config fields for breakpoints.
They are **hidden** in the admin (a developer-only feature).

### Defining them in theme.json

```json
{
  "name": "My custom theme",
  "config": {
    "fields": {
      "sw-breakpoint-xs": { "value": 0 },
      "sw-breakpoint-sm": { "value": 576 },
      "sw-breakpoint-md": { "value": 768 },
      "sw-breakpoint-lg": { "value": 992 },
      "sw-breakpoint-xl": { "value": 1200 },
      "sw-breakpoint-xxl": { "value": 1400 }
    }
  }
}
```

These values are made available automatically in **Twig** and **JavaScript**.

### Synchronizing Bootstrap breakpoints in SCSS

Because Shopware uses Bootstrap defaults in CSS, SCSS breakpoints have to be overridden separately.
The theme config values are available in SCSS as variables:

```scss
// src/Resources/app/storefront/src/scss/overrides.scss
$grid-breakpoints: (
    xs: $sw-breakpoint-xs,
    sm: $sw-breakpoint-sm,
    md: $sw-breakpoint-md,
    lg: $sw-breakpoint-lg,
    xl: $sw-breakpoint-xl,
    xxl: $sw-breakpoint-xxl
);
```

**Single source of truth:** define breakpoints only in `theme.json` and reference them in SCSS.

---

## Including JavaScript in a theme

JavaScript is compiled with **webpack** (via shopware-cli).

### Entry point

```
src/Resources/app/storefront/src/main.js
```

```javascript
// main.js
console.log('SwagBasicExampleTheme JS loaded');
```

### Compiling

```bash
shopware-cli project storefront-build
```

Output: `src/Resources/app/storefront/dist/storefront/js/swag-basic-example-theme/swag-basic-example-theme.js`

### Referencing it in theme.json

```json
{
  "script": [
    "@Storefront",
    "app/storefront/dist/storefront/js/swag-basic-example-theme/swag-basic-example-theme.js"
  ]
}
```

---

## Theme without the Shopware skin (Bootstrap only)

If the theme should build **exclusively** on Bootstrap (without the Shopware Storefront skin):

```json
{
  "style": [
    "@StorefrontBootstrap",
    "@Plugins",
    "app/storefront/src/scss/base.scss"
  ]
}
```

**Important restrictions for `@StorefrontBootstrap`:**
- Usable only in the `style` section — **not** in `views` or `script`
- All theme variables (`$sw-color-brand-primary` etc.) remain available
- `@Storefront` and `@StorefrontBootstrap` **must not** be used at the same time
- `@StorefrontBootstrap` does **not** contain `@Plugins` — it must be added explicitly
- All SCSS from `src/Storefront/Resources/app/storefront/src/scss/skin` is omitted

**Use case:** a completely custom design without Shopware Storefront styling as its basis.

---

## Namespace references in theme.json

Importing individual files from other themes/namespaces:

```json
{
  "style": [
    "app/storefront/src/scss/overrides.scss",
    "@Storefront",
    "@BasicTheme/app/storefront/src/scss/custom.scss",
    "app/storefront/src/scss/base.scss"
  ],
  "script": [
    "@Storefront",
    "@Plugins",
    "@BasicTheme/app/storefront/dist/storefront/custom-plugin.js",
    "app/storefront/dist/storefront/js/my-theme/my-theme.js"
  ]
}
```

---

## Quick reference: Shopware SCSS variables

Shopware injects all `config.fields` entries automatically as SCSS variables:

```scss
// automatically available from theme.json config.fields:
color: $sw-color-brand-primary;      // primary color
background: $sw-color-brand-secondary;
border-radius: $sw-border-radius;
font-family: $sw-font-family-base;

// breakpoints (as of 6.7.8.0):
@media (min-width: $sw-breakpoint-lg) { ... }
```
