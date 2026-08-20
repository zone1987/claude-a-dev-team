# Shopware Advanced Search — developer reference

## Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Architecture](#architecture)
- [Creating a custom Elasticsearch definition](#creating-a-custom-elasticsearch-definition)
- [Adding own fields to the product index](#adding-own-fields-to-the-product-index)
- [Decorating SearchLogic](#decorating-searchlogic)
- [Customizing language analyzers](#customizing-language-analyzers)
- [Completion (autocomplete)](#completion-autocomplete)
- [Cross search (experimental)](#cross-search-experimental)
- [Extending storefront templates](#extending-storefront-templates)

## Overview

Advanced Search is part of the Commercial plugin (from version 5.5.0), available in the **Evolve** and
**Beyond** plan. It is based on Elasticsearch/OpenSearch and replaces/extends the standard Shopware search
with a configurable multi-entity search (products, manufacturers, categories, own entities).

## Prerequisites

```env
OPENSEARCH_URL=http://localhost:9200
ES_MULTILINGUAL_INDEX=1
SHOPWARE_ES_ENABLED=1
SHOPWARE_ES_INDEXING_ENABLED=1
SHOPWARE_ES_INDEX_PREFIX=sw
```

The Elasticsearch bundle must be enabled in `config/bundles.php`:
`Shopware\Elasticsearch\Elasticsearch`

## Architecture

### Search and suggest routes

`ProductSearchRoute` is decorated by `ProductSearchRouteDecorator`, which adds a `multiSearchResult`
extension to the search result. The `multiSearchResult` contains results of all ES definitions
carrying the tag `advanced_search.supported_definition`.

`ProductSuggestRoute` works analogously — plus a `completionResult` extension.

Events for adjusting the criteria:
- `MultiContentSearchCriteriaEvent`
- `MultiContentSuggestCriteriaEvent`

### Search config

Search properties are stored per sales channel in `advanced_search_config` and
`advanced_search_config_field` (instead of per language as in the core).

Relevant classes:
- `\Shopware\Commercial\AdvancedSearch\Entity\AdvancedSearchConfig\AdvancedSearchConfigDefinition`
- `\Shopware\Commercial\AdvancedSearch\Entity\AdvancedSearchConfig\Aggregate\AdvancedSearchConfigFieldDefinition`

## Creating a custom Elasticsearch definition

Every own ES definition must extend `AbstractElasticsearchDefinition` and be registered
with two service tags:

```php
$services->set(YourCustomElasticsearchDefinition::class)
    ->args([
        service(YourCustomDefinition::class),
        service('Doctrine\DBAL\Connection'),
        service(SearchLogic::class),
    ])
    ->tag('shopware.es.definition')
    ->tag('advanced_search.supported_definition');
```

### Required methods

```php
class YourCustomElasticsearchDefinition extends AbstractElasticsearchDefinition
{
    public function getMapping(Context $context): array { ... }
    public function buildTermQuery(Context $context, Criteria $criteria): BoolQuery { ... }
    public function fetch(array $ids, Context $context): array { ... }
    public function getEntityDefinition(): EntityDefinition { ... }
}
```

### Multilingual mapping (from the new ADR onwards)

Fields with translations use language-based properties:

```php
$languageFields = [];
foreach ($languages as $languageId => $code) {
    $languageFields[$languageId] = self::getTextFieldConfig();
    // optional: set a language-specific analyzer
}
$properties = [
    'name' => ['properties' => $languageFields],
];
```

## Adding own fields to the product index

**3-step process:**

### 1. Decorate ElasticsearchProductDefinition

```php
$services->set(ElasticsearchProductDefinitionDecorator::class)
    ->decorate(ElasticsearchProductDefinition::class)
    ->args([service('.inner'), service(SearchLogic::class)]);
```

The decorator class implements `getMapping()` (add fields) and `fetch()` (fill in data).

### 2. Update the index

```bash
bin/console es:mapping:update   # Push the mapping to the OpenSearch server
bin/console es:index --no-queue # Reindex (if data already exists)
```

### 3. Migration for `advanced_search_config_field`

Insert a new field per sales channel config:

```php
$connection->insert('advanced_search_config_field', [
    'id' => Uuid::randomBytes(),
    'field' => 'prefixProductNumber',
    'config_id' => $configId,
    'entity' => 'product',
    'tokenize' => 1,
    'searchable' => 1,
    'ranking' => 500,
    'created_at' => (new \DateTime())->format(Defaults::STORAGE_DATE_TIME_FORMAT),
]);
```

## Decorating SearchLogic

The central place for assembling the ES query. It is composed with `AND`/`OR` from
configurable search fields.

```php
$services->set(SearchLogicDecorator::class)
    ->decorate(SearchLogic::class)
    ->args([service('.inner'), service(ConfigurationLoader::class)]);
```

In the decorator:

```php
public function build(EntityDefinition $definition, Criteria $criteria, Context $context): BoolQuery
{
    $salesChannelId = $context->getSource()->getSalesChannelId();
    $searchConfig = $this->configurationLoader->load($salesChannelId);
    $bool = $this->getDecorated()->build($definition, $criteria, $context);
    // Add own logic
    return $bool;
}
```

## Customizing language analyzers

In `config/packages/advanced_search.yaml`:

```yaml
advanced_search:
    analysis:
        analyzer:
            sw_your_custom_language_analyzer:
                type: custom
                tokenizer: standard
                filter: ['lowercase', 'my_stopwords_filter', 'my_stemmer_filter']
    filter:
        my_stopwords_filter:
            type: 'stop'
            stopwords: ['foo', 'bar']
        my_stemmer_filter:
            type: 'stemmer'
            language: 'english'
    language_analyzer_mapping:
        custom_iso: sw_your_custom_language_analyzer
```

## Completion (autocomplete)

Advanced Search does not use the native ES completion (too static/large), but
aggregations instead. Own definitions can use `CompletionDefinitionEnrichment`:

```php
// In getMapping():
return [
    '_source' => ['includes' => ['id']],
    'properties' => array_merge($properties, $this->completionDefinitionEnrichment->enrichMapping()),
];

// In fetch():
return $this->completionDefinitionEnrichment->enrichData($this->getEntityDefinition(), $documents);
```

Configuring completion keywords:

```yaml
advanced_search:
    completion:
        your_custom_entity:
            - email
            - company
```

## Cross search (experimental)

Enables searching across categories (e.g. finding categories via product names)
without a full denormalization of the data:

```yaml
advanced_search:
    cross_search:
        product.product_manufacturer: false
        product.category: false
        category.product: true
        product_manufacturer.product: true
```

Advantage: no bloating of the index. Disadvantage: an additional aggregated ES query.

## Extending storefront templates

### Search result page

```twig
{% set searchResult = page.listing.extensions.multiSearchResult %}
{% set products = page.listing %}
{% set manufacturers = searchResult.getResult('product_manufacturer') %}
{% set categories = searchResult.getResult('category') %}
{% set customEntities = searchResult.getResult('custom_entity') %}
```

### Suggest dropdown

```twig
{% set suggestResult = page.searchResult.extensions.multiSuggestResult %}
{% set products = page.searchResult %}
{% set completions = page.searchResult.extensions.completionResult %}
{% set manufacturers = suggestResult.getResult('product_manufacturer') %}
{% set categories = suggestResult.getResult('category') %}
```

Derive templates from:
- `search/index.html.twig` (search)
- `storefront/layout/header/search-suggest.html.twig` (suggest)
