# Shopware 6 — Admin build (Vite)

6.7 uses **Vite** for the admin build (replacing Webpack). Plugin admin code lives under
`src/Resources/app/administration/src/` with `main.js` as the entry — Shopware includes it automatically.

```
ddev exec shopware-cli project admin-build --only-extensions <PluginName>   # Build
ddev exec shopware-cli project admin-watch --only-extensions <PluginName>   # Dev watcher (HMR)
```

No custom Webpack config handling needed any more; Vite adjustments go through the Shopware build mechanics. Assets/SCSS
are bundled along (`sw-admin-assets`, `sw-admin-styles`). Lint: `npm --prefix src/Resources/app/administration run lint`. For plugins migrating from
Webpack, see `shopware-migration` (`sw-vite-migration`).
