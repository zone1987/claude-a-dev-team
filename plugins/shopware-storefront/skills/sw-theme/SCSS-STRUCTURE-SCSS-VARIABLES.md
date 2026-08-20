# Shopware 6 Storefront SCSS variables

All SCSS variables with default values, grouped by origin.  
Source: `src/Storefront/Resources/app/storefront/src/scss/`

---

## Contents

- [1. Theme variables (`skin/shopware/abstract/variables/_theme.scss`)](#1-theme-variables-skinshopwareabstractvariables_themescss)
- [2. Bootstrap overrides WITH theme colors (`skin/shopware/abstract/variables/_bootstrap.scss`)](#2-bootstrap-overrides-with-theme-colors-skinshopwareabstractvariables_bootstrapscss)
- [3. Custom variables WITH theme references (`skin/shopware/abstract/variables/_custom.scss`)](#3-custom-variables-with-theme-references-skinshopwareabstractvariables_customscss)
- [4. Bootstrap base overrides WITHOUT theme colors (`abstract/variables/_bootstrap.scss`)](#4-bootstrap-base-overrides-without-theme-colors-abstractvariables_bootstrapscss)
- [5. Framework custom variables (`abstract/variables/_custom.scss`)](#5-framework-custom-variables-abstractvariables_customscss)
- [6. Mixins / Functions](#6-mixins-functions)
- [7. Admin SCSS variables (`src/Administration/.../scss/variables.scss`)](#7-admin-scss-variables-srcadministrationscssvariablesscss)

## 1. Theme variables (`skin/shopware/abstract/variables/_theme.scss`)

These variables are the **configurable core design tokens** of the Shopware theme.  
They are identical to the `config.fields` entries in `theme.json` and are made
overridable by the Theme Manager in the admin.

### Colors

| Variable | Default | theme.json field | Block |
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

### Typography

| Variable | Default | theme.json field | Block |
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

### Breakpoints (via theme.json, not directly as an SCSS var)

They are mapped to the Bootstrap breakpoints `$grid-breakpoints`:

| theme.json field | Value |
|---|---|
| `sw-breakpoint-xs` | 0 |
| `sw-breakpoint-sm` | 576 |
| `sw-breakpoint-md` | 768 |
| `sw-breakpoint-lg` | 992 |
| `sw-breakpoint-xl` | 1200 |
| `sw-breakpoint-xxl` | 1400 |

---

## 2. Bootstrap overrides WITH theme colors (`skin/shopware/abstract/variables/_bootstrap.scss`)

This file overrides Bootstrap variables and uses the `$sw-*` theme variables as values.

### Color system

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

### Typography

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

### Miscellaneous

| Variable | Default |
|---|---|
| `$breadcrumb-bg` | `transparent` |
| `$breadcrumb-border-radius` | `0` |
| `$dropdown-border-color` | `$sw-border-color` |
| `$spinner-width` | `26px` |
| `$spinner-border-width` | `2px` |
| `$navbar-light-active-color` | `$primary` |

---

## 3. Custom variables WITH theme references (`skin/shopware/abstract/variables/_custom.scss`)

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

## 4. Bootstrap base overrides WITHOUT theme colors (`abstract/variables/_bootstrap.scss`)

Loaded **before** the skin variables; contains no color values.

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

## 5. Framework custom variables (`abstract/variables/_custom.scss`)

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

| Name | File | Signature |
|---|---|---|
| `truncate-multiline` | `abstract/mixins/truncate-multiline.scss` | `@mixin truncate-multiline($line-height: 1.2em, $line-count: 2, $bg-color: white)` |
| `feature` | `abstract/functions/feature.scss` | `@function feature($feature-flag)` — returns `map-get($sw-features, $flag)` |

---

## 7. Admin SCSS variables (`src/Administration/.../scss/variables.scss`)

Separate palette, for the administration only. No relation to Storefront variables.

### Gray palette (grayish blue)
`$color-gray-50…900`: `#f9fafb` to `#758ca3`

### Dark gray palette
`$color-darkgray-50…900`: `#667f99` to `#0a0d0f`

### Shopware Brand (vivid blue)
`$color-shopware-brand-50…900`: `#e3f3ff` to `#0870ff`

### Status colors
- Emerald (green): `$color-emerald-50…900`
- Pumpkin Spice (orange): `$color-pumpkin-spice-50…900`
- Crimson (red): `$color-crimson-50…900`

### Module colors
`$color-module-yellow/orange/pink/blue/purple/green-50…900`

### Typography

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

### Z-index admin

| Variable | Value |
|---|---|
| `$z-index-modal` | `1000` |
| `$z-index-notifications` | `1200` |
| `$z-index-dragdrop` | `1400` |
| `$z-index-help-sidebar` | `1500` |
