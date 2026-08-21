# Shopware 6 — Admin services

Register services via `addServiceProvider` and use them in components via `inject`.

```js
Shopware.Application.addServiceProvider('ffCalculator', () => new FfCalculator());
// Component:
Shopware.Component.register('ff-example-detail', { inject: ['ffCalculator', 'repositoryFactory'], /* ... */ });
```

Common built-in services: `repositoryFactory` (data), `systemConfigApiService` (config), `acl`, `loginService`,
`feature`. Custom ApiServices for custom endpoints (`sw-admin-api-requests`). `Shopware.Service('name')` for direct
access outside components.
