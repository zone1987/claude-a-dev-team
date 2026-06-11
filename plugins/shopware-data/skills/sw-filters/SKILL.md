---
name: sw-filters
description: >
  Filter in der Shopware-6 Criteria-API: EqualsFilter, EqualsAnyFilter, ContainsFilter, RangeFilter, MultiFilter
  (AND/OR), NotFilter, PrefixFilter, post-filter. Trigger: "Filter criteria", "EqualsFilter", "RangeFilter",
  "MultiFilter AND OR", "ContainsFilter", "NotFilter", "nach Wert filtern DAL". Shopware 6.7.
---

# Shopware 6 — Criteria-Filter

Filter schränken Ergebnisse ein, via `$criteria->addFilter(...)`.

```php
$criteria->addFilter(new EqualsFilter('active', true));
$criteria->addFilter(new EqualsAnyFilter('id', $ids));
$criteria->addFilter(new RangeFilter('price', [RangeFilter::GTE => 10, RangeFilter::LT => 50]));
$criteria->addFilter(new MultiFilter(MultiFilter::CONNECTION_OR, [
    new ContainsFilter('name', 'foo'),
    new PrefixFilter('name', 'bar'),
]));
$criteria->addFilter(new NotFilter(NotFilter::CONNECTION_AND, [new EqualsFilter('stock', 0)]));
```

`addFilter` filtert vor Aggregationen, `addPostFilter` danach (für Aggregations-unabhängige Anzeige).
Verschachtelte Felder per Punktnotation (`lines.product.active`).

→ Alle Filter-Typen: [references/search-criteria.md](references/search-criteria.md)
