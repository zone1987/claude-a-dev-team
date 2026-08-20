# Shopware 6 — Storefront-SCSS

Plugin-Styles liegen unter `src/Resources/app/storefront/src/scss/base.scss` und werden automatisch in die
Theme-Kompilierung einbezogen (kein manueller Import nötig). Bootstrap 5 steht zur Verfügung.

```scss
// src/Resources/app/storefront/src/scss/base.scss
.ff-hint {
    color: $color-primary;          // Theme-/Bootstrap-Variablen nutzbar
    @include media-breakpoint-up(md) { font-size: 1rem; }
}
```

Kompiliert über `bin/console theme:compile` (bzw. Watcher). Konfigurierbare Werte als SCSS-Variablen bereitstellen
(`sw-scss-variables`). Lint: `composer stylelint`. Größere UI-Logik in JS-Plugins (`sw-storefront-js-plugin`).
