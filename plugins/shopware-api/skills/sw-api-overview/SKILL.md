---
name: sw-api-overview
description: >
  Überblick über die Shopware-6-APIs: Admin API (/api), Store API (/store-api), Sync API (/api/_action/sync) —
  wofür welche, Auth-Modell je API, Base-URLs, wann welche nutzen. Trigger: "Shopware API", "welche API", "Admin API vs Store API",
  "Sync API", "API Übersicht", "base url api", "shopware rest api". Shopware 6.7.
---

# Shopware 6 — API-Überblick

Drei APIs mit unterschiedlichem Zweck und Auth:

| API | Base-URL | Zweck | Auth |
|---|---|---|---|
| **Admin API** | `/api` | volle CRUD-/Verwaltung, Integrationen, Backoffice | OAuth2 Bearer (`sw-admin-api-auth`) |
| **Store API** | `/store-api` | kundenseitig (Storefront/Headless): Katalog, Warenkorb, Checkout, Konto | `sw-access-key` (+ `sw-context-token`) (`sw-store-api-auth`) |
| **Sync API** | `/api/_action/sync` | Bulk-Schreiben vieler Entities in einem Request | Admin-OAuth (`sw-sync-api`) |

Faustregel: **Admin API** für Verwaltung/Datenpflege/Integrationen (server-to-server). **Store API** für alles
Kundenseitige (eigene Frontends, Apps). **Sync API** für effizienten Massen-Import/-Export.

- Endpunkte real abfragen/CRUD: `sw-admin-api-crud`, `sw-admin-api-search`; Store: `sw-store-api-endpoints`.
- Header/Kontext (Sprache, Währung, Version): `sw-api-headers`. Fehlerformat: `sw-api-errors`.
- **Vollständige Endpunktliste des konkreten Shops** (alle Pfade/Parameter/Schemas): Katalog via `sw-api-catalog` / `/sw-api-map`
  (liest die OpenAPI-Spec `/api/_info/openapi3.json` bzw. `/store-api/_info/openapi3.json`).
- Eigene API-Routen bauen: Plugin `shopware-framework` (`sw-store-api-route`, `sw-admin-api-controller`).
