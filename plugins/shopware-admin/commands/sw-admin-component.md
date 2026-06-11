---
name: sw-admin-component
description: Scaffold einer Admin-Komponente in Shopware 6 (Vue 3) — index.js (Component.register), .html.twig (Meteor mt-*), optional .scss; oder ein Component.override.
argument-hint: <component-name> [--plugin <PluginName>] [--override <coreComponent>]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /sw-admin-component

Erzeuge eine Admin-Komponente (oder ein Override). Skills: `sw-admin-component`, `sw-admin-component-override`,
`sw-meteor-components`, `sw-admin-styles`.

## Ablauf
1. Komponentenname (kebab, mit Owner-Präfix) + Ziel-Plugin. Bei `--override <coreComponent>` ein Override erzeugen.
2. Dateien in `.../component/<name>/` (oder `view/`): `index.js` (`Component.register` bzw. `Component.override`),
   `<name>.html.twig` (Meteor `mt-*`, bei Override `{% parent %}`), optional `<name>.scss`.
3. Bei Override: `this.$super('methode')` für Original-Logik, Block-Namen aus Core übernehmen.
4. In main.js / Modul importieren. Hinweis: Build + `eslint:admin`/`stylelint`.

Vor neuer Komponente Admin-Katalog prüfen (`/sw-admin-map`), ob etwas Passendes existiert.
