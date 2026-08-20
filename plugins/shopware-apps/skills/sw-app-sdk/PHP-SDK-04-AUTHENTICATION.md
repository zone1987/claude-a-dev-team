# PHP SDK — Authentication & Signature Verification

## RequestVerifier

`Shopware\App\SDK\Authentication\RequestVerifier`

Low-level HMAC-SHA256 and JWT verifier. All methods throw `SignatureInvalidException` or `SignatureNotFoundException` on failure.

**Public constant:** `SHOPWARE_SHOP_SIGNATURE_HEADER = 'shopware-shop-signature'`

```php
__construct(ClockInterface $clock = new SystemClock(UTC))
```

| Method | Signature | What it verifies |
|--------|-----------|-----------------|
| `authenticateRegistrationRequest` | `(RequestInterface $req, string $appSecret): void` | `shopware-app-signature` header against HMAC of query params |
| `authenticateRegistrationRequestWithShopSignature` | `(RequestInterface $req, string $shopSecret): void` | `shopware-shop-signature` header (double-sig step) |
| `authenticatePostRequest` | `(RequestInterface $req, string $secret, string $header = SHOPWARE_SHOP_SIGNATURE_HEADER): void` | HMAC of raw request body |
| `authenticateGetRequest` | `(RequestInterface $req, string $secret): void` | HMAC in `shopware-shop-signature` query param |
| `authenticateStorefrontRequest` | `(RequestInterface $req, string $shopId, string $secret): void` | JWT in `shopware-app-token` header via `lcobucci/jwt` |

### HMAC message construction

**Registration (GET):** sorted query params string without `shopware-app-signature`.

**POST body:** raw body string (read from stream, rewound after).

**GET (module/admin):** all query params except `shopware-shop-signature`, sorted, concatenated as `key=value` pairs joined by `&`.

**Storefront JWT:** `lcobucci/jwt` validates `sub = "{shopId}"` claim, `aud`, and HS256 signature with `shopSecret`.

## DualSignatureRequestVerifier

`Shopware\App\SDK\Authentication\DualSignatureRequestVerifier`

Wraps `RequestVerifier` with:
- **Secret rotation fallback:** if current secret fails, retries with `previousShopSecret` within 60-second window after `secretsRotatedAt`
- **Double-signature logic:** verifies both app secret and shop secret headers when re-registrations require it

**Constants (private):** `INFLIGHT_ALLOWANCE = 60`, `SHOPWARE_SHOP_SIGNATURE_PREVIOUS_HEADER = 'shopware-shop-signature-previous'`

```php
__construct(
    RequestVerifier $primaryVerifier = new RequestVerifier(),
    ?ClockInterface $clock = null
)
```

| Method | Purpose |
|--------|---------|
| `authenticatePostRequest(RequestInterface, ShopInterface): void` | POST signature with rotation fallback |
| `authenticateGetRequest(RequestInterface, ShopInterface): void` | GET signature with rotation fallback |
| `authenticateStorefrontRequest(RequestInterface, string $shopId, ShopInterface): void` | JWT with rotation fallback |
| `authenticateRegistrationConfirmation(RequestInterface, ShopInterface, AppConfiguration): void` | Verifies `shopware-shop-signature` against `pendingShopSecret`; if already confirmed + double-sig: also verifies `shopware-shop-signature-previous` against current secret |
| `authenticateRegistrationRequest(RequestInterface, AppConfiguration, ?ShopInterface): void` | Verifies `shopware-app-signature` with app secret; for confirmed shops with double-sig: also verifies `shopware-shop-signature` with current shop secret |

### Secret rotation fallback logic

```
1. Try current shopSecret → if OK: return
2. If $shop->getPreviousShopSecret() === null: rethrow
3. If $shop->getSecretsRotatedAt() === null: rethrow
4. If now() - secretsRotatedAt > 60s: rethrow
5. Try previousShopSecret → if OK: return; else rethrow original
```

## ResponseSigner

`Shopware\App\SDK\Authentication\ResponseSigner`

### `signResponse(ResponseInterface $response, ShopInterface $shop): ResponseInterface`

Computes `HMAC-SHA256(responseBody, shopSecret)`, sets `shopware-app-signature` header.

**Required for:** Tax provider responses, Payment responses, Gateway (Checkout/Context) responses.

```php
$response = $signer->signResponse(
    new JsonResponse(['status' => 'paid']),
    $shop
);
```

### `getRegistrationSignature(AppConfiguration $cfg, array $params): string`

`$params` must contain `'shop-id'` and `'shop-url'` keys.
Returns `HMAC-SHA256(shopId + shopUrl + appName, appSecret)`.
