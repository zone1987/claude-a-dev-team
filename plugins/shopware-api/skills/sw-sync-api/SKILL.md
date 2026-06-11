---
name: sw-sync-api
description: >
  Die Shopware-6 Sync API für Massen-Schreibvorgänge: POST /api/_action/sync, Operationen (entity, action upsert/delete,
  payload-Array), single-operation Header, fail-on-error, indexing-behavior/skip-indexer Header. Trigger: "Sync API",
  "/api/_action/sync", "Massen-Import API", "bulk upsert delete api", "single-operation header", "fail-on-error sync",
  "indexing-behavior". Shopware 6.7.
---

# Shopware 6 — Sync API (Bulk)

Mehrere Schreiboperationen über verschiedene Entities in **einem** Request — effizient für Import/Sync.

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

Jeder Key = eine benannte Operation (`entity`, `action` = `upsert`|`delete`, `payload`-Array). Steuer-Header:
- `single-operation: 1` — alles in einer Transaktion (sonst je Operation).
- `fail-on-error: false` — Teilerfolge zulassen.
- `indexing-behavior: use-queue-indexing` / `disable-indexing` — Indexer-Last steuern (großer Import).

Auth = Admin-OAuth (`sw-admin-api-auth`). Für einzelne Datensätze reicht `sw-admin-api-crud`.
