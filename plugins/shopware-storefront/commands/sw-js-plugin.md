---
name: sw-js-plugin
description: Scaffold eines JavaScript-Storefront-Plugins in Shopware 6 (PluginBaseClass) inkl. main.js-Registrierung, data-Selector und Template-Hook.
argument-hint: <PluginJsName> [--plugin <PluginName>] [--selector data-ff-x]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /sw-js-plugin

Erzeuge ein Storefront-JS-Plugin. Skill: `sw-storefront-js-plugin`.

## Ablauf
1. Name (PascalCase, ohne Suffix) + Ziel-Plugin + Selector (`data-...`) bestimmen.
2. Erzeugen:
   - `src/Resources/app/storefront/src/<kebab>/<kebab>.plugin.js` (extends `window.PluginBaseClass`, `static options`,
     `init()`, `_registerEvents()`).
   - Eintrag in `src/Resources/app/storefront/src/main.js`: `PluginManager.register('<Name>', <Class>, '[<selector>]')`.
   - Optional Template-Hook (`<div data-...>`).
3. Hinweis: Storefront-Build (`bin/build-storefront.sh`) + `composer eslint:storefront`.

Für das Ändern eines bestehenden Plugins stattdessen override/extend (Skills `sw-js-plugin-override`/`-extend`);
vorhandene Plugins via `/sw-js-plugin-map` prüfen.
