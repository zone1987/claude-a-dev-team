# Shopware 6 — Criteria

`Criteria` ist der Query-Builder der DAL (statt Doctrine QueryBuilder). Sie bündelt Filter, Sortierung,
Aggregationen, Associations und Paginierung und geht in `repository->search($criteria, $context)`.

```php
$criteria = new Criteria();                  // oder new Criteria([$id1, $id2]) für gezielte IDs
$criteria->setLimit(25)->setOffset(0);
$criteria->addAssociation('lines.product');  // verschachtelt nachladen
$criteria->getAssociation('lines')->addSorting(new FieldSorting('position'));
$criteria->setTotalCountMode(Criteria::TOTAL_COUNT_MODE_EXACT);
```

Bausteine: **Filter** (`sw-filters`), **Sorting** (`sw-sorting`), **Aggregations** (`sw-aggregations`).
Associations gezielt laden (kein `autoload`). `addAssociation('a.b.c')` lädt verschachtelt.

→ Vollständige Criteria-Referenz: [CRITERIA-SEARCH-CRITERIA.md](CRITERIA-SEARCH-CRITERIA.md)
