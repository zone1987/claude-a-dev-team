# Shopware 6 — Criteria filters

Filters narrow the result set, via `$criteria->addFilter(...)`.

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

`addFilter` filters before aggregations, `addPostFilter` after them (for display independent of the aggregations).
Reach nested fields with dot notation (`lines.product.active`).

→ All filter types: [FILTERS-SEARCH-CRITERIA.md](FILTERS-SEARCH-CRITERIA.md)
