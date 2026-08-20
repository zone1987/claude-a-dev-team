# Shopware 6 — Admin repository (JS)

```js
const repo = this.repositoryFactory.create('ff_example');

// new record
const entity = repo.create(Shopware.Context.api);
entity.name = 'Neu';
await repo.save(entity, Shopware.Context.api);

// single record with associations
const item = await repo.get(id, Shopware.Context.api, criteria);

// delete / clone
await repo.delete(id, Shopware.Context.api);
await repo.clone(id, Shopware.Context.api, behavior);
```

`create()` produces an entity with a generated ID (client-side, UUID). `save()` does create/update. For lists
`search()` returns an `EntityCollection` (add/remove/getIds). Versioning via `repositoryFactory` + version context
just like the DAL. Loading performance: request associations selectively via Criteria.
