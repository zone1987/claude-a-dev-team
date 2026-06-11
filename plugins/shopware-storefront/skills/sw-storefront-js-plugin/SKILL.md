---
name: sw-storefront-js-plugin
description: >
  Ein eigenes JavaScript-Storefront-Plugin in Shopware 6 schreiben & registrieren: Plugin extends window.PluginBaseClass,
  init(), this.options, _registerEvents, data-Selector, Registrierung in main.js via PluginManager.register, Build.
  Trigger: "JS Plugin Storefront", "PluginBaseClass", "PluginManager.register", "data-plugin storefront",
  "JavaScript Storefront", "main.js plugin register", "init() storefront plugin". Shopware 6.7. Scaffolder: /sw-js-plugin.
---

# Shopware 6 — JavaScript-Storefront-Plugin

Vanilla-JS-Plugin, das an ein `data-*`-Attribut gebunden und vom `PluginManager` initialisiert wird.

```js
// src/Resources/app/storefront/src/ff-example/ff-example.plugin.js
export default class FfExamplePlugin extends window.PluginBaseClass {
    static options = { url: '' };
    init() {
        this._button = this.el.querySelector('[data-ff-trigger]');
        this._registerEvents();
    }
    _registerEvents() { this._button?.addEventListener('click', this._onClick.bind(this)); }
    _onClick(e) { /* ... */ }
}
```
```js
// main.js
const PluginManager = window.PluginManager;
PluginManager.register('FfExample', FfExamplePlugin, '[data-ff-example]');
```

Template-Bindung: `<div data-ff-example data-ff-example-options='{"url":"..."}'>`. Build via `bin/build-storefront.sh`
bzw. Watcher. Daten ins DOM über `data-*` (`sw-ajax-data`). Bestehende Plugins anpassen: `sw-js-plugin-override` / `sw-js-plugin-extend`.

→ Gerüst: [examples/StorefrontJsPlugin.js](examples/StorefrontJsPlugin.js) · [examples/main.js](examples/main.js)
