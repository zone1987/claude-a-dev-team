---
name: sw-admin-module
description: Scaffolds an administration module in Shopware 6 — Module.register with its routes, navigation, snippets, list and detail pages, and ACL privileges.
argument-hint: <module-name> [--plugin <PluginName>] [--entity <entity>]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /sw-admin-module

Produce an admin module. Skills: `sw-components`, `sw-data`, `sw-meteor`.

## Steps
1. Settle the module name (kebab-case with an owner prefix, e.g. `ff-example`), the target plugin,
   and optionally the entity it is bound to.
2. Build `src/Resources/app/administration/src/module/<name>/`:
   - `index.js` (`Module.register` with the list and detail routes, navigation, snippets, and
     optionally a `settingsItem`)
   - `page/<name>-list/` and `page/<name>-detail/` (each an `index.js` plus a `.html.twig`, using
     Meteor `mt-*`)
   - `snippet/de-DE.json` and `en-GB.json`
   - ACL privileges (`addPrivilegeMappingEntry`) plus the `acl` service file
3. Import it in `main.js`. Note the follow-up: the admin watcher or build, and `eslint:admin`.

Data goes through `repositoryFactory` (with `--entity`). Build the UI from `mt-*`. Never overwrite an
existing module.
