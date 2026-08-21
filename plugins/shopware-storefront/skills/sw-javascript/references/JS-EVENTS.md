# Shopware 6 — JS events

Storefront JS uses a global event emitter and native DOM events for communication between plugins.

```js
// publish
this.$emitter.publish('ffExample/done', { id });
// subscribe (also across plugins)
document.$emitter.subscribe('ffExample/done', (event) => { const { id } = event.detail; });
```

**Which JS events exist?** Use the project catalog (`sw-js-event-catalog` / `/sw-js-plugin-map`) — it lists all
JS events with their publish/subscribe locations and arguments.

Your own plugins emit lifecycle events automatically; in addition you can react to initialization via
`window.PluginManager`. For core interactions (e.g. cart update), listen to the respective core events. After DOM updates
following AJAX → re-initialize the affected plugins (`window.PluginManager.initializePlugins()`).
