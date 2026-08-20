# Shopware 6 — Admin-Datenhandling

Daten laufen über `repositoryFactory` (DAL via Admin-API). Criteria-API gespiegelt in JS.

```js
const repo = this.repositoryFactory.create('ff_example');
const criteria = new Shopware.Data.Criteria(1, 25);
criteria.addAssociation('lines');
criteria.addFilter(Shopware.Data.Criteria.equals('active', true));
const result = await repo.search(criteria, Shopware.Context.api);
await repo.save(entity, Shopware.Context.api);
```

`repositoryFactory` via `inject(['repositoryFactory'])` bereitstellen. `Shopware.Context.api` als Kontext.
Filter/Sorting/Aggregation analog zur PHP-Criteria (`shopware-data`). Repository-Nutzung im Detail: `sw-admin-repository-js`.
Globaler State über Pinia (`sw-admin-pinia-store`).
