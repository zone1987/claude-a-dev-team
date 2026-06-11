# PHP SDK — Registration & AppConfiguration

## AppConfiguration

`Shopware\App\SDK\AppConfiguration` — central config value-object, passed everywhere.

```php
__construct(
    string $appName,
    string $appSecret,
    string $registrationConfirmationUrl,
    bool $enforceDoubleSignature = false  // @deprecated tag:v6.0.0 — will always be enforced
)
```

| Method | Returns | Notes |
|--------|---------|-------|
| `getAppName()` | `string` | |
| `getAppSecret()` | `string` | |
| `getRegistrationConfirmUrl()` | `string` | |
| `enforceDoubleSignature()` | `bool` | deprecated, always true in v6 |

## RegistrationService

`Shopware\App\SDK\Registration\RegistrationService` — orchestrates the two-step handshake.

```php
__construct(
    AppConfiguration $appConfiguration,
    ShopRepositoryInterface $shopRepository,
    DualSignatureRequestVerifier $dualSignatureVerifier = new DualSignatureRequestVerifier(),
    ResponseSigner $responseSigner = new ResponseSigner(),
    ShopSecretGeneratorInterface $shopSecretGeneratorInterface = new RandomStringShopSecretGenerator(),
    LoggerInterface $logger = new NullLogger(),
    ?EventDispatcherInterface $eventDispatcher = null
)
```

### Step 1 — `register(RequestInterface $request): ResponseInterface`

1. Reads `shop-id`, `shop-url`, `timestamp` from query string — throws `MissingShopParameterException` if absent.
2. Verifies `shopware-app-signature` header against app secret.
3. For re-registrations (confirmed shop): verifies `shopware-shop-signature` (current shop secret) if double-sig required.
4. Dispatches `BeforeRegistrationStartsEvent`.
5. Calls `$repo->createShopStruct()`, sets pending secret and URL, calls `createShop()` or `updateShop()`.
6. Returns 200 JSON: `{ "proof": "<HMAC>", "secret": "<pendingSecret>", "confirmation_url": "<url>" }`.

### Step 2 — `registerConfirm(RequestInterface $request): ResponseInterface`

1. Reads `shopId`, `apiKey`, `secretKey` from JSON body — throws on malformed.
2. Loads shop via `$repo->getShopFromId()`.
3. Calls `DualSignatureRequestVerifier::authenticateRegistrationConfirmation()` (verifies `shopware-shop-signature` against `pendingShopSecret`).
4. For re-registrations (already confirmed): rotates secrets — moves current → `previousShopSecret`, sets `secretsRotatedAt = now()`.
5. Dispatches `BeforeRegistrationCompletedEvent`.
6. Stores `apiKey` + `secretKey` via `$shop->setShopApiCredentials()`.
7. Clears pending fields, marks `setRegistrationConfirmed()`.
8. Dispatches `RegistrationCompletedEvent`.
9. Returns 204 No Content.

## ShopSecretGeneratorInterface

`Shopware\App\SDK\Registration\ShopSecretGeneratorInterface`

```php
interface ShopSecretGeneratorInterface {
    public function generate(): string;
}
```

`RandomStringShopSecretGenerator` (default): `bin2hex(random_bytes(64))` — 128-char hex string.

## AppLifecycle

`Shopware\App\SDK\AppLifecycle` — single entry point for all lifecycle endpoints.

```php
__construct(
    RegistrationService $registrationService,
    ShopResolver $shopResolver,
    ShopRepositoryInterface $shopRepository,
    LoggerInterface $logger = new NullLogger(),
    ?EventDispatcherInterface $eventDispatcher = null
)
```

| Method | HTTP | Returns | Events dispatched |
|--------|------|---------|-------------------|
| `register($req)` | GET | JSON 200 | `BeforeRegistrationStartsEvent`, `RegistrationCompletedEvent` (via RegistrationService) |
| `registerConfirm($req)` | POST | 204 | `BeforeRegistrationCompletedEvent` (via RegistrationService) |
| `activate($req)` | POST | 204 | `BeforeShopActivateEvent`, `ShopActivatedEvent` |
| `deactivate($req)` | POST | 204 | `BeforeShopDeactivatedEvent`, `ShopDeactivatedEvent` |
| `delete($req)` | POST | 204 | `BeforeShopDeletionEvent`, `ShopDeletedEvent` (removes shop from repository) |

## ResponseSigner

`Shopware\App\SDK\Authentication\ResponseSigner`

### `getRegistrationSignature(AppConfiguration $cfg, array $params): string`

Computes `HMAC-SHA256(shopId + shopUrl + appName, appSecret)`. Used to populate the `"proof"` field in the register response.

### `signResponse(ResponseInterface $response, ShopInterface $shop): ResponseInterface`

Adds `shopware-app-signature` header: `HMAC-SHA256(responseBody, shopSecret)`. Required for tax provider, payment, and gateway responses.
