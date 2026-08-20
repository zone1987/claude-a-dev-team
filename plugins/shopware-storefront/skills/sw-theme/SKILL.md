---
name: sw-theme
description: Shopware themes: creating a theme, theme.json config, inheritance, multiple themes, compilation, SCSS structure and variables, assets and icons. Use when building or styling a Shopware theme.
---

# Shopware theme and SCSS

A theme is a plugin with a theme.json. Variables and inheritance decide how much you have to override.

## Reference map

- **[ASSETS.md](ASSETS.md)**: Full reference: [ASSETS-DETAIL.md]. [ASSETS-DETAIL](ASSETS-DETAIL.md).
- **[COMPILE.md](COMPILE.md)**: Full reference: [COMPILE-DETAIL.md]. [COMPILE-DETAIL](COMPILE-DETAIL.md).
- **[CONFIG.md](CONFIG.md)**: `theme.json` can define configurable fields that are available as SCSS variables and in Twig via `theme_config`….
- **[CREATE.md](CREATE.md)**: Full step-by-step guide: [CREATE-DETAIL.md]. [CREATE-DETAIL](CREATE-DETAIL.md).
- **[INHERITANCE.md](INHERITANCE.md)**: Themes inherit via `@` references in `theme.json`.
- **[MULTIPLE.md](MULTIPLE.md)**: Full reference: [MULTIPLE-DETAIL.md]. [MULTIPLE-DETAIL](MULTIPLE-DETAIL.md).
- **[OVERVIEW.md](OVERVIEW.md)**: A theme is a plugin whose class implements `ThemeInterface`; its core is the `theme.json` in `src/….
- **[SCSS-CATALOG.md](SCSS-CATALOG.md)**: This skill scans a concrete Shopware 6 project and builds a complete SCSS catalog at `.sh….
- **[SCSS-STRUCTURE.md](SCSS-STRUCTURE.md)**: Full reference of the SCSS architecture in the Shopware 6 Storefront core. [SCSS-STRUCTURE-CSS-CUSTOM-PROPERTIES](SCSS-STRUCTURE-CSS-CUSTOM-PROPERTIES.md), [SCSS-STRUCTURE-SCSS-FILE-MAP](SCSS-STRUCTURE-SCSS-FILE-MAP.md), [SCSS-STRUCTURE-SCSS-VARIABLES](SCSS-STRUCTURE-SCSS-VARIABLES.md).
- **[SCSS-VARIABLES.md](SCSS-VARIABLES.md)**: Expose configurable values as SCSS variables.
- **[STOREFRONT-ASSETS.md](STOREFRONT-ASSETS.md)**: A plugin's static files live in `src/Resources/public/` and are published by `bin/console assets:install`….
- **[STOREFRONT-CUSTOMIZATION.md](STOREFRONT-CUSTOMIZATION.md)**: Full reference: [STOREFRONT-CUSTOMIZATION-CUSTOMIZATION.md]. [STOREFRONT-CUSTOMIZATION-CUSTOMIZATION](STOREFRONT-CUSTOMIZATION-CUSTOMIZATION.md).
- **[STOREFRONT-ICONS.md](STOREFRONT-ICONS.md)**: Icons are included via `sw_icon`.
- **[STOREFRONT-SCSS.md](STOREFRONT-SCSS.md)**: Plugin styles live in `src/Resources/app/storefront/src/scss/base.scss` and are automatically included in the th….

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) (Storefront guides and reference) plus the Shopware 6.7 Storefront source, retrieved 2026-08-20.
