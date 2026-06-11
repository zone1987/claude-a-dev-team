---
name: sw-aggregations
description: >
  Aggregationen in der Shopware-6 Criteria-API: TermsAggregation, CountAggregation, SumAggregation, AvgAggregation,
  StatsAggregation, FilterAggregation, verschachtelte Aggregationen + Ergebnis auslesen.
  Trigger: "Aggregation criteria", "TermsAggregation", "SumAggregation", "Statistik DAL", "gruppieren zählen",
  "getAggregations", "facetten". Shopware 6.7.
---

# Shopware 6 — Criteria-Aggregations

Aggregationen berechnen Kennzahlen/Facetten serverseitig.

```php
$criteria->addAggregation(new TermsAggregation('per-cat', 'categoryId', null, null,
    new SumAggregation('sum-price', 'price')));      // verschachtelt
$criteria->addAggregation(new StatsAggregation('stats', 'price'));

$result = $repo->aggregate($criteria, $context);
$terms  = $result->get('per-cat'); // TermsResult mit buckets
```

Typen u.a. `TermsAggregation` (Gruppieren), `CountAggregation`, `SumAggregation`, `AvgAggregation`,
`MinAggregation`/`MaxAggregation`, `StatsAggregation`, `FilterAggregation` (vorfiltern), `EntityAggregation`.
Mit `aggregate()` (nur Kennzahlen) oder als Teil von `search()`.

→ Alle Aggregations-Typen & Bucket-Auswertung: [references/search-criteria.md](references/search-criteria.md)
