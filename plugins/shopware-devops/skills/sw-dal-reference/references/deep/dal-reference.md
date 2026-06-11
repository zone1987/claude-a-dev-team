# Shopware 6 DAL Referenz (vollständige Referenz)

Quellen: `troubleshooting/dal-reference/filters-reference.md`, `aggregations-reference.md`, `flags-reference.md`, `fields-reference/index.md`, `enum-field.md`

## Filter-Referenz

Alle Filter sind case-insensitiv für String-Felder (Storage-System).

### equals

Exakter Match. SQL: `WHERE stock = 10`

```php
$criteria->addFilter(new EqualsFilter('stock', 10));
```

```json
{"filter": [{"type": "equals", "field": "stock", "value": 10}]}
```

### equalsAny

Mindestens ein exakter Match. SQL: `WHERE productNumber IN ('...', '...')`

```php
$criteria->addFilter(new EqualsAnyFilter('productNumber', ['AAA', 'BBB']));
```

```json
{"filter": [{"type": "equalsAny", "field": "productNumber", "value": ["AAA", "BBB"]}]}
```

### contains

Vor- und Nachher-Wildcard. SQL: `WHERE name LIKE '%Lightweight%'`

```php
$criteria->addFilter(new ContainsFilter('name', 'Lightweight'));
```

```json
{"filter": [{"type": "contains", "field": "name", "value": "Lightweight"}]}
```

### prefix

Nur Anfang-Wildcard. SQL: `WHERE name LIKE 'Lightweight%'`

```php
$criteria->addFilter(new PrefixFilter('name', 'Lightweight'));
```

```json
{"filter": [{"type": "prefix", "field": "name", "value": "Lightweight"}]}
```

### suffix

Nur Ende-Wildcard. SQL: `WHERE name LIKE '%Lightweight'`

```php
$criteria->addFilter(new SuffixFilter('name', 'Lightweight'));
```

```json
{"filter": [{"type": "suffix", "field": "name", "value": "Lightweight"}]}
```

### range

Wertebereich für Zahlen oder Datum. Parameter: `gte`, `lte`, `gt`, `lt`.
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

Container, der beliebige Filter negiert. `operator`: `or`, `and`.
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

Logische Verknüpfung mehrerer Filter. `operator`: `or`, `and`.
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

## Aggregations-Referenz

### avg — Durchschnitt

```php
$criteria->addAggregation(new AvgAggregation('avg-price', 'price'));
$aggregation = $result->getAggregations()->get('avg-price');
$aggregation->getAvg();
```

```json
{"aggregations": [{"name": "avg-price", "type": "avg", "field": "price"}]}
```

### count — Anzahl DISTINCT

```php
$criteria->addAggregation(new CountAggregation('count-manufacturers', 'manufacturerId'));
$aggregation->getCount();
```

### max — Maximum

```php
$criteria->addAggregation(new MaxAggregation('max-price', 'price'));
$aggregation->getMax();
```

### min — Minimum

```php
$criteria->addAggregation(new MinAggregation('min-price', 'price'));
$aggregation->getMin();
```

### sum — Summe

```php
$criteria->addAggregation(new SumAggregation('sum-price', 'price'));
$aggregation->getSum();
```

### stats — Mehrere Metriken

```php
$criteria->addAggregation(new StatsAggregation('stats-price', 'price'));
$aggregation->getSum();
$aggregation->getMax();
$aggregation->getAvg();
$aggregation->getMin();
```

### terms — Gruppen + Count (Bucket)

Unterstützt: `limit`, `sort`, verschachtelte `aggregation`.

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

### entity — Entities laden (Bucket)

Wie `terms`, lädt aber die zugehörigen Entities via Keys als IDs:

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

### filter — Aggregation filtern (Bucket)

Filtert nur die Aggregation, nicht das Suchergebnis:

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

### histogram — Datum-Gruppierung (Bucket)

Intervalle: `minute`, `hour`, `day`, `week`, `month`, `quarter`, `year`

```php
$criteria->addAggregation(new DateHistogramAggregation(
    'release-dates',
    'releaseDate',
    DateHistogramAggregation::PER_MONTH
));
foreach ($aggregation->getBuckets() as $bucket) {
    $bucket->getKey(); // z.B. "2020-04-01 00:00:00"
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

### range — Wertebereiche (Bucket)

`from`: >=, `to`: <

```php
$criteria->addAggregation(new RangeAggregation('price_ranges', 'products.price', [
    ['to' => 100],
    ['from' => 100, 'to' => 200],
    ['from' => 200],
]));
foreach ($aggregation->getRanges() as $key => $docCount) { ... }
```

### Verschachtelte Aggregations

```php
// Anzahl Hersteller pro Kategorie für Produkte > 500 €
$criteria->addAggregation(new FilterAggregation('my-filter',
    new TermsAggregation('per-category', 'categories.id', null, null,
        new TermsAggregation('manufacturer-ids', 'manufacturerId')
    ),
    [new RangeFilter('price', ['gte' => 500])]
));
```

---

## Flags-Referenz

| Flag | Beschreibung |
|---|---|
| `ApiAware` | Feld in Store- oder Admin-API verfügbar. Default: beide APIs. Kann auf `AdminApiSource`/`SalesChannelApiSource` eingeschränkt werden. |
| `Required` | Pflichtfeld beim Erstellen (Create-Request). Nur beim Schreiben relevant. |
| `PrimaryKey` | Definiert das Feld als Teil des Primary Keys. Normalerweise das ID-Feld. |
| `Runtime` | Wert wird zur Laufzeit berechnet (Event Subscriber o.ä.). Nicht direkt in DB gespeichert. |
| `Computed` | Indexer oder externe Systeme berechnen den Wert. Kein direkter DAL-Write möglich. |
| `WriteProtected` | API-Schreibzugriff eingeschränkt. Schützt indexierte Daten vor direkten API-Writes. |
| `Inherited` | Parent-Record kann den Wert dieses Felds vererben. |
| `ReverseInherited` | Gegenstück zu Inherited. |
| `CascadeDelete` | Wenn referenzierte Daten gelöscht werden, werden diese Daten auch gelöscht. |
| `RestrictDelete` | Verhindert Löschung der Entity, wenn ein Record mit diesem FK existiert. |
| `SetNullOnDelete` | FK wird auf NULL gesetzt wenn referenzierte Daten gelöscht werden. Written-Event wird ausgelöst. |
| `Immutable` | Write-once: kann beim Erstellen gesetzt werden, danach Read-only. |
| `Extension` | Daten werden in `Entity::$extension` gespeichert, nicht im Struct selbst. |
| `SearchRanking` | Gewichtung für Volltext-Suchquery auf dieser Entity für dieses Feld. |
| `Deprecated` | Feld als deprecated markiert. Wird mit nächster Major-Version entfernt. |
| `Since` | Ab welcher Shopware-Version das Feld verfügbar ist. |
| `AllowHtml` | HTML-escaped Daten in der Spalte erlaubt. Achtung: Injection-Risiko. |
| `AllowEmptyString` | Leerer String soll nicht als NULL behandelt werden. |

---

## Fields-Referenz (Übersicht aller Field-Klassen)

| Field-Klasse | Beschreibung | Extends | StorageAware |
|---|---|---|---|
| `IdField` | UUID-Primärschlüssel | Field | x |
| `FkField` | Foreign Key | Field | x |
| `StringField` | String-Wert | Field | x |
| `LongTextField` | Longtext | Field | x |
| `EmailField` | E-Mail (extends String) | StringField | - |
| `IntField` | Integer | Field | x |
| `FloatField` | Float | Field | x |
| `BoolField` | Boolean | Field | x |
| `DateField` | Datum | Field | x |
| `DateTimeField` | DateTime | Field | x |
| `JsonField` | JSON-Wert | Field | x |
| `ListField` | JSON-Array | JsonField | - |
| `ObjectField` | JSON-Objekt | JsonField | - |
| `PriceField` | Preis-Struct (JSON) | JsonField | - |
| `BlobField` | Blob | Field | x |
| `SerializedField` | Serialisierter Wert | Field | x |
| `PasswordField` | Passwort | Field | x |
| `EnumField` | BackedEnum-Wert | Field | x |
| `TranslatedField` | Übersetzter Wert | Field | - |
| `CreatedAtField` | Erstellt-Timestamp | DateTimeField | - |
| `UpdatedAtField` | Aktualisiert-Timestamp | DateTimeField | - |
| `ParentFkField` | Parent-FK | FkField | - |
| `VersionField` | Versions-FK | FkField | - |
| `StateMachineStateField` | State Machine FK | FkField | - |
| `ManyToOneAssociationField` | n:1 | AssociationField | - |
| `OneToManyAssociationField` | 1:n | AssociationField | - |
| `ManyToManyAssociationField` | n:m | AssociationField | - |
| `OneToOneAssociationField` | 1:1 | AssociationField | - |
| `ParentAssociationField` | Parent-Verknüpfung | ManyToOneAssociationField | - |
| `ChildrenAssociationField` | Kinder-Verknüpfung | OneToManyAssociationField | - |
| `TranslationsAssociationField` | Übersetzungs-Assoziaton | OneToManyAssociationField | - |
| `TreeLevelField` | Baum-Level | IntField | - |
| `TreePathField` | Baum-Pfad | LongTextField | - |
| `ChildCountField` | Kinder-Anzahl | IntField | - |
| `AutoIncrementField` | Auto-Increment | IntField | - |

## EnumField — Verwendung

```php
// BackedEnum definieren:
enum PaymentMethod: string {
    case PAYPAL = 'paypal';
    case CREDIT_CARD = 'credit_card';
}

// In Entity:
#[Field(type: FieldType::ENUM, column: 'payment_method')]
protected PaymentMethod $paymentMethod;

// Validierung:
$validMethod = PaymentMethod::tryFrom($userInput);
if ($validMethod === null) { /* Ungültiger Wert */ }

// DB: ENUM-Typ für Strings; INT-Spalte für Integer-Enums empfohlen
```

Twig-Beispiel:
```twig
<select name="payment_method">
    {% for method in PaymentMethod::cases() %}
        <option value="{{ method.value }}">{{ method.name }}</option>
    {% endfor %}
</select>
```
