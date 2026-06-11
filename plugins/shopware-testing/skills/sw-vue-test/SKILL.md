---
name: sw-vue-test
description: >
  Vue-3-Komponententests im Shopware-6-Admin: @vue/test-utils mount/shallowMount, Shopware.Component.build, Props/Events,
  Pinia-Store mocken. Trigger: "Vue test shopware", "@vue/test-utils", "Component.build test", "mount shallowMount admin",
  "vue komponente testen shopware". Shopware 6.7.
---

# Shopware 6 — Vue-Komponententest

Admin-Komponenten mit `@vue/test-utils` testen; die finale (inkl. Overrides) Komponente über
`Shopware.Component.build('name')` beziehen.

```js
const wrapper = mount(await Shopware.Component.build('ff-example-card'), {
    props: { item: { name: 'X', active: true } },
    global: { stubs: ['mt-card', 'mt-text-field'] },
});
await wrapper.find('[data-ff-save]').trigger('click');
expect(wrapper.emitted('save')).toBeTruthy();
```

Meteor-Komponenten ggf. stubben. Pinia-Stores (`Shopware.Store`) im Test initialisieren/mocken. Läuft über Jest
(`sw-jest-admin`). Composition API + `<script setup>` werden unterstützt.
