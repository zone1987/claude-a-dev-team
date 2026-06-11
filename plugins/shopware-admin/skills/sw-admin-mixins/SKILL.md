---
name: sw-admin-mixins
description: >
  Mixins im Shopware-6-Admin: Shopware.Mixin.getByName nutzen (notification, listing, placeholder), eigenes Mixin
  registrieren. Trigger: "Admin Mixin", "Mixin.getByName", "notification mixin", "listing mixin", "eigenes Mixin admin",
  "Shopware.Mixin.register". Shopware 6.7.
---

# Shopware 6 — Admin-Mixins

Mixins kapseln wiederverwendbares Komponentenverhalten. Eingebaute über `Shopware.Mixin.getByName`.

```js
Shopware.Component.register('ff-example-list', {
    mixins: [Shopware.Mixin.getByName('notification'), Shopware.Mixin.getByName('listing')],
    methods: {
        onSuccess() { this.createNotificationSuccess({ message: this.$tc('ff-example.saved') }); },
    },
});
```

Häufig: `notification` (Toast-Meldungen), `listing` (Paginierung/Sorting für Listen), `placeholder`.
Eigenes Mixin: `Shopware.Mixin.register('ff-shared', { ... })`. In Vue-3-Composition-API zunehmend durch
Composables/Services ersetzbar (`sw-admin-services`).
