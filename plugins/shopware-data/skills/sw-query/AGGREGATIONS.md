# Shopware 6 — Criteria aggregations

Aggregations compute metrics and facets server-side.

```php
$criteria->addAggregation(new TermsAggregation('per-cat', 'categoryId', null, null,
    new SumAggregation('sum-price', 'price')));      // nested
$criteria->addAggregation(new StatsAggregation('stats', 'price'));

$result = $repo->aggregate($criteria, $context);
$terms  = $result->get('per-cat'); // TermsResult with buckets
```

Types include `TermsAggregation` (grouping), `CountAggregation`, `SumAggregation`, `AvgAggregation`,
`MinAggregation`/`MaxAggregation`, `StatsAggregation`, `FilterAggregation` (pre-filtering), `EntityAggregation`.
Use `aggregate()` (metrics only) or run them as part of `search()`.

→ All aggregation types and bucket evaluation: [AGGREGATIONS-SEARCH-CRITERIA.md](AGGREGATIONS-SEARCH-CRITERIA.md)
