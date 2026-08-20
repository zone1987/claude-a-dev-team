# Shopware 6 DAL reference (complete reference)

Sources: `troubleshooting/dal-reference/filters-reference.md`, `aggregations-reference.md`, `flags-reference.md`, `fields-reference/index.md`, `enum-field.md`

## Contents

- [Filter reference](#filter-reference)
- [Aggregation reference](#aggregation-reference)
- [Flags reference](#flags-reference)
- [Fields reference (overview of all field classes)](#fields-reference-overview-of-all-field-classes)
- [EnumField — usage](#enumfield--usage)

## Filter reference

All filters are case-insensitive for string fields (storage system).

### equals

Exact match. SQL: `WHERE stock = 10`

```php
$criteria->addFilter(new EqualsFilter('stock', 10));
```

```json
{"filter": [{"type": "equals", "field": "stock", "value": 10}]}
```

### equalsAny

At least one exact match. SQL: `WHERE productNumber IN ('...', '...')`

```php
$criteria->addFilter(new EqualsAnyFilter('productNumber', ['AAA', 'BBB']));
```

```json
{"filter": [{"type": "equalsAny", "field": "productNumber", "value": ["AAA", "BBB"]}]}
```

### contains

Wildcard before and after. SQL: `WHERE name LIKE '%Lightweight%'`

```php
$criteria->addFilter(new ContainsFilter('name', 'Lightweight'));
```

```json
{"filter": [{"type": "contains", "field": "name", "value": "Lightweight"}]}
```

### prefix

Wildcard at the start only. SQL: `WHERE name LIKE 'Lightweight%'`

```php
$criteria->addFilter(new PrefixFilter('name', 'Lightweight'));
```

```json
{"filter": [{"type": "prefix", "field": "name", "value": "Lightweight"}]}
```

### suffix

Wildcard at the end only. SQL: `WHERE name LIKE '%Lightweight'`

```php
$criteria->addFilter(new SuffixFilter('name', 'Lightweight'));
```

```json
{"filter": [{"type": "suffix", "field": "name", "value": "Lightweight"}]}
```

### range

Value range for numbers or dates. Parameters: `gte`, `lte`, `gt`, `lt`.
SQL: `WHERE stock >= 20 AND stock <= 30`

```php
$criteria->addFilter(new RangeFilter('stock', [
    RangeFilter::GTE => 20,
    RangeFilter::LTE => 30,
]));
```

```json
{"filter": [{"type": "range", "field": "stock", "parameters": {"gte": 20, "lte": 30}}]}
```

### not

A container that negates any filter. `operator`: `or`, `and`.
SQL: `WHERE !(stock = 1 OR availableStock = 1) AND active = 1`

```php
$criteria->addFilter(new EqualsFilter('active', true));
$criteria->addFilter(new NotFilter(NotFilter::CONNECTION_OR, [
    new EqualsFilter('stock', 1),
    new EqualsFilter('availableStock', 10),
]));
```

```json
{"filter": [
  {"type": "not", "operator": "or", "queries": [
    {"type": "equals", "field": "stock", "value": 1},
    {"type": "equals", "field": "availableStock", "value": 1}
  ]},
  {"type": "equals", "field": "active", "value": true}
]}
```

### multi

Logical combination of several filters. `operator`: `or`, `and`.
SQL: `WHERE (stock = 1 OR availableStock = 1) AND active = 1`

```php
$criteria->addFilter(new MultiFilter(MultiFilter::CONNECTION_OR, [
    new EqualsFilter('stock', 1),
    new EqualsFilter('availableStock', 10),
]));
$criteria->addFilter(new EqualsFilter('active', true));
```

```json
{"filter": [
  {"type": "multi", "operator": "or", "queries": [
    {"type": "equals", "field": "stock", "value": 1},
    {"type": "equals", "field": "availableStock", "value": 1}
  ]},
  {"type": "equals", "field": "active", "value": true}
]}
```

---

## Aggregation reference

### avg — average

```php
$criteria->addAggregation(new AvgAggregation('avg-price', 'price'));
$aggregation = $result->getAggregations()->get('avg-price');
$aggregation->getAvg();
```

```json
{"aggregations": [{"name": "avg-price", "type": "avg", "field": "price"}]}
```

### count — DISTINCT count

```php
$criteria->addAggregation(new CountAggregation('count-manufacturers', 'manufacturerId'));
$aggregation->getCount();
```

### max — maximum

```php
$criteria->addAggregation(new MaxAggregation('max-price', 'price'));
$aggregation->getMax();
```

### min — minimum

```php
$criteria->addAggregation(new MinAggregation('min-price', 'price'));
$aggregation->getMin();
```

### sum — sum

```php
$criteria->addAggregation(new SumAggregation('sum-price', 'price'));
$aggregation->getSum();
```

### stats — several metrics

```php
$criteria->addAggregation(new StatsAggregation('stats-price', 'price'));
$aggregation->getSum();
$aggregation->getMax();
$aggregation->getAvg();
$aggregation->getMin();
```

### terms — groups + count (bucket)

Supports: `limit`, `sort`, a nested `aggregation`.

```php
$criteria->addAggregation(new TermsAggregation(
    'manufacturer-ids',
    'manufacturerId',
    10, // limit
    new FieldSorting('manufacturer.name', FieldSorting::DESCENDING)
));
foreach ($aggregation->getBuckets() as $bucket) {
    $bucket->getKey();
    $bucket->getCount();
}
```

```json
{"aggregations": [{
  "name": "manufacturer-ids",
  "type": "terms",
  "limit": 3,
  "sort": {"field": "manufacturer.name", "order": "DESC"},
  "field": "manufacturerId"
}]}
```

### entity — load entities (bucket)

Like `terms`, but loads the corresponding entities using the keys as IDs:

```php
$criteria->addAggregation(new EntityAggregation('manufacturers', 'manufacturerId', 'product_manufacturer'));
foreach ($aggregation->getEntities() as $entity) {
    $entity->getName();
}
```

```json
{"aggregations": [{
  "name": "manufacturers",
  "type": "entity",
  "definition": "product_manufacturer",
  "field": "manufacturerId"
}]}
```

### filter — filter the aggregation (bucket)

Filters only the aggregation, not the search result:

```php
$criteria->addAggregation(new FilterAggregation(
    'active-price-avg',
    new AvgAggregation('avg-price', 'price'),
    [new EqualsFilter('active', true)]
));
```

```json
{"aggregations": [{
  "name": "active-price-avg",
  "type": "filter",
  "filter": [{"type": "equals", "field": "active", "value": true}],
  "aggregation": {"name": "avg-price", "type": "avg", "field": "price"}
}]}
```

### histogram — date grouping (bucket)

Intervals: `minute`, `hour`, `day`, `week`, `month`, `quarter`, `year`

```php
$criteria->addAggregation(new DateHistogramAggregation(
    'release-dates',
    'releaseDate',
    DateHistogramAggregation::PER_MONTH
));
foreach ($aggregation->getBuckets() as $bucket) {
    $bucket->getKey(); // e.g. "2020-04-01 00:00:00"
    $bucket->getCount();
}
```

```json
{"aggregations": [{
  "name": "release-dates",
  "type": "histogram",
  "field": "releaseDate",
  "interval": "month"
}]}
```

### range — value ranges (bucket)

`from`: >=, `to`: <

```php
$criteria->addAggregation(new RangeAggregation('price_ranges', 'products.price', [
    ['to' => 100],
    ['from' => 100, 'to' => 200],
    ['from' => 200],
]));
foreach ($aggregation->getRanges() as $key => $docCount) { ... }
```

### Nested aggregations

```php
// Number of manufacturers per category for products > 500 €
$criteria->addAggregation(new FilterAggregation('my-filter',
    new TermsAggregation('per-category', 'categories.id', null, null,
        new TermsAggregation('manufacturer-ids', 'manufacturerId')
    ),
    [new RangeFilter('price', ['gte' => 500])]
));
```

---

## Flags reference

| Flag | Description |
|---|---|
| `ApiAware` | Field available in the Store or Admin API. Default: both APIs. Can be restricted to `AdminApiSource`/`SalesChannelApiSource`. |
| `Required` | Mandatory field on creation (create request). Only relevant when writing. |
| `PrimaryKey` | Defines the field as part of the primary key. Usually the ID field. |
| `Runtime` | The value is computed at runtime (event subscriber or similar). Not stored in the DB directly. |
| `Computed` | Indexers or external systems compute the value. No direct DAL write possible. |
| `WriteProtected` | API write access restricted. Protects indexed data from direct API writes. |
| `Inherited` | The parent record can pass on the value of this field. |
| `ReverseInherited` | Counterpart to Inherited. |
| `CascadeDelete` | When the referenced data is deleted, this data is deleted too. |
| `RestrictDelete` | Prevents deletion of the entity while a record with this FK exists. |
| `SetNullOnDelete` | The FK is set to NULL when the referenced data is deleted. A written event is dispatched. |
| `Immutable` | Write-once: can be set on creation, read-only afterwards. |
| `Extension` | Data is stored in `Entity::$extension`, not in the struct itself. |
| `SearchRanking` | Weighting for the full-text search query on this entity for this field. |
| `Deprecated` | Field marked as deprecated. Will be removed with the next major version. |
| `Since` | From which Shopware version the field is available. |
| `AllowHtml` | HTML-escaped data allowed in the column. Caution: injection risk. |
| `AllowEmptyString` | An empty string should not be treated as NULL. |

---

## Fields reference (overview of all field classes)

| Field class | Description | Extends | StorageAware |
|---|---|---|---|
| `IdField` | UUID primary key | Field | x |
| `FkField` | Foreign key | Field | x |
| `StringField` | String value | Field | x |
| `LongTextField` | Longtext | Field | x |
| `EmailField` | Email (extends String) | StringField | - |
| `IntField` | Integer | Field | x |
| `FloatField` | Float | Field | x |
| `BoolField` | Boolean | Field | x |
| `DateField` | Date | Field | x |
| `DateTimeField` | DateTime | Field | x |
| `JsonField` | JSON value | Field | x |
| `ListField` | JSON array | JsonField | - |
| `ObjectField` | JSON object | JsonField | - |
| `PriceField` | Price struct (JSON) | JsonField | - |
| `BlobField` | Blob | Field | x |
| `SerializedField` | Serialized value | Field | x |
| `PasswordField` | Password | Field | x |
| `EnumField` | BackedEnum value | Field | x |
| `TranslatedField` | Translated value | Field | - |
| `CreatedAtField` | Created timestamp | DateTimeField | - |
| `UpdatedAtField` | Updated timestamp | DateTimeField | - |
| `ParentFkField` | Parent FK | FkField | - |
| `VersionField` | Version FK | FkField | - |
| `StateMachineStateField` | State machine FK | FkField | - |
| `ManyToOneAssociationField` | n:1 | AssociationField | - |
| `OneToManyAssociationField` | 1:n | AssociationField | - |
| `ManyToManyAssociationField` | n:m | AssociationField | - |
| `OneToOneAssociationField` | 1:1 | AssociationField | - |
| `ParentAssociationField` | Parent link | ManyToOneAssociationField | - |
| `ChildrenAssociationField` | Children link | OneToManyAssociationField | - |
| `TranslationsAssociationField` | Translation association | OneToManyAssociationField | - |
| `TreeLevelField` | Tree level | IntField | - |
| `TreePathField` | Tree path | LongTextField | - |
| `ChildCountField` | Children count | IntField | - |
| `AutoIncrementField` | Auto increment | IntField | - |

## EnumField — usage

```php
// Define the BackedEnum:
enum PaymentMethod: string {
    case PAYPAL = 'paypal';
    case CREDIT_CARD = 'credit_card';
}

// In the entity:
#[Field(type: FieldType::ENUM, column: 'payment_method')]
protected PaymentMethod $paymentMethod;

// Validation:
$validMethod = PaymentMethod::tryFrom($userInput);
if ($validMethod === null) { /* Invalid value */ }

// DB: ENUM type for strings; an INT column is recommended for integer enums
```

Twig example:
```twig
<select name="payment_method">
    {% for method in PaymentMethod::cases() %}
        <option value="{{ method.value }}">{{ method.name }}</option>
    {% endfor %}
</select>
```
