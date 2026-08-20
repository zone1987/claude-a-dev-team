# Shopware 6 — API headers & context

| Header | Effect |
|---|---|
| `Authorization: Bearer {token}` | Admin API auth (`sw-admin-api-auth`) |
| `sw-access-key` | Store API: sales channel access (`sw-store-api-auth`) |
| `sw-context-token` | Store API: context/cart/login state |
| `Content-Type: application/json` | JSON body |
| `Accept: application/json` | plain JSON; `application/vnd.api+json` = **JSON:API** (with `included`/`relationships`) |
| `sw-language-id` | language of the request (translations) |
| `sw-currency-id` | currency |
| `sw-version-id` | entity version (e.g. order draft, `sw-entity-versioning`) |
| `sw-inheritance` | `1` = resolve inherited values (variants/parent) |

The default response format is "plain" JSON (`data`/`total`); with `Accept: application/vnd.api+json` the API returns the
JSON:API format. Error format: `sw-api-errors`. Search/Criteria: `sw-admin-api-search`.
