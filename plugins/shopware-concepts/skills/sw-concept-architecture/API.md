# Shopware APIs — Konzept

Vollständige Konzept-Doku: `API-DETAIL.md`

## Kurzüberblick

Shopware stellt **zwei funktionale APIs** bereit:

| | Store API | Admin API |
|---|---|---|
| Zweck | Kundenseitige Interaktionen | Administrative/Backend-Operationen |
| Auth | Öffentlich + Context-Header | OAuth 2.0 |
| Pfad | `/store-api/` | `/api/` |
| Einsatz | Storefront, Headless-Frontend, SPAs | Backend-Integrationen, Sync, Automatisierung |

## Gemeinsame Muster

- JSON-Payloads (HTTP)
- Search Criteria Abstraktion (Filter, Sorting, Pagination)
- Header-basiertes kontextuelles Verhalten

## Store API Besonderheit

Normalisierter Interface-Layer zwischen Frontend und Shopware-Core. Storefront und Headless-Clients
nutzen **dieselben Store-API-Routen** — keine doppelte Business-Logik.

Technische Umsetzung: `shopware-api`, `shopware-framework` (Dev-Plugins)
