# Shopware 6 — EntityRepository (CRUD)

`{entity}.repository` (`product.repository`, for example) is the facade for all read and write operations. Always with
a `Context` (admin) or via sales-channel repositories in the store context.

```php
// reading
$result = $this->repo->search(new Criteria([$id]), $context);
$entity = $result->getEntities()->first();
$ids    = $this->repo->searchIds($criteria, $context)->getIds();

// writing (array payload, IDs as hex UUID)
$this->repo->upsert([['id' => $id, 'name' => 'New']], $context);
$this->repo->delete([['id' => $id]], $context);
```

`create` (new), `update` (existing), `upsert` (both). Writing triggers write events (`sw-write-events`).
Shape queries in detail through `Criteria` (`sw-criteria`, `sw-filters`, `sw-sorting`, `sw-aggregations`).

→ Operations, batching, error cases: [REPOSITORY-OPERATIONS.md](REPOSITORY-OPERATIONS.md)
