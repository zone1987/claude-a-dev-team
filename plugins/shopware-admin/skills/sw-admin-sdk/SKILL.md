---
name: sw-admin-sdk
description: >
  Grundlagen der Shopware-6.7-Administration (Vue 3): das globale Shopware-Objekt, Verzeichnis
  Resources/app/administration/src, main.js Einstieg, Vite-Build, Meteor-Komponenten (mt-*), Composition API.
  Trigger: "Admin SDK", "Shopware Objekt", "Administration Grundlagen", "main.js admin", "wie Admin erweitern",
  "Shopware.Component", "admin entry". Shopware 6.7.
---

# Shopware 6 — Administration-Grundlagen

Die Admin ist eine Vue-3-App. Plugins erweitern sie über das globale `Shopware`-Objekt; Einstieg ist
`src/Resources/app/administration/src/main.js`.

```js
// main.js
import './module/ff-example';
```

Zentrale Registries am `Shopware`-Objekt: `Shopware.Module.register`, `Shopware.Component.register/override`,
`Shopware.Service(...)`, `Shopware.Store` (Pinia), `Shopware.Mixin`, `Shopware.Snippet`. Stack: Vue 3 +
**Composition API**, **Pinia** (Vuex nur Legacy), **Vite**-Build, **Meteor**-Komponenten (`mt-*`).

Bausteine: Module (`sw-admin-module`), Components (`sw-admin-component`), Routing (`sw-admin-routing`),
Daten (`sw-admin-data-handling`). Build/Watcher: `sw-admin-vite`. Für 6.6→6.7-Umstellung (sw-*→mt-*) siehe Plugin `shopware-migration`.
