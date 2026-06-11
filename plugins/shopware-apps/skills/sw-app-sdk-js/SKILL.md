---
name: sw-app-sdk-js
description: >
  Exhaustive reference for `@shopware-ag/app-server-sdk` (TypeScript, runtime-agnostic: Node 20,
  Bun, Deno, Cloudflare Workers). Use when: implementing the Shopware App registration flow
  (/authorize + /authorize/callback), verifying HMAC signatures via WebCrypto, implementing
  ShopRepositoryInterface (InMemory, DynamoDB, KV, SQLite), resolving Context from API or
  browser requests, handling lifecycle hooks (install/activate/deactivate/update/delete),
  building Admin API queries with Criteria, using response helpers (createNotificationResponse
  etc.), configuring Hono middleware, or understanding the full exported TypeScript API surface.
---

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
| `references/deep/01-overview.md` | Package metadata, runtime support, export map, bootstrap pattern |
| `references/deep/02-registration.md` | AppServer, Configuration, Registration class, full handshake flow |
| `references/deep/03-shop-repository.md` | ShopInterface, ShopRepositoryInterface, all storage adapters |
| `references/deep/04-authentication.md` | WebCryptoHmacSigner, DualSignatureVerifier, signature mechanics |
| `references/deep/05-context-resolver.md` | ContextResolver.fromAPI / fromBrowser, Context class |
| `references/deep/06-http-client.md` | HttpClient, token cache, error classes |
| `references/deep/07-hooks.md` | Hooks class, all event classes, lifecycle flow |
| `references/deep/08-helpers.md` | Criteria, admin-api helpers, app-actions, media, notification |
| `references/deep/09-integrations.md` | Hono configureAppServer, all storage integrations |
| `references/deep/10-types.md` | All exported types (BrowserAppModuleRequest, ActionButtonRequest …) |

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
