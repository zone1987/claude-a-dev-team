# JS SDK — AppServer, Configuration & Registration

## AppServer

`AppServer<Shop extends ShopInterface = ShopInterface>` — top-level wiring class.

```ts
constructor(
    public cfg: Configuration,
    public repository: ShopRepositoryInterface<Shop>,
    public httpClientTokenCache: HttpClientTokenCacheInterface = new InMemoryHttpClientTokenCache()
)
```

**Public properties:**

| Property | Type | Purpose |
|----------|------|---------|
| `cfg` | `Configuration` | App name/secret/URL/double-sig flag |
| `repository` | `ShopRepositoryInterface<Shop>` | Pluggable shop storage |
| `httpClientTokenCache` | `HttpClientTokenCacheInterface` | OAuth token cache |
| `registration` | `Registration<Shop>` | Lifecycle endpoint handlers |
| `contextResolver` | `ContextResolver<Shop>` | Context factory for incoming requests |
| `signer` | `WebCryptoHmacSigner` | Signs/verifies HMAC-SHA256 |
| `requestVerifier` | `DualSignatureVerifier<Shop>` | Multi-sig request verifier |
| `hooks` | `Hooks<Shop>` | Pub/sub lifecycle event system |

## Configuration

```ts
interface Configuration {
    appName: string;                    // Must match manifest.xml <name>
    appSecret: string;                  // App secret
    authorizeCallbackUrl: string;       // Absolute URL for Step 2 callback
    enforceDoubleSignature?: boolean;   // Default: false
}
```

## Registration

`Registration<Shop>` — handles all lifecycle HTTP endpoints. Accessed via `appServer.registration`.

### `authorize(req: Request): Promise<Response>` — Step 1

1. Validates query params: `shop-url`, `shop-id`, `timestamp` → 400 on missing.
2. Fires `onBeforeRegistrationEvent` hook (reject via `event.rejectRegistration(reason)` → 403).
3. Verifies `shopware-app-signature` header against app secret.
4. For re-registrations of confirmed shops: verifies `shopware-shop-signature` if double-sig required.
5. Creates or updates shop with pending secret + URL.
6. Returns 200 JSON: `{ proof: string, secret: string, confirmation_url: string }`.

### `authorizeCallback(req: Request): Promise<Response>` — Step 2

1. Parses JSON body: `{ shopId, apiKey, secretKey }` → 400 on missing.
2. Loads shop; verifies `shopware-shop-signature` against `pendingShopSecret`.
3. For re-registrations: rotates secrets (moves current → `previousShopSecret`, sets `secretsRotatedAt`).
4. Fires `onAuthorize` hook (reject via `event.rejectRegistration(reason)` → deletes shop, returns 403).
5. Sets credentials, clears pending, sets `registrationConfirmed`.
6. Returns 204.

### `activate(req: Request): Promise<Response>`
Resolves context via `fromAPI`, fires `onAppActivate`, sets `shopActive = true`, persists. Returns 204.

### `install(req: Request): Promise<Response>`
Fires `onAppInstall` with `appVersion` from body. Returns 204.

### `deactivate(req: Request): Promise<Response>`
Fires `onAppDeactivate`, sets `shopActive = false`, persists. Returns 204.

### `update(req: Request): Promise<Response>`
Fires `onAppUpdate` with `appVersion`. Returns 204.

### `delete(req: Request): Promise<Response>`
Fires `onAppUninstall` with `keepUserData` flag. If `event.keepUserData === false`: calls `repository.deleteShop()`. Returns 204.

## Event Classes

### BeforeRegistrationEvent

```ts
constructor(request: Request, shopId: string, shopUrl: string)
rejectRegistration(reason: string): void  // reject → 403 with reason
get reason(): string | null
```

### ShopAuthorizeEvent

```ts
constructor(request: Request, shop: Shop)
rejectRegistration(reason: string): void
get reason(): string | null
```

### AppInstallEvent / AppUpdateEvent

```ts
constructor(request: Request, shop: Shop, appVersion: string | null = null)
```

### AppActivateEvent / AppDeactivateEvent

```ts
constructor(request: Request, shop: Shop)
```

### AppUninstallEvent

```ts
constructor(request: Request, shop: Shop, keepUserData: boolean | null = null)
// Setting event.keepUserData = false triggers repository.deleteShop()
```

## randomString helper

```ts
function randomString(length = 120): string
```
Exported from `registration.ts` (not from `mod.ts`). Used internally for shop secret generation.
