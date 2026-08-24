---
name: sw-js-plugin
description: Scaffolds a JavaScript storefront plugin in Shopware 6 including its PluginManager registration and a template hook.
argument-hint: <Name> [--plugin <PluginName>] [--selector data-example]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /sw-js-plugin

Produce a storefront JS plugin. Skill: `sw-javascript`.

## Steps
1. Settle the name (PascalCase, no suffix), the target plugin and the selector (`data-…`).
2. Create:
   - `src/Resources/app/storefront/src/<kebab>/<kebab>.plugin.js` (extends `window.PluginBaseClass`,
     with `static options`, `init()` and `_registerEvents()`).
   - The entry in `src/Resources/app/storefront/src/main.js`:
     `PluginManager.register('<Name>', <Class>, '[<selector>]')`.
   - Optionally a template hook (`<div data-…>`).
3. Note the follow-up: the storefront build (`bin/build-storefront.sh`) and
   `composer eslint:storefront`.

To change an existing plugin, override or extend it instead (`sw-javascript`); check what is already
there with `/sw-js-plugin-map`.
