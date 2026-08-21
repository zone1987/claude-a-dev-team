---
name: sw-shared
description: Shopware API fundamentals: headers, error format, versioning, partial loading, integrations, the endpoint catalogue. Use when the request is about Shopware API headers or errors.
---

# Shopware API fundamentals

What both APIs share. Partial loading is the single biggest lever on response size.

## Reference map

- **[API-CATALOG.md](references/API-CATALOG.md)**: Answers: **"which API endpoints does THIS shop have, with which parameters/schemas?"** — version-exact, incl.
- **[API-ERRORS.md](references/API-ERRORS.md)**: Errors arrive as JSON with an `errors` array:.
- **[API-FLOWS.md](references/API-FLOWS.md)**: Complete walkthroughs as bash/curl sequences for local development on `http://127.0.0.1:8000`. [API-FLOWS-DETAIL](references/API-FLOWS-DETAIL.md).
- **[API-HEADERS.md](references/API-HEADERS.md)**: The default response format is "plain" JSON; with `Accept: application/vnd.api+json` the API returns the JSON:API….
- **[API-INTEGRATION.md](references/API-INTEGRATION.md)**: Prefer `POST /api/search/{entity}` over `GET /api/{entity}` — it supports filter/sort/associations. [API-INTEGRATION-DETAIL](references/API-INTEGRATION-DETAIL.md).
- **[API-OVERVIEW.md](references/API-OVERVIEW.md)**: Three APIs with different purposes and auth:.
- **[API-PARTIAL-LOADING.md](references/API-PARTIAL-LOADING.md)**: With the `fields` parameter only the requested columns are loaded at **database level**. [API-PARTIAL-LOADING-PARTIAL-DATA-LOADING](references/API-PARTIAL-LOADING-PARTIAL-DATA-LOADING.md).
- **[API-VERSIONING.md](references/API-VERSIONING.md)**: Modern Shopware 6 APIs are **versionless**: the bases are `/api` and `/store-api`.

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) plus the Shopware 6.7 source, retrieved 2026-08-20.
