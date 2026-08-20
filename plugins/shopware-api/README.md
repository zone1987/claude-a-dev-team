# shopware-api

> The three Shopware APIs (Admin/Store/Sync) for consuming and integrating.

`shopware-api` makes the **three Shopware APIs** manageable for consuming and integrating — as the counterpart to
*creating* custom routes (which lives in `shopware-framework`).

- **Admin API** (`/api`): OAuth2 (`/api/oauth/token`, `client_credentials`/`password`), bearer token, generic
  **CRUD** per entity, the **search endpoint** `/api/search/{entity}` with Criteria JSON, and all
  **`_action` endpoints** (order state transitions, cache, number range, documents, mail, ...).
- **Store API** (`/store-api`): auth via `sw-access-key` and the stateful `sw-context-token`; the most important
  endpoint groups (context, catalogue/listing, cart, checkout, account, methods) — including a
  **complete 110-operation reference** from the official OpenAPI.
- **Sync API** (`/api/_action/sync`): bulk operations.

In addition: all relevant **HTTP headers** (language/currency/version/inheritance), the **error format** (stable
`code`s) and **versioning**. The **OpenAPI introspection** (`/sw-api-map`, agent `shopware-api-mapper`) pulls the
**complete endpoint catalogue of the concrete shop** (including plugin routes) from `/_info/openapi3.json`.
Specialist: **`shopware-api-expert`**. **When to use:** for integrations, headless data access and API debugging.

Part of the **[claude-a-dev-team](../../README.md)** marketplace. The knowledge is distilled from the official
sources and embedded; depth sits in flat reference files beside each SKILL.md, loaded on demand.

## Installation

```
/plugin marketplace add https://github.com/zone1987/claude-a-dev-team
/plugin install shopware-api@claude-a-dev-team
```

## Skills (3)

| Skill | Description |
|---|---|
| `sw-admin` | Shopware Admin API: OAuth authentication, CRUD, search with Criteria, actions, the endpoint catalogue, the Sync API, the Sales Agent API. Use when the request names the Shopware Admin API or Sync API |
| `sw-shared` | Shopware API fundamentals: headers, error format, versioning, partial loading, integrations, the endpoint catalogue. Use when the request is about Shopware API headers or errors |
| `sw-store` | Shopware Store API: sw-access-key and sw-context-token authentication, the endpoint catalogue. Use when the request names the Shopware Store API, sw-access-key or sw-context-token |

## Agents (2)

| Agent | Description |
|---|---|
| `shopware-api-expert` | Specialist for the Shopware 6.7 APIs: Admin API (OAuth), Store API (sw-access-key/sw-context-token), Sync API |
| `shopware-api-mapper` | Introspection agent: derives the complete API endpoint list of a Shopware 6 project from the OpenAPI spec (Admin + Store, incl |

## Commands (1)

| Command | Description |
|---|---|
| `/sw-api-map` | Derives the complete API endpoint list of a Shopware project from the OpenAPI spec (Admin + Store, incl |
