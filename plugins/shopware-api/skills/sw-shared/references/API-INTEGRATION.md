# Shopware 6 — API integration quickstart

**Admin API**: OAuth2 `client_credentials` (production) or `password` (local). **Store API**: `sw-access-key` (sales channel).

## Fetch an Admin API token

```bash
# Production: client_credentials (integrations: Settings → System → Integrations)
curl -s "http://127.0.0.1:8000/api/oauth/token" -H "Content-Type: application/json" \
  -d '{"grant_type":"client_credentials","client_id":"ACCESS_KEY_ID","client_secret":"SECRET"}'

# Local only: password grant
curl -s -X POST "http://localhost:8000/api/oauth/token" -H "Content-Type: application/json" \
  -d '{"grant_type":"password","client_id":"administration","scopes":"write","username":"admin","password":"shopware"}'
# → access_token (expires_in 600 s, has a refresh_token)
```

## First Admin API request

Prefer `POST /api/search/{entity}` over `GET /api/{entity}` — it supports filter/sort/associations.

```bash
curl -X POST "http://127.0.0.1:8000/api/search/product" \
  -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" -d '{}'
```

A response with `data`, `meta`, `aggregations` → success (empty `data` = no products, not an error).

## Download the OpenAPI schema (`APP_ENV=dev` required)

```bash
curl -s "http://127.0.0.1:8000/api/_info/openapi3.json" -H "Authorization: Bearer $TOKEN" -o openapi.json
curl -s "http://127.0.0.1:8000/api/_info/open-api-schema.json" -H "Authorization: Bearer $TOKEN" -o entity-schema.json
# Store API:
curl -s "http://127.0.0.1:8000/store-api/_info/openapi3.json" -o store-openapi.json
```

Stoplight UI: `/api/_info/stoplightio.html` und `/store-api/_info/stoplightio.html`

## Store API — determine the access key

Administration → **Sales Channels → Storefront → API access** → copy the API access key.

```bash
curl -s "http://127.0.0.1:8000/store-api/product" -H "sw-access-key: $STORE_KEY"
```

## Common errors

| Error | Cause | Fix |
|---|---|---|
| `Table 'shopware.system_config' doesn't exist` | DB not initialised | `bin/console system:install --create-database --basic-setup` |
| HTTP 500 on `/api/_info/openapi3.json` | `APP_ENV` is not `dev` | `.env.local`: `APP_ENV=dev`, restart the container |
| `data` empty | No products / filter matches nothing | Normal result — not an error |
| Store API returns nothing | Wrong sales channel domain | Admin: Sales Channels → Domains → add `127.0.0.1:8000` |

Complete end-to-end flows (create a product, cart, checkout): `sw-api-flows`.
Header reference: `sw-api-headers`. Criteria/filter: `sw-admin-api-search`.
