# PHP SDK — Shop Repository & ShopInterface

## ShopInterface

`Shopware\App\SDK\Shop\ShopInterface` — contract for a persisted shop entity. All setters return `ShopInterface` (fluent).

### Getters

| Method | Return | Notes |
|--------|--------|-------|
| `getShopId()` | `string` | |
| `getShopUrl()` | `string` | |
| `getPendingShopUrl()` | `?string` | Set during re-registration |
| `getShopSecret()` | `string` | HMAC key for signature verification |
| `getPreviousShopSecret()` | `?string` | Valid for 60 s after rotation |
| `getPendingShopSecret()` | `?string` | Set during registration step 1 |
| `getSecretsRotatedAt()` | `?\DateTimeImmutable` | Timestamp of last secret rotation |
| `getShopClientId()` | `?string` | OAuth2 client ID (set after confirm) |
| `getShopClientSecret()` | `?string` | OAuth2 client secret |
| `isShopActive()` | `bool` | |
| `isRegistrationConfirmed()` | `bool` | `true` after first registerConfirm |
| `hasVerifiedWithDoubleSignature()` | `bool` | **@deprecated tag:v6.0.0** |

### Setters (all return `self`)

| Method | Param | When called |
|--------|-------|-------------|
| `setShopUrl(string)` | new URL | URL change |
| `setPendingShopUrl(?string)` | temp URL | re-registration start |
| `setShopSecret(string)` | new secret | after rotation confirmed |
| `setPendingShopSecret(?string)` | temp secret | registration step 1 |
| `setPreviousShopSecret(string)` | old secret | during rotation |
| `setSecretsRotatedAt(\DateTimeImmutable)` | rotation time | during rotation |
| `setShopApiCredentials(string $clientId, string $clientSecret)` | — | after registerConfirm |
| `setShopActive(bool)` | — | activate/deactivate |
| `setRegistrationConfirmed()` | — | after first registerConfirm |
| `setVerifiedWithDoubleSignature()` | — | **@deprecated tag:v6.0.0** |

## ShopRepositoryInterface

`Shopware\App\SDK\Shop\ShopRepositoryInterface<T of ShopInterface>`

```php
interface ShopRepositoryInterface {
    public function createShopStruct(string $shopId, string $shopUrl, string $shopSecret): ShopInterface;
    public function createShop(ShopInterface $shop): void;
    public function getShopFromId(string $shopId): ShopInterface|null;
    public function updateShop(ShopInterface $shop): void;
    public function deleteShop(string $shopId): void;
}
```

`createShopStruct` is a factory — it creates an unsaved struct in memory (not yet persisted).

### Minimal MySQL implementation example

```php
class MysqlShopRepository implements ShopRepositoryInterface {
    public function __construct(private \PDO $pdo) {}

    public function createShopStruct(string $shopId, string $shopUrl, string $shopSecret): ShopInterface {
        return new MyShop($shopId, $shopUrl, $shopSecret);
    }

    public function createShop(ShopInterface $shop): void {
        $stmt = $this->pdo->prepare('INSERT INTO shops (id, url, secret) VALUES (?, ?, ?)');
        $stmt->execute([$shop->getShopId(), $shop->getShopUrl(), $shop->getShopSecret()]);
    }

    public function getShopFromId(string $shopId): ?ShopInterface {
        $stmt = $this->pdo->prepare('SELECT * FROM shops WHERE id = ?');
        $stmt->execute([$shopId]);
        $row = $stmt->fetch(\PDO::FETCH_ASSOC);
        return $row ? MyShop::fromRow($row) : null;
    }

    public function updateShop(ShopInterface $shop): void {
        $stmt = $this->pdo->prepare('UPDATE shops SET url=?, secret=?, client_id=?, client_secret=?, active=? WHERE id=?');
        $stmt->execute([
            $shop->getShopUrl(), $shop->getShopSecret(),
            $shop->getShopClientId(), $shop->getShopClientSecret(),
            $shop->isShopActive() ? 1 : 0, $shop->getShopId()
        ]);
    }

    public function deleteShop(string $shopId): void {
        $this->pdo->prepare('DELETE FROM shops WHERE id = ?')->execute([$shopId]);
    }
}
```

## ShopResolver

`Shopware\App\SDK\Shop\ShopResolver` — resolves + authenticates a shop from any PSR-7 request.

```php
__construct(
    ShopRepositoryInterface $shopRepository,
    DualSignatureRequestVerifier $requestVerifier = new DualSignatureRequestVerifier()
)
```

`resolveShop(RequestInterface $request): ShopInterface`

Resolution strategy (auto-detected):
1. Header `shopware-app-shop-id` present → read JWT from `shopware-app-token` header (storefront path)
2. `Content-Type: application/json` → read `source.shopId` from JSON body
3. Otherwise → read `shop-id` query param

All paths verify the signature before returning. Throws:
- `ShopNotFoundException` — shop not in repository
- `SignatureInvalidException` — HMAC/JWT invalid
- `MissingShopParameterException` — required params absent
- `\JsonException` — malformed JSON body

## DynamoDB Adapter

`Shopware\App\SDK\Adapter\DynamoDB\DynamoDBRepository` implements `ShopRepositoryInterface<DynamoDBShop>`.

```php
__construct(DynamoDbClient $client, string $tableName)
```

**DynamoDB table attributes:**

| Attribute | Type | Notes |
|-----------|------|-------|
| `id` | S (PK) | shopId |
| `active` | BOOL | |
| `confirmed` | BOOL | registrationConfirmed |
| `url` | S | |
| `secret` | S | |
| `clientId` | S | |
| `clientSecret` | S | |
| `pendingShopSecret` | S | |
| `pendingShopUrl` | S | |
| `previousShopSecret` | S | |
| `secretsRotatedAt` | S | Unix timestamp string |
| `hasVerifiedWithDoubleSignature` | BOOL | @deprecated |

## Test Helpers

`Shopware\App\SDK\Test\MockShop` — in-memory `ShopInterface`. Same fields as `DynamoDBShop`.

`Shopware\App\SDK\Test\MockShopRepository` — in-memory `ShopRepositoryInterface`. Public `$shops` array.

```php
$repo = new MockShopRepository();
$shop = $repo->createShopStruct('shop-123', 'https://myshop.example.com', 'secret');
$repo->createShop($shop);
```
