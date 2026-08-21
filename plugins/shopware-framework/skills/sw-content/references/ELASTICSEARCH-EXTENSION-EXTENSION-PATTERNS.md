# Elasticsearch extension: exhaustive reference

## Contents

- [Mapping constants in detail](#mapping-constants-in-detail)
- [buildTextFieldConfig() — logic](#buildtextfieldconfig-logic)
- [ElasticsearchFieldBuilder::translated() — language mapping](#elasticsearchfieldbuildertranslated-language-mapping)
- [Product mapping completeness](#product-mapping-completeness)
- [Custom Fields — complete type mapping table](#custom-fields-complete-type-mapping-table)
- [Admin search: fetch return format](#admin-search-fetch-return-format)
- [Admin indexer: built-in fields](#admin-indexer-built-in-fields)
- [IndexerOffset tracking](#indexeroffset-tracking)
- [Elasticsearch exception codes](#elasticsearch-exception-codes)
- [Test behaviour](#test-behaviour)
- [Sorting extension: CountSort](#sorting-extension-countsort)
- [MatchBoolPrefixQuery](#matchboolprefixquery)

## Mapping constants in detail

### AbstractElasticsearchDefinition — all mapping arrays

```php
// 1. KEYWORD_FIELD
// Exact matches, case-insensitive via lowercase normalizer
// ignore_above: 10000 bytes
[
    'type' => 'keyword',
    'ignore_above' => 10000,
    'normalizer' => 'sw_lowercase_normalizer',
]

// 2. BOOLEAN_FIELD
['type' => 'boolean']

// 3. FLOAT_FIELD
['type' => 'double']

// 4. INT_FIELD
['type' => 'long']

// 5. SEARCH_FIELD (subfields, merged with KEYWORD_FIELD via +)
[
    'fields' => [
        'search' => ['type' => 'text', 'analyzer' => 'sw_whitespace_analyzer'],
        'ngram'  => ['type' => 'text', 'analyzer' => 'sw_ngram_analyzer'],
    ],
]
// Complete: KEYWORD_FIELD + SEARCH_FIELD:
// → type: keyword, ignore_above: 10000, normalizer: sw_lowercase_normalizer
//   fields.search: text/sw_whitespace_analyzer
//   fields.ngram:  text/sw_ngram_analyzer

// 6. SEARCH_FIELD_WITH_EXACT
[
    'fields' => [
        'exact' => [
            'type' => 'text',
            'analyzer' => 'sw_whitespace_analyzer',
            'search_analyzer' => 'sw_whitespace_analyzer',
            'norms' => false,
        ],
        'search' => ['type' => 'text', 'analyzer' => 'sw_whitespace_analyzer'],
        'ngram'  => ['type' => 'text', 'analyzer' => 'sw_ngram_analyzer'],
    ],
]

// 7. SEARCH_FIELD_WITH_LENGTH_NORM (for description, metaDescription)
[
    'fields' => [
        'search' => [
            'type' => 'text',
            'analyzer' => 'sw_whitespace_analyzer',
            'similarity' => 'sw_length_norm',  // BM25 b=0.75
        ],
        'ngram' => ['type' => 'text', 'analyzer' => 'sw_ngram_analyzer'],
    ],
]

// 8. TECHNICAL_TERM_SEARCH_FIELD (for productNumber, ean, manufacturerNumber)
[
    'fields' => [
        'search' => [
            'type' => 'text',
            'analyzer' => 'sw_whitespace_technical_term_index_analyzer',  // index-side: word_delimiter_graph
            'search_analyzer' => 'sw_whitespace_technical_term_search_analyzer', // search-side + dedup
        ],
        'ngram' => ['type' => 'text', 'analyzer' => 'sw_ngram_analyzer'],
    ],
]
```

---

## buildTextFieldConfig() — logic

```php
protected static function buildTextFieldConfig(
    bool $withExact = false,
    bool $technicalTerms = false,
    bool $lengthNorm = false
): array

// Step 1: choose base fields
$fieldConfig = $technicalTerms
    ? self::TECHNICAL_TERM_SEARCH_FIELD   // word_delimiter_graph for SKUs
    : self::SEARCH_FIELD;                  // whitespace + ngram

// Step 2: lengthNorm → override similarity
if ($lengthNorm) {
    $fieldConfig['fields']['search']['similarity'] = 'sw_length_norm';
}

// Step 3: prepend exact subfield
if ($withExact) {
    $fieldConfig['fields'] = ['exact' => self::SEARCH_FIELD_WITH_EXACT['fields']['exact']]
                           + $fieldConfig['fields'];
}

// Step 4: merge KEYWORD_FIELD + fieldConfig
return self::KEYWORD_FIELD + $fieldConfig;
```

Depending on the flags this yields:
- `()` → keyword + search(whitespace) + ngram
- `(withExact)` → keyword + exact(whitespace, no norms) + search(whitespace) + ngram
- `(technicalTerms)` → keyword + search(word_delimiter_graph) + ngram
- `(withExact, technicalTerms)` → keyword + exact + search(wdg) + ngram
- `(lengthNorm)` → keyword + search(whitespace, sw_length_norm) + ngram
- `(withExact, technicalTerms, lengthNorm)` → keyword + exact + search(wdg, sw_length_norm) + ngram

---

## ElasticsearchFieldBuilder::translated() — language mapping

```php
$this->fieldBuilder->translated(array $fieldConfig): array
```

**Sequence:**
1. Load all languages via `LanguageLoaderInterface::loadLanguages()`
2. For each language: check the locale (from `code` or `parentCode`, e.g. `de-DE` → `de`)
3. If `languageAnalyzerMapping[locale]` exists:
   - Default fields (`search.analyzer == sw_whitespace_analyzer`): replace with `sw_german_analyzer` etc.
   - Technical term fields (`search.analyzer == sw_whitespace_technical_term_index_analyzer`):
     replace with the language-specific `sw_german_technical_term_index_analyzer` / `_search_analyzer`
     (only if present for the language, otherwise fall back to the generic technical term analyzer)
4. `.exact` and `.ngram` always stay language-agnostic

**Return value:**
```php
[
    'properties' => [
        '2fbb5fe2e29a4d70aa5854ce7ce3e20b' => $fieldConfigForLanguage1,  // languageId → config
        'f57ab71e-c7b5-4c94-b7a7-c7b5c7b5c7b5' => $fieldConfigForLanguage2,
        // ...
    ],
]
```

For fields without a language analyzer (no match in `languageAnalyzerMapping`):
all languages get the same `fieldConfig` (generic analyzer).

---

## Product mapping completeness

### All indexed product fields

```php
// Text fields (translated)
'name'                → translated + withExact + technicalTerms (exact match + SKU analysis + language-specific)
'description'         → translated + lengthNorm (BM25 length normalization)
'metaTitle'           → translated
'metaDescription'     → translated + lengthNorm
'customSearchKeywords'→ translated + withExact + technicalTerms + lengthNorm (everything)

// SKU fields (not translated, since language-independent)
'productNumber'       → buildTextFieldConfig(withExact: true, technicalTerms: true)
'ean'                 → buildTextFieldConfig(withExact: true, technicalTerms: true)
'manufacturerNumber'  → buildTextFieldConfig(withExact: true, technicalTerms: true)

// Nested associations
'categories'          → nested {id, _count, name: translated}
'parent'              → nested {id, _count, name: translated + withExact + technicalTerms}
'manufacturer'        → nested {id, _count, name: translated}
'deliveryTime'        → nested {id, _count, name: translated}
'options'             → nested {id, _count, groupId: keyword, name: translated}
'properties'          → nested {id, _count, groupId: keyword, name: translated, group: nested{}}
'tags'                → nested {id, _count, name: text+exact (buildTextFieldConfig)}
'visibilities'        → nested {id: null, salesChannelId: keyword, visibility: int}
                        PLUS flattened: 'visibility_{salesChannelId}' → integer

// Boolean
'active', 'available', 'isCloseout', 'shippingFree', 'markAsTopseller' → boolean

// Integer
'stock', 'availableStock', 'sales', 'childCount', 'autoIncrement' → long

// Float
'ratingAverage', 'weight', 'width', 'length', 'height' → double

// Keyword
'id', 'parentId', 'coverId', 'taxId', 'manufacturerId', 'deliveryTimeId',
'displayGroup', 'type', 'states', 'categoryTree', 'categoryIds',
'propertyIds', 'optionIds', 'tagIds', 'streamIds' → keyword

// Date
'releaseDate', 'createdAt' → date (ISO + epoch_millis + custom)

// Dynamic (Custom Fields)
'customFields' → {properties: {[langId]: {type: object, dynamic: true, properties: {fieldName: esType}}}}

// Dynamic templates (from the mapping array)
'cheapest_price_rule*' → match → double
'price.*.percentage.*' → path_match → double
'long' type match → double
```

### `_source` optimization

If `elasticsearch.product.exclude_source = false` (default) and not dev/test:
```php
$mapping['_source'] = ['includes' => ['id', 'autoIncrement']];
```
Minimizes memory, since only IDs are read from `_source` (data comes from the DB).

---

## Custom Fields — complete type mapping table

From `ElasticsearchCustomFieldsMappingHelper::getTypeFromCustomFieldType()`:

| `CustomFieldTypes::*` | Value | ES mapping |
|----------------------|------|-----------|
| `INT` | `'int'` | `{type: 'long'}` |
| `FLOAT` | `'float'` | `{type: 'double'}` |
| `BOOL` | `'bool'` | `{type: 'boolean'}` |
| `DATETIME` | `'datetime'` | `{type: 'date', format: 'yyyy-MM-dd HH:mm:ss.SSS\|\|strict_date_optional_time\|\|epoch_millis', ignore_malformed: true}` |
| `PRICE` | `'price'` | `{type: 'object', dynamic: true}` |
| `JSON` | `'json'` | `{type: 'object', dynamic: true}` |
| all others (SELECT, MULTI_SELECT, TEXT, HTML, etc.) | various | `KEYWORD_FIELD + SEARCH_FIELD` |

**Dynamically loading new custom fields:**
`ElasticsearchCustomFieldsMappingHelper::createFieldsInIndices()` → `putMapping()` on all active indices, per language.

---

## Admin search: fetch return format

```php
// Required fields per ID:
[
    'id'         => string,       // hex UUID
    'text'       => string,       // main search text (indexed into TEXT_FIELD)
    'textBoosted'=> string|null,  // boosted search text (higher score)
    'completion' => list<string>|null, // lowercase dedupe for COMPLETION_FIELD
]
```

**`buildCompletion()` helper:**
```php
$this->buildCompletion(['T-Shirt Basic', 'Shirt', null, ''])
// → ['t-shirt basic', 'shirt']  (null/empty filtered, lowercase, dedupe)
```

**`decodeTranslatedValues()` helper:**
```php
// encoded = JSON string from SQL: '[{"languageId":"...","name":"..."}]'
$this->decodeTranslatedValues($encoded, 'name')
// → ['2fbb...5b' => 'Product Name', ...]
```

---

## Admin indexer: built-in fields

All concrete admin indexers inherit the default fields from `AbstractAdminIndexer::mapping()`:
`id` (KEYWORD_FIELD) is always added.

Typical pattern for texts:
```php
public function mapping(array $mapping): array {
    $mapping['properties']['name']        = self::TEXT_FIELD;
    $mapping['properties']['email']       = self::TEXT_FIELD;
    $mapping['properties']['completion']  = self::COMPLETION_FIELD; // for autocomplete
    return $mapping;
}
```

### COMPLETION_FIELD in detail

```php
[
    'type' => 'text',
    'analyzer' => 'sw_admin_completion_index_analyzer',   // word_delimiter_graph chain
    'search_analyzer' => 'sw_admin_completion_search_analyzer',
    'fields' => [
        'ngram' => [
            'type' => 'text',
            'analyzer' => 'sw_ngram_analyzer',
            'search_analyzer' => 'sw_whitespace_analyzer', // short queries → ngram path
        ],
    ],
]
```

---

## IndexerOffset tracking

```php
$offset = new IndexerOffset(
    definitions: iterable<string>,  // entity names
    timestamp: int                  // Unix timestamp for the index suffix
);

$offset->getDefinition(): ?string
$offset->hasNextDefinition(): bool
$offset->selectNextDefinition(): void
$offset->getLastId(): ?array
$offset->setLastId(?array): void
$offset->getTimestamp(): int
```

`IndexerOffset` is serialized as part of `ElasticsearchIndexingMessage`.

---

## Elasticsearch exception codes

```php
ElasticsearchException::serverNotAvailable()
ElasticsearchException::definitionNotFound(string $entityName)
ElasticsearchException::unsupportedElasticsearchDefinition(string $entityName)
ElasticsearchException::indexingError(array $errors)
ElasticsearchException::emptyIndexingRequest()
```

---

## Test behaviour

### ElasticsearchTestTestBehaviour

Trait for PHPUnit tests that index against ES:
- Writes test data into the ES index
- Cleans up after the test

### AdminElasticsearchTestBehaviour

Analogous trait for admin search tests.

---

## Sorting extension: CountSort

`CountSort` implements `BuilderInterface` for sorting by the count in nested fields
(e.g. sorting products by number of properties).

---

## MatchBoolPrefixQuery

Custom OpenSearchDSL query class for `match_bool_prefix` — used in `ProductSearchQueryBuilder`
for prefix matching in full-text search.
