---
name: sw-api-integration
description: >
  Shopware 6 API Integration-Einstieg: OAuth2 client_credentials, password-grant (lokal), erster Request,
  OpenAPI-Schema herunterladen, Store API access-key ermitteln, häufige Fehler (DB nicht initialisiert,
  falsche URL, leere data-Arrays). Trigger: "erste API Anfrage", "Shopware API starten", "Integration einrichten",
  "API Quickstart", "OAuth token holen", "admin api first request", "openapi schema herunterladen",
  "api instance running", "api troubleshooting local", "api 500 error", "system:install api". Shopware 6.7.
---

# Shopware 6 — API-Integration Quickstart

**Admin API**: OAuth2 `client_credentials` (Produktiv) oder `password` (lokal). **Store API**: `sw-access-key` (Sales Channel).

## Admin API Token holen

```bash
# Produktiv: client_credentials (Integrationen: Settings → System → Integrations)
curl -s "http://127.0.0.1:8000/api/oauth/token" -H "Content-Type: application/json" \
  -d '{"grant_type":"client_credentials","client_id":"ACCESS_KEY_ID","client_secret":"SECRET"}'

# Nur lokal: password grant
curl -s -X POST "http://localhost:8000/api/oauth/token" -H "Content-Type: application/json" \
  -d '{"grant_type":"password","client_id":"administration","scopes":"write","username":"admin","password":"shopware"}'
# → access_token (expires_in 600 s, hat refresh_token)
```

## Erster Admin-API-Request

Bevorzuge `POST /api/search/{entity}` statt `GET /api/{entity}` — unterstützt filter/sort/associations.

```bash
curl -X POST "http://127.0.0.1:8000/api/search/product" \
  -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" -d '{}'
```

Antwort mit `data`, `meta`, `aggregations` → Erfolg (leeres `data` = keine Produkte, kein Fehler).

## OpenAPI-Schema herunterladen (`APP_ENV=dev` nötig)

```bash
curl -s "http://127.0.0.1:8000/api/_info/openapi3.json" -H "Authorization: Bearer $TOKEN" -o openapi.json
curl -s "http://127.0.0.1:8000/api/_info/open-api-schema.json" -H "Authorization: Bearer $TOKEN" -o entity-schema.json
# Store API:
curl -s "http://127.0.0.1:8000/store-api/_info/openapi3.json" -o store-openapi.json
```

Stoplight UI: `/api/_info/stoplightio.html` und `/store-api/_info/stoplightio.html`

## Store API — Access Key ermitteln

Administration → **Sales Channels → Storefront → API access** → API access key kopieren.

```bash
curl -s "http://127.0.0.1:8000/store-api/product" -H "sw-access-key: $STORE_KEY"
```

## Häufige Fehler

| Fehler | Ursache | Fix |
|---|---|---|
| `Table 'shopware.system_config' doesn't exist` | DB nicht initialisiert | `bin/console system:install --create-database --basic-setup` |
| HTTP 500 auf `/api/_info/openapi3.json` | `APP_ENV` nicht `dev` | `.env.local`: `APP_ENV=dev`, Container neu starten |
| `data` leer | Keine Produkte/Filter passt | Normales Ergebnis — kein Fehler |
| Store API liefert nix | Falsche Sales-Channel-Domain | Admin: Sales Channels → Domains → `127.0.0.1:8000` ergänzen |

Vollständige End-to-End-Flows (Produkt anlegen, Warenkorb, Checkout): `sw-api-flows`.
Header-Referenz: `sw-api-headers`. Criteria/Filter: `sw-admin-api-search`.
