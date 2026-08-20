# Shopware 6 — Admin data handling

Data goes through `repositoryFactory` (DAL via the Admin API). The Criteria API is mirrored in JS.

```js
const repo = this.repositoryFactory.create('ff_example');
const criteria = new Shopware.Data.Criteria(1, 25);
criteria.addAssociation('lines');
criteria.addFilter(Shopware.Data.Criteria.equals('active', true));
const result = await repo.search(criteria, Shopware.Context.api);
await repo.save(entity, Shopware.Context.api);
```

Provide `repositoryFactory` via `inject(['repositoryFactory'])`. Use `Shopware.Context.api` as the context.
Filters/sorting/aggregation work like the PHP Criteria (`shopware-data`). Repository usage in detail: `sw-admin-repository-js`.
Global state via Pinia (`sw-admin-pinia-store`).
