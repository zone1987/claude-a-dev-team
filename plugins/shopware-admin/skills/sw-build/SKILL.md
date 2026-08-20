---
name: sw-build
description: Shopware admin build: Vite configuration, TypeScript, SCSS and styles, static assets, snippets and translations. Use when configuring the Shopware administration build or its assets.
---

# Shopware Administration build and assets

Vite replaced Webpack in 6.7. Snippets are the translation mechanism for admin strings.

## Reference map

- **[ADMIN-ASSETS.md](ADMIN-ASSETS.md)**: Static plugin assets live under `src/Resources/app/administration/src/assets/` and are bundled by the Vite build….
- **[ADMIN-SNIPPETS.md](ADMIN-SNIPPETS.md)**: Admin translations as JSON under `module/<name>/snippet/<locale>.json`, registered in the module.
- **[ADMIN-STYLES.md](ADMIN-STYLES.md)**: One `.scss` per component next to `index.js`/`.twig`, imported in the component's `index.js`.
- **[ADMIN-TYPESCRIPT.md](ADMIN-TYPESCRIPT.md)**: The administration is TypeScript-capable. [ADMIN-TYPESCRIPT-TYPESCRIPT](ADMIN-TYPESCRIPT-TYPESCRIPT.md).
- **[ADMIN-VITE.md](ADMIN-VITE.md)**: 6.7 uses **Vite** for the admin build.

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) (Administration guides) and the Meteor design system documentation, retrieved 2026-08-20. Shopware 6.7 administration: Vue 3, Pinia, Vite.
