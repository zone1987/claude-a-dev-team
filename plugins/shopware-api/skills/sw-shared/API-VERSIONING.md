# Shopware 6 — API-Versionierung

Moderne Shopware-6-APIs sind **versionslos**: Basis `/api` und `/store-api` (frühere explizite `/api/v{n}`-Pfade
sind entfallen). Breaking Changes der API folgen dem Major-Release-Zyklus (UPGRADE-Guides, Plugin `shopware-migration`).

- Schema/Diff prüfen über den OpenAPI-Endpunkt (APP_ENV=dev):
  `GET /api/_info/openapi3.json` bzw. `GET /store-api/_info/openapi3.json` (`?type=json`).
- Entity-/Datensatz-**Version** (nicht API-Version) wird per `sw-version-id`-Header gesteuert (`sw-api-headers`,
  `sw-entity-versioning`).
- Eigene Integrationen gegen stabile `code`-Werte (Fehler) und dokumentierte Felder bauen; nach Major-Upgrade
  OpenAPI-Diff fahren (Katalog `sw-api-catalog` / `/sw-api-map` vorher/nachher vergleichen).
