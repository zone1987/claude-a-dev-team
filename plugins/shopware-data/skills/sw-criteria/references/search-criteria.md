# Search / Criteria System

## Criteria

**Extends:** `Struct`, implements `\Stringable`
**Marked:** `@final`

Central query builder for all DAL read operations. Composes filters, sorting, aggregations, score queries, and grouping.

### Constants

| Constant | Value | Description |
|---|---|---|
| `TOTAL_COUNT_MODE_NONE` | `0` | No total count (fastest) |
| `TOTAL_COUNT_MODE_EXACT` | `1` | Exact total count |
| `TOTAL_COUNT_MODE_NEXT_PAGES` | `2` | Fetches limit*5+1 (fast "has next page" check) |

### Constructor

```php
public function __construct(?array $ids = null, protected int $nestingLevel = 0)
```

### All Public Methods

**Filtering:**
- `addFilter(Filter ...$queries): self`
- `setFilter(string $key, Filter $filter): self`
- `getFilters(): array`
- `hasEqualsFilter(string $field): bool`
- `resetFilters(): self`
- `addPostFilter(Filter ...$queries): self` (applied AFTER aggregations)
- `getPostFilters(): list<Filter>`
- `resetPostFilters(): self`

**Sorting:**
- `addSorting(FieldSorting ...$sorting): self`
- `getSorting(): list<FieldSorting>`
- `resetSorting(): self`

**Aggregations:**
- `addAggregation(Aggregation ...$aggregations): self`
- `getAggregations(): array<string, Aggregation>`
- `getAggregation(string $name): ?Aggregation`
- `resetAggregations(): self`

**Score Queries (full-text ranking):**
- `addQuery(ScoreQuery ...$queries): self`
- `getQueries(): list<ScoreQuery>`
- `resetQueries(): self`

**Grouping:**
- `addGroupField(FieldGrouping $grouping): self`
- `getGroupFields(): list<FieldGrouping>`

**Associations (dot-path support):**
- `addAssociation(string $path): self` (e.g., `'categories.media.thumbnails'`)
- `addAssociations(array $paths): self`
- `getAssociation(string $path): Criteria` (creates missing nested criteria)
- `hasAssociation(string $field): bool`
- `removeAssociation(string $association): void`
- `resetAssociations(): self`

**Pagination:**
- `setIds(array $ids): self` / `getIds(): array`
- `setOffset(?int $offset): self` / `getOffset(): ?int`
- `setLimit(?int $limit): self` / `getLimit(): ?int`
- `setTotalCountMode(int $mode): self` / `getTotalCountMode(): int`

**Search:**
- `setTerm(?string $term): self` / `getTerm(): ?string`

**Partial fields:**
- `addFields(list<string> $fields): self` / `getFields(): list<string>`
- `setIncludes(?array $includes): void` / `setExcludes(?array $excludes): void`

**Debug:**
- `setTitle(?string $title): self` / `getTitle(): ?string`

**Utility:**
- `cloneForRead(array $ids = []): Criteria` (keeps only associations, fields, title)
- `useIdSorting(): bool` (true if IDs present with no sorting/term/queries)

### Design: Filters vs PostFilters

- **Filters** apply before aggregations
- **PostFilters** apply after aggregations

This is critical for faceted search: aggregation counts should be unaffected by the current facet selection.

---

## Filters

### Hierarchy

```
Filter (abstract)
  ├── SingleFieldFilter (abstract)
  │     ├── EqualsFilter
  │     ├── EqualsAnyFilter
  │     ├── ContainsFilter
  │     ├── PrefixFilter
  │     ├── SuffixFilter
  │     └── RangeFilter
  └── MultiFilter
        ├── AndFilter
        ├── OrFilter
        ├── XOrFilter
        └── NotFilter
              ├── NandFilter
              ├── NorFilter
              ├── NotEqualsFilter
              └── NotEqualsAnyFilter
```

### EqualsFilter

```php
new EqualsFilter(string $field, string|bool|float|int|null $value)
```
SQL: `field = value`

### EqualsAnyFilter

```php
new EqualsAnyFilter(string $field, array $value)
```
SQL: `field IN (value1, value2, ...)`

### ContainsFilter

```php
new ContainsFilter(string $field, mixed $value)
```
SQL: `field LIKE '%value%'`

### PrefixFilter

```php
new PrefixFilter(string $field, string|bool|float|int|null $value)
```
SQL: `field LIKE 'value%'`

### SuffixFilter

```php
new SuffixFilter(string $field, string|bool|float|int|null $value)
```
SQL: `field LIKE '%value'`

### RangeFilter

```php
new RangeFilter(string $field, array $parameters)
```
Constants: `LTE`, `LT`, `GTE`, `GT`
SQL: `field >= X AND field <= Y`

### MultiFilter

```php
new MultiFilter(string $operator, array $queries)
```
Operators: `CONNECTION_AND`, `CONNECTION_OR`, `CONNECTION_XOR`

### Convenience Filters

| Class | Equivalent |
|---|---|
| `AndFilter($queries)` | `MultiFilter('AND', $queries)` |
| `OrFilter($queries)` | `MultiFilter('OR', $queries)` |
| `XOrFilter($queries)` | `MultiFilter('XOR', $queries)` |
| `NotFilter('AND', $queries)` | `NOT (A AND B)` |
| `NandFilter($queries)` | `NOT (A AND B)` |
| `NorFilter($queries)` | `NOT (A OR B)` |
| `NotEqualsFilter($field, $value)` | `NOT (field = value)` |
| `NotEqualsAnyFilter($field, $values)` | `NOT (field IN (...))` |

---

## Sorting

### FieldSorting

```php
new FieldSorting(string $field, string $direction = 'ASC', bool $naturalSorting = false)
```
Constants: `ASCENDING = 'ASC'`, `DESCENDING = 'DESC'`

### CountSorting

**Extends:** `FieldSorting`
Sort by count of a to-many association.

---

## Aggregations

### Hierarchy

```
Aggregation (abstract)
  ├── MaxAggregation
  ├── MinAggregation
  ├── AvgAggregation
  ├── SumAggregation
  ├── CountAggregation
  ├── StatsAggregation
  ├── EntityAggregation
  ├── RangeAggregation
  └── BucketAggregation
        ├── TermsAggregation
        ├── FilterAggregation
        └── DateHistogramAggregation
```

### Metric Aggregations

| Class | Constructor | Result |
|---|---|---|
| `MaxAggregation` | `(string $name, string $field)` | `MaxResult` with `getMax()` |
| `MinAggregation` | `(string $name, string $field)` | `MinResult` with `getMin()` |
| `AvgAggregation` | `(string $name, string $field)` | `AvgResult` with `getAvg()` |
| `SumAggregation` | `(string $name, string $field)` | `SumResult` with `getSum()` |
| `CountAggregation` | `(string $name, string $field)` | `CountResult` with `getCount()` |
| `StatsAggregation` | `(string $name, string $field, bool $max, bool $min, bool $sum, bool $avg)` | `StatsResult` with `getMin/Max/Avg/Sum()` |
| `EntityAggregation` | `(string $name, string $field, string $entity)` | `EntityResult` with `getEntities()` |
| `RangeAggregation` | `(string $name, string $field, array $ranges)` | `RangeResult` with `getRanges()` |

### Bucket Aggregations (with optional nested sub-aggregation)

| Class | Constructor | Result |
|---|---|---|
| `TermsAggregation` | `(string $name, string $field, ?int $limit, ?FieldSorting $sorting, ?Aggregation $agg)` | `TermsResult` with `getBuckets()` |
| `FilterAggregation` | `(string $name, Aggregation $agg, array $filter)` | Delegates to inner aggregation |
| `DateHistogramAggregation` | `(string $name, string $field, string $interval, ?FieldSorting, ?Aggregation, ?string $format, ?string $timeZone)` | `DateHistogramResult` |

DateHistogram intervals: `PER_MINUTE`, `PER_HOUR`, `PER_DAY`, `PER_WEEK`, `PER_MONTH`, `PER_QUARTER`, `PER_YEAR`

---

## Score Queries

```php
new ScoreQuery(Filter $query, float $score, ?string $scoreField = null)
```

Wraps a filter with a ranking score. When the filter matches, entity's `_score` increases by the specified amount. Used for full-text search ranking.

---

## Grouping

```php
new FieldGrouping(string $field)
```

Groups results by field value (like SQL GROUP BY). Used to deduplicate (e.g., one variant per product in listings).

---

## Result Classes

### EntitySearchResult

**Extends:** `EntityCollection`

Contains: `$total`, `$entities`, `$aggregations`, `$criteria`, `$context`, `$page`, `$limit`.

### IdSearchResult

Contains: `$total`, `$ids`, `$data` (extra data per ID), `$criteria`, `$context`.
Methods: `firstId()`, `getScore(string $id)`, `getDataOfId(string $id)`.

---

## Full-Text Search

### Flow

1. `SearchTermInterpreter::interpret(string $term)` -> `SearchPattern`
2. `Tokenizer::tokenize(string)` splits term into tokens
3. `EntityScoreQueryBuilder::buildScoreQueries(SearchPattern, EntityDefinition)` generates `ScoreQuery[]` for fields with `SearchRanking` flag
4. For each ranked field: exact match query (full score) + contains query (50% score)
5. Tokens generate additional score queries
