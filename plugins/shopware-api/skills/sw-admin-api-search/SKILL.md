---
name: sw-admin-api-search
description: >
  Der Such-Endpunkt der Shopware-6 Admin API: POST /api/search/{entity} mit Criteria-JSON (filter, sort, associations,
  aggregations, page, limit, total-count-mode, ids, term, post-filter, grouping). Trigger: "POST /api/search",
  "api search criteria", "filter sort associations api", "aggregations api", "total-count-mode", "Daten suchen Admin API".
  Shopware 6.7.
---

# Shopware 6 — Admin-API-Suche (Criteria)

Für echte Abfragen `POST /api/search/{entity}` mit Criteria-JSON (gespiegelt von der PHP-DAL-Criteria).

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

Filter-Typen: `equals`, `equalsAny`, `contains`, `prefix`, `suffix`, `range`, `multi` (operator AND/OR), `not`.
`associations` lädt verschachtelt (rekursiv mit eigener Criteria). `aggregations` für Kennzahlen/Facetten.
`total-count-mode`: 0 (keins), 1 (exact), 2 (next-pages). Antwort: `data`, `total`, `aggregations`.
Identisch nutzbar auf der Store API für `product-listing`/`search` (`sw-store-api-endpoints`). DAL-Pendant: `shopware-data` (`sw-criteria`).
