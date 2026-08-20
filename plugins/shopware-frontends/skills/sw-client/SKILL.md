---
name: sw-client
description: Shopware Frontends client: @shopware/api-client, api-gen types, composables, session and context tokens. Use when the request names the Shopware api-client, api-gen or a composable.
---

# Shopware Frontends API client

The data layer. api-gen turns the shop's OpenAPI into types, so the client is typed against your actual shop.

## Reference map

- **[API-CLIENT-JS.md](API-CLIENT-JS.md)**: Typisierter Client gegen die **Store API**. [API-CLIENT-JS-API-CLIENT-REFERENCE](API-CLIENT-JS-API-CLIENT-REFERENCE.md).
- **[API-GEN-TYPES.md](API-GEN-TYPES.md)**: Generiert TypeScript-Typen aus der OpenAPI-Spec des Shops — Grundlage der Typsicherheit des `api-client`. [API-GEN-TYPES-API-GEN-REFERENCE](API-GEN-TYPES-API-GEN-REFERENCE.md).
- **[COMPOSABLES.md](COMPOSABLES.md)**: Opinionierte Vue-Composables, die Geschäftslogik + State über dem `api-client` kapseln. [COMPOSABLES-REFERENCE](COMPOSABLES-REFERENCE.md).
- **[FRONTENDS-HELPERS.md](FRONTENDS-HELPERS.md)**: Reine Utility-Funktionen für wiederkehrende Aufgaben in headless Frontends:. [FRONTENDS-HELPERS-HELPERS-REFERENCE](FRONTENDS-HELPERS-HELPERS-REFERENCE.md).
- **[FRONTENDS-SESSION-CONTEXT.md](FRONTENDS-SESSION-CONTEXT.md)**: Der `sw-context-token` repräsentiert die Session. [FRONTENDS-SESSION-CONTEXT-SESSION-CONTEXT-REFERENCE](FRONTENDS-SESSION-CONTEXT-SESSION-CONTEXT-REFERENCE.md).

## Source

Distilled from [frontends.shopware.com](https://frontends.shopware.com) and the shopware/frontends repository, retrieved 2026-08-20.
