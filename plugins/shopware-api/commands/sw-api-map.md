---
name: sw-api-map
description: Derives the complete API endpoint list of a Shopware 6 project from its OpenAPI spec and writes cached Store API and Admin API catalogues.
argument-hint: [--store-only] [--admin-only]
allowed-tools: Read, Glob, Grep, Bash, Write, Task
model: haiku
---

# /sw-api-map

Create or refresh the API catalogues. Delegate to the `shopware-api-mapper` agent (skill
`sw-shared`).

## Steps
1. Obtain the OpenAPI spec, in this order: a local spec file in the project, then the running shop
   (`/store-api/_info/openapi3.json` with `sw-access-key`; `/api/_info/openapi3.json` with a bearer
   token and `APP_ENV=dev`), then a local reference repository (`storeapi.json`, `adminapi.json`).
2. Parse the spec with python3 or jq rather than reading it whole: `info.version`, `servers`,
   `securitySchemes`, and per `paths.<p>.<m>` the tag, summary, parameters, body and responses.
3. Write `.shopware-catalog/store-api.md` and `.shopware-catalog/admin-api.md`, grouped by tag, with
   the auth requirement per endpoint. `--store-only` and `--admin-only` narrow this.
4. Head each file with the source, API version, server and counts; print a short summary.

Where no spec is reachable, say so and point at the static list (`sw-store`). Never invent an
endpoint.
