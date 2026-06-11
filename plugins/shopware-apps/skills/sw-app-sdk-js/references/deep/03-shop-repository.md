# JS SDK — Shop Repository & ShopInterface

## ShopInterface

All implementations must provide these methods:

### Getters

| Method | Return | Notes |
|--------|--------|-------|
| `getShopId()` | `string` | |
| `getShopUrl()` | `string` | |
| `getShopSecret()` | `string` | HMAC key |
| `getPreviousShopSecret()` | `string \| null` | Valid 60s after rotation |
| `getPendingShopSecret()` | `string \| null` | |
| `getPendingShopUrl()` | `string \| null` | |
| `getSecretsRotatedAt()` | `Date \| null` | |
| `getShopClientId()` | `string \| null` | OAuth2 client ID |
| `getShopClientSecret()` | `string \| null` | |
| `getShopActive()` | `boolean` | |
| `isRegistrationConfirmed()` | `boolean` | |
| `hasVerifiedWithDoubleSignature()` | `boolean` | **@deprecated tag:v6.0.0** |

### Setters (all `void`)

| Method | Param |
|--------|-------|
| `setShopUrl(url)` | `string` |
| `setShopSecret(secret)` | `string` |
| `setPreviousShopSecret(secret)` | `string \| null` |
| `setPendingShopSecret(secret)` | `string \| null` |
| `setPendingShopUrl(url)` | `string \| null` |
| `setSecretsRotatedAt(date)` | `Date \| null` |
| `setShopCredentials(clientId, clientSecret)` | both `string` |
| `setShopActive(active)` | `boolean` |
| `setRegistrationConfirmed()` | — |
| `setVerifiedWithDoubleSignature()` | — **@deprecated** |

## ShopRepositoryInterface

```ts
interface ShopRepositoryInterface<Shop extends ShopInterface = ShopInterface> {
    createShop(id: string, url: string, secret: string): Promise<void>;
    getShopById(id: string): Promise<Shop | null>;
    updateShop(shop: Shop): Promise<void>;
    deleteShop(id: string): Promise<void>;
}
```

Unlike the PHP SDK, there is no `createShopStruct` factory method — `createShop` takes raw strings and constructs + persists in one step.

## SimpleShop

Reference in-memory implementation of `ShopInterface`.

```ts
constructor(
    shopId: string,
    shopUrl: string,
    shopSecret: string,
    registrationConfirmed = false
)
```

Stores all state as private fields. Initializes `shopActive = false`, all optional fields to `null`.

## InMemoryShopRepository

```ts
constructor()  // empty Map<string, SimpleShop>
```

Full `ShopRepositoryInterface<SimpleShop>` implementation backed by a `Map`. Intended for development/testing.

## Storage Adapters

All implement `ShopRepositoryInterface<SimpleShop>`.

### CloudflareShopRepository

```ts
import { CloudflareShopRepository } from "@shopware-ag/app-server-sdk/integration/cloudflare-kv";
constructor(storage: KVNamespace)
```

Uses 3 KV keys per shop: `{id}`, `{id}_active`, `{id}_credentials`. `secretsRotatedAt` stored as Unix ms.

### CloudflareHttpClientTokenCache

```ts
import { CloudflareHttpClientTokenCache } from "@shopware-ag/app-server-sdk/integration/cloudflare-kv";
constructor(storage: KVNamespace)
```

Key: `token_{shopId}`. Implements `HttpClientTokenCacheInterface`.

### DenoKVRepository

```ts
import { DenoKVRepository } from "@shopware-ag/app-server-sdk/integration/deno-kv";
constructor(namespace = "shops")
```

Uses `Deno.openKv()`. Stores entire `SimpleShop` object as value. Namespace = key prefix.

### DynamoDBRepository

```ts
import { DynamoDBRepository } from "@shopware-ag/app-server-sdk/integration/dynamodb";
constructor(client: DynamoDBClient, tableName: string)
```

Wraps `DynamoDBDocumentClient.from(client)`. Table attributes: `id`, `active`, `url`, `secret`, `clientId`, `clientSecret`, `pendingShopUrl`, `pendingShopSecret`, `previousShopSecret`, `secretsRotatedAt` (Unix ms), `verifiedWithDoubleSignature`, `registrationConfirmed`.

### BunSqliteRepository

```ts
import { BunSqliteRepository } from "@shopware-ag/app-server-sdk/integration/bun-sqlite";
constructor(fileName: string)
```

Opens/creates SQLite via `bun:sqlite`. WAL mode enabled. Auto-creates `shop` table.

**Table schema:** `id TEXT PK`, `active BOOLEAN DEFAULT 1`, `url TEXT`, `secret TEXT`, `client_id TEXT NULL`, `client_secret TEXT NULL`, `pending_shop_url TEXT NULL`, `pending_shop_secret TEXT NULL`, `previous_shop_secret TEXT NULL`, `secrets_rotated_at INTEGER NULL`, `verified_with_double_signatures BOOLEAN DEFAULT 0`, `registration_confirmed BOOLEAN DEFAULT 0`

### BetterSqlite3Repository

```ts
import { BetterSqlite3Repository } from "@shopware-ag/app-server-sdk/integration/better-sqlite3";
constructor(fileName: string)
```

Uses `better-sqlite3` (Node.js synchronous SQLite). Same table schema as `BunSqliteRepository`. All methods return `Promise<void>` despite using synchronous underlying API.

## Custom Repository Pattern

```ts
import { ShopInterface, ShopRepositoryInterface, SimpleShop } from "@shopware-ag/app-server-sdk";
import { Redis } from "ioredis";

class RedisShopRepository implements ShopRepositoryInterface<SimpleShop> {
    constructor(private redis: Redis) {}

    async createShop(id: string, url: string, secret: string): Promise<void> {
        const shop = new SimpleShop(id, url, secret);
        await this.redis.set(`shop:${id}`, JSON.stringify(this.serialize(shop)));
    }

    async getShopById(id: string): Promise<SimpleShop | null> {
        const raw = await this.redis.get(`shop:${id}`);
        if (!raw) return null;
        const data = JSON.parse(raw);
        const shop = new SimpleShop(data.id, data.url, data.secret, data.confirmed);
        if (data.clientId) shop.setShopCredentials(data.clientId, data.clientSecret);
        shop.setShopActive(data.active);
        return shop;
    }

    async updateShop(shop: SimpleShop): Promise<void> {
        await this.redis.set(`shop:${shop.getShopId()}`, JSON.stringify(this.serialize(shop)));
    }

    async deleteShop(id: string): Promise<void> {
        await this.redis.del(`shop:${id}`);
    }

    private serialize(shop: SimpleShop) {
        return {
            id: shop.getShopId(), url: shop.getShopUrl(), secret: shop.getShopSecret(),
            clientId: shop.getShopClientId(), clientSecret: shop.getShopClientSecret(),
            active: shop.getShopActive(), confirmed: shop.isRegistrationConfirmed(),
            pendingSecret: shop.getPendingShopSecret(), pendingUrl: shop.getPendingShopUrl(),
            previousSecret: shop.getPreviousShopSecret(),
            rotatedAt: shop.getSecretsRotatedAt()?.getTime() ?? null,
        };
    }
}
```
