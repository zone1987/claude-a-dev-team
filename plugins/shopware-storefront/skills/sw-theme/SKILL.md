---
name: sw-theme
description: Shopware themes: creating a theme, theme.json config, inheritance, multiple themes, compilation, SCSS structure and variables, assets and icons. Use when building or styling a Shopware theme.
---

# Shopware theme and SCSS

A theme is a plugin with a theme.json. Variables and inheritance decide how much you have to override.

## Reference map

- **[ASSETS.md](references/ASSETS.md)**: Full reference: [ASSETS-DETAIL.md]. [ASSETS-DETAIL](references/ASSETS-DETAIL.md).
- **[COMPILE.md](references/COMPILE.md)**: Full reference: [COMPILE-DETAIL.md]. [COMPILE-DETAIL](references/COMPILE-DETAIL.md).
- **[CONFIG.md](references/CONFIG.md)**: `theme.json` can define configurable fields that are available as SCSS variables and in Twig via `theme_config`….
- **[CREATE.md](references/CREATE.md)**: Full step-by-step guide: [CREATE-DETAIL.md]. [CREATE-DETAIL](references/CREATE-DETAIL.md).
- **[INHERITANCE.md](references/INHERITANCE.md)**: Themes inherit via `@` references in `theme.json`.
- **[MULTIPLE.md](references/MULTIPLE.md)**: Full reference: [MULTIPLE-DETAIL.md]. [MULTIPLE-DETAIL](references/MULTIPLE-DETAIL.md).
- **[OVERVIEW.md](references/OVERVIEW.md)**: A theme is a plugin whose class implements `ThemeInterface`; its core is the `theme.json` in `src/….
- **[SCSS-CATALOG.md](references/SCSS-CATALOG.md)**: This skill scans a concrete Shopware 6 project and builds a complete SCSS catalog at `.sh….
- **[SCSS-STRUCTURE.md](references/SCSS-STRUCTURE.md)**: Full reference of the SCSS architecture in the Shopware 6 Storefront core. [SCSS-STRUCTURE-CSS-CUSTOM-PROPERTIES](references/SCSS-STRUCTURE-CSS-CUSTOM-PROPERTIES.md), [SCSS-STRUCTURE-SCSS-FILE-MAP](references/SCSS-STRUCTURE-SCSS-FILE-MAP.md), [SCSS-STRUCTURE-SCSS-VARIABLES](references/SCSS-STRUCTURE-SCSS-VARIABLES.md).
- **[SCSS-VARIABLES.md](references/SCSS-VARIABLES.md)**: Expose configurable values as SCSS variables.
- **[STOREFRONT-ASSETS.md](references/STOREFRONT-ASSETS.md)**: A plugin's static files live in `src/Resources/public/` and are published by `bin/console assets:install`….
- **[STOREFRONT-CUSTOMIZATION.md](references/STOREFRONT-CUSTOMIZATION.md)**: Full reference: [STOREFRONT-CUSTOMIZATION-CUSTOMIZATION.md]. [STOREFRONT-CUSTOMIZATION-CUSTOMIZATION](references/STOREFRONT-CUSTOMIZATION-CUSTOMIZATION.md).
- **[STOREFRONT-ICONS.md](references/STOREFRONT-ICONS.md)**: Icons are included via `sw_icon`.
- **[STOREFRONT-SCSS.md](references/STOREFRONT-SCSS.md)**: Plugin styles live in `src/Resources/app/storefront/src/scss/base.scss` and are automatically included in the th….

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) (Storefront guides and reference) plus the Shopware 6.7 Storefront source, retrieved 2026-08-20.
