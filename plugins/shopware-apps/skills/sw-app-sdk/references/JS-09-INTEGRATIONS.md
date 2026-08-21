# JS SDK — Integrations (Hono, Storage Adapters)

## Hono Integration

`import { configureAppServer } from "@shopware-ag/app-server-sdk/integration/hono"`

`configureAppServer(hono: Hono, cfg: MiddlewareConfig): void`

Single call that registers all routes and middleware on the Hono app.

### MiddlewareConfig (discriminated union)

**Option A — provide existing AppServer instance:**

```ts
configureAppServer(app, {
    appServer: existingAppServer,
    // MiddlewareConfigBase fields optional
});
```

**Option B — provide factory params (AppServer created internally):**

```ts
configureAppServer(app, {
    appName: "MyApp",                                    // or (c) => c.env.APP_NAME
    appSecret: "secret",                                 // or (c) => c.env.APP_SECRET
    shopRepository: new BunSqliteRepository("shops.db"), // or (c) => new ...
    httpClientTokenCache: new InMemoryHttpClientTokenCache(), // optional
    authorizeCallbackUrl: "https://app.example.com/app/register/confirm",
    enforceDoubleSignature: false,
    setup(app) { /* hook registration */ },
});
```

Functions for `appName`, `appSecret`, `shopRepository`, `httpClientTokenCache` receive the Hono context — useful for Cloudflare Workers environment bindings.

### MiddlewareConfigBase defaults

| Field | Default |
|-------|---------|
| `appUrl` | Auto-detected from request origin |
| `registrationUrl` | `/app/register` |
| `registerConfirmationUrl` | `/app/register/confirm` |
| `appInstallUrl` | `/app/install` |
| `appActivateUrl` | `/app/activate` |
| `appUpdateUrl` | `/app/update` |
| `appDeactivateUrl` | `/app/deactivate` |
| `appDeleteUrl` | `/app/delete` |
| `appPath` | `/app/*` |
| `appIframeEnable` | `false` |
| `appIframePath` | `/client-api/*` |
| `appIframeRedirects` | `{}` |

### Registered routes

| Method | Path | Handler |
|--------|------|---------|
| GET | `{registrationUrl}` | `registration.authorize()` |
| POST | `{registerConfirmationUrl}` | `registration.authorizeCallback()` |
| POST | `{appInstallUrl}` | `registration.install()` |
| POST | `{appActivateUrl}` | `registration.activate()` |
| POST | `{appUpdateUrl}` | `registration.update()` |
| POST | `{appDeactivateUrl}` | `registration.deactivate()` |
| POST | `{appDeleteUrl}` | `registration.delete()` |

### appPath middleware (for custom handlers)

For all routes matching `appPath` (default `/app/*`) that are NOT lifecycle endpoints:

- GET → `contextResolver.fromBrowser()` → sets `c.var.shop` + `c.var.context`
- POST → `contextResolver.fromAPI()` → sets `c.var.shop` + `c.var.context`
- After handler: signs response with `shopware-app-signature` header

### Iframe mode (`appIframeEnable: true`)

```ts
configureAppServer(app, {
    // ...
    appIframeEnable: true,
    appIframePath: "/client-api/*",
    appIframeRedirects: {
        "/app/module": "/client-api/dashboard",  // sets signed cookie, redirects
    },
});
```

The signed cookie format: `shop={shopId}.{hmac}` with `SameSite=None; Secure; Partitioned`.
The `appIframePath` middleware validates this cookie for subsequent iframe requests.

### Environment variable

`SHOPWARE_APP_SDK_FORCE_HTTPS` — forces HTTPS in auto-derived `appUrl`. Useful behind reverse proxies/ingress that strip TLS.

### Cloudflare Workers example

```ts
import { Hono } from "hono";
import { configureAppServer } from "@shopware-ag/app-server-sdk/integration/hono";
import { CloudflareShopRepository, CloudflareHttpClientTokenCache } from "@shopware-ag/app-server-sdk/integration/cloudflare-kv";

type Env = { KV: KVNamespace };
const app = new Hono<{ Bindings: Env }>();

configureAppServer(app, {
    appName: (c) => "MyApp",
    appSecret: (c) => "my-secret",
    shopRepository: (c) => new CloudflareShopRepository(c.env.KV),
    httpClientTokenCache: (c) => new CloudflareHttpClientTokenCache(c.env.KV),
    authorizeCallbackUrl: "https://my-app.workers.dev/app/register/confirm",
});

app.post("/app/webhook/order-placed", async (c) => {
    const ctx = c.get("context");
    // process ctx.payload, call ctx.httpClient
    return new Response(null, { status: 204 });
});

export default app;
```

## Storage Adapters — Comparison

| Adapter | Import | Runtime | Persistence | Use case |
|---------|--------|---------|-------------|----------|
| `InMemoryShopRepository` | main | All | None | Dev/testing |
| `BunSqliteRepository` | `./integration/bun-sqlite` | Bun | SQLite file | Single-instance Bun apps |
| `BetterSqlite3Repository` | `./integration/better-sqlite3` | Node.js | SQLite file | Single-instance Node apps |
| `DynamoDBRepository` | `./integration/dynamodb` | Node/Bun/etc | AWS DynamoDB | Multi-instance, serverless |
| `CloudflareShopRepository` | `./integration/cloudflare-kv` | CF Workers | Cloudflare KV | Cloudflare Workers |
| `DenoKVRepository` | `./integration/deno-kv` | Deno | Deno KV | Deno Deploy |
