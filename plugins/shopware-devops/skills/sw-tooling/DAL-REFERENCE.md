# Shopware 6 — DAL reference (filters, aggregations, flags, fields)

## Filter types

| Type | PHP class | Description |
|---|---|---|
| `equals` | `EqualsFilter` | Exact match |
| `equalsAny` | `EqualsAnyFilter` | At least one match from a list (IN) |
| `contains` | `ContainsFilter` | LIKE '%value%' |
| `prefix` | `PrefixFilter` | LIKE 'value%' |
| `suffix` | `SuffixFilter` | LIKE '%value' |
| `range` | `RangeFilter` | gte/lte/gt/lt for numbers/dates |
| `not` | `NotFilter` | Negates any filter |
| `multi` | `MultiFilter` | AND/OR combination of several filters |

```php
// range: gte, lte, gt, lt
$criteria->addFilter(new RangeFilter('stock', [RangeFilter::GTE => 20, RangeFilter::LTE => 30]));

// multi with OR
$criteria->addFilter(new MultiFilter(MultiFilter::CONNECTION_OR, [
    new EqualsFilter('stock', 1),
    new EqualsFilter('availableStock', 10),
]));

// not
$criteria->addFilter(new NotFilter(NotFilter::CONNECTION_OR, [
    new EqualsFilter('stock', 1),
]));
```

## Aggregation types

| Type | PHP class | Kind | Description |
|---|---|---|---|
| `avg` | `AvgAggregation` | metric | Average |
| `count` | `CountAggregation` | metric | DISTINCT count |
| `max` | `MaxAggregation` | metric | Maximum |
| `min` | `MinAggregation` | metric | Minimum |
| `sum` | `SumAggregation` | metric | Sum |
| `stats` | `StatsAggregation` | metric | Avg+Min+Max+Sum in one |
| `terms` | `TermsAggregation` | bucket | Groups + count; supports limit/sort/aggregation |
| `entity` | `EntityAggregation` | bucket | Like terms, loads entities via IDs |
| `filter` | `FilterAggregation` | bucket | Filters only the aggregation (not the result) |
| `histogram` | `DateHistogramAggregation` | bucket | Date grouping (minute/hour/day/week/month/quarter/year) |
| `range` | `RangeAggregation` | bucket | Predefined value ranges (from/to) |

## Flags reference

| Flag | Description |
|---|---|
| `ApiAware` | Field available in the Store or Admin API |
| `Required` | Mandatory field on creation |
| `PrimaryKey` | Part of the primary key |
| `Runtime` | Computed at runtime, not stored in the DB |
| `Computed` | An indexer computes the value — no direct API write |
| `WriteProtected` | API write restricted |
| `Inherited` | Parent inheritance possible |
| `CascadeDelete` | Deletes associated data along with it |
| `RestrictDelete` | Prevents deletion while a reference exists |
| `SetNullOnDelete` | Sets the FK to NULL when the reference is deleted |
| `Immutable` | Write-once, then read-only |
| `Extension` | Data in `Entity::$extension`, not in the struct |
| `SearchRanking` | Weighting for the full-text search |
| `Deprecated` | Marked as deprecated |
| `Since` | From which Shopware version it is available |
| `AllowHtml` | HTML content allowed |
| `AllowEmptyString` | Empty string ≠ NULL |

Complete filter and aggregation examples (PHP + API JSON): `DAL-REFERENCE-DETAIL.md`.
