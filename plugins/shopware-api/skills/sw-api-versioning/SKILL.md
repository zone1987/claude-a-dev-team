---
name: sw-api-versioning
description: >
  API-Versionierung & Kompatibilität in Shopware 6: aktuelle versionslose Basis /api & /store-api, frühere /api/v{n},
  OpenAPI-Schema-Endpunkt, Umgang mit Breaking Changes über Major-Versionen. Trigger: "API Version", "/api/v3",
  "api versionless", "openapi3.json", "API breaking change", "api kompatibilität shopware". Shopware 6.7.
---

# Shopware 6 — API-Versionierung

Moderne Shopware-6-APIs sind **versionslos**: Basis `/api` und `/store-api` (frühere explizite `/api/v{n}`-Pfade
sind entfallen). Breaking Changes der API folgen dem Major-Release-Zyklus (UPGRADE-Guides, Plugin `shopware-migration`).

- Schema/Diff prüfen über den OpenAPI-Endpunkt (APP_ENV=dev):
  `GET /api/_info/openapi3.json` bzw. `GET /store-api/_info/openapi3.json` (`?type=json`).
- Entity-/Datensatz-**Version** (nicht API-Version) wird per `sw-version-id`-Header gesteuert (`sw-api-headers`,
  `sw-entity-versioning`).
- Eigene Integrationen gegen stabile `code`-Werte (Fehler) und dokumentierte Felder bauen; nach Major-Upgrade
  OpenAPI-Diff fahren (Katalog `sw-api-catalog` / `/sw-api-map` vorher/nachher vergleichen).
