# Shopware 6 — Storefront-Assets

Statische Dateien eines Plugins liegen in `src/Resources/public/` und werden per `bin/console assets:install`
nach `public/bundles/<plugin>/` veröffentlicht. Im Template über `asset()`:

```twig
<img src="{{ asset('bundles/ffplugin/img/logo.svg') }}">
```

**Medien aus dem DAL** (Media-Entity) nicht als Asset, sondern via `searchMedia(ids, context)` / `sw_thumbnails`
einbinden (responsive `srcset`). Eigene Icons als SVG-Set über `sw_icon` (`sw-storefront-icons`). JS/SCSS-Assets
werden über den Theme-/Webpack-Build gebündelt (nicht in `public/`).
