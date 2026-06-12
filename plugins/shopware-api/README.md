# shopware-api

**Wofür:** Die drei Shopware-APIs: Admin API (OAuth), Store API, Sync API — Auth, Endpunkte, Requests/Responses, Header, Fehler, Versionierung — plus OpenAPI-Introspektion (Endpunkt-Katalog des konkreten Shops).

Teil des Marketplace **[claude-a-dev-team](../../README.md)**. Wissen ist aus der Shopware-/OCTO-Quelle destilliert; Skills laden Tiefe progressiv aus `references/`.

## Installation (Claude Code)

```
/plugin marketplace add zone1987/claude-a-dev-team
/plugin install shopware-api@claude-a-dev-team
```

## Skills (17)

`sw-api-overview`, `sw-admin-api-actions`, `sw-admin-api-auth`, `sw-admin-api-crud`, `sw-admin-api-endpoints`, `sw-admin-api-search`, `sw-api-catalog`, `sw-api-errors`, `sw-api-flows`, `sw-api-headers`, `sw-api-integration`, `sw-api-partial-loading`, `sw-api-versioning`, `sw-sales-agent-api`, `sw-store-api-auth`, `sw-store-api-endpoints`, `sw-sync-api`

## Agents (2)

- **`shopware-api-expert`** — Spezialist für die Shopware-6.7-APIs: Admin API (OAuth), Store API (sw-access-key/sw-context-token), Sync API.
- **`shopware-api-mapper`** — Introspektions-Agent: gewinnt die vollständige API-Endpunktliste eines Shopware-6-Projekts aus der OpenAPI-Spec (Admin + Store, inkl.

## Commands (1)

- **`/sw-api-map`** — Gewinnt die vollständige API-Endpunktliste eines Shopware-Projekts aus der OpenAPI-Spec (Admin + Store, inkl.
