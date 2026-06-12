---
name: sw-scss-structure
description: >
  Vollständige SCSS-Struktur des Shopware 6 Storefronts (Trunk-Quelle). Nutze diesen Skill bei:
  "wo liegt SCSS Datei", "SCSS Struktur Shopware", "welche SCSS Variablen gibt es",
  "CSS Variablen storefront", "wo wird X gestylt", "scss verzeichnis", "sw-color Variable",
  "Bootstrap Override Shopware", "Theme Variablen SCSS", "wie override ich Header/Footer/Button SCSS".
  Enthält vollständige Datei-Karte, alle SCSS-Variablen mit Defaults und alle CSS Custom Properties.
---

# Shopware 6 Storefront SCSS-Struktur

Vollständige Referenz der SCSS-Architektur im Shopware 6 Storefront-Core.
Basiert auf Trunk: `src/Storefront/Resources/app/storefront/src/scss/`.

## Architektur-Überblick

Das Storefront-SCSS folgt dem **7-1-Pattern** (sass-guidelin.es).
Zwei Einstiegspunkte werden via `theme.json` geladen:

1. `base.scss` — Strukturdatei: Variablen, Bootstrap-Vendor, Base, Components, Layout, Pages
2. `skin/shopware/_base.scss` — Shopware-Default-Skin: Fonts, visuelles Styling über Components/Layout/Pages

Die **Variablen-Ladekette** in `variables.scss`:
```
abstract/variables/_bootstrap.scss  (SW Bootstrap-Overrides – OHNE Theme-Farben)
skin/shopware/abstract/_variables.scss  →  _theme.scss, _bootstrap.scss, _custom.scss
~vendor/bootstrap/scss/functions
~vendor/bootstrap/scss/variables
~vendor/bootstrap/scss/mixins
abstract/variables/_custom.scss  (Custom Non-Bootstrap-Variablen)
abstract/variables/_css-properties.scss  (CSS Custom Properties via :root)
```

## Vollständige Datei-Karte

Siehe `references/deep/scss-file-map.md`.

## SCSS-Variablen

Siehe `references/deep/scss-variables.md`.

## CSS Custom Properties

Siehe `references/deep/css-custom-properties.md`.

## Plugin-Override-Konvention

Plugins können Variablen überschreiben, indem sie **vor** dem Bootstrap-Import eigene
`$variable: value !default;`-Definitionen setzen. Der korrekte Ort ist eine eigene
`Resources/app/storefront/src/scss/variables.scss` im Plugin, die via `theme.json`
(`"style": ["app/storefront/src/scss/variables.scss", "@Storefront"]`) geladen wird.

Skin-Styles werden nach dem Core-Skin geladen; der Plugin-Skin-Override greift durch
hinzufügen eines zweiten `style`-Eintrags in der Plugin-`theme.json`.
