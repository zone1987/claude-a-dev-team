# JS SDK — Overview & Architecture

## Package

| Key | Value |
|-----|-------|
| NPM name | `@shopware-ag/app-server-sdk` |
| Build tool | `tshy` (dual CJS/ESM) |
| Main entry | `./dist/commonjs/mod.js` / `./dist/esm/mod.js` |
| Test runner | `bun test` |
| License | MIT |

## Runtime Support

| Runtime | Requirement | Notes |
|---------|-------------|-------|
| Node.js | 20+ | Web Crypto API available natively |
| Bun | Any current | Full support + `bun-sqlite` integration |
| Deno | Any current | `deno-kv` integration available |
| Cloudflare Workers | Any | `cloudflare-kv` integration available |

Key: uses **Web Crypto API** (`crypto.subtle`) and **standard `fetch`** — no Node-specific APIs.

## Export Map

| Import path | Purpose |
|-------------|---------|
| `@shopware-ag/app-server-sdk` | Main: `AppServer`, repos, `HttpClient`, events, `Context` |
| `.../helper/admin-api` | `EntityRepository`, `ApiContext`, `SyncService`, `Defaults` |
| `.../helper/criteria` | `Criteria` builder, `TotalCountMode`, `SingleFilter` |
| `.../helper/app-actions` | `createNotificationResponse`, `createNewTabResponse`, `createModalResponse` |
| `.../helper/media` | `uploadMediaFile`, `uploadMediaByUrl`, folder helpers |
| `.../helper/notification` | `sendNotification` |
| `.../integration/hono` | `configureAppServer` |
| `.../integration/cloudflare-kv` | `CloudflareShopRepository`, `CloudflareHttpClientTokenCache` |
| `.../integration/deno-kv` | `DenoKVRepository` |
| `.../integration/dynamodb` | `DynamoDBRepository` |
| `.../integration/bun-sqlite` | `BunSqliteRepository` |
| `.../integration/better-sqlite3` | `BetterSqlite3Repository` |
| `.../types` | `BrowserAppModuleRequest`, `Source`, `Meta`, `ActionButtonRequest`, `EntityWrittenRequest` |

## All Symbols from Main Entry

**Classes:** `AppServer`, `InMemoryShopRepository`, `SimpleShop`, `HttpClient`, `HttpClientResponse`, `ApiClientAuthenticationFailed`, `ApiClientRequestFailed`, `InMemoryHttpClientTokenCache`, `DualSignatureVerifier`, `Context`, `ShopAuthorizeEvent`, `AppInstallEvent`, `AppActivateEvent`, `AppDeactivateEvent`, `AppUpdateEvent`, `AppUninstallEvent`, `BeforeRegistrationEvent`

**Interfaces/Types:** `Configuration`, `ShopInterface`, `ShopRepositoryInterface`, `HttpClientTokenCacheInterface`

## Quick Bootstrap (Bun + Hono)

```ts
import { AppServer, InMemoryShopRepository } from "@shopware-ag/app-server-sdk";
import { configureAppServer } from "@shopware-ag/app-server-sdk/integration/hono";
import { Hono } from "hono";

const app = new Hono();
configureAppServer(app, {
    appName: "MyApp",
    appSecret: "my-secret",
    shopRepository: new InMemoryShopRepository(),
    authorizeCallbackUrl: "https://app.example.com/app/register/confirm",
});

app.post("/app/webhook/order-placed", async (c) => {
    const ctx  = c.get("context");  // Context<SimpleShop, { source, data, meta }>
    const shop = c.get("shop");
    const products = await ctx.httpClient.get("/product");
    return c.json({ ok: true });
});

export default app;
```

## Manual Bootstrap (any runtime)

```ts
import { AppServer, InMemoryShopRepository } from "@shopware-ag/app-server-sdk";

const appServer = new AppServer(
    { appName: "MyApp", appSecret: "secret", authorizeCallbackUrl: "https://app.example.com/app/register/confirm" },
    new InMemoryShopRepository()
);

// Route dispatcher
async function handler(req: Request): Promise<Response> {
    const url = new URL(req.url);
    switch (url.pathname) {
        case "/app/register":          return appServer.registration.authorize(req);
        case "/app/register/confirm":  return appServer.registration.authorizeCallback(req);
        case "/app/activate":          return appServer.registration.activate(req);
        case "/app/deactivate":        return appServer.registration.deactivate(req);
        case "/app/delete":            return appServer.registration.delete(req);
    }
    // Custom handler
    const ctx = await appServer.contextResolver.fromAPI(req);
    // ... handle webhook/action
    return new Response(null, { status: 204 });
}
```
