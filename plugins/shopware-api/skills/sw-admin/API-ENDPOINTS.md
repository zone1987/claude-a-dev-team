# Shopware Admin API — endpoint reference

**Version:** 6.7.9999999-dev | **Base URL:** `{shop}/api` | **Operations:** 1093 across 143 tags

## Authentication

Security scheme: `oAuth` (OAuth 2.0)

| Flow | Token URL | Scopes |
|------|-----------|--------|
| `password` | `/api/oauth/token` | `write` (Full write), `admin` (Admin ops) |
| `clientCredentials` | `/api/oauth/token` | `write`, `admin` |

Fetch a token:
```bash
curl -X POST "$SHOP/api/oauth/token" \
  -H "Content-Type: application/json" \
  -d '{"grant_type":"password","client_id":"administration","username":"admin","password":"shopware","scopes":"write"}'
```

All following requests: `Authorization: Bearer {token}`

Auth details → `sw-admin-api-auth`. CRUD schema → `sw-admin-api-crud`. Search/filter → `sw-admin-api-search`.

## Generic CRUD/search pattern

Every DAL entity (e.g. `product`, `order`, `customer`) has 7 standard operations:

```
GET    /api/{entity}            List (basic info)
POST   /api/{entity}            Create new
GET    /api/{entity}/{id}       Detail
PATCH  /api/{entity}/{id}       Partial update
DELETE /api/{entity}/{id}       Delete
POST   /api/search/{entity}     Search/filter with Criteria
POST   /api/aggregate/{entity}  Aggregation
```

Action endpoints: `POST/GET /api/_action/...`
Bulk sync: `POST /api/_action/sync`

Complete tag grouping of all endpoints → `API-ENDPOINTS-DETAIL.md`
