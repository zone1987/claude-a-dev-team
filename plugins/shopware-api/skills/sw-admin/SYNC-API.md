# Shopware 6 — Sync API (bulk)

Several write operations across different entities in **one** request — efficient for import/sync.

```bash
curl -X POST "$BASE/api/_action/sync" -H "Authorization: Bearer $T" -H "Content-Type: application/json" -d '{
  "write-products": {
    "entity": "product", "action": "upsert",
    "payload": [ { "id": "<hex>", "name": "A", "productNumber": "A1", "stock": 5, "taxId": "<id>",
                   "price": [{ "currencyId": "<id>", "gross": 9.99, "net": 8.4, "linked": true }] } ]
  },
  "delete-old": { "entity": "product", "action": "delete", "payload": [ { "id": "<hex>" } ] }
}'
```

Each key = one named operation (`entity`, `action` = `upsert`|`delete`, `payload` array). Control headers:
- `single-operation: 1` — everything in one transaction (otherwise one per operation).
- `fail-on-error: false` — allow partial success.
- `indexing-behavior: use-queue-indexing` / `disable-indexing` — control indexer load (large imports).

Auth = admin OAuth (`sw-admin-api-auth`). For single records `sw-admin-api-crud` is enough.
