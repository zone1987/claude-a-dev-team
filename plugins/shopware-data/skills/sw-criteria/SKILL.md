---
name: sw-criteria
description: >
  Die Shopware-6 Criteria-API als zentrales Query-Werkzeug der DAL: IDs, Limit/Offset, Associations laden,
  getAssociation, Total-Count-Mode, Criteria kombinieren. Trigger: "Criteria", "DAL query", "Criteria addAssociation",
  "getAssociation", "Daten abfragen DAL", "limit offset criteria", "wie Daten laden". Shopware 6.7.
---

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

→ Vollständige Criteria-Referenz: [references/search-criteria.md](references/search-criteria.md)
