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

`sw-api-overview`, `sw-admin-api-actions`, `sw-admin-api-auth`, `sw-admin-api-crud`, `sw-admin-api-endpoints`, `sw-admin-api-search`, `sw-api-catalog`, `sw-api-errors`, `sw-api-flows`, `sw-api-headers`, `sw-api-integration`, `sw-api-partial-loading`, `sw-api-versioning`, `sw-sales-agent-api`, `sw-store-api-auth`, `sw-store-api-endpoints`, `sw-sync-api`

## Agents (2)

- **`shopware-api-expert`** — Spezialist für die Shopware-6.7-APIs: Admin API (OAuth), Store API (sw-access-key/sw-context-token), Sync API.
- **`shopware-api-mapper`** — Introspektions-Agent: gewinnt die vollständige API-Endpunktliste eines Shopware-6-Projekts aus der OpenAPI-Spec (Admin + Store, inkl.

## Commands (1)

- **`/sw-api-map`** — Gewinnt die vollständige API-Endpunktliste eines Shopware-Projekts aus der OpenAPI-Spec (Admin + Store, inkl.
