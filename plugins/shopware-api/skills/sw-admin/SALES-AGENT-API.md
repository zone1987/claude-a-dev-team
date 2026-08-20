# Shopware 6 — Sales Agent API (Commercial)

**SwagSalesAgent** is a commercial extension: sales agents are managed in the Administration, get customers
assigned to them and can act in their context (quotes/orders). The extension ships its own API endpoints
(in addition to the Admin/Store API).

- Only available when the Commercial/Sales Agent extension is installed.
- Authentication follows the respective context (admin OAuth for management; Sales-Agent-specific auth/token
  for the agent app) — the exact scheme depends on the installed version.
- **Authoritative, complete endpoint list**: the installed extension exposes its routes in the OpenAPI spec —
  capture it via the API catalogue (`sw-api-catalog` / `/sw-api-map`); the official reference lives at
  `shopware.stoplight.io/docs/swag-sales-agent` (JS docs, in the browser).

For standard sales processes use the Store API (`sw-store-api-endpoints`); Sales Agent only with the B2B extension installed.
