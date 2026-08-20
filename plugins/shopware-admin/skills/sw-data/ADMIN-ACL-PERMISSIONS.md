# Shopware 6 — Admin ACL/permissions

Register privileges and bind them to module/route/navigation/buttons.

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

In the module's `navigation`/`routes` use `privilege: 'ff_example.viewer'`; in the template `v-if="acl.can('ff_example.editor')"`.
On the server side this corresponds to the Admin API ACL (`shopware-framework` → `sw-api-acl`). Privilege keys = `entity:action`.
