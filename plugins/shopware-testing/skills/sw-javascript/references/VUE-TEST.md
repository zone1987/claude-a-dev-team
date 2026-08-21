# Shopware 6 — Vue Component Test

Test admin components with `@vue/test-utils`; obtain the final component (including overrides) through
`Shopware.Component.build('name')`.

```js
const wrapper = mount(await Shopware.Component.build('ff-example-card'), {
    props: { item: { name: 'X', active: true } },
    global: { stubs: ['mt-card', 'mt-text-field'] },
});
await wrapper.find('[data-ff-save]').trigger('click');
expect(wrapper.emitted('save')).toBeTruthy();
```

Stub Meteor components where needed. Initialize or mock Pinia stores (`Shopware.Store`) in the test. Runs through Jest
(`sw-jest-admin`). Composition API and `<script setup>` are supported.
