---
name: sw-admin
description: Shopware Admin API: OAuth authentication, CRUD, search with Criteria, actions, the endpoint catalogue, the Sync API, the Sales Agent API. Use when the request names the Shopware Admin API or Sync API.
---

# Shopware Admin API

The Admin API is OAuth-authenticated and covers every entity. The Sync API batches writes across entities in one request.

## Reference map

- **[API-ACTIONS.md](API-ACTIONS.md)**: Operations that are not plain CRUD live under `/api/_action/...`.
- **[API-AUTH.md](API-AUTH.md)**: Fetch a token at `POST /api/oauth/token`, then send `Authorization: Bearer {access_token}` on all Admin API reques….
- **[API-CRUD.md](API-CRUD.md)**: Generic schema per DAL entity:.
- **[API-ENDPOINTS.md](API-ENDPOINTS.md)**: Security scheme: `oAuth`. [API-ENDPOINTS-DETAIL](API-ENDPOINTS-DETAIL.md).
- **[API-SEARCH.md](API-SEARCH.md)**: For real queries use `POST /api/search/{entity}` with Criteria JSON.
- **[SALES-AGENT-API.md](SALES-AGENT-API.md)**: For standard sales processes use the Store API; Sales Agent only with the B2B extension installed.
- **[SYNC-API.md](SYNC-API.md)**: Several write operations across different entities in **one** request — efficient for import/sync.

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) plus the Shopware 6.7 source, retrieved 2026-08-20.
