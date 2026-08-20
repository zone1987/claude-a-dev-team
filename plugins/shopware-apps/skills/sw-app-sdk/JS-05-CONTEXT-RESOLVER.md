# JS SDK — ContextResolver & Context

## ContextResolver

`ContextResolver<Shop extends ShopInterface>` — resolves shop, payload, and HttpClient from an incoming `Request`.

```ts
constructor(app: AppServer<Shop>, httpClientTokenCache: HttpClientTokenCacheInterface)
```

Accessed via `appServer.contextResolver`.

### `fromAPI<Payload>(req: Request): Promise<Context<Shop, Payload>>`

For POST requests (webhooks, action buttons, payment endpoints, etc.):

1. Reads and parses JSON body.
2. Extracts `body.source.shopId`.
3. Loads shop via `repository.getShopById()` → throws `Error("Cannot find shop by id X")` if missing.
4. Calls `requestVerifier.authenticatePostRequest()` — validates `shopware-shop-signature` header.
5. Returns `Context<Shop, Payload>` with shop, parsed body as payload, and a new `HttpClient`.

```ts
const ctx = await appServer.contextResolver.fromAPI<ActionButtonRequest>(req);
const ids = (ctx.payload as ActionButtonRequest).data.ids;
const shop = ctx.shop;
await ctx.httpClient.post("/order", { ids });
```

### `fromBrowser<Payload>(req: Request): Promise<Context<Shop, Payload>>`

For GET requests from the Shopware Administration iframe (module/menu entries):

1. Reads `shop-id` from URL query params.
2. Loads shop from repository.
3. Calls `requestVerifier.authenticateGetRequest()` — validates `shopware-shop-signature` query param.
4. Returns `Context<Shop, Payload>` with shop, all query params object as payload, and a new `HttpClient`.

```ts
const ctx = await appServer.contextResolver.fromBrowser<BrowserAppModuleRequest>(req);
const lang = (ctx.payload as BrowserAppModuleRequest)["sw-user-language"];
```

## Context

Simple data container — no methods, just properties.

```ts
class Context<Shop extends ShopInterface = ShopInterface, Payload = unknown> {
    constructor(
        public shop: Shop,
        public payload: Payload,
        public httpClient: HttpClient
    )
}
```

- `shop` — the resolved `ShopInterface` instance
- `payload` — typed payload: parsed JSON body for `fromAPI`, query params object for `fromBrowser`
- `httpClient` — pre-authenticated `HttpClient` for this shop (auto-handles OAuth2)

## In Hono middleware

When using `configureAppServer`, the resolved context is available via Hono context variables:

```ts
// TypeScript-typed via ContextVariableMap augmentation:
const app   = c.get("app");      // AppServer<ShopInterface>
const shop  = c.get("shop");     // ShopInterface
const ctx   = c.get("context");  // Context<ShopInterface, unknown>
```

The type augmentation is:
```ts
declare module "hono" {
    interface ContextVariableMap {
        app: AppServer<ShopInterface>;
        shop: ShopInterface;
        context: Context<ShopInterface, unknown>;
    }
}
```

Cast payload for type safety:
```ts
import type { ActionButtonRequest } from "@shopware-ag/app-server-sdk/types";
const payload = c.get("context").payload as ActionButtonRequest;
```
