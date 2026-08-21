# Shopware 6 — Admin routing

Routes are declared in the module under `routes` (Vue Router). Navigate via `this.$router.push({ name: 'ff.example.detail', params: { id } })`.

```js
routes: {
    detail: { component: 'ff-example-detail', path: 'detail/:id',
              meta: { parentPath: 'ff.example.index' },
              props: { default: (route) => ({ id: route.params.id }) } },
}
```

Extend existing routes (e.g. a new tab/child) via `routeMiddleware` in the module registration of the
target component:

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

Menu entries: `sw-admin-menu`. Tab UI via `sw-tabs`/`mt-tabs` in the detail template.
