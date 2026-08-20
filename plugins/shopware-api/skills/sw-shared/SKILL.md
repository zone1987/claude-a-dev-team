---
name: sw-shared
description: Shopware API fundamentals: headers, error format, versioning, partial loading, integrations, the endpoint catalogue. Use when the request is about Shopware API headers or errors.
---

# Shopware API fundamentals

What both APIs share. Partial loading is the single biggest lever on response size.

## Reference map

- **[API-CATALOG.md](API-CATALOG.md)**: Beantwortet: **„welche API-Endpunkte hat DIESER Shop, mit welchen Parametern/Schemas?"** — versionsgenau, inkl.
- **[API-ERRORS.md](API-ERRORS.md)**: Fehler kommen als JSON mit `errors`-Array:.
- **[API-FLOWS.md](API-FLOWS.md)**: Vollständige Abläufe als bash/curl-Sequenzen für lokale Entwicklung auf `http://127.0.0.1:8000`. [API-FLOWS-DETAIL](API-FLOWS-DETAIL.md).
- **[API-HEADERS.md](API-HEADERS.md)**: Standard-Antwortformat ist „plain" JSON; mit `Accept: application/vnd.api+json` liefert die API das JSON:API-….
- **[API-INTEGRATION.md](API-INTEGRATION.md)**: Bevorzuge `POST /api/search/{entity}` statt `GET /api/{entity}` — unterstützt filter/sort/associations. [API-INTEGRATION-DETAIL](API-INTEGRATION-DETAIL.md).
- **[API-OVERVIEW.md](API-OVERVIEW.md)**: Drei APIs mit unterschiedlichem Zweck und Auth:.
- **[API-PARTIAL-LOADING.md](API-PARTIAL-LOADING.md)**: Mit dem `fields`-Parameter werden nur die angeforderten Spalten auf **Datenbankebene** geladen. [API-PARTIAL-LOADING-PARTIAL-DATA-LOADING](API-PARTIAL-LOADING-PARTIAL-DATA-LOADING.md).
- **[API-VERSIONING.md](API-VERSIONING.md)**: Moderne Shopware-6-APIs sind **versionslos**: Basis `/api` und `/store-api`.

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) plus the Shopware 6.7 source, retrieved 2026-08-20.
