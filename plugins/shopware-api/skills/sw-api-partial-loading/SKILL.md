---
name: sw-api-partial-loading
description: >
  Shopware 6 Partial Data Loading — `fields`-Parameter in der API limitiert Datenbankabfrage
  auf benötigte Felder (Unterschied zu `includes`: DB-Level vs. Output-Filtering). Automatisches
  Nachladen von Assoziationen via Punkt-Notation. Einschränkungen (nur Entity-Level).
  Trigger: "partial data loading", "fields parameter api", "nur bestimmte felder laden",
  "response verkleinern api", "core.listing.partialDataLoading", "runtime fields api",
  "teilweise daten api", "performance api felder". Shopware 6.7.
---

# Shopware 6 — Partial Data Loading

Mit dem `fields`-Parameter werden nur die angeforderten Spalten auf **Datenbankebene** geladen.
Unterschied zu `includes` (Output-Post-Processing): Partial loading reduziert die DB-Last direkt.

## Verwendung

```http
POST /api/search/currency
Authorization: Bearer TOKEN
Content-Type: application/json

{
  "fields": ["name"]
}
```

```http
POST /api/search/currency
Content-Type: application/json

{
  "fields": ["name", "salesChannels.name"]
}
```

Punkt-Notation `salesChannels.name` → fügt Assoziations-Join automatisch hinzu.

## Partial Loading vs. Includes

| | `fields` (Partial Loading) | `includes` |
|---|---|---|
| Wann | DB-Abfrageebene | Ausgabe-Post-Processing |
| Performance | Besser (DB lädt weniger) | Komplette Entity wird geladen |
| Scope | Nur Entity-Level | Jeder Response-Typ |

## Feste Felder (immer geladen)

`id` und Join-relevante Felder (Foreign Keys) werden immer geladen — API braucht sie intern.

## Runtime Fields

Werden standardmäßig geladen wenn referenzierte Daten verfügbar. Via `fields` erzwingen.
In `EntityDefinition` mit `Runtime`-Flag und Dependencies definieren:

```php
(new StringField('url', 'url'))->addFlags(new ApiAware(), new Runtime(['path']))
```

## Einschränkungen

- Funktioniert **nur auf Entity-Ebene**
- Store-API Custom-Responses (Produkt-Detailseite, CMS) nicht unterstützt
- Für kleine Responses bei solchen Endpoints: `includes` verwenden

Storefront nutzt Partial Loading intern: `core.listing.partialDataLoading` = 1.
Vollständige Criteria-Referenz: `sw-admin-api-search`. Header: `sw-api-headers`.
