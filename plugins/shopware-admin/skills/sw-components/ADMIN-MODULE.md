# Shopware 6 — Admin-Modul

Ein Modul bündelt Routen, Komponenten und Navigation eines Backend-Bereichs. Registrierung via `Shopware.Module.register`.

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

Struktur: `src/Resources/app/administration/src/module/ff-example/` mit `index.js`, `page/`, `component/`,
`snippet/`. Komponenten separat registrieren (`sw-admin-component`), Daten via Repository (`sw-admin-data-handling`),
Rechte via ACL (`sw-admin-acl-permissions`).

→ Modul-Aufbau & Routing: [ADMIN-MODULE-ADMINISTRATION.md](ADMIN-MODULE-ADMINISTRATION.md) · Beispiel: [examples/index.js](examples/index.js)
