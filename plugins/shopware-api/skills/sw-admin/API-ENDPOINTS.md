# Shopware Admin API — Endpunkt-Referenz

**Version:** 6.7.9999999-dev | **Basis-URL:** `{shop}/api` | **Operationen:** 1093 in 143 Tags

## Authentifizierung

Security-Scheme: `oAuth` (OAuth 2.0)

| Flow | Token-URL | Scopes |
|------|-----------|--------|
| `password` | `/api/oauth/token` | `write` (Full write), `admin` (Admin-Ops) |
| `clientCredentials` | `/api/oauth/token` | `write`, `admin` |

Token holen:
```bash
curl -X POST "$SHOP/api/oauth/token" \
  -H "Content-Type: application/json" \
  -d '{"grant_type":"password","client_id":"administration","username":"admin","password":"shopware","scopes":"write"}'
```

Alle folgenden Requests: `Authorization: Bearer {token}`

Auth-Details → `sw-admin-api-auth`. CRUD-Schema → `sw-admin-api-crud`. Search/Filter → `sw-admin-api-search`.

## Generisches CRUD/Search-Muster

Jede DAL-Entity (z.B. `product`, `order`, `customer`) hat 7 Standard-Operationen:

```
GET    /api/{entity}            Liste (basic info)
POST   /api/{entity}            Neu anlegen
GET    /api/{entity}/{id}       Detail
PATCH  /api/{entity}/{id}       Teilweise aktualisieren
DELETE /api/{entity}/{id}       Löschen
POST   /api/search/{entity}     Suche/Filter mit Criteria
POST   /api/aggregate/{entity}  Aggregation
```

Aktions-Endpunkte: `POST/GET /api/_action/...`
Bulk-Sync: `POST /api/_action/sync`

Vollständige Tag-Gruppierung aller Endpunkte → `API-ENDPOINTS-DETAIL.md`
