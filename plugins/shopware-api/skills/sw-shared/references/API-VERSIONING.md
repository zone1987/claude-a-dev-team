# Shopware 6 — API versioning

Modern Shopware 6 APIs are **versionless**: the bases are `/api` and `/store-api` (the earlier explicit `/api/v{n}` paths
are gone). Breaking API changes follow the major release cycle (UPGRADE guides, plugin `shopware-migration`).

- Check the schema/diff via the OpenAPI endpoint (APP_ENV=dev):
  `GET /api/_info/openapi3.json` or `GET /store-api/_info/openapi3.json` (`?type=json`).
- The entity/record **version** (not the API version) is controlled via the `sw-version-id` header (`sw-api-headers`,
  `sw-entity-versioning`).
- Build your own integrations against stable `code` values (errors) and documented fields; after a major upgrade
  run an OpenAPI diff (compare the catalogue `sw-api-catalog` / `/sw-api-map` before/after).
