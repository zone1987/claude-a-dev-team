# Shopware 6 — Admin-API-CRUD

Generisches Schema je DAL-Entity (Entity-Name in **kebab/plural-Form** der Route, z.B. `product`, `product-manufacturer`):

```
GET    /api/{entity}            # Liste (einfach; für echte Queries -> /api/search)
GET    /api/{entity}/{id}       # einzeln
POST   /api/{entity}            # anlegen (Body = Attribute, optional eigene id als 32-hex-UUID)
PATCH  /api/{entity}/{id}       # teilweise aktualisieren
DELETE /api/{entity}/{id}       # löschen
```

```bash
curl -X POST "$BASE/api/product" -H "Authorization: Bearer $T" -H "Content-Type: application/json" -d '{
  "id": "0a1b...32hex", "name": "Demo", "productNumber": "SW-1", "stock": 10,
  "taxId": "<id>", "price": [{ "currencyId": "<id>", "gross": 19.99, "net": 16.8, "linked": true }]
}'
```

IDs sind 32-stellige Hex-UUIDs. Verschachtelte Associations direkt im Body (`"categories": [{"id": "..."}]`).
Erfolg meist `204 No Content` (kein Body) bzw. `200`. Filtern/Sortieren/Assoziationen laden → `sw-admin-api-search`.
Massen-Writes → `sw-sync-api`. Kontext-Header (Sprache/Währung/Version) → `sw-api-headers`.
