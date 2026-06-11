---
name: sw-vite-migration
description: >
  Migration des Admin-Builds von Webpack zu Vite (Shopware 6.7): Build-Konfiguration, Entry, Anpassungen, Watcher.
  Trigger: "Webpack zu Vite", "Vite migration admin", "admin build umstellen", "build system migration shopware".
  Shopware 6.7.
---

# Shopware 6 — Webpack → Vite (Admin-Build)

6.7 stellt den Admin-Build von Webpack auf **Vite** um. Plugins müssen i.d.R. nur dem neuen Build folgen
(Entry `main.js` bleibt); eigene Webpack-Configs entfallen/werden ersetzt.

- Eigene `build/webpack.config.js`-Anpassungen auf die Vite-Mechanik überführen (sofern vorhanden).
- Asset-/Alias-Auflösung über Vite; `import` statt Webpack-spezifischer Loader.
- Dev: `./bin/watch-administration.sh` (HMR). Build: `bin/console administration:build`.

Die meisten Standard-Plugins funktionieren ohne Build-Config-Änderung. Details/Edge-Cases in den References des Skills
`shopware-6.7-migration`. Storefront-Build bleibt Webpack-basiert.

→ [../shopware-6.7-migration/references/build-system-migration.md](../shopware-6.7-migration/references/build-system-migration.md)
