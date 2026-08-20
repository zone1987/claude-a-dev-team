---
name: sw-store
description: Shopware Store API: sw-access-key and sw-context-token authentication, the endpoint catalogue. Use when the request names the Shopware Store API, sw-access-key or sw-context-token.
---

# Shopware Store API

The customer-facing API. Two headers carry identity: the access key names the sales channel, the context token the session.

## Reference map

- **[API-AUTH.md](API-AUTH.md)**: Die Store API ist kundenseitig und nutzt **keine OAuth-Tokens**, sondern Header.
- **[API-ENDPOINTS.md](API-ENDPOINTS.md)**: Base `/store-api`, Header `sw-access-key`. [API-ENDPOINTS-DETAIL](API-ENDPOINTS-DETAIL.md).

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) plus the Shopware 6.7 source, retrieved 2026-08-20.
