---
name: sw-admin
description: Shopware Admin API: OAuth authentication, CRUD, search with Criteria, actions, the endpoint catalogue, the Sync API, the Sales Agent API. Use when the request names the Shopware Admin API or Sync API.
---

# Shopware Admin API

The Admin API is OAuth-authenticated and covers every entity. The Sync API batches writes across entities in one request.

## Reference map

- **[API-ACTIONS.md](API-ACTIONS.md)**: Operationen, die kein reines CRUD sind, liegen unter `/api/_action/...`.
- **[API-AUTH.md](API-AUTH.md)**: Token holen an `POST /api/oauth/token`, dann `Authorization: Bearer {access_token}` an allen Admin-API-Reques….
- **[API-CRUD.md](API-CRUD.md)**: Generisches Schema je DAL-Entity:.
- **[API-ENDPOINTS.md](API-ENDPOINTS.md)**: Security-Scheme: `oAuth`. [API-ENDPOINTS-DETAIL](API-ENDPOINTS-DETAIL.md).
- **[API-SEARCH.md](API-SEARCH.md)**: Für echte Abfragen `POST /api/search/{entity}` mit Criteria-JSON.
- **[SALES-AGENT-API.md](SALES-AGENT-API.md)**: Für Standard-Verkaufsprozesse die Store API; Sales-Agent nur bei installierter B2B-Extension.
- **[SYNC-API.md](SYNC-API.md)**: Mehrere Schreiboperationen über verschiedene Entities in **einem** Request — effizient für Import/Sync.

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) plus the Shopware 6.7 source, retrieved 2026-08-20.
