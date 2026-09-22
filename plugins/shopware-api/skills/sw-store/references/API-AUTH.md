# Shopware 6 — Store API auth & context

> **Credentials come from `shopware/.env.local`, never hard-coded.**
> `SHOPWARE_ADMIN_USERNAME`, `SHOPWARE_ADMIN_PASSWORD`, `SHOPWARE_ACCESS_KEY_ID`,
> `SHOPWARE_SECRET_ACCESS_KEY`. They are never printed to a console, never committed, and
> never written into documentation — a default pair in an example is the pair somebody
> copies into a shop that is reachable from the internet.

The Store API is customer-facing and uses **no OAuth tokens**, but headers instead.

- **`sw-access-key`** (required): the access key of the sales channel (Admin → sales channel → API access). Identifies the channel.
- **`sw-context-token`** (stateful): identifies the current context (cart, logged-in customer,
  chosen currency/language). Returned by the server (header/body) and **sent along** on follow-up requests.

```bash
# first request: the access key is enough; the server may return an sw-context-token
curl "$BASE/store-api/context" -H "sw-access-key: $KEY"

# login: the token is returned in the response header and reused afterwards
curl -X POST "$BASE/store-api/account/login" -H "sw-access-key: $KEY" -H "Content-Type: application/json" \
     -d '{ "username": "customer@example.com", "password": "..." }'   # -> sw-context-token
```

Keep the `sw-context-token` constant across the whole session/cart journey. Language/currency via the context
or headers (`sw-api-headers`). Endpoints: `sw-store-api-endpoints`.
