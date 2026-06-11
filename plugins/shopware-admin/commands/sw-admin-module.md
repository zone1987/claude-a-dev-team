---
name: sw-admin-module
description: Scaffold eines Admin-Moduls in Shopware 6 (Vue 3) — module/<name>/index.js mit Module.register, List/Detail-Pages, Navigation, Snippets, ACL.
argument-hint: <module-name> [--plugin <PluginName>] [--entity <entity>]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /sw-admin-module

Erzeuge ein Admin-Modul. Skills: `sw-admin-module`, `sw-admin-component`, `sw-admin-routing`, `sw-admin-menu`,
`sw-admin-data-handling`, `sw-admin-acl-permissions`, `sw-meteor-components`.

## Ablauf
1. Modulname (kebab, mit Owner-Präfix z.B. `ff-example`) + Ziel-Plugin (+ optional gebundene Entity) bestimmen.
2. Struktur `src/Resources/app/administration/src/module/<name>/`:
   - `index.js` (`Module.register` mit routes list/detail, navigation, snippets, optional settingsItem)
   - `page/<name>-list/` + `page/<name>-detail/` (je `index.js` + `.html.twig`, Meteor `mt-*`)
   - `snippet/de-DE.json` + `en-GB.json`
   - ACL-Privileges (`addPrivilegeMappingEntry`) + `acl`-Service-Datei
3. In `main.js` importieren. Hinweis: Admin-Watcher/Build + `eslint:admin`.

Daten via `repositoryFactory` (bei `--entity`). UI mit `mt-*`. Bestehende Module nicht überschreiben.
