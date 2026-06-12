# Shopware 6 Storefront CSS Custom Properties

Alle `--*`-Variablen des Shopware 6 Storefronts, gruppiert nach Herkunft und Typ.

---

## 1. Storefront Core: `:root`-Definitionen

Definiert in `abstract/variables/_css-properties.scss`.  
Alle Custom Properties werden dort als `--name: #{$scss-var}` aus den SCSS-Variablen abgeleitet.

### Z-Index-Properties

| Custom Property | SCSS-Quelle | Wert |
|---|---|---|
| `--search-suggest-zindex` | `$search-suggest-zindex` | `1000` |
| `--offcanvas-zindex` | `$offcanvas-zindex` | `1050` |
| `--cookie-msg-zindex` | `$cookie-msg-zindex` | `1100` |
| `--scroll-up-zindex` | `$scroll-up-zindex` | `700` |
| `--menu-flyout-zindex` | `$menu-flyout-zindex` | `1030` |
| `--zoom-modal-action-zindex` | `$zoom-modal-action-zindex` | `1051` |
| `--magnifier-overlay-zindex` | `$magnifier-overlay-zindex` | `1100` |

### Icon-Properties

| Custom Property | SCSS-Quelle | Wert |
|---|---|---|
| `--icon-base-size` | `$icon-base-size` | `1.375rem` |
| `--icon-base-color` | `$icon-base-color` | `#4a545b` |
| `--icon-review-color` | `$icon-review-color` | `#fedc70` |
| `--progress-bar-review` | `$progress-bar-review` | `#fedc70` |

### Layout/Spacing-Properties

| Custom Property | SCSS-Quelle | Wert |
|---|---|---|
| `--element-backdrop-bg` | `$element-backdrop-bg` | `rgba(#fff, 0.5)` |
| `--spacer-xs` | `$spacer-xs` | `$spacer * 0.25` |
| `--spacer-sm` | `$spacer-sm` | `$spacer * 0.5` |
| `--spacer-md` | `$spacer-md` | `$spacer` |
| `--spacer-lg` | `$spacer-lg` | `$spacer * 1.5` |
| `--spacer-xl` | `$spacer-xl` | `$spacer * 3` |

### E-Commerce-Properties

| Custom Property | SCSS-Quelle | Wert |
|---|---|---|
| `--buy-btn-bg` | `$buy-btn-bg` | `$sw-color-buy-button` → `#0042a0` |
| `--buy-btn-color` | `$buy-btn-color` | `$sw-color-buy-button-text` → `#fff` |
| `--disabled-btn-bg` | `$disabled-btn-bg` | `#eee` |
| `--disabled-btn-border-color` | `$disabled-btn-border-color` | `#eee` |
| `--price-color` | `$price-color` | `$sw-color-price` → `#2b3136` |

### CMS-Properties

| Custom Property | SCSS-Quelle | Wert |
|---|---|---|
| `--cms-block-text-hero-hr-color` | `$cms-block-text-hero-hr-color` | `#e9edf0` |
| `--cms-element-text-quotes-color` | `$cms-element-text-quotes-color` | `#9aa7be` |
| `--cms-element-product-listing-gutter-width` | `$cms-element-product-listing-gutter-width` | `30px` |

### Typografie-Properties

| Custom Property | SCSS-Quelle | Wert |
|---|---|---|
| `--font-weight-semibold` | `$font-weight-semibold` | `600` |

---

## 2. Bootstrap 5 CSS Custom Properties (via `--bs-*`)

Bootstrap 5 generiert automatisch `--bs-*`-Properties für Farbwerte, Typography und Komponenten.
Im Shopware-Storefront wird das Bootstrap-Prefix `$prefix` = `bs-` genutzt.

Wichtige Bootstrap-Properties, die im Shopware-Skin verwendet werden:

### Buttons (an `.btn`-Elementen gesetzt)

| Property | Wo gesetzt | Verwendungszweck |
|---|---|---|
| `--bs-btn-focus-box-shadow` | `.header-search-btn`, `.btn-buy`, `.btn-link` | Focus-Ring anpassen |
| `--bs-btn-border-color` | `.header-search-btn` | Border-Farbe |
| `--bs-btn-hover-color` | `.header-search-btn`, `.header-actions-btn` | Hover-Farbe |
| `--bs-btn-hover-border-color` | `.header-search-btn` | Hover-Border |
| `--bs-btn-active-border-color` | `.header-actions-btn` | Active-Border |
| `--bs-btn-active-bg` | `.header-actions-btn` | Active-Background |
| `--bs-btn-hover-bg` | `.header-actions-btn` | Hover-Background |
| `--bs-btn-disabled-bg` | `.header-search-btn` | Disabled-Background |
| `--bs-btn-disabled-border-color` | `.header-search-btn` | Disabled-Border |
| `--bs-btn-disabled-color` | `.btn` | Disabled-Text-Farbe |
| `--bs-btn-color` | `.top-bar-nav-btn` | Button-Textfarbe |
| `--bs-btn-font-weight` | `.top-bar-nav-btn`, `.btn-link` | Font-Weight |
| `--bs-btn-border-width` | `.top-bar-nav-btn` | Border-Breite |
| `--bs-btn-padding-x` | `.top-bar-nav-btn`, `.btn-link-inline` | Horizontal-Padding |
| `--bs-btn-padding-y` | `.top-bar-nav-btn`, `.btn-link-inline` | Vertikal-Padding |
| `--bs-btn-line-height` | `.btn-link-inline` | Zeilenhöhe |
| `--bs-btn-font-size` | `.btn-link-inline` | Schriftgröße |

### Navbar

| Property | Wo gesetzt |
|---|---|
| `--bs-navbar-color` | `.main-navigation-menu` |
| `--bs-navbar-nav-link-padding-x` | `.main-navigation-menu` |

### Dropdown

| Property | Wo gesetzt |
|---|---|
| `--bs-dropdown-spacer` | `.main-navigation-menu .dropdown-menu::after` (calc) |
| `--bs-dropdown-link-hover-bg` | `.top-bar-list` |
| `--bs-dropdown-link-hover-color` | `.top-bar-list` |
| `--bs-dropdown-link-active-color` | `.top-bar-list` |
| `--bs-dropdown-link-active-bg` | `.top-bar-list` |

### Card

| Property | Wo gesetzt |
|---|---|
| `--bs-card-bg` | `.product-box` |
| `--bs-card-spacer-y` | `.product-box .card-body` |
| `--bs-card-spacer-x` | `.product-box .card-body` |
| `--bs-card-border-width` | `.card-tabs` |
| `--bs-card-cap-bg` | `.card-tabs .card-header` |
| `--bs-card-cap-padding-x` | `.card-tabs .card-header` |

### Nav/Tabs

| Property | Wo gesetzt |
|---|---|
| `--bs-nav-link-padding-x` | `.card-tabs .nav-link` |
| `--bs-nav-link-padding-y` | `.card-tabs .nav-link` |
| `--bs-nav-link-color` | `.card-tabs .nav-link` |
| `--bs-nav-link-hover-color` | `.card-tabs .nav-link` |
| `--bs-nav-tabs-border-width` | `.card-tabs .nav-link` |
| `--bs-nav-tabs-border-radius` | `.card-tabs .nav-link` |
| `--bs-nav-tabs-link-hover-border-color` | `.card-tabs .nav-link` |
| `--bs-nav-tabs-link-active-color` | `.card-tabs .nav-link` |
| `--bs-nav-tabs-link-active-border-color` | `.card-tabs .nav-link` |

### Alert

| Property | Wo gesetzt |
|---|---|
| `--bs-alert-border-color` | `.alert-{variant}` (via Loop) |
| `--bs-alert-bg` | `.alert-{variant}` (via Loop) |
| `--bs-alert-color` | `.alert-{variant}` (via Loop) |

### List Group

| Property | Wo gesetzt |
|---|---|
| `--bs-list-group-item-padding-x` | `.account-aside-item` |
| `--bs-list-group-action-active-color` | `.account-aside-item` |
| `--bs-list-group-action-active-bg` | `.account-aside-item` |
| `--bs-list-group-action-hover-color` | `.account-aside-item` |
| `--bs-list-group-action-hover-bg` | `.account-aside-item` |
| `--bs-list-group-border-width` | `.account-aside-item` |

### Modal

| Property | Wo gesetzt |
|---|---|
| `--bs-modal-box-shadow` | `.modal-content` |

---

## 3. Administration CSS Custom Properties

In `global.scss` werden **alle** SCSS-Variablen aus `variables.scss` automatisch als CSS Custom Properties registriert:

```scss
:root {
    @each $name, $value in meta.module-variables("variables") {
        --#{$name}: #{meta.inspect($value)};
    }
}
```

Das bedeutet: Jede `$variable` aus `variables.scss` wird zu `--variable` in `:root`.

Beispiele:
- `--color-gray-50` → `#f9fafb`
- `--color-shopware-brand-500` → `#189eff`
- `--font-size-s` → `16px`
- `--z-index-modal` → `1000`

Zusätzlich nutzt die Admin semantische Properties (aus dem Meteor Component Library):
- `--color-text-primary-default`
- `--color-text-brand-default`
- `--color-elevation-surface-sunken`
- `--color-background-secondary-default`
- `--color-border-primary-default`
- `--color-icon-brand-default`

Diese werden von der Meteor Component Library (`@shopware-ag/meteor-component-library`) bereitgestellt.

---

## Verwendung in Plugin/Theme-Overrides

Um eine CSS Custom Property aus dem Storefront in einem Plugin zu überschreiben:

```scss
// In deinem Plugin-SCSS:
:root {
    --buy-btn-bg: #ff6600;    // überschreibt den Kauf-Button-Hintergrund
    --price-color: #cc0000;   // überschreibt die Preisfarbe
}
```

Oder SCSS-Variable override (wird dann über CSS-Property abgeleitet):
```scss
// Muss VOR dem Core-Laden stehen (in variables.scss des Plugins):
$sw-color-buy-button: #ff6600 !default;  // FALSCH — !default wirkt nicht wenn bereits gesetzt
$sw-color-buy-button: #ff6600;           // Korrekt: ohne !default
```
