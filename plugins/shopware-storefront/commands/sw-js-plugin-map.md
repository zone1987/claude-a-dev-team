---
name: sw-js-plugin-map
description: Scans the current Shopware project for JavaScript storefront plugins and JS events, then writes a cached catalogue of both.
argument-hint: [--custom-only]
allowed-tools: Read, Glob, Grep, Bash, Write, Task
model: haiku
---

# /sw-js-plugin-map

Create or refresh the JS plugin catalogue. Delegate to the `shopware-js-plugin-mapper` agent
(skill `sw-javascript`).

## Steps
1. Scan scope: the core storefront
   (`vendor/shopware/storefront/Resources/app/storefront/src/plugin/**`) plus custom code
   (`custom/plugins/*/src/Resources/app/storefront/src/**`). With `--custom-only`, custom code only.
2. Record the plugin classes (`*.plugin.js`), their `static options`, and the
   `PluginManager.register/override/extend` entries (name, selector, class).
3. Write `.shopware-catalog/js-plugins.md` (the plugins) **and** `.shopware-catalog/js-events.md`
   (the JS events: publish and subscribe sites, arguments and `detail`, type) — formats from
   `sw-javascript`.
4. Head each file with the scan date, scope and counts; print a short summary.

Scan with grep (`PluginManager.register|override|extend`, `class .*Plugin`,
`\$emitter\.(publish|subscribe)`, `dispatchEvent\(new CustomEvent`). Record only what is really
there.
