# sw-app-sdk-js — Shopware App JS/TS SDK Reference

## When to Apply

- Setting up an app server in TypeScript (Node/Bun/Deno/Cloudflare Workers)
- Implementing `/app/register` + `/app/register/confirm` endpoints
- Validating `shopware-shop-signature` HMAC with WebCrypto
- Storing shops via InMemoryShopRepository, DynamoDB, Cloudflare KV, Deno KV, or SQLite
- Resolving `Context` (shop + payload + HttpClient) from POST/GET requests
- Using `HttpClient` to query the Shopware Admin API with OAuth2 auto-refresh
- Building type-safe `Criteria` for Admin API searches
- Using `createNotificationResponse`, `createNewTabResponse`, `createModalResponse`
- Wiring lifecycle hooks: onAuthorize / onAppInstall / onAppActivate / onAppDeactivate / onAppUpdate / onAppUninstall
- Setting up Hono integration with `configureAppServer`
- Uploading media files or sending admin notifications programmatically

## Reference Files

| File | Content |
|------|---------|
| `JS-01-OVERVIEW.md` | Package metadata, runtime support, export map, bootstrap pattern |
| `JS-02-REGISTRATION.md` | AppServer, Configuration, Registration class, full handshake flow |
| `JS-03-SHOP-REPOSITORY.md` | ShopInterface, ShopRepositoryInterface, all storage adapters |
| `JS-04-AUTHENTICATION.md` | WebCryptoHmacSigner, DualSignatureVerifier, signature mechanics |
| `JS-05-CONTEXT-RESOLVER.md` | ContextResolver.fromAPI / fromBrowser, Context class |
| `JS-06-HTTP-CLIENT.md` | HttpClient, token cache, error classes |
| `JS-07-HOOKS.md` | Hooks class, all event classes, lifecycle flow |
| `JS-08-HELPERS.md` | Criteria, admin-api helpers, app-actions, media, notification |
| `JS-09-INTEGRATIONS.md` | Hono configureAppServer, all storage integrations |
| `JS-10-TYPES.md` | All exported types (BrowserAppModuleRequest, ActionButtonRequest …) |

## Quick Bootstrap (Hono + Bun)

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

// Custom webhook handler
app.post("/app/webhook/order-placed", async (c) => {
    const ctx = c.get("context");   // Context<SimpleShop, { source, data, meta }>
    const shop = c.get("shop");
    // use ctx.httpClient to call shop API
    return c.json({ success: true });
});

export default app;
```
