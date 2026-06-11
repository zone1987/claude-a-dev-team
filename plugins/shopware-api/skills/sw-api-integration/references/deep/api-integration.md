# Shopware 6 — API-Integration (vollständige Referenz)

Quellen: `guides/development/integrations-api/index.md`, `auth-api-requests.md`

## Überblick

Shopware bietet zwei HTTP-APIs:

- **Admin API** (`/api/*`): Backend-Operationen — Produkte, Bestellungen, Kunden, Plugins, Bulk-Verarbeitung
- **Store API** (`/store-api/*`): Kundenseitige Interaktionen — Headless-Frontends, Mobile Apps, Warenkorb, Checkout, Sales-Channel-Zugang

Offizielle Stoplight-Dokumentation:
- Admin API: https://shopware.stoplight.io/docs/admin-api/
- Store API: https://shopware.stoplight.io/docs/store-api/

Vollständige Endpunkt-Dokumentation (lokale Instanz): `/api/_info/stoplightio.html`

## Voraussetzungen

- Shopware-Instanz läuft: `http://127.0.0.1:8000`
- Admin: `http://localhost:8000/admin`
- `APP_ENV=dev` für Schema-Zugriff und bessere Fehlermeldungen

```bash
# Prüfen:
docker compose exec web printenv APP_ENV
# Falls nicht 'dev': .env.local → APP_ENV=dev → make up
```

## Schritt 1: Admin API Token (OAuth2 client_credentials)

Integration anlegen: **Admin → Settings → System → Integrations** → Toggle "Administrator" aktivieren.
- Access key ID → `client_id`
- Secret access key → `client_secret`

```bash
curl -s "http://127.0.0.1:8000/api/oauth/token" \
  -H "Content-Type: application/json" \
  -d '{
    "grant_type": "client_credentials",
    "client_id": "YOUR_ACCESS_KEY_ID",
    "client_secret": "YOUR_SECRET_ACCESS_KEY"
  }'
```

Antwort:
```json
{
  "token_type": "Bearer",
  "expires_in": 3600,
  "access_token": "..."
}
```

## Lokaler Shortcut: password grant (NUR lokal)

```bash
curl -X POST "http://localhost:8000/api/oauth/token" \
  -H "Content-Type: application/json" \
  -d '{
    "grant_type": "password",
    "client_id": "administration",
    "scopes": "write",
    "username": "admin",
    "password": "shopware"
  }'
```

Antwort enthält `access_token` (600 s) und `refresh_token`. **Nur für lokale Entwicklung** — in Integrationen immer `client_credentials` verwenden.

## Schritt 2: Authentifizierter API-Request

Bevorzuge `POST /api/search/{entity}` gegenüber `GET /api/{entity}`:
- GET: einfaches Listing ohne Filter/Sort
- POST search: vollständige Criteria (filter, sort, associations, aggregations, pagination)

```bash
curl -X POST "http://127.0.0.1:8000/api/search/product" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{}'
```

Erfolgreiche Antwort enthält Keys: `data`, `meta`, `aggregations`. Leeres `data`-Array = kein Fehler, nur keine Produkte.

## Schritt 3: OpenAPI-Schema herunterladen

**Voraussetzung: `APP_ENV=dev`**

```bash
# Admin API OpenAPI Spec
curl -X GET "http://localhost:8000/api/_info/openapi3.json" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -o openapi.json

# Entity-Schema
curl -X GET "http://localhost:8000/api/_info/open-api-schema.json" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -o entity-schema.json

# Store API
curl -s "http://127.0.0.1:8000/store-api/_info/openapi3.json" -o store-openapi.json

# Verfügbare Pfade filtern:
jq -r '.paths | keys[]' store-openapi.json | grep -E 'checkout|account|payment'
```

Schema-Endpunkte:
- OpenAPI Spec: `/(api|store-api)/_info/openapi3.json`
- Entity Schema: `/(api|store-api)/_info/open-api-schema.json`
- Stoplight UI: `/(api|store-api)/_info/stoplightio.html`

## Schritt 4: Store API

Sales Channel Access Key: Admin → **Sales Channels → Storefront (oder aktiver Channel)** → API access-Bereich.

Neuen Key generieren invalidiert den alten.

```bash
curl -s "http://127.0.0.1:8000/store-api/product" \
  -H "sw-access-key: YOUR_ACCESS_KEY"
```

Antwort mit JSON = Erfolg. Leeres `elements`-Array = kein Fehler, keine Produkte.

Store API-Domain: Falls `127.0.0.1:8000` nicht funktioniert → Admin: Sales Channels → Domains → ergänzen.

## Troubleshooting

### DB-Fehler: `Table 'shopware.system_config' doesn't exist`

```bash
docker compose exec web bin/console system:install --create-database --basic-setup
```

### HTTP 500 auf Schema-Endpunkten

`APP_ENV` muss `dev` sein. `.env.local`:
```dotenv
APP_ENV=dev
```
Dann Container neu starten: `make up` (oder `docker compose up -d`).

### Token-Request liefert keinen Output

Aus verschachtelten Shell-Sessions herausgehen und erneut versuchen.

### Store API: Produkt erscheint nicht

Checkliste:
- Produkt ist `active`
- Hat gültigen `price`
- Hat `visibilities` für den Sales Channel
- Korrekte Store API Access Key verwendet
- Storefront Sales Channel Domain entspricht lokaler URL

## Gemeinsame Konzepte beider APIs

- Gleiche Search-Criteria-Syntax (Filtering, Sorting, Pagination)
- Context-abhängige Antworten (Berechtigungen / Sales-Channel-Status)

Faustregel: Admin API = Daten verwalten. Store API = als Käufer agieren.
