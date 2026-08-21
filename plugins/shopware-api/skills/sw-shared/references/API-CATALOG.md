# Shopware 6 — API catalogue (OpenAPI introspection)

Answers: **"which API endpoints does THIS shop have, with which parameters/schemas?"** — version-exact, including
all installed plugin routes. Source = the shop's OpenAPI spec (not static docs).

## Usage
1. Catalogues live at `.shopware-catalog/admin-api.md` and `.shopware-catalog/store-api.md`.
2. **Missing/outdated** → regenerate with `/sw-api-map` (agent `shopware-api-mapper`, haiku).
3. Look up: path/method → parameters, request body schema, response, auth → build the request.

## Source of truth (OpenAPI)
- Admin: `GET /api/_info/openapi3.json` (bearer, APP_ENV=dev).
- Store: `GET /store-api/_info/openapi3.json` (`sw-access-key`, APP_ENV=dev).
- Fallback (no running shop): the official reference repos `shopware/store-api-reference` (+ the Admin counterpart)
  or the Stoplight docs in the browser.

## When to regenerate
- After a plugin install/update (new routes), after a major upgrade (diff old/new), for new API routes of your own.

Auth/requests in detail: `sw-admin-api-auth`, `sw-store-api-auth`, `sw-admin-api-search`, `sw-api-headers`, `sw-api-errors`.
