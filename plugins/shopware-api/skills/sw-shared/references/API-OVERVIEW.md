# Shopware 6 — API overview

Three APIs with different purposes and auth:

| API | Base URL | Purpose | Auth |
|---|---|---|---|
| **Admin API** | `/api` | full CRUD/administration, integrations, back office | OAuth2 bearer (`sw-admin-api-auth`) |
| **Store API** | `/store-api` | customer-facing (storefront/headless): catalogue, cart, checkout, account | `sw-access-key` (+ `sw-context-token`) (`sw-store-api-auth`) |
| **Sync API** | `/api/_action/sync` | bulk-writing many entities in one request | admin OAuth (`sw-sync-api`) |

Rule of thumb: **Admin API** for administration/data maintenance/integrations (server-to-server). **Store API** for everything
customer-facing (your own frontends, apps). **Sync API** for efficient mass import/export.

- Query endpoints live/CRUD: `sw-admin-api-crud`, `sw-admin-api-search`; store: `sw-store-api-endpoints`.
- Headers/context (language, currency, version): `sw-api-headers`. Error format: `sw-api-errors`.
- **Complete endpoint list of the specific shop** (all paths/parameters/schemas): catalogue via `sw-api-catalog` / `/sw-api-map`
  (reads the OpenAPI spec `/api/_info/openapi3.json` or `/store-api/_info/openapi3.json`).
- Build your own API routes: plugin `shopware-framework` (`sw-store-api-route`, `sw-admin-api-controller`).
