# Shopware 6 — API/Backend ACL

Backend access is secured through privileges (`entity:action`). On routes via `_acl`, on entities automatically
(`ff_example:read/create/update/delete`).

```php
#[Route(..., defaults: ['_acl' => ['ff_example:update']])]
```

- Own entity → CRUD privileges exist automatically; assignable in the admin role (`shopware-admin` → `sw-admin-acl-permissions`).
- Own action → enforce an own privilege via `_acl` and make it visible in the PrivilegeMapping (admin).
- Declare additional privileges / dependent rights through the admin `privileges` service mapping.

Integrations (client_credentials) receive rights through assigned roles. Field visibility additionally through
`ApiAware`/protection (`shopware-data` → `sw-entity-protection`).
