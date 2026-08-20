# Shopware 6 — Admin-Services

Services über `addServiceProvider` registrieren, in Komponenten via `inject` nutzen.

```js
Shopware.Application.addServiceProvider('ffCalculator', () => new FfCalculator());
// Komponente:
Shopware.Component.register('ff-example-detail', { inject: ['ffCalculator', 'repositoryFactory'], /* ... */ });
```

Häufige eingebaute Services: `repositoryFactory` (Daten), `systemConfigApiService` (Config), `acl`, `loginService`,
`feature`. Eigene ApiServices für Custom-Endpoints (`sw-admin-api-requests`). `Shopware.Service('name')` für direkten
Zugriff außerhalb von Komponenten.
