---
name: sw-admin-error-handling
description: >
  Fehlerbehandlung im Shopware-6-Admin: notification-Mixin (createNotificationError), API-Fehler aus Promise fangen,
  Error-Config/error codes, Validierungsfehler an Feldern. Trigger: "Admin error handling", "createNotificationError",
  "API Fehler admin", "catch repository error", "Fehlermeldung admin", "validation error field". Shopware 6.7.
---

# Shopware 6 — Admin-Fehlerbehandlung

API-/Save-Fehler abfangen und als Notification zeigen; Validierungsfehler werden von Meteor-Feldern automatisch
an der Entity gebunden.

```js
try {
    await this.repository.save(this.entity, Shopware.Context.api);
    this.createNotificationSuccess({ message: this.$tc('ff-example.saved') });
} catch (error) {
    this.createNotificationError({ message: this.$tc('ff-example.saveError') });
}
```

`notification`-Mixin liefert `createNotificationError/Success/Warning/Info`. Konsistente Fehlermeldungen über
Error-Codes/Snippets. Domain-Exceptions des Backends (`shopware-quality` → `sw-domain-exceptions`) erscheinen mit
`detail`/`code` in der API-Antwort und sollten benutzerfreundlich gemappt werden.
