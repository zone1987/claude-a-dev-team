# Shopware 6 — Admin-Build (Vite)

6.7 nutzt **Vite** für den Admin-Build (löst Webpack ab). Plugin-Admin-Code unter
`src/Resources/app/administration/src/` mit `main.js` als Entry — Shopware bindet ihn automatisch ein.

```
bin/console administration:build      # Build
./bin/watch-administration.sh         # Dev-Watcher (HMR)
```

Kein eigenes Webpack-Config-Handling mehr nötig; Vite-Anpassungen über die Shopware-Build-Mechanik. Assets/SCSS
werden mitgebündelt (`sw-admin-assets`, `sw-admin-styles`). Lint: `composer eslint:admin`. Für Plugins, die von
Webpack migrieren, siehe `shopware-migration` (`sw-vite-migration`).
