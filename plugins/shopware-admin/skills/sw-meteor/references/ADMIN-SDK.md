# Shopware 6 — administration fundamentals

The admin is a Vue 3 app. Plugins extend it through the global `Shopware` object; the entry point is
`src/Resources/app/administration/src/main.js`.

```js
// main.js
import './module/ff-example';
```

Central registries on the `Shopware` object: `Shopware.Module.register`, `Shopware.Component.register/override`,
`Shopware.Service(...)`, `Shopware.Store` (Pinia), `Shopware.Mixin`, `Shopware.Snippet`. Stack: Vue 3 +
**Composition API**, **Pinia** (Vuex is legacy only), **Vite** build, **Meteor** components (`mt-*`).

Building blocks: modules (`sw-admin-module`), components (`sw-admin-component`), routing (`sw-admin-routing`),
data (`sw-admin-data-handling`). Build/watcher: `sw-admin-vite`. For the 6.6→6.7 switch (sw-*→mt-*) see the plugin `shopware-migration`.
