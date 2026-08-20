# PHP SDK — ContextResolver

`Shopware\App\SDK\Context\ContextResolver` — deserialises incoming PSR-7 requests into typed PHP structs.

```php
__construct(?InAppPurchaseProvider $inAppPurchaseProvider = null)
```

All methods throw `MalformedWebhookBodyException` on unparseable body, `SignatureInvalidException` on bad signature.

## Method Reference

| Method | Returns | Source |
|--------|---------|--------|
| `assembleWebhook($req, $shop)` | `WebhookAction` | POST body JSON |
| `assembleActionButton($req, $shop)` | `ActionButtonAction` | POST body JSON |
| `assembleModule($req, $shop)` | `ModuleAction` | GET query params |
| `assembleTaxProvider($req, $shop)` | `TaxProviderAction` | POST body JSON |
| `assemblePaymentPay($req, $shop)` | `PaymentPayAction` | POST body JSON |
| `assemblePaymentFinalize($req, $shop)` | `PaymentFinalizeAction` | POST body JSON |
| `assemblePaymentCapture($req, $shop)` | `PaymentCaptureAction` | POST body JSON |
| `assemblePaymentRecurringCapture($req, $shop)` | `PaymentRecurringAction` | POST body JSON |
| `assemblePaymentValidate($req, $shop)` | `PaymentValidateAction` | POST body JSON |
| `assemblePaymentRefund($req, $shop)` | `RefundAction` | POST body JSON |
| `assembleStorefrontRequest($req, $shop)` | `StorefrontAction` | GET + JWT header |
| `assembleCheckoutGatewayRequest($req, $shop)` | `CheckoutGatewayAction` | POST body JSON |
| `assembleContextGatewayRequest($req, $shop)` | `ContextGatewayAction` | POST body JSON |
| `assembleInAppPurchasesFilterRequest($req, $shop)` | `FilterAction` | POST body JSON |

## Module query param keys

`assembleModule` reads from query string:
- `sw-version` → `shopwareVersion: string`
- `sw-context-language` → `contentLanguage: string` (UUID)
- `sw-user-language` → `userLanguage: string` (BCP 47, e.g. `en-GB`)
- `in-app-purchases` (optional, JWT-signed string from SBP)

## PaymentFinalize compatibility note

Shopware 6.7 sends `requestData`; Shopware 6.6 sends `queryParameters`. The SDK reads either key:

```php
$action = $resolver->assemblePaymentFinalize($request, $shop);
$params = $action->queryParameters; // @deprecated tag:v5.0.0 — rename to requestData when on 6.7+
```

## Storefront request flow

`assembleStorefrontRequest` reads the JWT from the `shopware-app-token` header, decodes the payload using `lcobucci/jwt` with `shopSecret`, and optionally decodes in-app purchases from the `inAppPurchases` claim via `InAppPurchaseProvider`.

```php
$storefront = $resolver->assembleStorefrontRequest($request, $shop);
$customerId = $storefront->claims->getCustomerId(); // throws MissingClaimException if absent
```

## StorefrontClaims methods

All throw `MissingClaimException` if the JWT claim is missing:

| Method | Returns |
|--------|---------|
| `getSalesChannelId()` | `string` |
| `getCustomerId()` | `string` |
| `getCurrencyId()` | `string` |
| `getLanguageId()` | `string` |
| `getPaymentMethodId()` | `string` |
| `getShippingMethodId()` | `string` |
| `getInAppPurchases()` | `string` (raw JWT) |

## In-App Purchase Provider

`Shopware\App\SDK\Context\InAppPurchase\InAppPurchaseProvider`

```php
__construct(SBPStoreKeyFetcher $keyFetcher, LoggerInterface $logger = new NullLogger())
```

`decodePurchases(non-empty-string $encodedPurchases, ShopInterface $shop): Collection<InAppPurchase>`

- Fetches JWKS from `https://api.shopware.com/inappfeatures/jwks` (cached via PSR-16)
- Validates RS256/RS384/RS512 JWT signature
- On failure: retries once with `$refresh = true` (re-fetches JWKS), then logs error and returns empty Collection

`InAppPurchase` properties: `string $key`, `int $quantity`, `?\DateTime $nextBookingDate`

`SBPStoreKeyFetcher` constants:
- `SBP_JWT_API_HOST = 'https://api.shopware.com'`
- `SBP_JWT_CACHE_KEY = 'store-jwks-key'`
