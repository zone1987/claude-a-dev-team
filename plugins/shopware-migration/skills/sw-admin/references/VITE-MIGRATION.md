# Shopware 6 — Webpack → Vite (admin build)

6.7 switches the admin build from Webpack to **Vite**. Plugins usually only have to follow the new build
(entry `main.js` stays); custom Webpack configs are dropped/replaced.

- Port custom `build/webpack.config.js` adjustments to the Vite mechanics (if any exist).
- Asset/alias resolution via Vite; `import` instead of Webpack-specific loaders.
- Dev: `./bin/watch-administration.sh` (HMR). Build: `bin/console administration:build`.

Most standard plugins work without a build config change. Details/edge cases in the references of the
`shopware-6.7-migration` skill. The storefront build stays Webpack-based.

→ [../shopware-6.7-migration/`VITE-MIGRATION-BUILD-SYSTEM-MIGRATION.md`](../shopware-6.7-migration/`VITE-MIGRATION-BUILD-SYSTEM-MIGRATION.md`)
