# Shopware 6.7 — migrating from Vuex to Pinia

With 6.7 Pinia replaces Vuex as the administration's state management library. Pinia drops mutations
entirely, types better, and works with the Composition API.

## Contents

- [Registering a store](#registering-a-store)
- [State](#state)
- [Mutations are gone](#mutations-are-gone)
- [Getters](#getters)
- [TypeScript](#typescript)
- [Composables as a store](#composables-as-a-store)
- [Accessing a store](#accessing-a-store)
- [Testing](#testing)

## Registering a store

Vuex:

```javascript
export default {
    namespaced: true,
    state: { /* ... */ },
    mutations: { /* ... */ },
    getters: { /* ... */ },
    actions: { /* ... */ },
};
```

Pinia — `Shopware.Store.register`, with `state`, `getters` and `actions`:

```javascript
const store = Shopware.Store.register('myStore', {
    state: () => ({ /* ... */ }),
    getters: { /* ... */ },
    actions: { /* ... */ },
});

export default store;
```

The id can also live in the definition object:

```javascript
const store = Shopware.Store.register({
    id: 'myStore',
    state: () => ({ /* ... */ }),
    getters: { /* ... */ },
    actions: { /* ... */ },
});
```

**Registering a store that already exists overwrites it.** To remove one:

```javascript
Shopware.Store.unregister('myStore');
```

Registration from a component or index file also becomes simpler — importing the file is enough,
where Vuex needed an explicit `registerModule`:

```javascript
// Vuex
import productsStore from './state/products.state';
Shopware.State.registerModule('product', productsStore);

// Pinia
import './state/products.state';
```

## State

**`state` must be a function returning the initial state**, not a static object:

```javascript
state: () => ({
    productName: '',
})
```

## Mutations are gone

There are no mutations in Pinia. Modify state directly in an action, or compute it:

```javascript
actions: {
    updateProductName(newName) {
        this.productName = newName;   // direct
    },
},
```

## Getters

- **A getter cannot share a name with a state property** — both are exposed at the same level of the
  store.
- A getter computes and returns from state; it does not modify it.

## TypeScript

Migrating a JavaScript store to TypeScript is recommended: stricter typing, better autocompletion,
fewer mistakes.

```typescript
const store = Shopware.Store.register({
    id: 'myStore',
    // ...
});

export type StoreType = ReturnType<typeof store>;
```

Then extend `PiniaRootState` with it:

```typescript
import type { StoreType } from './store/myStore';

declare global {
    interface PiniaRootState {
        myStore: StoreType;
    }
}
```

## Composables as a store

A store can be written as a composable, using reactive properties. **Pinia's devtools only track
what the store returns**, so return everything you want visible.

```typescript
const store = Shopware.Store.register('myStore', function () {
    const count = ref(0);
    const doubled = computed(() => count.value * 2);

    function increment() {
        count.value++;
    }

    function decrement() {
        count.value--;
    }

    return { count, doubled, increment, decrement };
});
```

A composable defined outside the store works too, which is what makes the logic reusable across
stores and components:

```typescript
// composables/myComposable.ts
export function useMyComposable() {
    const count = ref(0);
    const doubled = computed(() => count.value * 2);

    function increment() { count.value++; }
    function decrement() { count.value--; }

    return { count, doubled, increment, decrement };
}
```

```typescript
// store/myStore.ts
import { useMyComposable } from '../composables/myComposable';

const store = Shopware.Store.register('myStore', useMyComposable);
```

## Accessing a store

```javascript
Shopware.State.get('myStore');   // Vuex
Shopware.Store.get('myStore');   // Pinia
```

## Testing

Import the store so it registers, and use `$reset()` between tests:

```javascript
import './store/my.store';

describe('my store', () => {
    const store = Shopware.Store.get('myStore');

    beforeEach(() => {
        store.$reset();
    });

    it('has initial state', () => {
        expect(store.count).toBe(0);
    });
});
```

For a component that uses a store, create the Pinia instance once, make it active before each test,
and pass it as a plugin to `mount`:

```javascript
import { createPinia, setActivePinia } from 'pinia';

const pinia = createPinia();

describe('my component', () => {
    beforeEach(() => {
        setActivePinia(pinia);
    });

    it('is a component', async () => {
        const wrapper = mount(await wrapTestComponent('myComponent', { sync: true }), {
            global: {
                plugins: [pinia],
                stubs: {
                    // ...
                },
            },
        });

        expect(wrapper.exists()).toBe(true);
    });
});
```

## Source

[developer.shopware.com/docs/guides/upgrades-migrations/administration/pinia.html](https://developer.shopware.com/docs/guides/upgrades-migrations/administration/pinia.html),
Shopware 6.7, retrieved 2026-08-21.
