# Shopware 6 Storefront CSS Custom Properties

All `--*` variables of the Shopware 6 Storefront, grouped by origin and type.

---

## Contents

- [1. Storefront Core: `:root` definitions](#1-storefront-core-root-definitions)
- [2. Bootstrap 5 CSS Custom Properties (via `--bs-*`)](#2-bootstrap-5-css-custom-properties-via---bs-)
- [3. Administration CSS Custom Properties](#3-administration-css-custom-properties)
- [Usage in plugin/theme overrides](#usage-in-plugintheme-overrides)

## 1. Storefront Core: `:root` definitions

Defined in `abstract/variables/_css-properties.scss`.  
There, all custom properties are derived from the SCSS variables as `--name: #{$scss-var}`.

### Z-index properties

| Custom Property | SCSS source | Value |
|---|---|---|
| `--search-suggest-zindex` | `$search-suggest-zindex` | `1000` |
| `--offcanvas-zindex` | `$offcanvas-zindex` | `1050` |
| `--cookie-msg-zindex` | `$cookie-msg-zindex` | `1100` |
| `--scroll-up-zindex` | `$scroll-up-zindex` | `700` |
| `--menu-flyout-zindex` | `$menu-flyout-zindex` | `1030` |
| `--zoom-modal-action-zindex` | `$zoom-modal-action-zindex` | `1051` |
| `--magnifier-overlay-zindex` | `$magnifier-overlay-zindex` | `1100` |

### Icon properties

| Custom Property | SCSS source | Value |
|---|---|---|
| `--icon-base-size` | `$icon-base-size` | `1.375rem` |
| `--icon-base-color` | `$icon-base-color` | `#4a545b` |
| `--icon-review-color` | `$icon-review-color` | `#fedc70` |
| `--progress-bar-review` | `$progress-bar-review` | `#fedc70` |

### Layout/spacing properties

| Custom Property | SCSS source | Value |
|---|---|---|
| `--element-backdrop-bg` | `$element-backdrop-bg` | `rgba(#fff, 0.5)` |
| `--spacer-xs` | `$spacer-xs` | `$spacer * 0.25` |
| `--spacer-sm` | `$spacer-sm` | `$spacer * 0.5` |
| `--spacer-md` | `$spacer-md` | `$spacer` |
| `--spacer-lg` | `$spacer-lg` | `$spacer * 1.5` |
| `--spacer-xl` | `$spacer-xl` | `$spacer * 3` |

### E-commerce properties

| Custom Property | SCSS source | Value |
|---|---|---|
| `--buy-btn-bg` | `$buy-btn-bg` | `$sw-color-buy-button` → `#0042a0` |
| `--buy-btn-color` | `$buy-btn-color` | `$sw-color-buy-button-text` → `#fff` |
| `--disabled-btn-bg` | `$disabled-btn-bg` | `#eee` |
| `--disabled-btn-border-color` | `$disabled-btn-border-color` | `#eee` |
| `--price-color` | `$price-color` | `$sw-color-price` → `#2b3136` |

### CMS properties

| Custom Property | SCSS source | Value |
|---|---|---|
| `--cms-block-text-hero-hr-color` | `$cms-block-text-hero-hr-color` | `#e9edf0` |
| `--cms-element-text-quotes-color` | `$cms-element-text-quotes-color` | `#9aa7be` |
| `--cms-element-product-listing-gutter-width` | `$cms-element-product-listing-gutter-width` | `30px` |

### Typography properties

| Custom Property | SCSS source | Value |
|---|---|---|
| `--font-weight-semibold` | `$font-weight-semibold` | `600` |

---

## 2. Bootstrap 5 CSS Custom Properties (via `--bs-*`)

Bootstrap 5 automatically generates `--bs-*` properties for color values, typography and components.
In the Shopware Storefront the Bootstrap prefix `$prefix` = `bs-` is used.

Important Bootstrap properties that are used in the Shopware skin:

### Buttons (set on `.btn` elements)

| Property | Where set | Purpose |
|---|---|---|
| `--bs-btn-focus-box-shadow` | `.header-search-btn`, `.btn-buy`, `.btn-link` | Adjust focus ring |
| `--bs-btn-border-color` | `.header-search-btn` | Border color |
| `--bs-btn-hover-color` | `.header-search-btn`, `.header-actions-btn` | Hover color |
| `--bs-btn-hover-border-color` | `.header-search-btn` | Hover border |
| `--bs-btn-active-border-color` | `.header-actions-btn` | Active border |
| `--bs-btn-active-bg` | `.header-actions-btn` | Active background |
| `--bs-btn-hover-bg` | `.header-actions-btn` | Hover background |
| `--bs-btn-disabled-bg` | `.header-search-btn` | Disabled background |
| `--bs-btn-disabled-border-color` | `.header-search-btn` | Disabled border |
| `--bs-btn-disabled-color` | `.btn` | Disabled text color |
| `--bs-btn-color` | `.top-bar-nav-btn` | Button text color |
| `--bs-btn-font-weight` | `.top-bar-nav-btn`, `.btn-link` | Font weight |
| `--bs-btn-border-width` | `.top-bar-nav-btn` | Border width |
| `--bs-btn-padding-x` | `.top-bar-nav-btn`, `.btn-link-inline` | Horizontal padding |
| `--bs-btn-padding-y` | `.top-bar-nav-btn`, `.btn-link-inline` | Vertical padding |
| `--bs-btn-line-height` | `.btn-link-inline` | Line height |
| `--bs-btn-font-size` | `.btn-link-inline` | Font size |

### Navbar

| Property | Where set |
|---|---|
| `--bs-navbar-color` | `.main-navigation-menu` |
| `--bs-navbar-nav-link-padding-x` | `.main-navigation-menu` |

### Dropdown

| Property | Where set |
|---|---|
| `--bs-dropdown-spacer` | `.main-navigation-menu .dropdown-menu::after` (calc) |
| `--bs-dropdown-link-hover-bg` | `.top-bar-list` |
| `--bs-dropdown-link-hover-color` | `.top-bar-list` |
| `--bs-dropdown-link-active-color` | `.top-bar-list` |
| `--bs-dropdown-link-active-bg` | `.top-bar-list` |

### Card

| Property | Where set |
|---|---|
| `--bs-card-bg` | `.product-box` |
| `--bs-card-spacer-y` | `.product-box .card-body` |
| `--bs-card-spacer-x` | `.product-box .card-body` |
| `--bs-card-border-width` | `.card-tabs` |
| `--bs-card-cap-bg` | `.card-tabs .card-header` |
| `--bs-card-cap-padding-x` | `.card-tabs .card-header` |

### Nav/Tabs

| Property | Where set |
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

| Property | Where set |
|---|---|
| `--bs-alert-border-color` | `.alert-{variant}` (via loop) |
| `--bs-alert-bg` | `.alert-{variant}` (via loop) |
| `--bs-alert-color` | `.alert-{variant}` (via loop) |

### List Group

| Property | Where set |
|---|---|
| `--bs-list-group-item-padding-x` | `.account-aside-item` |
| `--bs-list-group-action-active-color` | `.account-aside-item` |
| `--bs-list-group-action-active-bg` | `.account-aside-item` |
| `--bs-list-group-action-hover-color` | `.account-aside-item` |
| `--bs-list-group-action-hover-bg` | `.account-aside-item` |
| `--bs-list-group-border-width` | `.account-aside-item` |

### Modal

| Property | Where set |
|---|---|
| `--bs-modal-box-shadow` | `.modal-content` |

---

## 3. Administration CSS Custom Properties

In `global.scss`, **all** SCSS variables from `variables.scss` are automatically registered as CSS custom properties:

```scss
:root {
    @each $name, $value in meta.module-variables("variables") {
        --#{$name}: #{meta.inspect($value)};
    }
}
```

This means: every `$variable` from `variables.scss` becomes `--variable` in `:root`.

Examples:
- `--color-gray-50` → `#f9fafb`
- `--color-shopware-brand-500` → `#189eff`
- `--font-size-s` → `16px`
- `--z-index-modal` → `1000`

In addition, the admin uses semantic properties (from the Meteor Component Library):
- `--color-text-primary-default`
- `--color-text-brand-default`
- `--color-elevation-surface-sunken`
- `--color-background-secondary-default`
- `--color-border-primary-default`
- `--color-icon-brand-default`

These are provided by the Meteor Component Library (`@shopware-ag/meteor-component-library`).

---

## Usage in plugin/theme overrides

To override a CSS custom property from the Storefront inside a plugin:

```scss
// In your plugin SCSS:
:root {
    --buy-btn-bg: #ff6600;    // overrides the buy button background
    --price-color: #cc0000;   // overrides the price color
}
```

Or override the SCSS variable (which is then derived via the CSS property):
```scss
// Must come BEFORE the core is loaded (in the plugin's variables.scss):
$sw-color-buy-button: #ff6600 !default;  // WRONG — !default has no effect if already set
$sw-color-buy-button: #ff6600;           // Correct: without !default
```
