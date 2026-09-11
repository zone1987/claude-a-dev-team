# Shopware 6 — Vue component tests

Admin components are tested with `@vue/test-utils`, mounted through Jest. Setup in
`sw-testing-standard` → `STANDARD-JEST-ADMIN.md`; what to assert in
[JEST-ADMIN.md](JEST-ADMIN.md).

## Mount the plugin's own component

```javascript
import { mount } from '@vue/test-utils';
import YourCard from './index';

const wrapper = mount(YourCard, {
    props: { item: { name: 'X', active: true } },
    global: {
        stubs: {
            // Real templates with a slot. A bare string stub renders nothing, so the
            // button below never exists and the test passes for the wrong reason.
            'mt-card': { template: '<div><slot /></div>' },
            'mt-text-field': { template: '<input />', props: ['modelValue'] },
        },
    },
});

await wrapper.find('[data-your-save]').trigger('click');

expect(wrapper.emitted('save')).toBeTruthy();
```

**Never `stubs: ['mt-card']`.** The array form produces an empty element: slots do not
render, children do not exist, and a test looking for something inside the card finds
nothing — which reads as a passing test when the assertion is `.exists()` on the stub
itself.

## When to use Component.build instead

`Shopware.Component.build('name')` resolves a component **through the registry, including
every override**. Use it when the subject *is* an override of a core component:

```javascript
const wrapper = mount(await Shopware.Component.build('sw-product-detail-base'), { … });
```

For the plugin's own components, import them directly — the registry adds nothing, and the
direct import keeps the test independent of registration order.

## Pinia stores

The stub's `Shopware.Store` implements `get()` only, which is enough for a component that
reads `Store.get('error')` or `Store.get('context')`.

A component that needs its own store is given it directly rather than through the registry
— `Store.register` takes a factory function in the administration, and reproducing that in
a stub buys nothing:

```javascript
const wrapper = mount(YourCard, {
    global: {
        provide: { yourStore: { items: [] } },
    },
});
```

## What to assert

The behaviour, not the rendering: the request it makes, what it shows when the answer is
empty, what a click triggers, which notification a failure raises. → [JEST-ADMIN.md](JEST-ADMIN.md)

Composition API and `<script setup>` are supported.
