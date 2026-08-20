---
name: sw-query
description: Shopware DAL queries: the Criteria API, filters, sorting, aggregations, and when plain SQL beats the DAL. Use when the request names a Shopware Criteria, DAL filter or aggregation.
---

# Shopware DAL queries

Reading data. Criteria is the single entry point; filters, sorting and aggregations are its parts.

## Reference map

- **[AGGREGATIONS.md](AGGREGATIONS.md)**: Aggregationen berechnen Kennzahlen/Facetten serverseitig. [AGGREGATIONS-SEARCH-CRITERIA](AGGREGATIONS-SEARCH-CRITERIA.md).
- **[CRITERIA.md](CRITERIA.md)**: `Criteria` ist der Query-Builder der DAL. [CRITERIA-SEARCH-CRITERIA](CRITERIA-SEARCH-CRITERIA.md).
- **[FILTERS.md](FILTERS.md)**: Filter schränken Ergebnisse ein, via `$criteria->addFilter`. [FILTERS-SEARCH-CRITERIA](FILTERS-SEARCH-CRITERIA.md).
- **[PLAIN-SQL-VS-DAL.md](PLAIN-SQL-VS-DAL.md)**: Risiko bei SQL: keine Write-Events, kein Cache-Invalidation, keine Translation-/Inheritance-Logik, UUID-Binar….
- **[SORTING.md](SORTING.md)**: Mehrere Sortierungen werden in Reihenfolge angewendet. [SORTING-SEARCH-CRITERIA](SORTING-SEARCH-CRITERIA.md).

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) (Data Abstraction Layer guides and reference) plus the Shopware 6.7 source, retrieved 2026-08-20.
