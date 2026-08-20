---
name: sw-build
description: Shopware admin build: Vite configuration, TypeScript, SCSS and styles, static assets, snippets and translations. Use when configuring the Shopware administration build or its assets.
---

# Shopware Administration build and assets

Vite replaced Webpack in 6.7. Snippets are the translation mechanism for admin strings.

## Reference map

- **[ADMIN-ASSETS.md](ADMIN-ASSETS.md)**: Statische Plugin-Assets liegen unter `src/Resources/app/administration/src/assets/` und werden vom Vite-Build….
- **[ADMIN-SNIPPETS.md](ADMIN-SNIPPETS.md)**: Admin-Übersetzungen als JSON unter `module/<name>/snippet/<locale>.json`, im Modul registriert.
- **[ADMIN-STYLES.md](ADMIN-STYLES.md)**: Pro Komponente eine `.scss` neben `index.js`/`.twig`, importiert im Komponenten-`index.js`.
- **[ADMIN-TYPESCRIPT.md](ADMIN-TYPESCRIPT.md)**: Die Administration ist TypeScript-fähig. [ADMIN-TYPESCRIPT-TYPESCRIPT](ADMIN-TYPESCRIPT-TYPESCRIPT.md).
- **[ADMIN-VITE.md](ADMIN-VITE.md)**: 6.7 nutzt **Vite** für den Admin-Build.

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) (Administration guides) and the Meteor design system documentation, retrieved 2026-08-20. Shopware 6.7 administration: Vue 3, Pinia, Vite.
