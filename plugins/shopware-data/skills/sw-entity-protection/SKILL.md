---
name: sw-entity-protection
description: >
  Zugriffsschutz in Shopware 6 DAL: ApiAware-Scopes, ReadProtected/WriteProtected, EntityProtection,
  interne Felder von der API ausschließen. Trigger: "EntityProtection", "ReadProtected", "WriteProtected",
  "Feld vor API schützen", "ApiAware scope", "internal field protection". Shopware 6.7.
---

# Shopware 6 — Entity-/Field-Protection

Steuert, welche Felder/Entities über welche API-Quelle (Admin/Store) les- oder schreibbar sind.

- `ApiAware` (ohne Flag = nicht über API): markiert API-Sichtbarkeit, optional je Quelle
  `new ApiAware(SalesChannelApiSource::class)`.
- `WriteProtected` / `ReadProtected`: Schreib-/Leseschutz je Scope (z.B. nur System darf schreiben).
- Sensible interne Felder (Tokens, Flags) bewusst **ohne** `ApiAware` lassen.

```php
(new StringField('secret', 'secret'))->addFlags(new WriteProtected(Context::SYSTEM_SCOPE)),
```

So bleiben interne Daten aus Admin-/Store-API heraus, ohne separate Entity. Ergänzend ACL für Admin-Rechte (`shopware-framework` → `sw-api-acl`).

→ Protection-Details: [references/protection.md](references/protection.md)
