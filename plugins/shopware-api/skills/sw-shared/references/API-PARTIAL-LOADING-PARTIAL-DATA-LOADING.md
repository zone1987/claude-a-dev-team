# Shopware 6 — Partial Data Loading (complete reference)

Source: `guides/development/integrations-api/partial-data-loading.md`

## Contents

- [Concept](#concept)
- [Usage — simple fields](#usage--simple-fields)
- [Usage — association fields](#usage--association-fields)
- [Always-loaded fields (default fields)](#always-loaded-fields-default-fields)
- [Runtime Fields](#runtime-fields)
- [Limitations](#limitations)
- [Comparison: partial loading vs. includes](#comparison-partial-loading-vs-includes)

## Concept

Partial Data Loading allows selecting the specific entity fields the API returns. The difference from `includes`:

- **`fields` (Partial Data Loading)**: works at database level — only the requested fields are loaded. Reduces the DB load directly.
- **`includes`**: post-output processing — the complete entity is loaded and then filtered in the response.

Shopware itself uses this mechanism for storefront product listings: `core.listing.partialDataLoading` = 1. See Performance Tweaks.

## Usage — simple fields

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

## Usage — association fields

Dot notation references fields of associations. The necessary joins are added automatically:

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

## Always-loaded fields (default fields)

Certain fields are always loaded because they are necessary for the API to work correctly:
- `id`
- Join-relevant fields (foreign keys)

These cannot be removed.

## Runtime Fields

Some API fields are generated at runtime (e.g. `isSystemDefault` on currency). These are loaded by default when the referenced data is available. They can also be requested explicitly in the `fields` parameter to force the loading.

In your own EntityDefinitions:
```php
protected function defineFields(): FieldCollection
{
    return new FieldCollection([
        (new IdField('id', 'id'))->addFlags(new ApiAware(), new PrimaryKey(), new Required()),
        (new StringField('path', 'path'))->addFlags(new ApiAware()),
        // If this field is requested, we need 'path' to generate the URL:
        (new StringField('url', 'url'))->addFlags(new ApiAware(), new Runtime(['path'])),
    ]);
}
```

## Limitations

The current limitation of Partial Data Loading: it works **only at entity level**.

Custom responses such as product detail pages or CMS in the Store API cannot use this feature, because the Store API needs the complete entity to generate the response.

**Recommendation**: on such endpoints → use the `includes` feature of the search API.

## Comparison: partial loading vs. includes

```json
// With includes only (complete entity loaded, output filtered):
{
  "includes": {
    "product": ["id", "name"]
  }
}

// With fields (the DB loads only the requested columns):
{
  "fields": ["id", "name"]
}
```

For maximum performance on simple entity queries: prefer `fields`.
For complex custom responses or Store API CMS: use `includes`.
