---
name: sw-api-catalog
description: >
  Den projektspezifischen API-Katalog von Shopware nutzen — ALLE Endpunkte (Admin & Store API), Methoden, Parameter,
  Request-/Response-Schemas und Auth, gewonnen aus der OpenAPI-Spec des konkreten Shops (inkl. Plugin-Routen). Trigger:
  "welche API-Endpunkte gibt es", "API-Katalog", "alle Endpunkte Shopware", "welche Parameter hat Endpoint X",
  "request/response schema api", "openapi katalog", "api map". Shopware 6.7. Erzeuger: /sw-api-map.
---

# Shopware 6 — API-Katalog (OpenAPI-Introspektion)

Beantwortet: **„welche API-Endpunkte hat DIESER Shop, mit welchen Parametern/Schemas?"** — versionsgenau, inkl.
aller installierten Plugin-Routen. Quelle = die OpenAPI-Spec des Shops (nicht statische Doku).

## Nutzung
1. Kataloge liegen unter `.shopware-catalog/admin-api.md` und `.shopware-catalog/store-api.md`.
2. **Fehlt/veraltet** → mit `/sw-api-map` (Agent `shopware-api-mapper`, haiku) neu erzeugen.
3. Nachschlagen: Pfad/Methode → Parameter, Request-Body-Schema, Response, Auth → Request bauen.

## Quelle der Wahrheit (OpenAPI)
- Admin: `GET /api/_info/openapi3.json` (Bearer, APP_ENV=dev).
- Store: `GET /store-api/_info/openapi3.json` (`sw-access-key`, APP_ENV=dev).
- Fallback (kein laufender Shop): die offiziellen Referenz-Repos `shopware/store-api-reference` (+ Admin-Pendant)
  bzw. die Stoplight-Doku im Browser.

## Wann neu erzeugen
- Nach Plugin-Install/-Update (neue Routen), nach Major-Upgrade (Diff alt/neu), bei neuen eigenen API-Routen.

Auth/Requests im Detail: `sw-admin-api-auth`, `sw-store-api-auth`, `sw-admin-api-search`, `sw-api-headers`, `sw-api-errors`.
