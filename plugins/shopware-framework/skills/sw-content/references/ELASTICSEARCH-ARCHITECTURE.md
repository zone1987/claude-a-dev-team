# Shopware Elasticsearch Bundle — Exhaustive architecture reference

## Contents

- [Bundle entry point](#bundle-entry-point)
- [Configuration tree (`Configuration`)](#configuration-tree-configuration)
- [Core services](#core-services)
- [Indexing flow in detail](#indexing-flow-in-detail)
- [Storefront search integration](#storefront-search-integration)
- [Admin search integration](#admin-search-integration)
- [Product indexing](#product-indexing)
- [Custom Fields in ES](#custom-fields-in-es)
- [Indexing events](#indexing-events)
- [Analyzer constants (`ElasticsearchFieldBuilder`)](#analyzer-constants-elasticsearchfieldbuilder)
- [ElasticsearchFieldMapper (static)](#elasticsearchfieldmapper-static)
- [TokenQueryBuilder / FieldQueryBuilder](#tokenquerybuilder-fieldquerybuilder)
- [Test helper classes](#test-helper-classes)
- [Database tables](#database-tables)
- [AWS OpenSearch / SigV4](#aws-opensearch-sigv4)
- [Profiler](#profiler)

## Bundle entry point

**Class:** `Shopware\Elasticsearch\Elasticsearch extends Bundle`

Registers two compiler passes:
- `ElasticsearchMigrationCompilerPass` — integrates bundle migrations
- `ElasticsearchProfileCompilerPass` — enables the profiler in dev mode

**Extension:** `ElasticsearchExtension` loads `Resources/config/services.xml` and registers all config parameters as container parameters (`elasticsearch.*`).

---

## Configuration tree (`Configuration`)

```
elasticsearch:
  enabled: bool
  indexing_enabled: bool
  indexing_batch_size: int (default 100)
  hosts: string
  index_prefix: string
  throw_exception: bool
  ssl:
    cert_path, cert_password, cert_key_path, cert_key_password
    verify_server_cert: bool (default true)
    sigV4:
      enabled, region, service
      credentials_provider: {key_id, secret_key}
  index_settings: array        ← custom index settings (shards, replicas etc.)
  analysis: array              ← custom analyzer/tokenizer config (no deep merge!)
  language_analyzer_mapping: array  ← locale → analyzer name (e.g. de → sw_german_analyzer)
  use_language_analyzer: bool (default true)
  dimension_normalize: bool (default false)
  dynamic_templates: array
  product:
    custom_fields_mapping: array
    exclude_source: bool
  search:
    timeout, term_max_length, search_type
    precision_threshold: int|null
    dismax_tie_breaker: float (default 0.2, 0.0–1.0)
  administration:
    hosts, enabled, refresh_indices, indexing_batch_size (1000)
    index_prefix, throw_exception, index_settings, analysis, dynamic_templates
    search: {timeout, term_max_length, search_type}
```

---

## Core services

### ElasticsearchRegistry

Service ID: `Shopware\Elasticsearch\Framework\ElasticsearchRegistry`

Holds all registered `AbstractElasticsearchDefinition` instances (tagged: `shopware.es.definition`).

```php
$registry->getDefinitions(): iterable<AbstractElasticsearchDefinition>
$registry->get(string $entityName): ?AbstractElasticsearchDefinition
$registry->has(string $entityName): bool
$registry->getDefinitionNames(): iterable<string>
```

### ElasticsearchHelper

Central helper class. Checks whether search/indexing is allowed, builds DSL elements.

```php
$helper->allowIndexing(): bool              // checks ES connection + indexing_enabled
$helper->allowSearch(EntityDefinition, Context, Criteria): bool
$helper->getIndexName(EntityDefinition): string  // = prefix_entityName
$helper->isSupported(EntityDefinition): bool
$helper->handleIds(...)                     // ids → EqualsAnyFilter → BoolQuery::FILTER
$helper->addFilters(...)                    // criteria->filters → BoolQuery::FILTER
$helper->addPostFilters(...)                // criteria->postFilters → post_filter
$helper->addTerm(...)                       // criteria->term → buildTermQuery()
$helper->addQueries(...)                    // criteria->queries → BoolQuery::SHOULD
$helper->addSortings(...)                   // criteria->sorting → sort
$helper->addAggregations(...)               // criteria->aggregations → aggs
```

`MAX_SIZE_VALUE = 10000` (OpenSearch default max without custom settings).

### ElasticsearchIndexer (`#[AsMessageHandler]`)

Processes `ElasticsearchIndexingMessage` messages.

```php
$indexer->iterate(?IndexerOffset, array $entities = []): ?ElasticsearchIndexingMessage
$indexer->updateIds(EntityDefinition, array $ids): void
$indexer->__invoke(ElasticsearchIndexingMessage): void
```

Sequence in `init()`:
1. `DELETE FROM elasticsearch_index_task` (reset)
2. `DateTime::now()` as timestamp
3. For each definition: `IndexCreator::createIndex(definition, index, alias, context)`
4. Entry in `elasticsearch_index_task` (id, entity, index, alias, doc_count)

### IndexCreator

Creates the ES index with mapping + analysis config.

```php
$creator->createIndex(AbstractElasticsearchDefinition, string $index, string $alias, Context)
$creator->aliasExists(string $alias): bool
```

Config merge: `index_settings` + `analysis` + mapping from `IndexMappingProvider`.

**`dimension_normalize`:** when enabled, the `sw_dimension_normalize` char filter is injected into all `TECHNICAL_TERM_ANALYZERS`.

### IndexMappingProvider

Merges the base mapping (from `elasticsearch.yaml` `index_settings`/`analysis`/`dynamic_templates`) with the entity-specific mapping from `AbstractElasticsearchDefinition::getMapping()`.

### CreateAliasTaskHandler / CreateAliasTask

Scheduled task (runs after indexing). Switches the alias from the old to the new index (blue-green).

---

## Indexing flow in detail

```
es:index command
  ↓ iterate(null, entities)
  ElasticsearchIndexer
    ↓ IndexerOffset(definitions, timestamp)
    ↓ for each definition: createIterator(batchSize)
    ↓ ElasticsearchIndexIteratorEvent (extensible: custom iterator)
    ↓ ElasticsearchIndexingMessage(IndexingDto, IndexerOffset, Context)
  ↓ dispatch via MessageBus (or directly __invoke)
  ↓ __invoke(message)
    ↓ check allowIndexing()
    ↓ UPDATE elasticsearch_index_task SET doc_count = doc_count - idCount
    ↓ definition->fetch(hexIds, context) → array<id, document>
    ↓ bulk request: [{index: {_id: id}}, {document}]
    ↓ parseErrors()
  ↓ last batch: markAsLastMessage()
    ↓ ElasticsearchIndexingFinishedEvent
  CreateAliasTaskHandler::run()
    ↓ switch alias
    ↓ ElasticsearchIndexAliasSwitchedEvent
```

---

## Storefront search integration

### ElasticsearchEntitySearcher (decorates EntitySearcher)

```php
// Checks: allowSearch + Criteria::STATE_ELASTICSEARCH_AWARE
// Builds: ids → filter, postFilter, sorting, term, queries, aggs
// Returns: IdSearchResult
```

### ElasticsearchEntityAggregator (decorates EntityAggregator)

Runs a separate aggregation query against ES, hydrates via `ElasticsearchEntityAggregatorHydrator`.

### CriteriaParser

Translates DAL filters/sorting/aggregations → OpenSearch DSL:
- `EqualsFilter` → `TermQuery`
- `EqualsAnyFilter` → `TermsQuery`
- `RangeFilter` → `RangeQuery`
- `ContainsFilter` → `WildcardQuery` / `MatchQuery`
- `MultiFilter` → `BoolQuery` (AND = must, OR = should, NEITHER = must_not)
- `NotFilter` → `BoolQuery::MUST_NOT`
- `PrefixFilter` → `PrefixQuery`
- `CountSorting` → via `CountSort` (nested agg-based)
- Aggregations: Terms, Avg, Min, Max, Sum, Stats, Filter, DateHistogram, Range, Entity

### ElasticsearchTokenizer

Tokenizes search terms for multi-token search.

---

## Admin search integration

### AbstractAdminIndexer

Base for all admin indexers. Required methods:
```php
abstract public function getName(): string;          // unique name
abstract public function getEntity(): string;        // entity name
abstract public function getIterator(): IterableQuery;
abstract public function fetch(array $ids): array;   // returns {id, text, textBoosted?, completion?}
abstract public function globalData(array $result, Context $context): array; // {total, data}
```

**Fields:**
- `TEXT_FIELD`: `{type: text}` — for text/textBoosted
- `COMPLETION_FIELD`: word_delimiter_graph analyzer + ngram subfield — for autocomplete

```php
public function mapping(array $mapping): array;              // extend mapping
public function globalCriteria(string $term, Search): Search; // adjust global search
public function moduleCriteria(string $term, Search): Search; // adjust module search
```

**Helper methods in AbstractAdminIndexer:**
```php
protected function buildCompletion(array $values): array;         // dedupe + lowercase
protected function decodeTranslatedValues(?string $encoded): array; // JSON → [langId => value]
protected function parseTagIds(array $row, string $key = 'tagIds'): array;
protected function formatDateTime(array $row, string $key): ?string;
```

### AdminSearchRegistry

Collects all admin indexers (tagged: `shopware.es.admin_definition`).

### AdminSearcher

`search(string $term, Context): array` — global search across all admin indexers.
`searchIds(string $term, string $entity, Context): IdSearchResult` — module search.

### AdminElasticsearchHelper

Separate helper instance for admin ES (own prefix, own connection configuration).

---

## Product indexing

### ElasticsearchProductDefinition

Extends `AbstractElasticsearchDefinition`. Internal `@internal`.

**`getMapping(Context)`** builds the complete product mapping:

| Field | ES type | Notes |
|------|--------|-------------|
| `id` | KEYWORD_FIELD | |
| `name` | translated + withExact + technicalTerms | language-aware |
| `description` | translated + lengthNorm | BM25 length-norm |
| `metaTitle` | translated | |
| `metaDescription` | translated + lengthNorm | |
| `customSearchKeywords` | translated + withExact + technicalTerms + lengthNorm | |
| `productNumber`, `ean`, `manufacturerNumber` | buildTextFieldConfig(withExact, technicalTerms) | SKU analysis |
| `categories`, `manufacturer`, `deliveryTime`, `options`, `properties`, `tags`, `visibilities` | nested | with `_count` |
| `active`, `available`, `isCloseout`, `shippingFree`, `markAsTopseller` | boolean | |
| `stock`, `availableStock`, `sales`, `childCount`, `autoIncrement` | long | |
| `ratingAverage`, `weight`, `width`, `length`, `height` | double | |
| `releaseDate`, `createdAt` | date | |
| `customFields` | object/dynamic | per language |
| `visibility_{salesChannelId}` | integer | flattened per SalesChannel |
| `cheapest_price_rule*` | dynamic template → double | |

**`fetch(ids, Context)`** loads products via raw SQL (joins across product, product_translation, category_translation, product_visibility, tag etc.). Runs several SQL queries — one base query plus one translation query per language.

**Dynamic templates:**
- `cheapest_price_rule*` → `double`
- `price.*.percentage.*` → `double`
- `long` → `double` (global fallback)

---

## Custom Fields in ES

### ElasticsearchFieldBuilder::customFields()

Builds `{properties: {[languageId]: {type: object, dynamic: true, properties: {fieldName: esType}}}}`.

### ElasticsearchCustomFieldsMappingHelper

**`getTypeFromCustomFieldType(string $type): array`**

| CustomFieldType | ES type |
|----------------|--------|
| `int` | `{type: long}` |
| `float` | `{type: double}` |
| `bool` | `{type: boolean}` |
| `datetime` | `{type: date, format: ...}` |
| `price`, `json` | `{type: object, dynamic: true}` |
| all others | `KEYWORD_FIELD + SEARCH_FIELD` (keyword + text) |

### ElasticsearchCustomFieldsMappingEvent

Allows plugins to override the custom fields mapping:

```php
// EventListener
public function onMapping(ElasticsearchCustomFieldsMappingEvent $event): void {
    if ($event->getEntity() !== ProductDefinition::ENTITY_NAME) {
        return;
    }
    // switch field to integer
    $event->setMapping('custom_my_numeric', CustomFieldTypes::INT);
    // remove field entirely
    $event->removeMapping('custom_unwanted');
}
```

---

## Indexing events

| Event | Timing |
|-------|-----------|
| `ElasticsearchIndexConfigEvent` | before index creation (adjust mapping/settings) |
| `ElasticsearchIndexCreatedEvent` | after index creation |
| `ElasticsearchIndexAliasSwitchedEvent` | after alias switch |
| `ElasticsearchIndexingFinishedEvent` | all batches processed |
| `ElasticsearchIndexIteratorEvent` | per definition while iterating (swap iterator) |
| `ElasticsearchIndexerLanguageCriteriaEvent` | adjust language criteria |
| `ElasticsearchEntitySearcherSearchEvent` | before the ES search request |
| `ElasticsearchEntitySearcherSearchedEvent` | after the ES search request |
| `ElasticsearchEntityAggregatorSearchEvent` | before the ES aggregation request |
| `ElasticsearchEntityAggregatorSearchedEvent` | after the ES aggregation request |

---

## Analyzer constants (`ElasticsearchFieldBuilder`)

| Constant | Value | Usage |
|-----------|------|------------|
| `NORMALIZER_LOWERCASE` | `sw_lowercase_normalizer` | all keyword fields |
| `SIMILARITY_LENGTH_NORM` | `sw_length_norm` | BM25 b=0.75 for long text |
| `ANALYZER_WHITESPACE` | `sw_whitespace_analyzer` | default search/exact |
| `ANALYZER_NGRAM` | `sw_ngram_analyzer` | ngram subfields |
| `ANALYZER_WHITESPACE_TECHNICAL_INDEX` | `sw_whitespace_technical_term_index_analyzer` | SKU index-side |
| `ANALYZER_WHITESPACE_TECHNICAL_SEARCH` | `sw_whitespace_technical_term_search_analyzer` | SKU search-side |

Language-specific analyzers: `sw_german_analyzer`, `sw_english_analyzer`, `sw_german_technical_term_{index,search}_analyzer`, `sw_english_technical_term_{index,search}_analyzer`.

---

## ElasticsearchFieldMapper (static)

```php
ElasticsearchFieldMapper::translated(
    string $field,
    array $items,
    array $fallbackItems = [],
    bool $stripText = true
): array  // [languageId => value]

ElasticsearchFieldMapper::toManyAssociations(
    array $items,
    array $translatedFields = []
): array
```

`translated()` merges `fallbackItems + items`, so parent translations act as a fallback.

---

## TokenQueryBuilder / FieldQueryBuilder

`TokenQueryBuilder` iterates `SearchFieldConfig` configs, resolves DAL fields,
delegates to `AbstractFieldQueryBuilder::build(ResolvedField, token, config, Context)`.

`FieldQueryBuilder` and `ExplainFieldQueryBuilder` (debug) implement the concrete query logic.

`TranslatedFieldQueryBuilder` / `NestedFieldQueryBuilder` — specialised implementations.

`SearchFieldConfig`: `{andLogic, field, tokenize, ranking}` — configured in the admin under product search settings.

---

## Test helper classes

- `ElasticsearchTestTestBehaviour` — trait for storefront ES tests (indexing etc.)
- `AdminElasticsearchTestBehaviour` — trait for admin ES tests

---

## Database tables

| Table | Purpose |
|---------|-------|
| `elasticsearch_index_task` | tracking of running indexing runs (id, entity, index, alias, doc_count) |

Migrations in `Migration/V6_5/`:
- `Migration1689083660ElasticsearchIndexTask` — main table
- `Migration1689084023AdminElasticsearchIndexTask` — admin variant

---

## AWS OpenSearch / SigV4

With `elasticsearch.ssl.sigV4.enabled=true`, `AsyncAwsSigner` is used for request signing.
Credentials via `key_id`/`secret_key` in the config or an IAM role (omit `credentials_provider`).

---

## Profiler

In dev/test: `ClientProfiler` decorates the OpenSearch client, `DataCollector` collects query times for the Symfony profiler.
