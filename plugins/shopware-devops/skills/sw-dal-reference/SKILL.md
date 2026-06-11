---
name: sw-dal-reference
description: >
  Shopware 6 DAL Referenz: alle Filter-Typen (equals, equalsAny, contains, range, not, multi, prefix, suffix),
  alle Aggregations-Typen (avg, count, max, min, sum, stats, terms, filter, entity, histogram, range),
  Flags-Referenz (ApiAware, Required, Runtime, WriteProtected, Inherited, CascadeDelete, etc.),
  Fields-Referenz (alle Field-Klassen). Trigger: "dal filter", "dal aggregation", "dal flags",
  "dal fields", "equalsAny filter", "RangeFilter", "NotFilter", "MultiFilter", "AvgAggregation",
  "TermsAggregation", "DateHistogramAggregation", "EntityAggregation", "ApiAware flag",
  "CascadeDelete flag", "WriteProtected flag", "Runtime flag", "dal referenz". Shopware 6.7.
---

# Shopware 6 — DAL Referenz (Filter, Aggregations, Flags, Fields)

## Filter-Typen

| Typ | PHP-Klasse | Beschreibung |
|---|---|---|
| `equals` | `EqualsFilter` | Exakter Match |
| `equalsAny` | `EqualsAnyFilter` | Mindestens ein Match aus Liste (IN) |
| `contains` | `ContainsFilter` | LIKE '%value%' |
| `prefix` | `PrefixFilter` | LIKE 'value%' |
| `suffix` | `SuffixFilter` | LIKE '%value' |
| `range` | `RangeFilter` | gte/lte/gt/lt für Zahlen/Datum |
| `not` | `NotFilter` | Negiert beliebigen Filter |
| `multi` | `MultiFilter` | AND/OR-Verknüpfung mehrerer Filter |

```php
// range: gte, lte, gt, lt
$criteria->addFilter(new RangeFilter('stock', [RangeFilter::GTE => 20, RangeFilter::LTE => 30]));

// multi mit OR
$criteria->addFilter(new MultiFilter(MultiFilter::CONNECTION_OR, [
    new EqualsFilter('stock', 1),
    new EqualsFilter('availableStock', 10),
]));

// not
$criteria->addFilter(new NotFilter(NotFilter::CONNECTION_OR, [
    new EqualsFilter('stock', 1),
]));
```

## Aggregations-Typen

| Typ | PHP-Klasse | Art | Beschreibung |
|---|---|---|---|
| `avg` | `AvgAggregation` | metric | Durchschnitt |
| `count` | `CountAggregation` | metric | Anzahl DISTINCT |
| `max` | `MaxAggregation` | metric | Maximum |
| `min` | `MinAggregation` | metric | Minimum |
| `sum` | `SumAggregation` | metric | Summe |
| `stats` | `StatsAggregation` | metric | Avg+Min+Max+Sum in einem |
| `terms` | `TermsAggregation` | bucket | Gruppen + Count; unterstützt limit/sort/aggregation |
| `entity` | `EntityAggregation` | bucket | Wie terms, lädt Entities via IDs |
| `filter` | `FilterAggregation` | bucket | Filtert nur die Aggregation (nicht Result) |
| `histogram` | `DateHistogramAggregation` | bucket | Datum-Gruppierung (minute/hour/day/week/month/quarter/year) |
| `range` | `RangeAggregation` | bucket | Vordefinierte Wertebereiche (from/to) |

## Flags-Referenz

| Flag | Beschreibung |
|---|---|
| `ApiAware` | Feld in Store- oder Admin-API verfügbar |
| `Required` | Pflichtfeld beim Anlegen |
| `PrimaryKey` | Teil des Primary Keys |
| `Runtime` | Wird zur Laufzeit berechnet, nicht in DB gespeichert |
| `Computed` | Indexer berechnet Wert — kein direkter API-Write |
| `WriteProtected` | API-Write eingeschränkt |
| `Inherited` | Parent-Vererbung möglich |
| `CascadeDelete` | Löscht assoziierte Daten mit |
| `RestrictDelete` | Verhindert Löschung wenn Referenz existiert |
| `SetNullOnDelete` | Setzt FK auf NULL wenn Referenz gelöscht |
| `Immutable` | Write-once, dann Read-only |
| `Extension` | Daten in `Entity::$extension`, nicht im Struct |
| `SearchRanking` | Gewichtung für Volltextsuche |
| `Deprecated` | Als deprecated markiert |
| `Since` | Ab welcher Shopware-Version verfügbar |
| `AllowHtml` | HTML-Inhalt erlaubt |
| `AllowEmptyString` | Leerer String ≠ NULL |

Vollständige Filter- und Aggregations-Beispiele (PHP + API-JSON): `references/deep/dal-reference.md`.
