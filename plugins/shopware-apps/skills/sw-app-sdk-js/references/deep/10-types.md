# JS SDK — Types Reference

`import type { ... } from "@shopware-ag/app-server-sdk/types"`

## BrowserAppModuleRequest

Query params sent by Shopware Administration when loading an App Module iframe.

```ts
type BrowserAppModuleRequest = {
    "shop-id": string;
    "shop-url": string;
    timestamp: string;
    "sw-version": string;
    "sw-context-language": string;  // language UUID
    "sw-user-language": string;     // BCP 47, e.g. "en-GB"
}
```

Used with `contextResolver.fromBrowser<BrowserAppModuleRequest>(req)`.

## Source

Present in all webhook/API POST request bodies.

```ts
type Source = {
    url: string;        // shop URL
    shopId: string;     // shop ID
    appVersion: string; // installed app version
}
```

## Meta

Present in webhook request bodies.

```ts
type Meta = {
    timestamp: number;   // Unix timestamp (ms)
    reference: string;   // webhook reference ID
    language: string;    // language ID
}
```

## ActionButtonRequest

Body payload for action button webhooks from the Shopware Administration.

```ts
type ActionButtonRequest = {
    source: Source;
    data: {
        ids: string[];      // selected entity IDs
        entity: string;     // e.g. "order"
        action: string;     // action name from manifest
    };
    meta: Meta;
}
```

## EntityWrittenRequest

Body payload for `entity.written` webhooks.

```ts
type EntityWrittenRequest<PrimaryKey = string> = {
    data: {
        event: string;      // e.g. "order.written"
        payload: {
            entity: string;
            operation: string;      // "insert" | "update" | "delete"
            primaryKey: PrimaryKey;
            updatedFields: string[];
            versionId: string;
        }[];
    };
}
```

## Usage Examples

```ts
import type {
    BrowserAppModuleRequest,
    ActionButtonRequest,
    EntityWrittenRequest,
    Source,
    Meta,
} from "@shopware-ag/app-server-sdk/types";

// In a Hono action button handler
app.post("/app/action/create-invoice", async (c) => {
    const ctx = c.get("context");
    const payload = ctx.payload as ActionButtonRequest;

    const orderIds = payload.data.ids;
    const entity   = payload.data.entity;  // "order"

    for (const orderId of orderIds) {
        await createInvoice(ctx.httpClient, orderId);
    }

    return createNotificationResponse("success", `Invoices created for ${orderIds.length} orders`);
});

// In a module iframe handler
app.get("/app/module/dashboard", async (c) => {
    const ctx = c.get("context");
    const query = ctx.payload as BrowserAppModuleRequest;
    const language = query["sw-user-language"]; // e.g. "de-DE"
    // ...
});

// In an entity.written webhook handler
app.post("/app/webhook/order-written", async (c) => {
    const ctx = c.get("context");
    const body = ctx.payload as EntityWrittenRequest;

    for (const event of body.data.payload) {
        if (event.operation === "insert") {
            await handleNewOrder(event.primaryKey);
        }
    }

    return new Response(null, { status: 204 });
});
```

## Configuration interface (from main entry)

```ts
interface Configuration {
    appName: string;
    appSecret: string;
    authorizeCallbackUrl: string;
    enforceDoubleSignature?: boolean;  // default false; will always be true in v6
}
```

## ShopInterface (from main entry)

All methods documented in `03-shop-repository.md`. Key points:
- `setVerifiedWithDoubleSignature()` and `hasVerifiedWithDoubleSignature()` are **@deprecated tag:v6.0.0**
- `isRegistrationConfirmed()` is `false` until `authorizeCallback()` completes Step 2
- `getPreviousShopSecret()` + `getSecretsRotatedAt()` enable the 60-second rotation fallback window

## HttpClientTokenCacheInterface (from main entry)

```ts
interface HttpClientTokenCacheInterface {
    getToken(shopId: string): Promise<HttpClientTokenCacheItem | null>;
    setToken(shopId: string, token: HttpClientTokenCacheItem): Promise<void>;
    clearToken(shopId: string): Promise<void>;
}

interface HttpClientTokenCacheItem {
    token: string;
    expiresIn: Date;
}
```
