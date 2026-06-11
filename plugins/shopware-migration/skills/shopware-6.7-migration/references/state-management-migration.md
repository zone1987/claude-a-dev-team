# State Management Migration: Vuex to Pinia

Shopware 6.7 deprecates Vuex in favor of Pinia. Vuex will be removed in 6.8.0. This reference covers migrating plugin state management.

---

## Overview

| Aspect | Shopware 6.6 (Vuex) | Shopware 6.7 (Pinia) |
|---|---|---|
| Library | Vuex 4 | Pinia 2.3 |
| API | `Shopware.State` | `Shopware.Store` |
| Mutations | Required (commit) | Not needed (direct) |
| State access | `Shopware.State.get('name')` | `Shopware.Store.get('name')` |
| Registration | `Shopware.State.registerModule()` | `Shopware.Store.register()` |
| TypeScript | Partial | Full support |

---

## Quick Migration Guide

### Accessing State

```javascript
// BEFORE (Vuex)
const session = Shopware.State.get('session');
const currentUser = Shopware.State.get('session').currentUser;

// AFTER (Pinia)
const sessionStore = Shopware.Store.get('session');
const currentUser = sessionStore.currentUser;
```

### Committing Changes

```javascript
// BEFORE (Vuex) - mutations required
Shopware.State.commit('myPlugin/setItems', items);
Shopware.State.commit('myPlugin/setLoading', true);

// AFTER (Pinia) - direct mutation
const myPluginStore = Shopware.Store.get('myPlugin');
myPluginStore.items = items;
myPluginStore.loading = true;
```

### Dispatching Actions

```javascript
// BEFORE (Vuex)
await Shopware.State.dispatch('myPlugin/fetchItems');

// AFTER (Pinia)
const myPluginStore = Shopware.Store.get('myPlugin');
await myPluginStore.fetchItems();
```

### Using Getters

```javascript
// BEFORE (Vuex)
const total = Shopware.State.getters['myPlugin/totalItems'];

// AFTER (Pinia) - getters are computed properties
const myPluginStore = Shopware.Store.get('myPlugin');
const total = myPluginStore.totalItems; // accessed like a property
```

---

## Registering a New Store

### BEFORE (Vuex Module)

```javascript
Shopware.State.registerModule('myPlugin', {
    namespaced: true,

    state: {
        items: [],
        loading: false,
        currentItem: null,
    },

    mutations: {
        setItems(state, items) {
            state.items = items;
        },
        setLoading(state, loading) {
            state.loading = loading;
        },
        setCurrentItem(state, item) {
            state.currentItem = item;
        },
    },

    actions: {
        async fetchItems({ commit }) {
            commit('setLoading', true);
            try {
                const response = await httpClient.get('/my-plugin/items');
                commit('setItems', response.data);
            } finally {
                commit('setLoading', false);
            }
        },

        async deleteItem({ commit, state }, itemId) {
            await httpClient.delete(`/my-plugin/items/${itemId}`);
            const filtered = state.items.filter(i => i.id !== itemId);
            commit('setItems', filtered);
        },
    },

    getters: {
        totalItems(state) {
            return state.items.length;
        },
        activeItems(state) {
            return state.items.filter(i => i.active);
        },
    },
});
```

### AFTER (Pinia Store)

```javascript
const myPluginStore = Shopware.Store.register({
    id: 'myPlugin',

    state: () => ({
        items: [],
        loading: false,
        currentItem: null,
    }),

    actions: {
        async fetchItems() {
            this.loading = true;
            try {
                const response = await httpClient.get('/my-plugin/items');
                this.items = response.data;
            } finally {
                this.loading = false;
            }
        },

        async deleteItem(itemId) {
            await httpClient.delete(`/my-plugin/items/${itemId}`);
            this.items = this.items.filter(i => i.id !== itemId);
        },
    },

    getters: {
        totalItems(state) {
            return state.items.length;
        },
        activeItems(state) {
            return state.items.filter(i => i.active);
        },
    },
});

export default myPluginStore;
export type MyPluginStore = ReturnType<typeof myPluginStore>;
```

**Key differences:**
- No `namespaced: true` needed
- No `mutations` — mutate state directly in actions via `this`
- `state` is a **function** returning the initial state (not an object)
- Actions receive no `{ commit, state }` context — use `this` instead
- Getters work the same way
- `id` replaces the module name

---

## TypeScript Patterns

### Store with Types

```typescript
interface MyPluginItem {
    id: string;
    name: string;
    active: boolean;
}

interface MyPluginState {
    items: MyPluginItem[];
    loading: boolean;
    currentItem: MyPluginItem | null;
}

const myPluginStore = Shopware.Store.register({
    id: 'myPlugin',

    state: (): MyPluginState => ({
        items: [],
        loading: false,
        currentItem: null,
    }),

    actions: {
        async fetchItems(): Promise<void> {
            this.loading = true;
            try {
                const response = await httpClient.get<MyPluginItem[]>('/my-plugin/items');
                this.items = response.data;
            } finally {
                this.loading = false;
            }
        },

        setCurrentItem(item: MyPluginItem | null): void {
            this.currentItem = item;
        },
    },

    getters: {
        totalItems(state: MyPluginState): number {
            return state.items.length;
        },

        activeItems(state: MyPluginState): MyPluginItem[] {
            return state.items.filter((i: MyPluginItem) => i.active);
        },
    },
});

export default myPluginStore;
export type MyPluginStore = ReturnType<typeof myPluginStore>;
```

### Using in Components

```typescript
// In a Vue component
import { defineComponent } from 'vue';

export default defineComponent({
    computed: {
        myPluginStore() {
            return Shopware.Store.get('myPlugin');
        },

        items() {
            return this.myPluginStore.items;
        },

        totalItems() {
            return this.myPluginStore.totalItems;
        },
    },

    methods: {
        async loadItems() {
            await this.myPluginStore.fetchItems();
        },

        selectItem(item) {
            this.myPluginStore.setCurrentItem(item);
        },
    },
});
```

---

## Subscribing to State Changes

### BEFORE (Vuex)

```javascript
// Watch for state changes
Shopware.State.watch(
    (state) => state.myPlugin.items,
    (newItems) => {
        console.log('Items changed:', newItems);
    }
);
```

### AFTER (Pinia)

```javascript
// Use $subscribe for store changes
const myPluginStore = Shopware.Store.get('myPlugin');
myPluginStore.$subscribe((mutation, state) => {
    console.log('State changed:', state.items);
});

// Or use Vue's watch in a component
import { watch } from 'vue';

watch(
    () => Shopware.Store.get('myPlugin').items,
    (newItems) => {
        console.log('Items changed:', newItems);
    }
);
```

---

## Unregistering Stores

```javascript
// BEFORE (Vuex)
Shopware.State.unregisterModule('myPlugin');

// AFTER (Pinia)
Shopware.Store.unregister('myPlugin');
```

---

## Migration Checklist

1. Replace `Shopware.State.registerModule()` with `Shopware.Store.register()`
2. Remove all `mutations` — mutate state directly in actions
3. Change `state: { ... }` to `state: () => ({ ... })` (function form)
4. Replace `{ commit, state, dispatch }` in actions with `this`
5. Replace `Shopware.State.get()` with `Shopware.Store.get()`
6. Replace `Shopware.State.commit()` with direct property assignment
7. Replace `Shopware.State.dispatch()` with direct method calls
8. Replace `Shopware.State.getters[]` with direct property access
9. Replace `Shopware.State.watch()` with `$subscribe` or Vue `watch()`
10. Add TypeScript types if using TypeScript

---

## Vue 3 Composition API Integration

For components using the Composition API:

```typescript
import { defineComponent, computed } from 'vue';

export default defineComponent({
    setup() {
        const store = Shopware.Store.get('myPlugin');

        const items = computed(() => store.items);
        const loading = computed(() => store.loading);
        const totalItems = computed(() => store.totalItems);

        async function loadItems() {
            await store.fetchItems();
        }

        return {
            items,
            loading,
            totalItems,
            loadItems,
        };
    },
});
```
