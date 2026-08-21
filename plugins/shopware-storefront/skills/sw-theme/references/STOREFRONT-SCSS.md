# Shopware 6 — Storefront SCSS

Plugin styles live in `src/Resources/app/storefront/src/scss/base.scss` and are automatically included in the
theme compilation (no manual import needed). Bootstrap 5 is available.

```scss
// src/Resources/app/storefront/src/scss/base.scss
.ff-hint {
    color: $color-primary;          // theme/Bootstrap variables are usable
    @include media-breakpoint-up(md) { font-size: 1rem; }
}
```

Compiled via `bin/console theme:compile` (or the watcher). Expose configurable values as SCSS variables
(`sw-scss-variables`). Lint: `composer stylelint`. Put larger UI logic into JS plugins (`sw-storefront-js-plugin`).
