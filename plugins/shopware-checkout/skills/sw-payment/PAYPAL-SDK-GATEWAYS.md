# shopware/paypal-sdk — Exhaustive Gateway & Struct Reference

Repo: `shopware/paypal-sdk` | Namespace root: `Shopware\PayPalSDK\` | PHP ≥ 8.1 | MIT

---

## Contents

- [Constants](#constants)
- [Context layer](#context-layer)
- [TokenGateway (`Shopware\PayPalSDK\Gateway\TokenGateway`)](#tokengateway-shopwarepaypalsdkgatewaytokengateway)
- [AbstractGateway (`Shopware\PayPalSDK\Gateway\AbstractGateway`)](#abstractgateway-shopwarepaypalsdkgatewayabstractgateway)
- [OrderGateway (`Shopware\PayPalSDK\Gateway\OrderGateway`)](#ordergateway-shopwarepaypalsdkgatewayordergateway)
- [PaymentGateway (`Shopware\PayPalSDK\Gateway\PaymentGateway`)](#paymentgateway-shopwarepaypalsdkgatewaypaymentgateway)
- [PaymentV1Gateway (`Shopware\PayPalSDK\Gateway\PaymentV1Gateway`)](#paymentv1gateway-shopwarepaypalsdkgatewaypaymentv1gateway)
- [WebhookGateway (`Shopware\PayPalSDK\Gateway\WebhookGateway`)](#webhookgateway-shopwarepaypalsdkgatewaywebhookgateway)
- [CustomerGateway (`Shopware\PayPalSDK\Gateway\CustomerGateway`)](#customergateway-shopwarepaypalsdkgatewaycustomergateway)
- [ReportingGateway (`Shopware\PayPalSDK\Gateway\ReportingGateway`)](#reportinggateway-shopwarepaypalsdkgatewayreportinggateway)
- [Struct overview by API area](#struct-overview-by-api-area)
- [Error structs](#error-structs)
- [Exceptions](#exceptions)
- [RequestService](#requestservice)
- [Complete third-party example](#complete-third-party-example)
- [Util classes](#util-classes)

## Constants

```php
// Shopware\PayPalSDK\Constants
Constants::BASEURL_SANDBOX = 'https://api-m.sandbox.paypal.com/'
Constants::BASEURL_LIVE    = 'https://api-m.paypal.com/'
```

---

## Context layer

### `ApiContext` (`Shopware\PayPalSDK\Context\ApiContext`)

Immutable value object. Every wither returns a new ApiContext.

```php
new ApiContext(
    OAuthContextInterface $oauthContext,
    bool $sandbox,
    ?string $merchantId = null,
    array $headers = [],
    array $queryParameters = [],
    bool $thirdParty = false,
)
```

| Method | Description |
|---------|-------------|
| `isSandbox(): bool` | Sandbox mode |
| `getMerchantId(): ?string` | Merchant ID for third-party calls |
| `isThirdParty(): bool` | Third-party flag |
| `getHeaders(): array` | All headers set (lowercase keys) |
| `getQueryParameters(): array` | URL query parameters |
| `withSandbox(bool): static` | New ctx with a changed sandbox flag |
| `withMerchantId(?string): static` | New ctx with a merchant ID |
| `withHeader(string, ?string): static` | Set/remove a single header |
| `withQueryParameter(string, ?string): static` | Set a query parameter |
| `withThirdParty(bool): static` | Change the third-party flag |
| `withPartnerAttributionId(?string): self` | `PayPal-Partner-Attribution-Id` header |
| `withPreferRepresentation(bool): self` | `Prefer: return=representation` header |
| `withRequestId(?string): self` | `PayPal-Request-Id` header (idempotency) |
| `withClientMetadataId(?string): self` | `PayPal-Client-Metadata-Id` header |

### OAuthContext implementations

#### `CredentialsOAuthContext`
- Constructor: `(string $clientId, string $clientSecret)`
- `grant_type`: `client_credentials`
- Header: `Authorization: Basic base64(clientId:clientSecret)`
- Methods: `getClientId()`, `intoUserIdContext(?string $targetCustomerId)`, `intoClientTokenContext()`

#### `ClientTokenOAuthContext extends CredentialsOAuthContext`
- Constructor: `(string $clientId, string $clientSecret, array $domains = [])`
- `grant_type`: `client_credentials` + `response_type=client_token`
- `withDomains(string ...$domains): self` — domain filtering (validated, no IPs, no TLD-less names)

#### `AuthorizationCodeOAuthContext`
- Constructor: `(string $authCode, string $sharedId, string $nonce)`
- `grant_type`: `authorization_code` + `code` + `code_verifier`
- For the onboarding auth-code exchange

#### `UserIdOAuthContext` (via `CredentialsOAuthContext::intoUserIdContext()`)
- User-ID-based token flow

---

## TokenGateway (`Shopware\PayPalSDK\Gateway\TokenGateway`)

Endpoint: `POST /v1/oauth2/token`

```php
new TokenGateway(
    ClientInterface $client = new Psr18Client(),
    CacheInterface $tokenCache = new TokenArrayCache(),
    RequestServiceInterface $requestService = new RequestService(),
)
```

| Method | Signature |
|---------|---------|
| `getToken` | `getToken(ApiContextInterface $context): Token` |

- The token is cached automatically (`TokenArrayCache` = in-memory PSR-16 implementation)
- Cache key: hash of client ID + secret + merchant ID + sandbox flag
- The token is invalidated before it expires (TTL threshold)

---

## AbstractGateway (`Shopware\PayPalSDK\Gateway\AbstractGateway`)

Base class for all domain gateways. Internally: fetch token → build request → deserialize response.

```php
new OrderGateway(
    ClientInterface $client = new Psr18Client(),
    TokenGatewayInterface $tokenGateway = new TokenGateway(),
    RequestServiceInterface $requestService = new RequestService(),
)
```

---

## OrderGateway (`Shopware\PayPalSDK\Gateway\OrderGateway`)

Base URL: `POST /v2/checkout/orders`

| Method | HTTP | Path | Description |
|---------|------|------|-------------|
| `createOrder(Order, ApiContextInterface): Order` | POST | `/v2/checkout/orders` | Create order |
| `getOrder(string $orderId, ApiContextInterface): Order` | GET | `/v2/checkout/orders/{id}` | Fetch order |
| `authorizeOrder(string $orderId, ApiContextInterface): Order` | POST | `/v2/checkout/orders/{id}/authorize` | Authorize order |
| `captureOrder(string $orderId, ApiContextInterface): Order` | POST | `/v2/checkout/orders/{id}/capture` | Capture order |
| `patchOrder(string $orderId, PatchCollection, ApiContextInterface): void` | PATCH | `/v2/checkout/orders/{id}` | Patch order fields |
| `addTracker(Tracker, string $orderId, ApiContextInterface): Order` | POST | `/v2/checkout/orders/{id}/track` | Add tracking |
| `removeTracker(Tracker, string $orderId, ApiContextInterface): void` | PATCH | `/v2/checkout/orders/{id}/trackers/{captureId}-{trackingNumber}` | Cancel tracking (status=CANCELLED) |

Important structs:
- `Shopware\PayPalSDK\Struct\V2\Order` — main order object
- `Shopware\PayPalSDK\Struct\V2\Order\Tracker`
- `Shopware\PayPalSDK\Struct\V2\Patch` / `PatchCollection`
- `Order::INTENT_CAPTURE` / `Order::INTENT_AUTHORIZE`

---

## PaymentGateway (`Shopware\PayPalSDK\Gateway\PaymentGateway`)

Base URL: `/v2/payments`

| Method | HTTP | Path | Returns |
|---------|------|------|---------|
| `getCapture(string $captureId, ApiContextInterface): Capture` | GET | `/v2/payments/captures/{id}` | Capture details |
| `getAuthorization(string $authorizationId, ApiContextInterface): Authorization` | GET | `/v2/payments/authorizations/{id}` | Authorization details |
| `getRefund(string $refundId, ApiContextInterface): Refund` | GET | `/v2/payments/refunds/{id}` | Refund details |
| `refundCapture(string $captureId, Refund, ApiContextInterface): Refund` | POST | `/v2/payments/captures/{id}/refund` | Refund on a capture |
| `captureAuthorization(string $authorizationId, Capture, ApiContextInterface): Capture` | POST | `/v2/payments/authorizations/{id}/capture` | Capture an authorization |
| `voidAuthorization(string $authorizationId, ApiContextInterface): void` | POST | `/v2/payments/authorizations/{id}/void` | Void an authorization |
| `findEligibleMethods(FindEligibleMethods, ApiContextInterface): EligibleMethodsData` | POST | `/v2/payments/find-eligible-methods` | Payment method eligibility |

Structs: `Struct\V2\Order\PurchaseUnit\Payments\{Authorization, Capture, Refund}`, `Struct\V2\{EligibleMethodsData, FindEligibleMethods}`

---

## PaymentV1Gateway (`Shopware\PayPalSDK\Gateway\PaymentV1Gateway`)

Base URL: `/v1/payments` — the old PayPal Payments API (legacy)

| Method | HTTP | Path |
|---------|------|------|
| `getAuthorization(string $authorizationId, ApiContextInterface): Authorization` | GET | `/v1/payments/authorization/{id}` |
| `getCapture(string $captureId, ApiContextInterface): Capture` | GET | `/v1/payments/capture/{id}` |
| `getOrder(string $orderId, ApiContextInterface): Order` | GET | `/v1/payments/orders/{id}` |
| `getPayment(string $paymentId, ApiContextInterface): Payment` | GET | `/v1/payments/payment/{id}` |
| `getSale(string $saleId, ApiContextInterface): Sale` | GET | `/v1/payments/sale/{id}` |

Structs: `Struct\V1\{Capture, Payment}`, `Struct\V1\Payment\Transaction\RelatedResource\{Authorization, Order, Sale}`

---

## WebhookGateway (`Shopware\PayPalSDK\Gateway\WebhookGateway`)

Base URL: `/v1/notifications/webhooks`

| Method | HTTP | Path | Description |
|---------|------|------|-------------|
| `createWebhook(Webhook, ApiContextInterface): Webhook` | POST | `/v1/notifications/webhooks` | Create webhook |
| `getWebhook(string $webhookId, ApiContextInterface): Webhook` | GET | `/v1/notifications/webhooks/{id}` | Fetch webhook |
| `getWebhookList(ApiContextInterface): WebhookList` | GET | `/v1/notifications/webhooks` | All webhooks |
| `updateWebhook(string $webhookId, PatchCollection, ApiContextInterface): void` | PATCH | `/v1/notifications/webhooks/{id}` | Patch webhook |
| `deleteWebhook(string $webhookId, ApiContextInterface): void` | DELETE | `/v1/notifications/webhooks/{id}` | Delete webhook |

Structs: `Struct\V1\{Webhook, WebhookList}`, `Struct\V1\PatchCollection`

---

## CustomerGateway (`Shopware\PayPalSDK\Gateway\CustomerGateway`)

Base URLs: `/v1/customer`, `/v2/customer`, `/v3/customer`

| Method | HTTP | Path | Description |
|---------|------|------|-------------|
| `getMerchantIntegrations(string $partnerId, string $merchantId, ApiContextInterface): MerchantIntegrations` | GET | `/v1/customer/partners/{partnerId}/merchant-integrations/{merchantId}` | Fetch merchant integration |
| `getMerchantTracking(string $partnerId, string $trackingId, ApiContextInterface): MerchantTracking` | GET | `/v1/customer/partners/{partnerId}/merchant-integrations?tracking_id=` | Onboarding tracking |
| `getCredentials(string $partnerId, ApiContextInterface): Credentials` | GET | `/v1/customer/partners/{partnerId}/merchant-integrations/credentials` | Fetch credentials |
| `createPartnerReferral(Referral, ApiContextInterface): Referral` | POST | `/v2/customer/partner-referrals` | Create partner referral |
| `getDisputes(ApiContextInterface): Disputes` | GET | `/v1/customer/disputes` | All disputes |
| `getDispute(string $disputeId, ApiContextInterface): DisputeItem` | GET | `/v1/customer/disputes/{id}` | Single dispute |
| `getManagedAccounts(ApiContextInterface): ManagedAccounts` | GET | `/v3/customer/managed-accounts` | Managed accounts (filter via queryParams) |
| `getManagedAccount(string $merchantId, ApiContextInterface): ManagedAccount` | GET | `/v3/customer/managed-accounts/{merchantId}` | Single managed account |
| `createWalletDomain(WalletDomain, ApiContextInterface): WalletDomain` | POST | `/v1/customer/wallet-domains` | Register an Apple Pay domain |
| `getWalletDomains(ApiContextInterface, int $page = 1, int $pageSize = 99): WalletDomains` | GET | `/v1/customer/wallet-domains?page=&page_size=` | List wallet domains |
| `deleteWalletDomain(WalletDomain, ApiContextInterface): WalletDomain` | POST | `/v1/customer/unregister-wallet-domain` | Unregister a domain |

Note: `getMerchantIntegrations`, `getMerchantTracking`, `getCredentials`, `createPartnerReferral`, `getManagedAccounts`, `getManagedAccount` internally call `$context->withThirdParty(false)`.

Structs: `Struct\V1\{MerchantIntegrations, MerchantTracking, Disputes, WalletDomain, WalletDomains}`, `Struct\V1\MerchantIntegrations\Credentials`, `Struct\V2\Referral`, `Struct\V3\{ManagedAccount, ManagedAccounts}`

---

## ReportingGateway (`Shopware\PayPalSDK\Gateway\ReportingGateway`)

Base URL: `/v1/reporting`

| Method | HTTP | Path | Description |
|---------|------|------|-------------|
| `listTransactions(TransactionSearch, ApiContextInterface): Transactions` | GET | `/v1/reporting/transactions` | Fetch transactions (parameters from the `TransactionSearch` struct) |
| `listBalances(?BalanceSearch, ApiContextInterface): Balances` | GET | `/v1/reporting/balances` | Fetch balances |

Structs: `Struct\V1\Reporting\{Transactions, TransactionSearch, Balances, BalanceSearch}`

---

## Struct overview by API area

### V1 — legacy PayPal API

| Struct | Usage |
|--------|-----------|
| `V1\Token` | OAuth token with `getAccessToken()`, `getTokenType()`, `getExpiresIn()`, `getExpireDateTime()` |
| `V1\ClientToken` | Client token for the browser |
| `V1\Payment` | Legacy payment object |
| `V1\Capture` | V1 capture |
| `V1\Refund` | V1 refund |
| `V1\Patch` / `V1\PatchCollection` | PATCH operations |
| `V1\Webhook` / `V1\WebhookList` | Webhook entities |
| `V1\Disputes` / `V1\Disputes\Item` | Dispute entities (including evidence, adjudication, offer, extensions) |
| `V1\MerchantIntegrations` | Onboarding information |
| `V1\MerchantTracking` | Onboarding tracking |
| `V1\Shipping` | Shipping info |
| `V1\Plan` / `V1\Subscription` | Subscription API (billing plan, subscriber, billing info) |
| `V1\WalletDomain` / `V1\WalletDomains` | Apple Pay wallet domain |
| `V1\Reporting\TransactionSearch` | Filter for the transaction report |
| `V1\Reporting\Transactions` | Transaction response |
| `V1\Reporting\BalanceSearch` | Filter for the balance report |
| `V1\Reporting\Balances` | Balance response |
| `V1\Common\{Address, Amount, Details, Money, Link, Value}` | Shared value objects |
| `ConstantsV1` | V1 string constants |

### V2 — current PayPal Orders & Payments API

| Struct | Usage |
|--------|-----------|
| `V2\Order` | Main order (intent, purchaseUnits, paymentSource, status) |
| `V2\Order\Tracker` | Shipment tracker |
| `V2\Order\PurchaseUnit` | Purchase unit (amount, payee, items, shipping, payments) |
| `V2\Order\PurchaseUnit\Amount` | Amount with breakdown |
| `V2\Order\PurchaseUnit\Amount\Breakdown` | Breakdown (item_total, shipping, etc.) |
| `V2\Order\PurchaseUnit\Payee` | Payee (email, merchant_id) |
| `V2\Order\PurchaseUnit\PaymentInstruction` | Platform fees |
| `V2\Order\PurchaseUnit\Payments\Authorization` | Authorization object |
| `V2\Order\PurchaseUnit\Payments\Authorization\*` | Seller protection, expiration time, etc. |
| `V2\Order\PurchaseUnit\Payments\Capture` | Capture object |
| `V2\Order\PurchaseUnit\Payments\Capture\*` | SellerReceivableBreakdown, FinalCapture |
| `V2\Order\PurchaseUnit\Payments\Refund` | Refund object |
| `V2\Order\PurchaseUnit\Shipping` | Shipping (address, trackers) |
| `V2\Order\PurchaseUnit\Shipping\Tracker` | Tracker with STATUS_CANCELLED |
| `V2\Order\PurchaseUnit\SupplementaryData` | Card / risk data |
| `V2\Order\PaymentSource` | Payment source (PayPal, card, Klarna, SEPA, vault, etc.) |
| `V2\Order\PaymentSource\Card` | Card payment including AuthenticationResult |
| `V2\Order\PaymentSource\Klarna` | Klarna payment |
| `V2\Order\PaymentSource\PayUponInvoice` | Pay upon invoice |
| `V2\Order\PaymentSource\Token` | Vault token |
| `V2\Order\PaymentSource\Common\Attributes` | Vault attribute (customer, vault) |
| `V2\Patch` / `V2\PatchCollection` | PATCH operations (op: add/replace/remove/copy/move/test) |
| `V2\Referral` | Partner referral (onboarding link) |
| `V2\Referral\BusinessEntity` | Business information |
| `V2\Referral\Operation\ApiIntegrationPreference` | Integration settings |
| `V2\FindEligibleMethods` | Eligibility query |
| `V2\EligibleMethodsData` | Eligibility response |
| `V2\EligibleMethodsData\EligibleMethods\AdvancedCards` | Advanced cards eligibility |
| `V2\Common\*` | Shared V2 value objects |
| `ConstantsV2` | V2 string constants |

### V3 — new PayPal APIs

| Struct | Usage |
|--------|-----------|
| `V3\ManagedAccount` | Managed account for partner onboarding |
| `V3\ManagedAccount\BusinessEntity` | Business entity info |
| `V3\ManagedAccount\IndividualOwner` | Individual owner (BirthDetails, IdentificationDocument) |
| `V3\ManagedAccounts` | List of managed accounts |
| `V3\PaymentToken` | Vault payment token |
| `V3\PaymentToken\Metadata` | Token metadata |
| `V3\Common\{Email, Name, PhoneNumber}` | Shared V3 value objects |

### AgenticCommerce V1 — PayPal Agentic Commerce API

A new API for AI-driven purchase flows. Namespace: `Shopware\PayPalSDK\Struct\AgenticCommerce\V1\`

| Struct | Usage |
|--------|-----------|
| `PayPalCart` | Cart object |
| `CartItem` / `CartItemCollection` | Cart positions |
| `CartTotals` | Totals |
| `Customer` | Customer info |
| `ShippingAddress` / `BillingAddress` | Addresses |
| `ShippingOption` / `ShippingOptionCollection` | Shipping options |
| `PaymentMethod` | Payment method |
| `CheckoutField` / `CheckoutFieldCollection` | Checkout fields |
| `ValidationIssue` / `ValidationIssueCollection` | Validation errors |
| `ResolutionOption` / `ResolutionOptionCollection` | Resolution options |
| `AgentError` / `AgentErrorDetail` | Agent errors |
| `AppliedCoupon` / `Coupon` | Coupon objects |
| `GiftOptions` | Gift options |
| `Value\*` | Typed value objects (AgeVerification, GiftMessage, etc.) |
| `Context\*` | Error contexts (BusinessRuleError, DataError, InventoryIssue, etc.) |
| `Referral\*` | Referral-specific structs |
| `Builder\MetaDataBuilder` | Fluent builder for MetaData |
| `Builder\ResolutionBuilder` | Fluent builder for Resolution |
| `Builder\ValidationIssueBuilder` | Fluent builder for ValidationIssue |

---

## Error structs

| Struct | Description |
|--------|-------------|
| `Struct\Error\Error` | PayPal error response |
| `Struct\Error\Detail` / `DetailCollection` | Error detail entries |

---

## Exceptions

| Class | When |
|--------|------|
| `ApiException` | General HTTP errors ≥ 400 |
| `OAuthApiException extends ApiException` | The OAuth endpoint returns an error |
| `ErrorApiException extends ApiException` | PayPal error response with `name`/`details[]` |

`ExceptionFactory::createFromResponse(ResponseInterface): ApiException` — creates the correct subclass.

---

## RequestService

`Shopware\PayPalSDK\RequestService` implements `RequestServiceInterface`:

- `createRequest(string $method, string $path, ApiContextInterface): RequestInterface`
  - Picks the base URL based on `$ctx->isSandbox()`
  - Sets `Content-Type: application/json` on POST/PUT/PATCH
  - Sets the `PayPal-Auth-Assertion` header on third-party calls
- `withBody(RequestInterface, array|\JsonSerializable): RequestInterface`
- `handleResponse(ResponseInterface): ?array` — throws `ApiException` on ≥ 400

Third-party assertion: a JWT-like header `base64({"alg":"none"}).base64({"iss":"clientId","payer_id":"merchantId"}).`

---

## Complete third-party example

```php
use Shopware\PayPalSDK\Context\ApiContext;
use Shopware\PayPalSDK\Context\CredentialsOAuthContext;
use Shopware\PayPalSDK\Gateway\OrderGateway;

// Partner calls on behalf of a merchant:
$ctx = new ApiContext(
    oauthContext: new CredentialsOAuthContext('PARTNER_CLIENT_ID', 'PARTNER_CLIENT_SECRET'),
    sandbox: true,
    merchantId: 'MERCHANT_PAYPAL_ID',
    thirdParty: true,
);
$ctx = $ctx->withPartnerAttributionId('PARTNER_BN_CODE');

$gateway = new OrderGateway();
$order = $gateway->getOrder('ORDER_ID', $ctx);
```

---

## Util classes

| Class | Description |
|--------|-------------|
| `Util\TokenArrayCache` | PSR-16 in-memory cache for tokens |
| `Util\CaseConverter` | camelCase ↔ snake_case for JSON serialization |
| `Util\QueryParameterFormatter` | Builds query parameters from struct properties (`withStructQueryParameters()`) |
