---
name: sw-admin-acl-permissions
description: >
  ACL/Berechtigungen im Shopware-6-Admin: Shopware.Service('privileges').addPrivilegeMappingEntry, acl.can(),
  privilege an Modul/Route/Navigation koppeln, viewer/editor/creator/deleter. Trigger: "Admin ACL", "Berechtigungen admin",
  "addPrivilegeMappingEntry", "acl.can", "privilege admin", "Rechte Modul", "permission administration". Shopware 6.7.
---

# Shopware 6 — Admin-ACL/Berechtigungen

Privilegien registrieren und an Modul/Route/Navigation/Buttons binden.

```js
Shopware.Service('privileges').addPrivilegeMappingEntry({
    category: 'permissions', parent: null, key: 'ff_example',
    roles: {
        viewer:  { privileges: ['ff_example:read'], dependencies: [] },
        editor:  { privileges: ['ff_example:update'], dependencies: ['ff_example.viewer'] },
        creator: { privileges: ['ff_example:create'], dependencies: ['ff_example.editor'] },
        deleter: { privileges: ['ff_example:delete'], dependencies: ['ff_example.viewer'] },
    },
});
```

Im Modul `navigation`/`routes` `privilege: 'ff_example.viewer'`; im Template `v-if="acl.can('ff_example.editor')"`.
Server-seitig korrespondiert die Admin-API-ACL (`shopware-framework` → `sw-api-acl`). Privilege-Keys = `entity:action`.
