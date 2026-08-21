# Shopware 6 — Partial Data Loading

With the `fields` parameter only the requested columns are loaded at **database level**.
Difference from `includes` (output post-processing): partial loading reduces the DB load directly.

## Usage

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

Dot notation `salesChannels.name` → adds the association join automatically.

## Partial Loading vs. Includes

| | `fields` (partial loading) | `includes` |
|---|---|---|
| When | DB query level | output post-processing |
| Performance | Better (the DB loads less) | the complete entity is loaded |
| Scope | Entity level only | every response type |

## Fixed fields (always loaded)

`id` and join-relevant fields (foreign keys) are always loaded — the API needs them internally.

## Runtime Fields

Loaded by default when the referenced data is available. Force them via `fields`.
Define them in `EntityDefinition` with the `Runtime` flag and its dependencies:

```php
(new StringField('url', 'url'))->addFlags(new ApiAware(), new Runtime(['path']))
```

## Limitations

- Works **only at entity level**
- Store API custom responses (product detail page, CMS) are not supported
- For small responses on such endpoints: use `includes`

The storefront uses partial loading internally: `core.listing.partialDataLoading` = 1.
Complete Criteria reference: `sw-admin-api-search`. Headers: `sw-api-headers`.
