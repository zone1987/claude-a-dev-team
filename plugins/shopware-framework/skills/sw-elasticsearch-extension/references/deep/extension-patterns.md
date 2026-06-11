# Elasticsearch-Extension: Erschöpfende Referenz

## Mapping-Konstanten im Detail

### AbstractElasticsearchDefinition — Alle Mapping-Arrays

```php
// 1. KEYWORD_FIELD
// Exakte Matches, case-insensitiv via lowercase normalizer
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

// 5. SEARCH_FIELD (subfields, wird mit KEYWORD_FIELD gemergt via +)
[
    'fields' => [
        'search' => ['type' => 'text', 'analyzer' => 'sw_whitespace_analyzer'],
        'ngram'  => ['type' => 'text', 'analyzer' => 'sw_ngram_analyzer'],
    ],
]
// Vollständig: KEYWORD_FIELD + SEARCH_FIELD:
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

// 7. SEARCH_FIELD_WITH_LENGTH_NORM (für description, metaDescription)
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

// 8. TECHNICAL_TERM_SEARCH_FIELD (für productNumber, ean, manufacturerNumber)
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

## buildTextFieldConfig() — Logik

```php
protected static function buildTextFieldConfig(
    bool $withExact = false,
    bool $technicalTerms = false,
    bool $lengthNorm = false
): array

// Schritt 1: Basis-Felder wählen
$fieldConfig = $technicalTerms
    ? self::TECHNICAL_TERM_SEARCH_FIELD   // word_delimiter_graph für SKUs
    : self::SEARCH_FIELD;                  // whitespace + ngram

// Schritt 2: lengthNorm → similarity überschreiben
if ($lengthNorm) {
    $fieldConfig['fields']['search']['similarity'] = 'sw_length_norm';
}

// Schritt 3: exact subfeld prependen
if ($withExact) {
    $fieldConfig['fields'] = ['exact' => self::SEARCH_FIELD_WITH_EXACT['fields']['exact']]
                           + $fieldConfig['fields'];
}

// Schritt 4: KEYWORD_FIELD + fieldConfig mergen
return self::KEYWORD_FIELD + $fieldConfig;
```

Ergibt je nach Flags:
- `()` → keyword + search(whitespace) + ngram
- `(withExact)` → keyword + exact(whitespace, no norms) + search(whitespace) + ngram
- `(technicalTerms)` → keyword + search(word_delimiter_graph) + ngram
- `(withExact, technicalTerms)` → keyword + exact + search(wdg) + ngram
- `(lengthNorm)` → keyword + search(whitespace, sw_length_norm) + ngram
- `(withExact, technicalTerms, lengthNorm)` → keyword + exact + search(wdg, sw_length_norm) + ngram

---

## ElasticsearchFieldBuilder::translated() — Sprach-Mapping

```php
$this->fieldBuilder->translated(array $fieldConfig): array
```

**Ablauf:**
1. Lade alle Sprachen via `LanguageLoaderInterface::loadLanguages()`
2. Für jede Sprache: prüfe Locale (aus `code` oder `parentCode`, z.B. `de-DE` → `de`)
3. Wenn `languageAnalyzerMapping[locale]` vorhanden:
   - Standard-Felder (`search.analyzer == sw_whitespace_analyzer`): ersetze durch `sw_german_analyzer` etc.
   - Technical-Term-Felder (`search.analyzer == sw_whitespace_technical_term_index_analyzer`):
     ersetze durch sprach-spezifisches `sw_german_technical_term_index_analyzer` / `_search_analyzer`
     (nur wenn für die Sprache vorhanden, sonst fallback auf generic technical-term analyzer)
4. `.exact` und `.ngram` bleiben immer sprach-agnostisch

**Rückgabe:**
```php
[
    'properties' => [
        '2fbb5fe2e29a4d70aa5854ce7ce3e20b' => $fieldConfigForLanguage1,  // languageId → config
        'f57ab71e-c7b5-4c94-b7a7-c7b5c7b5c7b5' => $fieldConfigForLanguage2,
        // ...
    ],
]
```

Für Felder ohne Sprach-Analyzer (kein Matching in `languageAnalyzerMapping`):
alle Sprachen bekommen denselben `fieldConfig` (generic analyzer).

---

## Produkt-Mapping-Vollständigkeit

### Alle indizierten Produkt-Felder

```php
// Textfelder (translated)
'name'                → translated + withExact + technicalTerms (Exact-Match + SKU-Analyse + sprachspezifisch)
'description'         → translated + lengthNorm (BM25 Längen-Normalisierung)
'metaTitle'           → translated
'metaDescription'     → translated + lengthNorm
'customSearchKeywords'→ translated + withExact + technicalTerms + lengthNorm (alles)

// SKU-Felder (nicht translated, da Sprach-unabhängig)
'productNumber'       → buildTextFieldConfig(withExact: true, technicalTerms: true)
'ean'                 → buildTextFieldConfig(withExact: true, technicalTerms: true)
'manufacturerNumber'  → buildTextFieldConfig(withExact: true, technicalTerms: true)

// Nested-Assoziationen
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

// Dynamic Templates (aus Mapping-Array)
'cheapest_price_rule*' → match → double
'price.*.percentage.*' → path_match → double
'long' type match → double
```

### `_source` Optimierung

Wenn `elasticsearch.product.exclude_source = false` (Standard) und nicht dev/test:
```php
$mapping['_source'] = ['includes' => ['id', 'autoIncrement']];
```
Minimiert Speicher, da nur IDs aus `_source` gelesen werden (Daten kommen aus DB).

---

## Custom Fields — Vollständige Type-Mapping-Tabelle

Aus `ElasticsearchCustomFieldsMappingHelper::getTypeFromCustomFieldType()`:

| `CustomFieldTypes::*` | Wert | ES-Mapping |
|----------------------|------|-----------|
| `INT` | `'int'` | `{type: 'long'}` |
| `FLOAT` | `'float'` | `{type: 'double'}` |
| `BOOL` | `'bool'` | `{type: 'boolean'}` |
| `DATETIME` | `'datetime'` | `{type: 'date', format: 'yyyy-MM-dd HH:mm:ss.SSS\|\|strict_date_optional_time\|\|epoch_millis', ignore_malformed: true}` |
| `PRICE` | `'price'` | `{type: 'object', dynamic: true}` |
| `JSON` | `'json'` | `{type: 'object', dynamic: true}` |
| alle anderen (SELECT, MULTI_SELECT, TEXT, HTML, etc.) | diverse | `KEYWORD_FIELD + SEARCH_FIELD` |

**Dynamisches Nachladen neuer Custom-Fields:**
`ElasticsearchCustomFieldsMappingHelper::createFieldsInIndices()` → `putMapping()` auf allen aktiven Indizes, pro Sprache.

---

## Admin-Suche: Fetch-Return-Format

```php
// Pflicht-Felder je ID:
[
    'id'         => string,       // hex UUID
    'text'       => string,       // Haupt-Suchtext (wird in TEXT_FIELD indiziert)
    'textBoosted'=> string|null,  // boost-Suchtext (höherer Score)
    'completion' => list<string>|null, // lowercase dedupe für COMPLETION_FIELD
]
```

**`buildCompletion()` helper:**
```php
$this->buildCompletion(['T-Shirt Basic', 'Shirt', null, ''])
// → ['t-shirt basic', 'shirt']  (null/empty gefiltert, lowercase, dedupe)
```

**`decodeTranslatedValues()` helper:**
```php
// encoded = JSON-String aus SQL: '[{"languageId":"...","name":"..."}]'
$this->decodeTranslatedValues($encoded, 'name')
// → ['2fbb...5b' => 'Produkt Name', ...]
```

---

## Admin-Indexer: built-in Felder

Alle konkreten Admin-Indexer erben die Standard-Felder aus `AbstractAdminIndexer::mapping()`:
`id` (KEYWORD_FIELD) wird immer hinzugefügt.

Typisches Muster für Texte:
```php
public function mapping(array $mapping): array {
    $mapping['properties']['name']        = self::TEXT_FIELD;
    $mapping['properties']['email']       = self::TEXT_FIELD;
    $mapping['properties']['completion']  = self::COMPLETION_FIELD; // für Autocomplete
    return $mapping;
}
```

### COMPLETION_FIELD im Detail

```php
[
    'type' => 'text',
    'analyzer' => 'sw_admin_completion_index_analyzer',   // word_delimiter_graph chain
    'search_analyzer' => 'sw_admin_completion_search_analyzer',
    'fields' => [
        'ngram' => [
            'type' => 'text',
            'analyzer' => 'sw_ngram_analyzer',
            'search_analyzer' => 'sw_whitespace_analyzer', // kurze Queries → ngram-Pfad
        ],
    ],
]
```

---

## IndexerOffset-Tracking

```php
$offset = new IndexerOffset(
    definitions: iterable<string>,  // entity names
    timestamp: int                  // Unix-Timestamp für Index-Suffix
);

$offset->getDefinition(): ?string
$offset->hasNextDefinition(): bool
$offset->selectNextDefinition(): void
$offset->getLastId(): ?array
$offset->setLastId(?array): void
$offset->getTimestamp(): int
```

`IndexerOffset` wird als Teil von `ElasticsearchIndexingMessage` serialisiert.

---

## Elasticsearch-Exception Codes

```php
ElasticsearchException::serverNotAvailable()
ElasticsearchException::definitionNotFound(string $entityName)
ElasticsearchException::unsupportedElasticsearchDefinition(string $entityName)
ElasticsearchException::indexingError(array $errors)
ElasticsearchException::emptyIndexingRequest()
```

---

## Test-Verhalten

### ElasticsearchTestTestBehaviour

Trait für PHPUnit-Tests, die gegen ES indizieren:
- Schreibt Testdaten in ES-Index
- Bereinigt nach Test

### AdminElasticsearchTestBehaviour

Analoges Trait für Admin-Suche-Tests.

---

## Sorting-Erweiterung: CountSort

`CountSort` implementiert `BuilderInterface` für sortieren nach Anzahl in Nested-Feldern
(z.B. Produkte nach Anzahl Properties sortieren).

---

## MatchBoolPrefixQuery

Eigene OpenSearchDSL-Query-Klasse für `match_bool_prefix` — wird in `ProductSearchQueryBuilder`
für Prefix-Matching in Volltext-Suche verwendet.
