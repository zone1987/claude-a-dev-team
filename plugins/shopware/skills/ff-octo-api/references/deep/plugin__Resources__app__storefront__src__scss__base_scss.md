# Storefront base.scss (`src/Resources/app/storefront/src/scss/base.scss`)

## Zweck
SCSS-Einstiegspunkt des Storefronts. Importiert Variablen und Komponenten-Styles.

## Inhalt
- `@import 'variables/custom'` (Spacing/Typografie), `@import 'variables/colors'` (Farben).
- `@import './component/product-detail-configurator'`, `'./component/line-item'`, `'./component/flatpickr'`.

## Besonderheiten / Fallstricke
- Wird über `manifest.json`/Theme-Build eingebunden; Reihenfolge/Variablen können mit FfLondonTheme kollidieren (kein expliziter Cross-Import).

## Bezüge
`variables/_custom.scss`, `variables/_colors.scss`, `component/*.scss`, `../twig-templates.md`.
