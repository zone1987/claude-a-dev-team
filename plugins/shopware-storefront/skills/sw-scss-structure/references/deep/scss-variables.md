# Shopware 6 Storefront SCSS-Variablen

Alle SCSS-Variablen mit Default-Werten, gruppiert nach Herkunft.  
Quelle: `src/Storefront/Resources/app/storefront/src/scss/`

---

## 1. Theme-Variablen (`skin/shopware/abstract/variables/_theme.scss`)

Diese Variablen sind die **konfigurierbaren Kern-Design-Tokens** des Shopware-Themes.  
Sie sind identisch mit den `config.fields`-Einträgen in `theme.json` und werden vom
Theme-Manager im Admin überschreibbar gemacht.

### Farben

| Variable | Default | theme.json-Field | Block |
|---|---|---|---|
| `$sw-color-brand-primary` | `#0042a0` | `sw-color-brand-primary` | themeColors |
| `$sw-color-brand-secondary` | `#474a57` | `sw-color-brand-secondary` | themeColors |
| `$sw-color-price` | `#2b3136` | `sw-color-price` | eCommerce |
| `$sw-color-success` | `#007e4e` | `sw-color-success` | statusColors |
| `$sw-color-info` | `#005b99` | `sw-color-info` | statusColors |
| `$sw-color-warning` | `#974200` | `sw-color-warning` | statusColors |
| `$sw-color-danger` | `#c20017` | `sw-color-danger` | statusColors |
| `$sw-background-color` | `#fff` | `sw-background-color` | themeColors |
| `$sw-text-color` | `#2b3136` | `sw-text-color` | typography |
| `$sw-headline-color` | `#2b3136` | `sw-headline-color` | typography |
| `$sw-border-color` | `#798490` | `sw-border-color` | themeColors |
| `$sw-color-buy-button` | `#0042a0` | `sw-color-buy-button` | eCommerce |
| `$sw-color-buy-button-text` | `#fff` | `sw-color-buy-button-text` | eCommerce |

### Typografie

| Variable | Default | theme.json-Field | Block |
|---|---|---|---|
| `$sw-font-family-base` | `'Inter', sans-serif` | `sw-font-family-base` | typography |
| `$sw-font-family-headline` | `'Inter', sans-serif` | `sw-font-family-headline` | typography |

### Logos

| Variable | Default |
|---|---|
| `$sw-logo-default` | `url('logo.png')` |
| `$sw-logo-default-sm` | `url('logo.png')` |
| `$sw-logo-default-md` | `url('logo.png')` |
| `$sw-logo-default-lg` | `url('logo.png')` |
| `$sw-logo-default-xl` | `url('logo.png')` |
| `$sw-logo-share` | `url('logo-share.png')` |
| `$sw-logo-favicon` | `url('logo-favicon.png')` |
| `$sw-logo-app-icon` | `url('logo-app-icon.png')` |

### Breakpoints (via theme.json, nicht direkt als SCSS-Var)

Werden als Bootstrap-Breakpoints `$grid-breakpoints` gemappt:

| theme.json-Field | Wert |
|---|---|
| `sw-breakpoint-xs` | 0 |
| `sw-breakpoint-sm` | 576 |
| `sw-breakpoint-md` | 768 |
| `sw-breakpoint-lg` | 992 |
| `sw-breakpoint-xl` | 1200 |
| `sw-breakpoint-xxl` | 1400 |

---

## 2. Bootstrap-Overrides MIT Theme-Farben (`skin/shopware/abstract/variables/_bootstrap.scss`)

Diese Datei überschreibt Bootstrap-Variablen und nutzt dabei die `$sw-*`-Theme-Variablen als Werte.

### Farb-System

| Variable | Default |
|---|---|
| `$gray-100` | `#f9f9f9` |
| `$gray-200` | `#eee` |
| `$gray-300` | `#bcc1c7` |
| `$gray-600` | `#798490` |
| `$gray-800` | `#4a545b` |
| `$primary` | `$sw-color-brand-primary` |
| `$secondary` | `$sw-color-brand-secondary` |
| `$success` | `$sw-color-success` |
| `$info` | `$sw-color-info` |
| `$warning` | `$sw-color-warning` |
| `$danger` | `$sw-color-danger` |
| `$light` | `$gray-100` |
| `$dark` | `$gray-800` |

### Body / Layout

| Variable | Default |
|---|---|
| `$body-bg` | `$sw-background-color` |
| `$body-color` | `$sw-text-color` |
| `$body-secondary-color` | `$sw-text-color` |
| `$border-color` | `$sw-border-color` |
| `$grid-gutter-width` | `40px` |
| `$border-radius` | `0` |
| `$border-radius-lg` | `0` |
| `$border-radius-sm` | `0` |

### Typografie

| Variable | Default |
|---|---|
| `$headings-color` | `$sw-headline-color` |
| `$headings-font-weight` | `700` |
| `$headings-font-family` | `$sw-font-family-headline` |
| `$font-family-base` | `$sw-font-family-base` |
| `$font-size-base` | `1rem` |
| `$font-size-lg` | `1.125rem` |
| `$font-size-sm` | `0.875rem` |
| `$font-weight-normal` | `400` |
| `$h1-font-size` | `36px` |
| `$h2-font-size` | `28px` |
| `$h3-font-size` | `24px` |
| `$h4-font-size` | `20px` |
| `$h5-font-size` | `16px` |
| `$h6-font-size` | `14px` |
| `$nav-link-font-size` | `$font-size-base` |
| `$paragraph-margin-bottom` | `2rem` |
| `$link-decoration` | `underline` |
| `$link-hover-decoration` | `underline` |

### Buttons

| Variable | Default |
|---|---|
| `$btn-padding-y` | `2px` |
| `$btn-padding-x` | `12px` |
| `$btn-line-height` | `2.125rem` |
| `$btn-white-space` | `nowrap` |
| `$btn-padding-y-sm` | `2px` |
| `$btn-padding-x-sm` | `12px` |
| `$btn-font-size-sm` | `14px` |
| `$btn-line-height-sm` | `1.875rem` |
| `$btn-padding-y-lg` | `2px` |
| `$btn-padding-x-lg` | `12px` |
| `$btn-font-size-lg` | `16px` |
| `$btn-line-height-lg` | `2.375rem` |
| `$btn-font-weight` | `600` |
| `$btn-disabled-opacity` | `1` |
| `$btn-link-disabled-color` | `$gray-300` |

### Forms / Inputs

| Variable | Default |
|---|---|
| `$input-padding-y` | `0.438rem` |
| `$input-padding-x` | `0.5625rem` |
| `$input-placeholder-color` | `#666977` |
| `$input-color` | `$sw-text-color` |
| `$input-border-color` | `$sw-border-color` |
| `$input-focus-border-color` | `$sw-color-brand-primary` |
| `$form-label-margin-bottom` | `3px` |
| `$form-check-input-border` | `1px solid $sw-border-color` |
| `$form-check-input-width` | `1rem` |
| `$form-check-padding-start` | `1.5rem` |
| `$enable-validation-icons` | `false` |

### Focus Ring (Accessibility)

| Variable | Default |
|---|---|
| `$focus-ring-width` | `0.25rem` |
| `$focus-ring-opacity` | `1` |
| `$focus-ring-color` | `rgba($primary, 1)` |
| `$focus-ring-blur` | `0` |
| `$focus-ring-box-shadow` | `0 0 0 0.125rem $body-bg, 0 0 0 0.25rem $focus-ring-color` |
| `$focus-ring-box-shadow-inset` | `inset 0 0 0 0.125rem $focus-ring-color, inset 0 0 0 0.25rem $body-bg` |

### Pagination

| Variable | Default |
|---|---|
| `$pagination-color` | `$sw-text-color` |
| `$pagination-hover-color` | `$sw-text-color` |
| `$pagination-border-width` | `0` |
| `$pagination-padding-y` | `0.595rem` |
| `$pagination-padding-x` | `0.75rem` |
| `$pagination-disabled-color` | `$gray-600` |
| `$pagination-disabled-bg` | `transparent` |

### Modal

| Variable | Default |
|---|---|
| `$modal-content-border-width` | `0` |
| `$modal-content-box-shadow-xs` | `0 43px 43px -6px rgba(#000, 0.2)` |
| `$modal-content-box-shadow-sm-up` | `0 43px 43px -6px rgba(#000, 0.2)` |

### Offcanvas

| Variable | Default |
|---|---|
| `$offcanvas-padding-y` | `$grid-gutter-width / 2` |
| `$offcanvas-padding-x` | `$grid-gutter-width / 2` |
| `$offcanvas-border-width` | `0` |
| `$offcanvas-backdrop-opacity` | `1` |

### Alerts

| Variable | Default |
|---|---|
| `$alert-padding-x` | `0.5rem` |
| `$alert-padding-y` | `0.5rem` |
| `$alert-border-width` | `1px` |

### Badges

| Variable | Default |
|---|---|
| `$badge-font-size` | `12px` |
| `$badge-border-radius` | `50px` |
| `$badge-padding-x` | `5px` |
| `$badge-padding-y` | `0` |

### Cards

| Variable | Default |
|---|---|
| `$card-border-color` | `transparent` |
| `$card-bg` | `transparent` |
| `$card-spacer-y` | `0` |
| `$card-spacer-x` | `0` |

### Tables

| Variable | Default |
|---|---|
| `$table-striped-bg` | `#f9f9f9` |
| `$table-color` | `$sw-text-color` |

### Sonstiges

| Variable | Default |
|---|---|
| `$breadcrumb-bg` | `transparent` |
| `$breadcrumb-border-radius` | `0` |
| `$dropdown-border-color` | `$sw-border-color` |
| `$spinner-width` | `26px` |
| `$spinner-border-width` | `2px` |
| `$navbar-light-active-color` | `$primary` |

---

## 3. Custom-Variablen MIT Theme-Referenzen (`skin/shopware/abstract/variables/_custom.scss`)

| Variable | Default |
|---|---|
| `$buy-btn-bg` | `$sw-color-buy-button` |
| `$buy-btn-color` | `$sw-color-buy-button-text` |
| `$disabled-btn-bg` | `#eee` |
| `$disabled-btn-border-color` | `#eee` |
| `$cms-block-text-hero-hr-color` | `#e9edf0` |
| `$cms-element-text-quotes-color` | `#9aa7be` |
| `$cms-element-product-listing-gutter-width` | `30px` |
| `$price-color` | `$sw-color-price` |
| `$font-weight-semibold` | `600` |
| `$order-grid-gutter-width` | `20px` |

---

## 4. Bootstrap-Basis-Overrides OHNE Theme-Farben (`abstract/variables/_bootstrap.scss`)

Wird geladen **bevor** Skin-Variablen; enthält keine Farbwerte.

| Variable | Default |
|---|---|
| `$enable-responsive-font-sizes` | `true` |
| `$modal-backdrop-bg` | `rgba(#000, 0.5)` |
| `$modal-transition` | `opacity 0.45s cubic-bezier(0.3, 0, 0.15, 1), visibility 0.45s linear` |
| `$container-max-widths` | `(xs: 1400px)` |
| `$enable-validation-icons` | `true` |
| `$enable-important-utilities` | `false` |
| `$zindex-levels` | `(n1: -1, 0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5)` |

---

## 5. Framework Custom-Variablen (`abstract/variables/_custom.scss`)

| Variable | Default |
|---|---|
| `$search-suggest-zindex` | `1000` |
| `$offcanvas-zindex` | `1050` |
| `$cookie-msg-zindex` | `1100` |
| `$scroll-up-zindex` | `700` |
| `$menu-flyout-zindex` | `1030` |
| `$zoom-modal-action-zindex` | `1051` |
| `$magnifier-overlay-zindex` | `1100` |
| `$icon-base-size` | `1.375rem` |
| `$icon-base-color` | `#4a545b` |
| `$icon-review-color` | `#fedc70` |
| `$progress-bar-review` | `$icon-review-color` |
| `$element-backdrop-bg` | `rgba(#fff, 0.5)` |
| `$spacer-xs` | `$spacer * 0.25` |
| `$spacer-sm` | `$spacer * 0.5` |
| `$spacer-md` | `$spacer` |
| `$spacer-lg` | `$spacer * 1.5` |
| `$spacer-xl` | `$spacer * 3` |
| `$sw-asset-theme-url` | `''` |
| `$sw-features` | `()` |
| `$theme-id` | `''` |
| `$app-css-relative-asset-path` | `'../../' + $theme-id + '/assets'` |

---

## 6. Mixins / Functions

| Name | Datei | Signatur |
|---|---|---|
| `truncate-multiline` | `abstract/mixins/truncate-multiline.scss` | `@mixin truncate-multiline($line-height: 1.2em, $line-count: 2, $bg-color: white)` |
| `feature` | `abstract/functions/feature.scss` | `@function feature($feature-flag)` — gibt `map-get($sw-features, $flag)` zurück |

---

## 7. Admin-SCSS-Variablen (`src/Administration/.../scss/variables.scss`)

Separate Palette, nur für die Administration. Kein Bezug zu Storefront-Variablen.

### Grau-Palette (Grayish blue)
`$color-gray-50…900`: `#f9fafb` bis `#758ca3`

### Dunkelgrau-Palette
`$color-darkgray-50…900`: `#667f99` bis `#0a0d0f`

### Shopware Brand (Vivid blue)
`$color-shopware-brand-50…900`: `#e3f3ff` bis `#0870ff`

### Status-Farben
- Emerald (Grün): `$color-emerald-50…900`
- Pumpkin Spice (Orange): `$color-pumpkin-spice-50…900`
- Crimson (Rot): `$color-crimson-50…900`

### Modul-Farben
`$color-module-yellow/orange/pink/blue/purple/green-50…900`

### Typografie

| Variable | Default |
|---|---|
| `$font-family-default` | `"Inter", -apple-system, ...` |
| `$font-size-xxs` | `12px` |
| `$font-size-xs` | `14px` |
| `$font-size-s` | `16px` |
| `$font-size-m` | `18px` |
| `$font-size-l` | `20px` |
| `$font-size-xl` | `24px` |
| `$font-size-3xl` | `28px` |

### Z-Index Admin

| Variable | Wert |
|---|---|
| `$z-index-modal` | `1000` |
| `$z-index-notifications` | `1200` |
| `$z-index-dragdrop` | `1400` |
| `$z-index-help-sidebar` | `1500` |
