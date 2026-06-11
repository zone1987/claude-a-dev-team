---
name: sw-admin-pinia-store
description: >
  State-Management im Shopware-6.7-Admin mit Pinia: Shopware.Store.register, state/getters/actions, Store nutzen,
  Migration von Vuex. Trigger: "Pinia store admin", "Shopware.Store.register", "admin state pinia", "store admin 6.7",
  "useStore admin", "global state administration". Shopware 6.7.
---

# Shopware 6 — Admin-State (Pinia)

Seit 6.6/6.7 ist **Pinia** der Standard (ADR „replace Vuex with Pinia"). Stores via `Shopware.Store.register`.

```js
Shopware.Store.register('ffExample', {
    state: () => ({ items: [], loading: false }),
    getters: { count: (state) => state.items.length },
    actions: { setItems(items) { this.items = items; } },
});
// Nutzung in Komponente:
const store = Shopware.Store.get('ffExample');
store.setItems(result);
```

Zugriff über `Shopware.Store.get('name')`. Kein verschachteltes `mapState` mehr nötig — direkter Store-Zugriff.
Legacy-Vuex nur noch für alte Core-Stores (`sw-admin-vuex-store`). Lokaler Komponenten-State bleibt im Component.
