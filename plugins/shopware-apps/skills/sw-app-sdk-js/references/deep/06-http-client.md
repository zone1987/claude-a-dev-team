# JS SDK — HttpClient & Token Cache

## HttpClient

Fetch-based client pre-configured for a specific shop. Handles OAuth2 client credentials token acquisition, caching, and automatic 401 retry.

```ts
constructor(
    private shop: ShopInterface,
    private tokenCache: HttpClientTokenCacheInterface = new InMemoryHttpClientTokenCache(),
    private defaultTimeout: number = 0  // 0 = no timeout
)
```

All requests are prefixed with `shop.getShopUrl() + "/api"`.

### Methods

All return `Promise<HttpClientResponse<ResponseType>>`.

```ts
get<T>(url: string, headers?: Record<string,string>, options?: { timeout?: number })
post<T>(url: string, json?: object | FormData | Blob, headers?, options?)
put<T>(url: string, json?: object, headers?, options?)
patch<T>(url: string, json?: object, headers?, options?)
delete<T>(url: string, json?: object, headers?, options?)
```

**`post` body handling:**
- `object` (not Blob/FormData) → serialized to JSON, `content-type: application/json` set
- `FormData` or `Blob` → sent as-is, no content-type override

**`put`/`patch`/`delete`** always serialize to JSON.

### Automatic behaviors

- `Authorization: Bearer {token}` injected automatically (via `getToken()`)
- `redirect: "manual"` — 301/302 throws `ApiClientRequestFailed`
- **401 retry:** clears token cache entry, fetches new token, retries once
- **204:** returns `{} as ResponseType`
- **Timeout:** uses `AbortSignal.timeout(ms)` — per-request `timeout` option overrides `defaultTimeout`

### `getToken(): Promise<string>`

1. Checks `tokenCache.getToken(shopId)`.
2. If valid (not expired): returns cached token.
3. Otherwise: `POST {shopUrl}/api/oauth/token` with `grant_type: client_credentials`, `client_id`, `client_secret`.
4. Throws `ApiClientAuthenticationFailed` on non-200.
5. Throws `ApiClientRequestFailed` on 301 redirect.
6. Caches result and returns token.

## HttpClientResponse

```ts
class HttpClientResponse<ResponseType> {
    constructor(
        public statusCode: number,
        public body: ResponseType,
        public headers: Headers
    )
}
```

## Error Classes

### ApiClientAuthenticationFailed extends Error

```ts
constructor(shopId: string, response: HttpClientResponse<string>)
// Message: "The api client authentication to shop with id: {shopId} with response: {body}"
response: HttpClientResponse<string>  // public property
```

Thrown when OAuth2 token fetch (`/api/oauth/token`) returns non-200.

### ApiClientRequestFailed extends Error

```ts
constructor(shopId: string, response: HttpClientResponse<ShopwareErrorResponse>)
// Message: comma-joined detail values from errors[] + shop ID
response: HttpClientResponse<ShopwareErrorResponse>  // public property
```

Thrown when an API request returns non-2xx status (after retry).

`ShopwareErrorResponse` shape: `{ errors: Array<{ detail: string }> }`

## Token Cache

### HttpClientTokenCacheInterface

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

### InMemoryHttpClientTokenCache

```ts
constructor()  // private Record<string, HttpClientTokenCacheItem>
```

Default implementation. No persistence — tokens lost on restart. Suitable for development and single-instance deployments.

### CloudflareHttpClientTokenCache

```ts
import { CloudflareHttpClientTokenCache } from "@shopware-ag/app-server-sdk/integration/cloudflare-kv";
constructor(storage: KVNamespace)
```

Stores tokens in Cloudflare KV under key `token_{shopId}`. `expiresIn` stored as ISO string.

### Custom token cache (e.g. Redis)

```ts
import type { HttpClientTokenCacheInterface, HttpClientTokenCacheItem } from "@shopware-ag/app-server-sdk";

class RedisTokenCache implements HttpClientTokenCacheInterface {
    constructor(private redis: Redis) {}

    async getToken(shopId: string): Promise<HttpClientTokenCacheItem | null> {
        const raw = await this.redis.get(`token:${shopId}`);
        if (!raw) return null;
        const d = JSON.parse(raw);
        return { token: d.token, expiresIn: new Date(d.expiresIn) };
    }

    async setToken(shopId: string, item: HttpClientTokenCacheItem): Promise<void> {
        const ttl = Math.floor((item.expiresIn.getTime() - Date.now()) / 1000);
        await this.redis.setex(`token:${shopId}`, ttl, JSON.stringify({
            token: item.token, expiresIn: item.expiresIn.toISOString()
        }));
    }

    async clearToken(shopId: string): Promise<void> {
        await this.redis.del(`token:${shopId}`);
    }
}
```
