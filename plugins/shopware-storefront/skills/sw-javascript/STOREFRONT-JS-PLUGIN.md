# Shopware 6 — JavaScript Storefront plugin

A vanilla JS plugin bound to a `data-*` attribute and initialized by the `PluginManager`.

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

Template binding: `<div data-ff-example data-ff-example-options='{"url":"..."}'>`. Build via `bin/build-storefront.sh`
or the watcher. Pass data into the DOM via `data-*` (`sw-ajax-data`). Adjust existing plugins: `sw-js-plugin-override` / `sw-js-plugin-extend`.

→ Scaffold: [examples/StorefrontJsPlugin.js](examples/StorefrontJsPlugin.js) · [examples/main.js](examples/main.js)
