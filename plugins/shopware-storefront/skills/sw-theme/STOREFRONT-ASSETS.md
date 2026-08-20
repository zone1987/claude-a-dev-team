# Shopware 6 — Storefront assets

A plugin's static files live in `src/Resources/public/` and are published to `public/bundles/<plugin>/`
by `bin/console assets:install`. In the template use `asset()`:

```twig
<img src="{{ asset('bundles/ffplugin/img/logo.svg') }}">
```

**Media from the DAL** (media entity) are not included as assets but via `searchMedia(ids, context)` / `sw_thumbnails`
(responsive `srcset`). Provide custom icons as an SVG set via `sw_icon` (`sw-storefront-icons`). JS/SCSS assets
are bundled by the theme/webpack build (not placed in `public/`).
