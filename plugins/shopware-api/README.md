# shopware-api

> Die drei Shopware-APIs (Admin/Store/Sync) zum Konsumieren & Integrieren.

`shopware-api` macht die **drei Shopware-APIs** zum Konsumieren und Integrieren beherrschbar — als Gegenstück zum
*Erstellen* eigener Routen (das liegt in `shopware-framework`).

- **Admin API** (`/api`): OAuth2 (`/api/oauth/token`, `client_credentials`/`password`), Bearer-Token, generisches
  **CRUD** je Entity, der **Such-Endpunkt** `/api/search/{entity}` mit Criteria-JSON, sowie alle **`_action`-
  Endpunkte** (Order-State-Transitions, Cache, Number-Range, Dokumente, Mail …).
- **Store API** (`/store-api`): Auth über `sw-access-key` und der zustandsbehaftete `sw-context-token`; die
  wichtigsten Endpunkt-Gruppen (Kontext, Katalog/Listing, Warenkorb, Checkout, Konto, Methoden) — inkl. einer
  **vollständigen 110-Operationen-Referenz** aus der offiziellen OpenAPI.
- **Sync API** (`/api/_action/sync`): Bulk-Operationen.

Dazu: alle relevanten **HTTP-Header** (Sprache/Währung/Version/Inheritance), das **Fehlerformat** (stabile
`code`s) und **Versionierung**. Die **OpenAPI-Introspektion** (`/sw-api-map`, Agent `shopware-api-mapper`) zieht aus
`/_info/openapi3.json` den **vollständigen Endpunkt-Katalog des konkreten Shops** (inkl. Plugin-Routen). Spezialist:
**`shopware-api-expert`**. **Wann nutzen:** für Integrationen, Headless-Datenzugriff und API-Debugging.

Teil des Marketplace **[claude-a-dev-team](../../README.md)**. Das Wissen ist aus den offiziellen Quellen destilliert und eingebettet; Skills laden ihre Tiefe progressiv aus `references/`.

## Installation

```
/plugin marketplace add https://github.com/zone1987/claude-a-dev-team
/plugin install shopware-api@claude-a-dev-team
```

## Skills (17)

| Skill | Beschreibung |
|---|---|
| `sw-api-overview` | Überblick über die Shopware-6-APIs: Admin API (/api), Store API (/store-api), Sync API (/api/_action/sync) — wofür welche, Auth-Modell je API, Base-URLs, wann welche nutzen |
| `sw-admin-api-actions` | Die _action-Endpunkte der Shopware-6 Admin API (nicht-CRUD-Operationen): Order-State-Transitions (/api/_action/order/{id}/state/{transition}), Cache (/api/_action/cache, index), Number-Range, Document-Erzeugung, Mail send, Clone |
| `sw-admin-api-auth` | Authentifizierung an der Shopware-6 Admin API: OAuth2 token endpoint /api/oauth/token, grant_type client_credentials (Integration: client_id/client_secret) und password (client_id 'administration', dev), Bearer-Token, expires_in 600s, refre |
| `sw-admin-api-crud` | CRUD über die Shopware-6 Admin API: GET/POST/PATCH/DELETE /api/{entity}[/{id}], Payload-Format, Hex-UUID-IDs, Associations im Payload, Response-Codes (204) |
| `sw-admin-api-endpoints` | Vollständige Endpunkt-Referenz der Shopware 6 Admin API (adminapi.json, v6.7) |
| `sw-admin-api-search` | Der Such-Endpunkt der Shopware-6 Admin API: POST /api/search/{entity} mit Criteria-JSON (filter, sort, associations, aggregations, page, limit, total-count-mode, ids, term, post-filter, grouping) |
| `sw-api-catalog` | Den projektspezifischen API-Katalog von Shopware nutzen — ALLE Endpunkte (Admin & Store API), Methoden, Parameter, Request-/Response-Schemas und Auth, gewonnen aus der OpenAPI-Spec des konkreten Shops (inkl |
| `sw-api-errors` | Fehlerformat & Status-Codes der Shopware-6-APIs: JSON:API errors-Array (status, code, title, detail, source.pointer), typische HTTP-Codes (400/401/403/404/412/500), Validierungsfehler, Domain-Exception-Codes |
| `sw-api-flows` | Shopware 6 API End-to-End-Flows: Produkt anlegen (Admin API) → Store API lesen → Warenkorb → Kunde registrieren → Bestellung aufgeben → Zahlung |
| `sw-api-headers` | Wichtige HTTP-Header der Shopware-6-APIs: Authorization Bearer, sw-access-key, sw-context-token, sw-language-id, sw-currency-id, sw-version-id, sw-inheritance, sw-include-seo-urls, Content-Type/Accept (JSON vs JSON:API) |
| `sw-api-integration` | Shopware 6 API Integration-Einstieg: OAuth2 client_credentials, password-grant (lokal), erster Request, OpenAPI-Schema herunterladen, Store API access-key ermitteln, häufige Fehler (DB nicht initialisiert, falsche URL, leere data-Arrays) |
| `sw-api-partial-loading` | Shopware 6 Partial Data Loading — `fields`-Parameter in der API limitiert Datenbankabfrage auf benötigte Felder (Unterschied zu `includes`: DB-Level vs |
| `sw-api-versioning` | API-Versionierung & Kompatibilität in Shopware 6: aktuelle versionslose Basis /api & /store-api, frühere /api/v{n}, OpenAPI-Schema-Endpunkt, Umgang mit Breaking Changes über Major-Versionen |
| `sw-sales-agent-api` | Die Shopware Commercial "Sales Agent" (SwagSalesAgent) API: B2B-Vertriebs-Extension, in der Sales-Agents zugewiesene Kunden verwalten/in deren Namen bestellen |
| `sw-store-api-auth` | Authentifizierung/Kontext der Shopware-6 Store API: sw-access-key (Sales-Channel-Access-Key) als Pflicht-Header, sw-context-token (Kontext-/Warenkorb-/Login-Token) Lebenszyklus, Kunden-Login |
| `sw-store-api-endpoints` | Die wichtigsten Store-API-Endpunkte in Shopware 6: context, product, product-listing, search, navigation/category, cart (checkout/cart), checkout/order, account (login/register/customer), payment-/shipping-method |
| `sw-sync-api` | Die Shopware-6 Sync API für Massen-Schreibvorgänge: POST /api/_action/sync, Operationen (entity, action upsert/delete, payload-Array), single-operation Header, fail-on-error, indexing-behavior/skip-indexer Header |

## Agents (2)

| Agent | Beschreibung |
|---|---|
| `shopware-api-expert` | Spezialist für die Shopware-6.7-APIs: Admin API (OAuth), Store API (sw-access-key/sw-context-token), Sync API |
| `shopware-api-mapper` | Introspektions-Agent: gewinnt die vollständige API-Endpunktliste eines Shopware-6-Projekts aus der OpenAPI-Spec (Admin + Store, inkl |

## Commands (1)

| Command | Beschreibung |
|---|---|
| `/sw-api-map` | Gewinnt die vollständige API-Endpunktliste eines Shopware-Projekts aus der OpenAPI-Spec (Admin + Store, inkl |
