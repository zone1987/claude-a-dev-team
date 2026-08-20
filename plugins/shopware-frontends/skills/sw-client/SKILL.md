---
name: sw-client
description: Shopware Frontends client: @shopware/api-client, api-gen types, composables, session and context tokens. Use when the request names the Shopware api-client, api-gen or a composable.
---

# Shopware Frontends API client

The data layer. api-gen turns the shop's OpenAPI into types, so the client is typed against your actual shop.

## Reference map

- **[API-CLIENT-JS.md](API-CLIENT-JS.md)**: Typed client against the **Store API**. [API-CLIENT-JS-API-CLIENT-REFERENCE](API-CLIENT-JS-API-CLIENT-REFERENCE.md).
- **[API-GEN-TYPES.md](API-GEN-TYPES.md)**: Generates TypeScript types from the shop's OpenAPI spec — the basis of the `api-client`'s type safety. [API-GEN-TYPES-API-GEN-REFERENCE](API-GEN-TYPES-API-GEN-REFERENCE.md).
- **[COMPOSABLES.md](COMPOSABLES.md)**: Opinionated Vue composables that encapsulate business logic + state on top of the `api-client`. [COMPOSABLES-REFERENCE](COMPOSABLES-REFERENCE.md).
- **[FRONTENDS-HELPERS.md](FRONTENDS-HELPERS.md)**: Pure utility functions for recurring tasks in headless frontends:. [FRONTENDS-HELPERS-HELPERS-REFERENCE](FRONTENDS-HELPERS-HELPERS-REFERENCE.md).
- **[FRONTENDS-SESSION-CONTEXT.md](FRONTENDS-SESSION-CONTEXT.md)**: The `sw-context-token` represents the session. [FRONTENDS-SESSION-CONTEXT-SESSION-CONTEXT-REFERENCE](FRONTENDS-SESSION-CONTEXT-SESSION-CONTEXT-REFERENCE.md).

## Source

Distilled from [frontends.shopware.com](https://frontends.shopware.com) and the shopware/frontends repository, retrieved 2026-08-20.
