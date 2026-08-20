---
name: sw-theme
description: Shopware themes: creating a theme, theme.json config, inheritance, multiple themes, compilation, SCSS structure and variables, assets and icons. Use when building or styling a Shopware theme.
---

# Shopware theme and SCSS

A theme is a plugin with a theme.json. Variables and inheritance decide how much you have to override.

## Reference map

- **[ASSETS.md](ASSETS.md)**: Vollständige Referenz: [ASSETS-DETAIL.md]. [ASSETS-DETAIL](ASSETS-DETAIL.md).
- **[COMPILE.md](COMPILE.md)**: Vollständige Referenz: [COMPILE-DETAIL.md]. [COMPILE-DETAIL](COMPILE-DETAIL.md).
- **[CONFIG.md](CONFIG.md)**: `theme.json` kann konfigurierbare Felder definieren, die als SCSS-Variablen und im Twig via `theme_config` ve….
- **[CREATE.md](CREATE.md)**: Vollständige Schritt-für-Schritt-Anleitung: [CREATE-DETAIL.md]. [CREATE-DETAIL](CREATE-DETAIL.md).
- **[INHERITANCE.md](INHERITANCE.md)**: Themes erben über `@`-Referenzen in `theme.json`.
- **[MULTIPLE.md](MULTIPLE.md)**: Vollständige Referenz: [MULTIPLE-DETAIL.md]. [MULTIPLE-DETAIL](MULTIPLE-DETAIL.md).
- **[OVERVIEW.md](OVERVIEW.md)**: Ein Theme ist ein Plugin, dessen Klasse `ThemeInterface` implementiert; Kern ist die `theme.json` unter `src/….
- **[SCSS-CATALOG.md](SCSS-CATALOG.md)**: Dieser Skill scannt ein konkretes Shopware-6-Projekt und erstellt einen vollständigen SCSS-Katalog unter `.sh….
- **[SCSS-STRUCTURE.md](SCSS-STRUCTURE.md)**: Vollständige Referenz der SCSS-Architektur im Shopware 6 Storefront-Core. [SCSS-STRUCTURE-CSS-CUSTOM-PROPERTIES](SCSS-STRUCTURE-CSS-CUSTOM-PROPERTIES.md), [SCSS-STRUCTURE-SCSS-FILE-MAP](SCSS-STRUCTURE-SCSS-FILE-MAP.md), [SCSS-STRUCTURE-SCSS-VARIABLES](SCSS-STRUCTURE-SCSS-VARIABLES.md).
- **[SCSS-VARIABLES.md](SCSS-VARIABLES.md)**: Konfigurierbare Werte als SCSS-Variablen verfügbar machen.
- **[STOREFRONT-ASSETS.md](STOREFRONT-ASSETS.md)**: Statische Dateien eines Plugins liegen in `src/Resources/public/` und werden per `bin/console assets:install`….
- **[STOREFRONT-CUSTOMIZATION.md](STOREFRONT-CUSTOMIZATION.md)**: Vollständige Referenz: [STOREFRONT-CUSTOMIZATION-CUSTOMIZATION.md]. [STOREFRONT-CUSTOMIZATION-CUSTOMIZATION](STOREFRONT-CUSTOMIZATION-CUSTOMIZATION.md).
- **[STOREFRONT-ICONS.md](STOREFRONT-ICONS.md)**: Icons werden über `sw_icon` eingebunden.
- **[STOREFRONT-SCSS.md](STOREFRONT-SCSS.md)**: Plugin-Styles liegen unter `src/Resources/app/storefront/src/scss/base.scss` und werden automatisch in die Th….

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) (Storefront guides and reference) plus the Shopware 6.7 Storefront source, retrieved 2026-08-20.
