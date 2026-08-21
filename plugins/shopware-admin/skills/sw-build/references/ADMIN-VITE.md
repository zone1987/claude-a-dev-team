# Shopware 6 — Admin build (Vite)

6.7 uses **Vite** for the admin build (replacing Webpack). Plugin admin code lives under
`src/Resources/app/administration/src/` with `main.js` as the entry — Shopware includes it automatically.

```
bin/console administration:build      # Build
./bin/watch-administration.sh         # Dev watcher (HMR)
```

No custom Webpack config handling needed any more; Vite adjustments go through the Shopware build mechanics. Assets/SCSS
are bundled along (`sw-admin-assets`, `sw-admin-styles`). Lint: `composer eslint:admin`. For plugins migrating from
Webpack, see `shopware-migration` (`sw-vite-migration`).
