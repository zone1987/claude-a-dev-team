---
name: sw-js-events
description: >
  Auf JavaScript-Events im Shopware-6-Storefront reagieren: PluginManager-Events, document.$emitter, native Events,
  zwischen JS-Plugins kommunizieren. Trigger: "JS Event storefront", "$emitter", "document.$emitter", "plugin event listen",
  "JS Plugins kommunizieren", "emit subscribe storefront". Shopware 6.7.
---

# Shopware 6 — JS-Events

Storefront-JS nutzt einen globalen Event-Emitter und native DOM-Events zur Kommunikation zwischen Plugins.

```js
// senden
this.$emitter.publish('ffExample/done', { id });
// empfangen (auch plugin-übergreifend)
document.$emitter.subscribe('ffExample/done', (event) => { const { id } = event.detail; });
```

**Welche JS-Events gibt es?** Projekt-Katalog nutzen (`sw-js-event-catalog` / `/sw-js-plugin-map`) — listet alle
JS-Events mit Publish-/Subscribe-Orten und Argumenten.

Eigene Plugins emittieren Lifecycle-Events automatisch; zusätzlich kann man via `window.PluginManager` auf
Initialisierung reagieren. Für Core-Interaktionen (z.B. Cart-Update) auf die jeweiligen Core-Events hören. DOM-Updates
nach AJAX → betroffene Plugins re-initialisieren (`window.PluginManager.initializePlugins()`).
