# Shopware 6 — Admin API CRUD

Generic schema per DAL entity (entity name in **kebab/plural form** in the route, e.g. `product`, `product-manufacturer`):

```
GET    /api/{entity}            # list (simple; for real queries -> /api/search)
GET    /api/{entity}/{id}       # single
POST   /api/{entity}            # create (body = attributes, optionally your own id as 32-hex UUID)
PATCH  /api/{entity}/{id}       # partial update
DELETE /api/{entity}/{id}       # delete
```

```bash
curl -X POST "$BASE/api/product" -H "Authorization: Bearer $T" -H "Content-Type: application/json" -d '{
  "id": "0a1b...32hex", "name": "Demo", "productNumber": "SW-1", "stock": 10,
  "taxId": "<id>", "price": [{ "currencyId": "<id>", "gross": 19.99, "net": 16.8, "linked": true }]
}'
```

IDs are 32-character hex UUIDs. Nested associations go directly in the body (`"categories": [{"id": "..."}]`).
Success is usually `204 No Content` (no body) or `200`. Filtering/sorting/loading associations → `sw-admin-api-search`.
Bulk writes → `sw-sync-api`. Context headers (language/currency/version) → `sw-api-headers`.
