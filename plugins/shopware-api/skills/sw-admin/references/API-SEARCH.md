# Shopware 6 — search criteria

Endpoints taking `POST` with a criteria JSON object are **search criteria** endpoints. The object
takes the same arguments as a DAL criteria. Individual endpoints may accept further parameters of
their own, which differ per endpoint.

## Contents

- [The parameters](#the-parameters)
- [associations](#associations)
- [includes and apiAlias](#includes-and-apialias)
- [ids](#ids)
- [total-count-mode](#total-count-mode)
- [page and limit](#page-and-limit)
- [filter and post-filter](#filter-and-post-filter)
- [query and term](#query-and-term)
- [sort](#sort)
- [aggregations](#aggregations)
- [grouping](#grouping)

A typical criteria, combining nested associations with a per-type `includes`:

```json
{
  "limit": 10,
  "associations": {
    "manufacturer": {},
    "propertyIds": {},
    "cover": {},
    "options": {
      "associations": { "productOptions": {}, "group": {} }
    }
  },
  "includes": {
    "product": ["calculatedPrice", "cover", "id", "translated", "seoUrls",
                "manufacturer", "propertyIds", "options"],
    "product_media": ["media"],
    "media": ["thumbnails", "width", "height", "url"],
    "calculated_price": ["unitPrice", "quantity"]
  }
}
```

Note how `includes` is keyed per type — `product`, `product_media`, `media`, `calculated_price` —
which is what lets a nested association be trimmed as tightly as the root entity.

## The parameters

| Parameter | Usage |
|---|---|
| `associations` | loads additional data alongside an entity's standard data |
| `includes` | restricts the output to the fields named |
| `ids` | limits the search to a list of ids |
| `total-count-mode` | whether a total is determined |
| `page` | which page the result starts at |
| `limit` | how many entries to determine |
| `filter` | filters the result **and** the aggregations |
| `post-filter` | filters the result but **not** the aggregations |
| `query` | determines a ranking for the result |
| `term` | determines a ranking for the result |
| `sort` | the sorting of the result |
| `aggregations` | aggregations computed on the fly |
| `grouping` | groups records by fields |

```bash
curl -X POST "$BASE/api/search/product" -H "Authorization: Bearer $T" \
  -H "Content-Type: application/json" -d '{
  "page": 1, "limit": 25, "total-count-mode": 1,
  "filter": [{ "type": "equals", "field": "active", "value": true }],
  "sort": [{ "field": "createdAt", "order": "DESC" }],
  "associations": { "categories": {}, "manufacturer": {} }
}'
```

## associations

Loads extra data without a second request, like a SQL join. **The key is the association's property
name on the entity**, and the value is a nested criteria — so an association can carry its own
limit, filter and sort:

```json
{
  "associations": {
    "products": {
      "limit": 5,
      "filter": [{ "type": "equals", "field": "active", "value": true }],
      "sort": [{ "field": "name", "order": "ASC" }]
    }
  }
}
```

## includes and apiAlias

`includes` restricts the fields returned: a smaller payload, easier to consume, and easier to read
while debugging.

```json
{ "includes": { "product": ["id", "name"] } }
```

**Every response type carries an `apiAlias` field, and that alias is the key to use in `includes`.**
For entities it is the entity name — `product`, `product_manufacturer`, `order_line_item`. For
non-entity types, such as a listing result or a line item, read the alias off the full response
first. The pattern applies to associations as much as to plain fields.

```json
{
  "total": 120,
  "data": [
    { "name": "Synergistic Rubber Fish Soda", "id": "012cd563cf8e4f0384eed93b5201cc98", "apiAlias": "product" }
  ]
}
```

## ids

A plain lookup by id:

```json
{ "ids": ["012cd563cf8e4f0384eed93b5201cc98", "075fb241b769444bb72431f797fd5776"] }
```

## total-count-mode

| Value | Behaviour | When to use |
|---|---|---|
| `0` (default) | no total determined | pagination is not needed; the fastest mode, since MySQL runs no `SQL_CALC_FOUND_ROWS` |
| `1` | an exact total | pagination showing exact page numbers. **Performance intensive** — it needs `SQL_CALC_FOUND_ROWS` |
| `2` | whether a next page exists | infinite scrolling, where that is all you need. Performs as well as `0` |

## page and limit

```json
{ "page": 1, "limit": 5 }
```

**`page` is 1-indexed.**

## filter and post-filter

Filter types are the same as the DAL's. **When filtering on a nested value, load it through
`associations` first** — filtering orders by `order.transactions.stateMachineState` requires that
association to be fetched:

```json
{
  "associations": { "transactions": { "associations": { "stateMachineState": {} } } },
  "filter": [{
    "type": "multi", "operator": "and",
    "queries": [
      { "type": "multi", "operator": "or", "queries": [
        { "type": "equals", "field": "transactions.stateMachineState.technicalName", "value": "paid" },
        { "type": "equals", "field": "transactions.stateMachineState.technicalName", "value": "open" }
      ]},
      { "type": "equals", "field": "customFields.exportedFlag", "value": null }
    ]
  }]
}
```

`post-filter` works identically **but does not apply to aggregations** — which is what makes it right
for a filter navigation: the facets stay computed over the unfiltered set while the results are
already narrowed, in one request.

## query and term

`query` builds a weighted search returning a `_score` per entity. Any filter type works as a query,
and **each query needs a `score`**; the sum of the matching ones is the total.

```json
{
  "query": [
    { "score": 500, "query": { "type": "contains", "field": "name", "value": "Bronze" } },
    { "score": 500, "query": { "type": "equals", "field": "active", "value": true } },
    { "score": 100, "query": { "type": "equals", "field": "manufacturerId", "value": "db3c17b1e572432eb4a4c881b6f9d68f" } }
  ]
}
```

The score arrives on each record under `extensions.search._score`.

`term` instead runs a text search across all records, weighted by the entity definition's
`SearchRanking` flag:

```json
{ "term": "Awesome Bronze" }
```

**Do not combine `term` with `query`.**

## sort

Several sortings at once:

| Key | Meaning |
|---|---|
| `field` | the field to sort by |
| `order` | the direction |
| `naturalSorting` | uses a natural sorting algorithm |
| `type` | divergent behaviour; `count` sorts by the number of associations — `ORDER BY COUNT({field}) {order}` |

```json
{
  "limit": 5,
  "sort": [
    { "field": "name", "order": "ASC", "naturalSorting": true },
    { "field": "active", "order": "DESC" },
    { "field": "products.id", "order": "DESC", "type": "count" }
  ]
}
```

**`type: count` arrived with Shopware 6.4.12.0** and is absent before that. Combined with a `count`
aggregation, the order of the returned elements matches the order of the aggregated buckets:

```json
{
  "limit": 3,
  "includes": { "product": ["id"] },
  "sort": [{ "field": "categories.id", "order": "DESC", "type": "count" }],
  "aggregations": [{
    "name": "product-id", "type": "terms", "field": "id", "limit": 3,
    "sort": { "field": "_count", "order": "DESC" },
    "aggregation": { "name": "category-count", "type": "count", "field": "product.categories.id" }
  }]
}
```

## aggregations

Metadata for a search query — statistics and metrics, or the possible filters for a facet
navigation. The types match the DAL's aggregations.

```json
{
  "limit": 1,
  "includes": { "product": ["id", "name"] },
  "aggregations": [{ "name": "average-price", "type": "avg", "field": "price" }]
}
```

## grouping

Groups the result over fields — one product per manufacturer, one order per day and customer:

```json
{ "limit": 5, "grouping": ["active"] }
```

## Related

The same criteria work on the Store API for `product-listing` and `search`; see the Store API
endpoints. For the PHP-side counterpart, call the Skill tool with `sw-query`.

## Source

[developer.shopware.com/docs/guides/development/integrations-api/search-criteria.html](https://developer.shopware.com/docs/guides/development/integrations-api/search-criteria.html),
Shopware 6.7, retrieved 2026-08-21.
