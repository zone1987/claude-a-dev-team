# Shopware 6 Storefront SCSS structure

Full reference for the SCSS architecture in the Shopware 6 Storefront core.
Based on trunk: `src/Storefront/Resources/app/storefront/src/scss/`.

## Architecture overview

The Storefront SCSS follows the **7-1 pattern** (sass-guidelin.es).
Two entry points are loaded via `theme.json`:

1. `base.scss` — structure file: variables, Bootstrap vendor, base, components, layout, pages
2. `skin/shopware/_base.scss` — Shopware default skin: fonts, visual styling via components/layout/pages

The **variable loading chain** in `variables.scss`:
```
abstract/variables/_bootstrap.scss  (SW Bootstrap overrides – WITHOUT theme colors)
skin/shopware/abstract/_variables.scss  →  _theme.scss, _bootstrap.scss, _custom.scss
~vendor/bootstrap/scss/functions
~vendor/bootstrap/scss/variables
~vendor/bootstrap/scss/mixins
abstract/variables/_custom.scss  (custom non-Bootstrap variables)
abstract/variables/_css-properties.scss  (CSS custom properties via :root)
```

## Full file map

See `SCSS-STRUCTURE-SCSS-FILE-MAP.md`.

## SCSS variables

See `SCSS-STRUCTURE-SCSS-VARIABLES.md`.

## CSS custom properties

See `SCSS-STRUCTURE-CSS-CUSTOM-PROPERTIES.md`.

## Plugin override convention

Plugins can override variables by setting their own `$variable: value !default;` definitions
**before** the Bootstrap import. The correct place is a dedicated
`Resources/app/storefront/src/scss/variables.scss` inside the plugin, loaded via `theme.json`
(`"style": ["app/storefront/src/scss/variables.scss", "@Storefront"]`).

Skin styles are loaded after the core skin; the plugin skin override takes effect by
adding a second `style` entry in the plugin's `theme.json`.
