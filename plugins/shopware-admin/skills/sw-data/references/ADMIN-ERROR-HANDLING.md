# Shopware 6 — Admin error handling

Catch API/save errors and show them as a notification; validation errors are bound to the entity automatically
by Meteor fields.

```js
try {
    await this.repository.save(this.entity, Shopware.Context.api);
    this.createNotificationSuccess({ message: this.$tc('ff-example.saved') });
} catch (error) {
    this.createNotificationError({ message: this.$tc('ff-example.saveError') });
}
```

The `notification` mixin provides `createNotificationError/Success/Warning/Info`. Keep error messages consistent via
error codes/snippets. Backend domain exceptions (`shopware-quality` → `sw-domain-exceptions`) appear with
`detail`/`code` in the API response and should be mapped to something user-friendly.
