# Shopware Advanced Search — Entwickler-Referenz

## Uberblick

Advanced Search ist Teil des Commercial Plugins (ab Version 5.5.0), verfuegbar im **Evolve** und
**Beyond** Plan. Basiert auf Elasticsearch/OpenSearch und ersetzt/ergaenzt die Standard-Shopware-Suche
um konfigurierbare Mehrfach-Entity-Suche (Produkte, Hersteller, Kategorien, eigene Entities).

## Voraussetzungen

```env
OPENSEARCH_URL=http://localhost:9200
ES_MULTILINGUAL_INDEX=1
SHOPWARE_ES_ENABLED=1
SHOPWARE_ES_INDEXING_ENABLED=1
SHOPWARE_ES_INDEX_PREFIX=sw
```

Elasticsearch-Bundle muss in `config/bundles.php` aktiviert sein:
`Shopware\Elasticsearch\Elasticsearch`

## Architektur

### Such- und Suggest-Routes

`ProductSearchRoute` wird durch `ProductSearchRouteDecorator` dekoriert, der ein `multiSearchResult`
Extension zum Suchergebnis hinzufuegt. Das `multiSearchResult` enthaelt Ergebnisse aller ES-Definitionen
mit dem Tag `advanced_search.supported_definition`.

`ProductSuggestRoute` analog — zusaetzlich `completionResult` Extension.

Events zum Anpassen der Criteria:
- `MultiContentSearchCriteriaEvent`
- `MultiContentSuggestCriteriaEvent`

### Search Config

Sucheigenschaften werden pro Sales Channel in `advanced_search_config` und
`advanced_search_config_field` gespeichert (statt per Sprache wie im Core).

Relevante Klassen:
- `\Shopware\Commercial\AdvancedSearch\Entity\AdvancedSearchConfig\AdvancedSearchConfigDefinition`
- `\Shopware\Commercial\AdvancedSearch\Entity\AdvancedSearchConfig\Aggregate\AdvancedSearchConfigFieldDefinition`

## Custom Elasticsearch Definition erstellen

Jede eigene ES-Definition muss `AbstractElasticsearchDefinition` erweitern und mit
zwei Service-Tags registriert werden:

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

### Pflichtmethoden

```php
class YourCustomElasticsearchDefinition extends AbstractElasticsearchDefinition
{
    public function getMapping(Context $context): array { ... }
    public function buildTermQuery(Context $context, Criteria $criteria): BoolQuery { ... }
    public function fetch(array $ids, Context $context): array { ... }
    public function getEntityDefinition(): EntityDefinition { ... }
}
```

### Multilingual Mapping (ab neuem ADR)

Felder mit Uebersetzungen verwenden sprachbasierte Properties:

```php
$languageFields = [];
foreach ($languages as $languageId => $code) {
    $languageFields[$languageId] = self::getTextFieldConfig();
    // optional: sprachspezifischen Analyzer setzen
}
$properties = [
    'name' => ['properties' => $languageFields],
];
```

## Eigene Felder zum Produkt-Index hinzufuegen

**3-Schritt-Prozess:**

### 1. ElasticsearchProductDefinition dekorieren

```php
$services->set(ElasticsearchProductDefinitionDecorator::class)
    ->decorate(ElasticsearchProductDefinition::class)
    ->args([service('.inner'), service(SearchLogic::class)]);
```

Decorator-Klasse implementiert `getMapping()` (Felder ergaenzen) und `fetch()` (Daten befuellen).

### 2. Index aktualisieren

```bash
bin/console es:mapping:update   # Mapping auf OpenSearch-Server pushen
bin/console es:index --no-queue # Neu indizieren (wenn Daten schon vorhanden)
```

### 3. Migration fuer `advanced_search_config_field`

Neues Feld pro Sales-Channel-Config einfuegen:

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

## SearchLogic dekorieren

Zentraler Ort fuer den Aufbau der ES-Query. Wird mit `AND`/`OR` aus konfigurierbaren
Suchfeldern zusammengesetzt.

```php
$services->set(SearchLogicDecorator::class)
    ->decorate(SearchLogic::class)
    ->args([service('.inner'), service(ConfigurationLoader::class)]);
```

Im Decorator:

```php
public function build(EntityDefinition $definition, Criteria $criteria, Context $context): BoolQuery
{
    $salesChannelId = $context->getSource()->getSalesChannelId();
    $searchConfig = $this->configurationLoader->load($salesChannelId);
    $bool = $this->getDecorated()->build($definition, $criteria, $context);
    // Eigene Logik ergaenzen
    return $bool;
}
```

## Language Analyzers anpassen

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

## Completion (Autovervollstaendigung)

Advanced Search verwendet keine native ES-Completion (zu statisch/gross), sondern
Aggregations. Eigene Definitionen koennen `CompletionDefinitionEnrichment` nutzen:

```php
// In getMapping():
return [
    '_source' => ['includes' => ['id']],
    'properties' => array_merge($properties, $this->completionDefinitionEnrichment->enrichMapping()),
];

// In fetch():
return $this->completionDefinitionEnrichment->enrichData($this->getEntityDefinition(), $documents);
```

Completion-Keywords konfigurieren:

```yaml
advanced_search:
    completion:
        your_custom_entity:
            - email
            - company
```

## Cross Search (experimentell)

Ermoeglicht kategorienuebergreifende Suche (z.B. Kategorien ueber Produktnamen finden)
ohne vollstaendige Daten-Denormalisierung:

```yaml
advanced_search:
    cross_search:
        product.product_manufacturer: false
        product.category: false
        category.product: true
        product_manufacturer.product: true
```

Vorteil: Kein Aufblaehen des Index. Nachteil: Zusaetzliche aggregierte ES-Query.

## Storefront Templates erweitern

### Suchergebnisseite

```twig
{% set searchResult = page.listing.extensions.multiSearchResult %}
{% set products = page.listing %}
{% set manufacturers = searchResult.getResult('product_manufacturer') %}
{% set categories = searchResult.getResult('category') %}
{% set customEntities = searchResult.getResult('custom_entity') %}
```

### Suggest-Dropdown

```twig
{% set suggestResult = page.searchResult.extensions.multiSuggestResult %}
{% set products = page.searchResult %}
{% set completions = page.searchResult.extensions.completionResult %}
{% set manufacturers = suggestResult.getResult('product_manufacturer') %}
{% set categories = suggestResult.getResult('category') %}
```

Templates ableiten von:
- `search/index.html.twig` (Suche)
- `storefront/layout/header/search-suggest.html.twig` (Suggest)
