# Shopware 6 — Admin API search (Criteria)

For real queries use `POST /api/search/{entity}` with Criteria JSON (mirrored from the PHP DAL Criteria).

```bash
curl -X POST "$BASE/api/search/product" -H "Authorization: Bearer $T" -H "Content-Type: application/json" -d '{
  "page": 1, "limit": 25, "total-count-mode": 1,
  "filter": [{ "type": "equals", "field": "active", "value": true },
             { "type": "range", "field": "stock", "parameters": { "gte": 1 } }],
  "sort": [{ "field": "createdAt", "order": "DESC" }],
  "associations": { "categories": {}, "manufacturer": {} },
  "aggregations": [{ "name": "perManufacturer", "type": "terms", "field": "manufacturerId" }]
}'
```

Filter types: `equals`, `equalsAny`, `contains`, `prefix`, `suffix`, `range`, `multi` (operator AND/OR), `not`.
`associations` loads nested data (recursively, with its own Criteria). `aggregations` for metrics/facets.
`total-count-mode`: 0 (none), 1 (exact), 2 (next-pages). Response: `data`, `total`, `aggregations`.
Usable identically on the Store API for `product-listing`/`search` (`sw-store-api-endpoints`). DAL counterpart: `shopware-data` (`sw-criteria`).
