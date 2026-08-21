# Shopware 6 — Admin mixins

Mixins encapsulate reusable component behaviour. Built-in ones via `Shopware.Mixin.getByName`.

```js
Shopware.Component.register('ff-example-list', {
    mixins: [Shopware.Mixin.getByName('notification'), Shopware.Mixin.getByName('listing')],
    methods: {
        onSuccess() { this.createNotificationSuccess({ message: this.$tc('ff-example.saved') }); },
    },
});
```

Common ones: `notification` (toast messages), `listing` (pagination/sorting for lists), `placeholder`.
Your own mixin: `Shopware.Mixin.register('ff-shared', { ... })`. In the Vue 3 Composition API increasingly replaceable by
composables/services (`sw-admin-services`).
