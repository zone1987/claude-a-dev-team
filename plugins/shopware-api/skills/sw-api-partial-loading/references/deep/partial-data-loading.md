# Shopware 6 — Partial Data Loading (vollständige Referenz)

Quelle: `guides/development/integrations-api/partial-data-loading.md`

## Konzept

Partial Data Loading ermöglicht die Selektion spezifischer Entity-Felder, die von der API zurückgegeben werden. Der Unterschied zu `includes`:

- **`fields` (Partial Data Loading)**: Arbeitet auf Datenbankebene — nur angeforderte Felder werden geladen. Reduziert DB-Last direkt.
- **`includes`**: Post-Output-Processing — vollständige Entity wird geladen und dann im Response gefiltert.

Shopware selbst nutzt diesen Mechanismus für Storefront-Produktlistings: `core.listing.partialDataLoading` = 1. Siehe [Performance Tweaks](../../hosting/performance/performance-tweaks.md#reduced-product-data-in-listings).

## Verwendung — Einfache Felder

```http
POST /api/search/currency
Authorization: Bearer YOUR_ACCESS_TOKEN
Content-Type: application/json
Accept: application/json

{
  "fields": ["name"]
}
```

Response:
```json
{
  "total": 1,
  "data": [
    {
      "extensions": [],
      "_uniqueIdentifier": "018cda3ac909712496bccc065acf0ff4",
      "translated": { "name": "US-Dollar" },
      "id": "018cda3ac909712496bccc065acf0ff4",
      "name": "US-Dollar",
      "isSystemDefault": false,
      "apiAlias": "currency"
    }
  ],
  "aggregations": []
}
```

## Verwendung — Assoziationsfelder

Punkt-Notation referenziert Felder von Assoziationen. Die notwendigen Joins werden automatisch hinzugefügt:

```http
POST /api/search/currency
Content-Type: application/json

{
  "fields": ["name", "salesChannels.name"]
}
```

Response:
```json
{
  "total": 1,
  "data": [
    {
      "id": "018cda3ac909712496bccc065acf0ff4",
      "name": "US-Dollar",
      "salesChannels": [
        {
          "id": "018cda3af56670d6a3fa515a85967bd2",
          "name": "Storefront",
          "apiAlias": "sales_channel"
        }
      ],
      "apiAlias": "currency"
    }
  ]
}
```

## Immer geladene Felder (Default Fields)

Bestimmte Felder werden immer geladen, da sie für das korrekte Funktionieren der API notwendig sind:
- `id`
- Join-relevante Felder (Foreign Keys)

Diese können nicht entfernt werden.

## Runtime Fields

Einige API-Felder werden zur Laufzeit generiert (z.B. `isSystemDefault` bei Currency). Diese werden standardmäßig geladen, wenn die referenzierten Daten verfügbar sind. Sie können auch explizit im `fields`-Parameter angefordert werden, um das Laden zu erzwingen.

In eigenen EntityDefinitions:
```php
protected function defineFields(): FieldCollection
{
    return new FieldCollection([
        (new IdField('id', 'id'))->addFlags(new ApiAware(), new PrimaryKey(), new Required()),
        (new StringField('path', 'path'))->addFlags(new ApiAware()),
        // Wenn dieses Feld angefordert wird, brauchen wir 'path' zum Generieren der URL:
        (new StringField('url', 'url'))->addFlags(new ApiAware(), new Runtime(['path'])),
    ]);
}
```

## Einschränkungen

Die aktuelle Einschränkung von Partial Data Loading: Funktioniert **nur auf Entity-Ebene**.

Custom Responses wie Produkt-Detailseiten oder CMS in der Store API können diese Funktion nicht nutzen, da die Store API die vollständige Entity benötigt, um die Response zu generieren.

**Empfehlung**: Bei solchen Endpoints → `includes`-Feature des Search API nutzen.

## Vergleich: Partial Loading vs. Includes

```json
// Nur mit includes (vollständige Entity geladen, Output gefiltert):
{
  "includes": {
    "product": ["id", "name"]
  }
}

// Mit fields (DB lädt nur angeforderte Spalten):
{
  "fields": ["id", "name"]
}
```

Für maximale Performance bei einfachen Entity-Abfragen: `fields` bevorzugen.
Für komplexe Custom-Responses oder Store-API-CMS: `includes` verwenden.
