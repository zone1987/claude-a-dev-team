# Shopware 6 — Admin state (Pinia)

Since 6.6/6.7 **Pinia** is the standard (ADR "replace Vuex with Pinia"). Stores via `Shopware.Store.register`.

```js
Shopware.Store.register('ffExample', {
    state: () => ({ items: [], loading: false }),
    getters: { count: (state) => state.items.length },
    actions: { setItems(items) { this.items = items; } },
});
// Usage in a component:
const store = Shopware.Store.get('ffExample');
store.setItems(result);
```

Access via `Shopware.Store.get('name')`. No more nested `mapState` needed — direct store access.
Legacy Vuex only for old core stores (`sw-admin-vuex-store`). Local component state stays in the component.
