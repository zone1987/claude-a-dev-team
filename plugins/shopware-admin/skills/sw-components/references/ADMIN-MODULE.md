# Shopware 6 — Admin module

A module bundles the routes, components and navigation of a backend area. Registration via `Shopware.Module.register`.

```js
Shopware.Module.register('ff-example', {
    type: 'plugin',
    title: 'ff-example.general.title',
    color: '#ff3d58',
    icon: 'regular-cog',
    routes: {
        list:   { component: 'ff-example-list',   path: 'index' },
        detail: { component: 'ff-example-detail', path: 'detail/:id', meta: { parentPath: 'ff.example.index' } },
    },
    navigation: [{ label: 'ff-example.general.title', path: 'ff.example.index', parent: 'sw-catalogue', position: 50 }],
});
```

Structure: `src/Resources/app/administration/src/module/ff-example/` with `index.js`, `page/`, `component/`,
`snippet/`. Register components separately (`sw-admin-component`), data via repository (`sw-admin-data-handling`),
permissions via ACL (`sw-admin-acl-permissions`).

→ Module structure & routing: [ADMIN-MODULE-ADMINISTRATION.md](ADMIN-MODULE-ADMINISTRATION.md) · Example: [examples/index.js](examples/index.js)
