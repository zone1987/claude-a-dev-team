---
name: sw-admin-routing
description: >
  Admin-Routing in Shopware 6: Routen im Module.register (routes), Parameter, meta.parentPath, $router/$route,
  bestehende Routen erweitern (routeMiddleware), Tab zu Modul hinzufügen. Trigger: "Admin Route", "admin routing",
  "routeMiddleware", "parentPath admin", "$router.push admin", "Tab zu Modul", "routes module register". Shopware 6.7.
---

# Shopware 6 — Admin-Routing

Routen werden im Modul unter `routes` deklariert (Vue Router). Navigation per `this.$router.push({ name: 'ff.example.detail', params: { id } })`.

```js
routes: {
    detail: { component: 'ff-example-detail', path: 'detail/:id',
              meta: { parentPath: 'ff.example.index' },
              props: { default: (route) => ({ id: route.params.id }) } },
}
```

Bestehende Routen erweitern (z.B. neuen Tab/Child) über `routeMiddleware` in der Modul-Registrierung der
Ziel-Komponente:

```js
Shopware.Module.register('ff-product-tab', {
    routeMiddleware(next, currentRoute) {
        if (currentRoute.name === 'sw.product.detail') {
            currentRoute.children.push({ name: 'sw.product.detail.ff', path: 'ff', component: 'ff-product-tab' });
        }
        next(currentRoute);
    },
});
```

Menüeinträge: `sw-admin-menu`. Tab-UI per `sw-tabs`/`mt-tabs` im Detail-Template.
