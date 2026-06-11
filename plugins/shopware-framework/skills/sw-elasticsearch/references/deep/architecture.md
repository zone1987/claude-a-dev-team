# Shopware Elasticsearch Bundle — Erschöpfende Architektur-Referenz

## Bundle-Einstieg

**Klasse:** `Shopware\Elasticsearch\Elasticsearch extends Bundle`

Registriert zwei Compiler-Passes:
- `ElasticsearchMigrationCompilerPass` — integriert Bundle-Migrationen
- `ElasticsearchProfileCompilerPass` — aktiviert Profiler im dev-Modus

**Extension:** `ElasticsearchExtension` lädt `Resources/config/services.xml` und trägt alle Config-Parameter als Container-Parameter ein (`elasticsearch.*`).

---

## Konfigurationsbaum (`Configuration`)

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
  language_analyzer_mapping: array  ← locale → analyzer name (z.B. de → sw_german_analyzer)
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

## Kern-Services

### ElasticsearchRegistry

Service-ID: `Shopware\Elasticsearch\Framework\ElasticsearchRegistry`

Hält alle registrierten `AbstractElasticsearchDefinition`-Instanzen (tagged: `shopware.es.definition`).

```php
$registry->getDefinitions(): iterable<AbstractElasticsearchDefinition>
$registry->get(string $entityName): ?AbstractElasticsearchDefinition
$registry->has(string $entityName): bool
$registry->getDefinitionNames(): iterable<string>
```

### ElasticsearchHelper

Zentrale Helper-Klasse. Prüft ob Suche/Indizierung erlaubt ist, baut DSL-Elemente.

```php
$helper->allowIndexing(): bool              // prüft ES-Verbindung + indexing_enabled
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

`MAX_SIZE_VALUE = 10000` (OpenSearch Standard-Max ohne custom settings).

### ElasticsearchIndexer (`#[AsMessageHandler]`)

Verarbeitet `ElasticsearchIndexingMessage`-Nachrichten.

```php
$indexer->iterate(?IndexerOffset, array $entities = []): ?ElasticsearchIndexingMessage
$indexer->updateIds(EntityDefinition, array $ids): void
$indexer->__invoke(ElasticsearchIndexingMessage): void
```

Ablauf in `init()`:
1. `DELETE FROM elasticsearch_index_task` (reset)
2. `DateTime::now()` als Timestamp
3. Für jede Definition: `IndexCreator::createIndex(definition, index, alias, context)`
4. Eintrag in `elasticsearch_index_task` (id, entity, index, alias, doc_count)

### IndexCreator

Erstellt den ES-Index mit Mapping + Analysis-Config.

```php
$creator->createIndex(AbstractElasticsearchDefinition, string $index, string $alias, Context)
$creator->aliasExists(string $alias): bool
```

Config-Merge: `index_settings` + `analysis` + Mapping aus `IndexMappingProvider`.

**`dimension_normalize`:** Wenn aktiviert, wird der `sw_dimension_normalize`-CharFilter in alle `TECHNICAL_TERM_ANALYZERS` injiziert.

### IndexMappingProvider

Merged Base-Mapping (aus `elasticsearch.yaml` `index_settings`/`analysis`/`dynamic_templates`) mit dem Entity-spezifischen Mapping aus `AbstractElasticsearchDefinition::getMapping()`.

### CreateAliasTaskHandler / CreateAliasTask

Scheduled Task (läuft nach Indexierung). Wechselt Alias von altem auf neuen Index (blue-green).

---

## Indexierungs-Flow im Detail

```
es:index-Command
  ↓ iterate(null, entities)
  ElasticsearchIndexer
    ↓ IndexerOffset(definitions, timestamp)
    ↓ für jede Definition: createIterator(batchSize)
    ↓ ElasticsearchIndexIteratorEvent (erweiterbar: custom Iterator)
    ↓ ElasticsearchIndexingMessage(IndexingDto, IndexerOffset, Context)
  ↓ dispatch via MessageBus (oder direkt __invoke)
  ↓ __invoke(message)
    ↓ allowIndexing() prüfen
    ↓ UPDATE elasticsearch_index_task SET doc_count = doc_count - idCount
    ↓ definition->fetch(hexIds, context) → array<id, document>
    ↓ Bulk-Request: [{index: {_id: id}}, {document}]
    ↓ parseErrors()
  ↓ letztes Batch: markAsLastMessage()
    ↓ ElasticsearchIndexingFinishedEvent
  CreateAliasTaskHandler::run()
    ↓ Alias switchen
    ↓ ElasticsearchIndexAliasSwitchedEvent
```

---

## Storefront-Suche-Integration

### ElasticsearchEntitySearcher (dekoriert EntitySearcher)

```php
// Prüft: allowSearch + Criteria::STATE_ELASTICSEARCH_AWARE
// Baut: ids → Filter, postFilter, sorting, term, queries, aggs
// Gibt: IdSearchResult zurück
```

### ElasticsearchEntityAggregator (dekoriert EntityAggregator)

Führt separate Aggregations-Query gegen ES aus, hydriert über `ElasticsearchEntityAggregatorHydrator`.

### CriteriaParser

Übersetzt DAL-Filter/Sorting/Aggregations → OpenSearch-DSL:
- `EqualsFilter` → `TermQuery`
- `EqualsAnyFilter` → `TermsQuery`
- `RangeFilter` → `RangeQuery`
- `ContainsFilter` → `WildcardQuery` / `MatchQuery`
- `MultiFilter` → `BoolQuery` (AND = must, OR = should, NEITHER = must_not)
- `NotFilter` → `BoolQuery::MUST_NOT`
- `PrefixFilter` → `PrefixQuery`
- `CountSorting` → via `CountSort` (nested agg-based)
- Aggregationen: Terms, Avg, Min, Max, Sum, Stats, Filter, DateHistogram, Range, Entity

### ElasticsearchTokenizer

Tokenisiert Suchbegriffe für Multi-Token-Suche.

---

## Admin-Suche-Integration

### AbstractAdminIndexer

Basis für alle Admin-Indexer. Pflicht-Methoden:
```php
abstract public function getName(): string;          // unique name
abstract public function getEntity(): string;        // entity name
abstract public function getIterator(): IterableQuery;
abstract public function fetch(array $ids): array;   // returns {id, text, textBoosted?, completion?}
abstract public function globalData(array $result, Context $context): array; // {total, data}
```

**Felder:**
- `TEXT_FIELD`: `{type: text}` — für text/textBoosted
- `COMPLETION_FIELD`: word_delimiter_graph Analyzer + ngram subfield — für Autocomplete

```php
public function mapping(array $mapping): array;              // Mapping erweitern
public function globalCriteria(string $term, Search): Search; // Global-Search anpassen
public function moduleCriteria(string $term, Search): Search; // Modul-Search anpassen
```

**Helper-Methoden in AbstractAdminIndexer:**
```php
protected function buildCompletion(array $values): array;         // dedupe + lowercase
protected function decodeTranslatedValues(?string $encoded): array; // JSON → [langId => value]
protected function parseTagIds(array $row, string $key = 'tagIds'): array;
protected function formatDateTime(array $row, string $key): ?string;
```

### AdminSearchRegistry

Sammelt alle Admin-Indexer (tagged: `shopware.es.admin_definition`).

### AdminSearcher

`search(string $term, Context): array` — Global-Suche über alle Admin-Indexer.
`searchIds(string $term, string $entity, Context): IdSearchResult` — Modul-Suche.

### AdminElasticsearchHelper

Separate Helper-Instanz für Admin-ES (eigener Prefix, eigene Connection-Konfiguration).

---

## Produkt-Indexierung

### ElasticsearchProductDefinition

Extends `AbstractElasticsearchDefinition`. Internes `@internal`.

**`getMapping(Context)`** baut das vollständige Produkt-Mapping:

| Feld | ES-Typ | Besonderheit |
|------|--------|-------------|
| `id` | KEYWORD_FIELD | |
| `name` | translated + withExact + technicalTerms | language-aware |
| `description` | translated + lengthNorm | BM25 length-norm |
| `metaTitle` | translated | |
| `metaDescription` | translated + lengthNorm | |
| `customSearchKeywords` | translated + withExact + technicalTerms + lengthNorm | |
| `productNumber`, `ean`, `manufacturerNumber` | buildTextFieldConfig(withExact, technicalTerms) | SKU-Analyse |
| `categories`, `manufacturer`, `deliveryTime`, `options`, `properties`, `tags`, `visibilities` | nested | mit `_count` |
| `active`, `available`, `isCloseout`, `shippingFree`, `markAsTopseller` | boolean | |
| `stock`, `availableStock`, `sales`, `childCount`, `autoIncrement` | long | |
| `ratingAverage`, `weight`, `width`, `length`, `height` | double | |
| `releaseDate`, `createdAt` | date | |
| `customFields` | object/dynamic | per Sprache |
| `visibility_{salesChannelId}` | integer | flattened per SalesChannel |
| `cheapest_price_rule*` | dynamic template → double | |

**`fetch(ids, Context)`** lädt Produkte via Raw-SQL (Joins über product, product_translation, category_translation, product_visibility, tag etc.). Führt mehrere SQL-Queries aus — eine Base-Query + eine Translation-Query pro Sprache.

**Dynamic templates:**
- `cheapest_price_rule*` → `double`
- `price.*.percentage.*` → `double`
- `long` → `double` (global fallback)

---

## Custom Fields in ES

### ElasticsearchFieldBuilder::customFields()

Baut `{properties: {[languageId]: {type: object, dynamic: true, properties: {fieldName: esType}}}}`.

### ElasticsearchCustomFieldsMappingHelper

**`getTypeFromCustomFieldType(string $type): array`**

| CustomFieldType | ES-Typ |
|----------------|--------|
| `int` | `{type: long}` |
| `float` | `{type: double}` |
| `bool` | `{type: boolean}` |
| `datetime` | `{type: date, format: ...}` |
| `price`, `json` | `{type: object, dynamic: true}` |
| alle anderen | `KEYWORD_FIELD + SEARCH_FIELD` (keyword + text) |

### ElasticsearchCustomFieldsMappingEvent

Erlaubt Plugins, das Custom-Fields-Mapping zu überschreiben:

```php
// EventListener
public function onMapping(ElasticsearchCustomFieldsMappingEvent $event): void {
    if ($event->getEntity() !== ProductDefinition::ENTITY_NAME) {
        return;
    }
    // Feld auf integer umstellen
    $event->setMapping('custom_my_numeric', CustomFieldTypes::INT);
    // Feld komplett entfernen
    $event->removeMapping('custom_unwanted');
}
```

---

## Indexing-Events

| Event | Zeitpunkt |
|-------|-----------|
| `ElasticsearchIndexConfigEvent` | Vor Index-Erstellung (Mapping/Settings anpassen) |
| `ElasticsearchIndexCreatedEvent` | Nach Index-Erstellung |
| `ElasticsearchIndexAliasSwitchedEvent` | Nach Alias-Switch |
| `ElasticsearchIndexingFinishedEvent` | Alle Batches verarbeitet |
| `ElasticsearchIndexIteratorEvent` | Pro Definition beim Iterieren (Iterator austauschen) |
| `ElasticsearchIndexerLanguageCriteriaEvent` | Sprachen-Kriterien anpassen |
| `ElasticsearchEntitySearcherSearchEvent` | Vor ES-Search-Request |
| `ElasticsearchEntitySearcherSearchedEvent` | Nach ES-Search-Request |
| `ElasticsearchEntityAggregatorSearchEvent` | Vor ES-Aggregation-Request |
| `ElasticsearchEntityAggregatorSearchedEvent` | Nach ES-Aggregation-Request |

---

## Analyzer-Konstanten (`ElasticsearchFieldBuilder`)

| Konstante | Wert | Verwendung |
|-----------|------|------------|
| `NORMALIZER_LOWERCASE` | `sw_lowercase_normalizer` | Alle keyword-Felder |
| `SIMILARITY_LENGTH_NORM` | `sw_length_norm` | BM25 b=0.75 für Langtext |
| `ANALYZER_WHITESPACE` | `sw_whitespace_analyzer` | Standard search/exact |
| `ANALYZER_NGRAM` | `sw_ngram_analyzer` | ngram-Subfelder |
| `ANALYZER_WHITESPACE_TECHNICAL_INDEX` | `sw_whitespace_technical_term_index_analyzer` | SKU index-side |
| `ANALYZER_WHITESPACE_TECHNICAL_SEARCH` | `sw_whitespace_technical_term_search_analyzer` | SKU search-side |

Sprach-spezifische Analyzer: `sw_german_analyzer`, `sw_english_analyzer`, `sw_german_technical_term_{index,search}_analyzer`, `sw_english_technical_term_{index,search}_analyzer`.

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

`translated()` merged `fallbackItems + items`, sodass parent-Übersetzungen als Fallback dienen.

---

## TokenQueryBuilder / FieldQueryBuilder

`TokenQueryBuilder` iteriert `SearchFieldConfig`-Configs, löst DAL-Felder auf,
delegiert an `AbstractFieldQueryBuilder::build(ResolvedField, token, config, Context)`.

`FieldQueryBuilder` und `ExplainFieldQueryBuilder` (Debug) implementieren die konkrete Query-Logik.

`TranslatedFieldQueryBuilder` / `NestedFieldQueryBuilder` — spezialisierte Implementierungen.

`SearchFieldConfig`: `{andLogic, field, tokenize, ranking}` — konfiguriert in Admin unter Produktsuche-Einstellungen.

---

## Test-Hilfsklassen

- `ElasticsearchTestTestBehaviour` — Trait für Storefront-ES-Tests (Indexierung etc.)
- `AdminElasticsearchTestBehaviour` — Trait für Admin-ES-Tests

---

## Datenbank-Tabellen

| Tabelle | Zweck |
|---------|-------|
| `elasticsearch_index_task` | Tracking laufender Indexierungen (id, entity, index, alias, doc_count) |

Migrationen in `Migration/V6_5/`:
- `Migration1689083660ElasticsearchIndexTask` — Haupttabelle
- `Migration1689084023AdminElasticsearchIndexTask` — Admin-Variante

---

## AWS OpenSearch / SigV4

Bei `elasticsearch.ssl.sigV4.enabled=true` wird `AsyncAwsSigner` für Request-Signing verwendet.
Credentials über `key_id`/`secret_key` in Config oder IAM-Rolle (`credentials_provider` weglassen).

---

## Profiler

In dev/test: `ClientProfiler` dekoriert den OpenSearch-Client, `DataCollector` sammelt Query-Zeiten für den Symfony Profiler.
