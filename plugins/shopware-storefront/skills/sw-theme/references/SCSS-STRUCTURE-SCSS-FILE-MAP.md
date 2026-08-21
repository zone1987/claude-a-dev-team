# Shopware 6 Storefront SCSS — Complete File Map

Base: `src/Storefront/Resources/app/storefront/src/scss/`  
Trunk source: Shopware 6 Core (as of 2026).

---

## Contents

- [Entry points (via theme.json)](#entry-points-via-themejson)
- [abstract/ — Functions, mixins, variables (framework level)](#abstract--functions-mixins-variables-framework-level)
- [base/ — Global base styles](#base--global-base-styles)
- [component/ — UI components (structural, skin-neutral)](#component--ui-components-structural-skin-neutral)
- [layout/ — Page layout areas](#layout--page-layout-areas)
- [page/ — Page-specific styles](#page--page-specific-styles)
- [vendor/ — External dependencies](#vendor--external-dependencies)
- [skin/shopware/ — Shopware Default Visual Skin](#skinshopware--shopware-default-visual-skin)
- [Admin SCSS (delimitation)](#admin-scss-delimitation)

## Entry points (via theme.json)

| File | Purpose |
|---|---|
| `base.scss` | Main entry point: loads variables, vendor (Bootstrap/TinySlider/Flatpickr), base, all component/layout/page partials |
| `variables.scss` | Variable aggregator: loads Bootstrap overrides, skin variables, Bootstrap core, custom vars, CSS properties |
| `skin/shopware/_base.scss` | Shopware default skin entry: loads Inter font, base, typography, all skin component/layout/page partials |

---

## abstract/ — Functions, mixins, variables (framework level)

| File | Purpose |
|---|---|
| `abstract/functions/feature.scss` | SCSS function `feature($flag)` — checks feature flags from the `$sw-features` map (injected by ThemeCompiler/webpack) |
| `abstract/mixins/truncate-multiline.scss` | Mixin `truncate-multiline($line-height, $line-count, $bg-color)` — multi-line text truncation with `-webkit-line-clamp` |
| `abstract/variables/_bootstrap.scss` | Bootstrap overrides **without** skin/theme (structural changes only): container, modal transition, z-index levels, `$enable-important-utilities: false` |
| `abstract/variables/_custom.scss` | Own non-Bootstrap variables: z-index values, icon base, spacer XS…XL, asset path vars (`$sw-asset-theme-url`, `$theme-id`) |
| `abstract/variables/_css-properties.scss` | Exposes SCSS variables as CSS custom properties in `:root` (complete list → `css-custom-properties.md`) |

---

## base/ — Global base styles

| File | Purpose |
|---|---|
| `base/_base.scss` | HTML base: `no-scroll` class, `sw-text-editor-table` styles (tables from the rich text editor), hide `col-selector` |
| `base/_reboot.scss` | Storefront reboot: small additional reset beyond the Bootstrap reboot |

---

## component/ — UI components (structural, skin-neutral)

| File | Purpose |
|---|---|
| `component/_address-manager.scss` | Address management modal (account area) |
| `component/_alert.scss` | Bootstrap alert base styles |
| `component/_ar-overlay.scss` | AR (augmented reality) overlay layer |
| `component/_ar-qr-modal.scss` | AR QR code modal |
| `component/_ar-splash-screen.scss` | AR splash/loading screen |
| `component/_backdrop.scss` | Element backdrop (semi-transparent overlay, e.g. while loading) |
| `component/_base-slider.scss` | Base slider styles (TinySlider base) |
| `component/_basic-captcha.scss` | Basic captcha form field |
| `component/_card.scss` | Bootstrap card extensions |
| `component/_category-navigation.scss` | Category navigation (desktop dropdown) |
| `component/_cms-block.scss` | CMS block layout (shopping experiences) |
| `component/_cms-element.scss` | CMS element base styles (text, image, video, etc.) |
| `component/_cms-form-confirmation.scss` | Confirmation page CMS form |
| `component/_cms-sections.scss` | CMS section layout (full-width, sidebar, etc.) |
| `component/_delivery-status.scss` | Delivery status display |
| `component/_filter-boolean.scss` | Filter panel: boolean/yes-no filter |
| `component/_filter-multi-select.scss` | Filter panel: multi-select |
| `component/_filter-panel.scss` | Filter panel wrapper/container |
| `component/_filter-property-select.scss` | Filter panel: property filter |
| `component/_filter-range.scss` | Filter panel: range filter (price) |
| `component/_filter-rating-select.scss` | Filter panel: rating filter |
| `component/_flags.scss` | Country flag icons |
| `component/_forms.scss` | Form base styles (input, select, checkbox) |
| `component/_gallery-slider.scss` | Product gallery slider (detail page) |
| `component/_icon.scss` | Icon base styles (SVG icons) |
| `component/_image-slider.scss` | General image slider |
| `component/_line-item.scss` | Cart/order line items |
| `component/_loader.scss` | Loading spinner/overlay |
| `component/_magnifier.scss` | Product image magnifier/zoom hover |
| `component/_modal.scss` | Bootstrap modal base styles |
| `component/_notification-dot.scss` | Notification badge (cart counter) |
| `component/_offcanvas.scss` | Bootstrap offcanvas base styles |
| `component/_pagination.scss` | Pagination |
| `component/_payment-method.scss` | Payment method selection |
| `component/_product-box.scss` | Product tile (listing) |
| `component/_product-feature.scss` | Product property display |
| `component/_product-slider.scss` | Product slider (CMS element) |
| `component/_product-wishlist.scss` | Wishlist button/icon |
| `component/_quantity-selector.scss` | Quantity selection stepper |
| `component/_quickview-modal.scss` | Quickview modal (quick view) |
| `component/_shipping-method.scss` | Shipping method selection |
| `component/_sorting.scss` | Listing sorting (dropdown) |
| `component/_visibility.scss` | Visibility utility classes |
| `component/_zoom-modal.scss` | Product zoom modal |

---

## layout/ — Page layout areas

| File | Purpose |
|---|---|
| `layout/_account-menu.scss` | Account dropdown menu (header) |
| `layout/_container.scss` | Container overrides (max-width adjustments) |
| `layout/_cookie-configuration.scss` | Cookie settings modal |
| `layout/_cookie-permission.scss` | Cookie banner |
| `layout/_footer.scss` | Footer structure |
| `layout/_header.scss` | Header structure (logo, search, actions) |
| `layout/_header-minimal.scss` | Minimal header (e.g. checkout) |
| `layout/_navigation-offcanvas.scss` | Mobile navigation offcanvas (structure) |
| `layout/_offcanvas-cart.scss` | Cart offcanvas (structure) |
| `layout/_recaptcha.scss` | reCAPTCHA integration |
| `layout/_scroll-up.scss` | Scroll-to-top button |
| `layout/_search-suggest.scss` | Search suggestions dropdown |

---

## page/ — Page-specific styles

### page/account/
| File | Purpose |
|---|---|
| `page/account/_account.scss` | Account page wrapper |
| `page/account/_address.scss` | Address management |
| `page/account/_edit-order.scss` | Edit order afterwards |
| `page/account/_order.scss` | Order overview |
| `page/account/_order-detail.scss` | Order detail |
| `page/account/_overview.scss` | Account overview |
| `page/account/_register.scss` | Registration page |

### page/checkout/
| File | Purpose |
|---|---|
| `page/checkout/_aside.scss` | Checkout sidebar (summary) |
| `page/checkout/_cart.scss` | Cart page |
| `page/checkout/_checkout.scss` | Checkout wrapper |
| `page/checkout/_confirm.scss` | Checkout confirmation step |
| `page/checkout/_finish.scss` | Checkout finish page |
| `page/checkout/_register.scss` | Checkout guest order/registration |

### page/product-detail/
| File | Purpose |
|---|---|
| `page/product-detail/_configurator.scss` | Variant configurator (swatches, dropdowns) |
| `page/product-detail/_product-detail.scss` | Product detail page wrapper |
| `page/product-detail/_review.scss` | Product reviews |
| `page/product-detail/_tabs.scss` | Tab navigation (description, properties) |

### page/search/
| File | Purpose |
|---|---|
| `page/search/_search.scss` | Search result page |

### page/wishlist/
| File | Purpose |
|---|---|
| `page/wishlist/_wishlist.scss` | Wishlist page |

---

## vendor/ — External dependencies

| File | Purpose |
|---|---|
| `vendor/_bootstrap.scss` | Bootstrap 5.x complete import (`~vendor/bootstrap/scss/bootstrap`) |
| `vendor/_datepicker.scss` | Flatpickr datepicker styles |
| `vendor/_tiny-slider.scss` | TinySlider slider styles |

---

## skin/shopware/ — Shopware Default Visual Skin

Overrides/complements the structural styles with visual styles.
All files live under `skin/shopware/`.

### skin/shopware/abstract/

| File | Purpose |
|---|---|
| `abstract/_variables.scss` | Import aggregator: loads `_theme.scss`, `_bootstrap.scss`, `_custom.scss` |
| `abstract/variables/_theme.scss` | **Theme variables** (all `$sw-*` variables — colors, fonts, logos) |
| `abstract/variables/_bootstrap.scss` | Bootstrap overrides WITH theme colors (colors, typography, buttons, forms, etc.) |
| `abstract/variables/_custom.scss` | Custom non-Bootstrap vars with theme color references (`$buy-btn-bg`, `$price-color`, etc.) |
| `abstract/mixins/` | (empty, `.gitkeep`) |

### skin/shopware/base/

| File | Purpose |
|---|---|
| `base/_base.scss` | `body` globally: font smoothing, min-height 100vh, flex-column |
| `base/_typography.scss` | Heading line heights, blockquote styling, list margin |

### skin/shopware/component/

| File | Purpose |
|---|---|
| `component/_alert.scss` | Alert colors via `$theme-colors` loop, icon spacing |
| `component/_badge.scss` | Badge height (20px/28px), box-sizing |
| `component/_breadcrumb.scss` | Breadcrumb links (color, hover → primary), active weight |
| `component/_button.scss` | `.btn-buy` (Bootstrap variant with `$buy-btn-bg`), `.btn-link-inline`, focus box-shadow loop |
| `component/_card.scss` | Card background via `$body-bg` |
| `component/_cms-block.scss` | CMS block visual adjustments |
| `component/_cms-element.scss` | CMS element visual adjustments |
| `component/_custom-select.scss` | Custom select styling |
| `component/_form.scss` | Form: `.form-group` spacing, validation box-shadow, `.form-required-label` (danger color) |
| `component/_modal.scss` | Modal box-shadow, title line height, back button icon |
| `component/_pagination.scss` | Page link height/min-width |
| `component/_product-box.scss` | `.product-box` border, `.product-name` weight, `.product-price` color |
| `component/_quickview-modal.scss` | Quickview modal visual styling |
| `component/_tab-menu.scss` | `.card-tabs` tab navigation: colors, border-bottom indicator |

### skin/shopware/layout/

| File | Purpose |
|---|---|
| `layout/_header.scss` | Header: search input/button styles, actions button hover, cart total color |
| `layout/_footer.scss` | Footer: border-top, column headlines (primary), links, bottom background |
| `layout/_main-navigation.scss` | Desktop navigation: active border indicator (primary), dropdown overlay |
| `layout/_navigation-flyout.scss` | Navigation flyout: links (color, hover indentation, bold level 0) |
| `layout/_navigation-offcanvas.scss` | Mobile nav offcanvas: list item border, active link color (primary) |
| `layout/_offcanvas-cart.scss` | Cart offcanvas: header count (`$text-muted`), tax notice |
| `layout/_top-bar.scss` | Top bar buttons: color, padding, hover (primary), dropdown active |

### skin/shopware/page/account/

| File | Purpose |
|---|---|
| `page/account/_aside.scss` | Account sidebar: header bold, list items without border, active = primary |
| `page/account/_address.scss` | Address card styles |
| `page/account/_order.scss` | Order overview table |
| `page/account/_order-detail.scss` | Order detail view |
| `page/account/_profile.scss` | Profile page styles |
| `page/account/_register.scss` | Registration form (skin) |

### skin/shopware/page/checkout/

| File | Purpose |
|---|---|
| `page/checkout/_aside.scss` | Checkout sidebar summary: `$light` background, spacing |
| `page/checkout/_cart.scss` | Cart table: remove mobile border |

### skin/shopware/page/contact/

| File | Purpose |
|---|---|
| `page/contact/_contact.scss` | Contact form page |

### skin/shopware/page/newsletter/

| File | Purpose |
|---|---|
| `page/newsletter/_newsletter.scss` | Newsletter subscription page |

### skin/shopware/page/product-detail/

| File | Purpose |
|---|---|
| `page/product-detail/_product-detail.scss` | Product name (headline color), prices (danger for list price), strikethrough prices, order number |
| `page/product-detail/_tabs.scss` | Tab navigation: responsive flex-direction, preview text, tab link styles |
| `page/product-detail/_review.scss` | Reviews area |
| `page/product-detail/_cross-selling.scss` | Cross-selling tabs: mobile = all expanded, desktop = tab navigation |

### skin/shopware/vendor/

| File | Purpose |
|---|---|
| `vendor/_inter-fontface.scss` | Inter font @font-face declarations (variable font, several unicode ranges: Latin, Cyrillic, Greek, Vietnamese) |

---

## Admin SCSS (delimitation)

Base: `src/Administration/Resources/app/administration/src/app/assets/scss/`

| File | Purpose |
|---|---|
| `all.scss` | Entry point: loads variables, typography, global, directives, pages |
| `variables.scss` | All admin design tokens (color palette, typography, z-index, border radius) |
| `global.scss` | Global base styles; automatically generates CSS custom properties via `@each meta.module-variables("variables")` |
| `typography.scss` | Admin typography styles |
| `mixins.scss` | Admin SCSS mixins |
| `directives/tooltip.scss` | Tooltip directive styles |
| `directives/dragdrop.scss` | Drag-and-drop directive styles |
| `pages/error.scss` | Error page styles (500, 404) |

Admin SCSS is **completely separate from Storefront SCSS** — no shared variables.
