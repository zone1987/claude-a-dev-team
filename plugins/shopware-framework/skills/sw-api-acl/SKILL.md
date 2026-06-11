---
name: sw-api-acl
description: >
  Zugriffsrechte (ACL) für Admin-API/Backend in Shopware 6: _acl-Route-Default, Privileges (entity:read/update/...),
  Privilegien für eigene Entities/Aktionen registrieren, Zusammenspiel mit Admin-ACL. Trigger: "API ACL", "_acl route",
  "Privileges shopware", "Berechtigung api", "acl privilege entity:action", "Rechte Admin API". Shopware 6.7.
---

# Shopware 6 — API/Backend-ACL

Backend-Zugriffe werden über Privilegien (`entity:action`) abgesichert. An Routen via `_acl`, an Entities automatisch
(`ff_example:read/create/update/delete`).

```php
#[Route(..., defaults: ['_acl' => ['ff_example:update']])]
```

- Eigene Entity → CRUD-Privilegien existieren automatisch; in der Admin-Rolle zuweisbar (`shopware-admin` → `sw-admin-acl-permissions`).
- Eigene Aktion → eigenes Privileg über `_acl` erzwingen und im PrivilegeMapping (Admin) sichtbar machen.
- Additional Privileges / abhängige Rechte über das Admin-`privileges`-Service-Mapping deklarieren.

Integrationen (client_credentials) erhalten Rechte über zugewiesene Rollen. Feld-Sichtbarkeit zusätzlich über
`ApiAware`/Protection (`shopware-data` → `sw-entity-protection`).
