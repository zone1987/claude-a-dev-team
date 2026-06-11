---
name: sw-entity-repository
description: >
  CRUD mit dem Shopware-6 EntityRepository: search, searchIds, create, update, upsert, delete, aggregate;
  Context vs. SalesChannelContext. Trigger: "EntityRepository", "Daten lesen/schreiben", "repository search",
  "upsert create update delete", "searchIds", "{entity}.repository", "DAL operations". Shopware 6.7.
---

# Shopware 6 — EntityRepository (CRUD)

`{entity}.repository` (z.B. `product.repository`) ist die Fassade für alle Lese-/Schreiboperationen. Immer mit
`Context` (Admin) bzw. via SalesChannel-Repos im Store-Kontext.

```php
// Lesen
$result = $this->repo->search(new Criteria([$id]), $context);
$entity = $result->getEntities()->first();
$ids    = $this->repo->searchIds($criteria, $context)->getIds();

// Schreiben (Array-Payload, IDs als Hex-UUID)
$this->repo->upsert([['id' => $id, 'name' => 'Neu']], $context);
$this->repo->delete([['id' => $id]], $context);
```

`create` (neu), `update` (vorhanden), `upsert` (beides). Schreiben löst Write-Events aus (`sw-write-events`).
Abfragen feingranular über `Criteria` (`sw-criteria`, `sw-filters`, `sw-sorting`, `sw-aggregations`).

→ Operationen, Batch, Fehlerfälle: [references/operations.md](references/operations.md)
