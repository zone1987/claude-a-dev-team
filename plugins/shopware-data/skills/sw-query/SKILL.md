---
name: sw-query
description: Shopware DAL queries: the Criteria API, filters, sorting, aggregations, and when plain SQL beats the DAL. Use when the request names a Shopware Criteria, DAL filter or aggregation.
---

# Shopware DAL queries

Reading data. Criteria is the single entry point; filters, sorting and aggregations are its parts.

## Reference map

- **[AGGREGATIONS.md](references/AGGREGATIONS.md)**: Aggregations compute metrics and facets server-side. [AGGREGATIONS-SEARCH-CRITERIA](references/AGGREGATIONS-SEARCH-CRITERIA.md).
- **[CRITERIA.md](references/CRITERIA.md)**: `Criteria` is the DAL's query builder. [CRITERIA-SEARCH-CRITERIA](references/CRITERIA-SEARCH-CRITERIA.md).
- **[FILTERS.md](references/FILTERS.md)**: Filters narrow the result set, via `$criteria->addFilter`. [FILTERS-SEARCH-CRITERIA](references/FILTERS-SEARCH-CRITERIA.md).
- **[PLAIN-SQL-VS-DAL.md](references/PLAIN-SQL-VS-DAL.md)**: The risk with SQL: no write events, no cache invalidation, no translation/inheritance logic, UUID binar….
- **[SORTING.md](references/SORTING.md)**: Multiple sortings apply in the order they are added. [SORTING-SEARCH-CRITERIA](references/SORTING-SEARCH-CRITERIA.md).

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) (Data Abstraction Layer guides and reference) plus the Shopware 6.7 source, retrieved 2026-08-20.
