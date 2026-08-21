# Shopware 6 — Criteria

`Criteria` is the DAL's query builder (instead of the Doctrine QueryBuilder). It bundles filters, sorting,
aggregations, associations and pagination, and goes into `repository->search($criteria, $context)`.

```php
$criteria = new Criteria();                  // or new Criteria([$id1, $id2]) for specific IDs
$criteria->setLimit(25)->setOffset(0);
$criteria->addAssociation('lines.product');  // load nested
$criteria->getAssociation('lines')->addSorting(new FieldSorting('position'));
$criteria->setTotalCountMode(Criteria::TOTAL_COUNT_MODE_EXACT);
```

Building blocks: **filters** (`sw-filters`), **sorting** (`sw-sorting`), **aggregations** (`sw-aggregations`).
Load associations explicitly (no `autoload`). `addAssociation('a.b.c')` loads nested.

→ Full Criteria reference: [CRITERIA-SEARCH-CRITERIA.md](CRITERIA-SEARCH-CRITERIA.md)
