# shopware/paypal-sdk — Erschöpfende Gateway- & Struct-Referenz

Repo: `shopware/paypal-sdk` | Namespace-Root: `Shopware\PayPalSDK\` | PHP ≥ 8.1 | MIT

---

## Konstanten

```php
// Shopware\PayPalSDK\Constants
Constants::BASEURL_SANDBOX = 'https://api-m.sandbox.paypal.com/'
Constants::BASEURL_LIVE    = 'https://api-m.paypal.com/'
```

---

## Context-Layer

### `ApiContext` (`Shopware\PayPalSDK\Context\ApiContext`)

Immutabler Value-Object. Alle Wither geben neuen ApiContext zurück.

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

| Methode | Beschreibung |
|---------|-------------|
| `isSandbox(): bool` | Sandbox-Modus |
| `getMerchantId(): ?string` | Merchant-ID für Third-Party |
| `isThirdParty(): bool` | Third-Party-Flag |
| `getHeaders(): array` | Alle gesetzten Header (lowercase keys) |
| `getQueryParameters(): array` | URL-Query-Parameter |
| `withSandbox(bool): static` | Neuer Ctx mit geändertem Sandbox-Flag |
| `withMerchantId(?string): static` | Neuer Ctx mit Merchant-ID |
| `withHeader(string, ?string): static` | Einzelnen Header setzen/entfernen |
| `withQueryParameter(string, ?string): static` | Query-Parameter setzen |
| `withThirdParty(bool): static` | Third-Party-Flag ändern |
| `withPartnerAttributionId(?string): self` | `PayPal-Partner-Attribution-Id` Header |
| `withPreferRepresentation(bool): self` | `Prefer: return=representation` Header |
| `withRequestId(?string): self` | `PayPal-Request-Id` Header (Idempotency) |
| `withClientMetadataId(?string): self` | `PayPal-Client-Metadata-Id` Header |

### OAuthContext-Implementierungen

#### `CredentialsOAuthContext`
- Konstruktor: `(string $clientId, string $clientSecret)`
- `grant_type`: `client_credentials`
- Header: `Authorization: Basic base64(clientId:clientSecret)`
- Methoden: `getClientId()`, `intoUserIdContext(?string $targetCustomerId)`, `intoClientTokenContext()`

#### `ClientTokenOAuthContext extends CredentialsOAuthContext`
- Konstruktor: `(string $clientId, string $clientSecret, array $domains = [])`
- `grant_type`: `client_credentials` + `response_type=client_token`
- `withDomains(string ...$domains): self` — Domain-Filterung (validiert, keine IPs/keine TLD-losen)

#### `AuthorizationCodeOAuthContext`
- Konstruktor: `(string $authCode, string $sharedId, string $nonce)`
- `grant_type`: `authorization_code` + `code` + `code_verifier`
- Für Onboarding-AuthCode-Exchange

#### `UserIdOAuthContext` (via `CredentialsOAuthContext::intoUserIdContext()`)
- User-ID-basierter Token-Fluss

---

## TokenGateway (`Shopware\PayPalSDK\Gateway\TokenGateway`)

Endpunkt: `POST /v1/oauth2/token`

```php
new TokenGateway(
    ClientInterface $client = new Psr18Client(),
    CacheInterface $tokenCache = new TokenArrayCache(),
    RequestServiceInterface $requestService = new RequestService(),
)
```

| Methode | Signatur |
|---------|---------|
| `getToken` | `getToken(ApiContextInterface $context): Token` |

- Token wird automatisch gecacht (`TokenArrayCache` = In-Memory-PSR-16-Impl.)
- Cache-Key: Hash aus ClientId + Secret + MerchantId + Sandbox-Flag
- Token wird vor Ablauf (TTL-Threshold) invalidiert

---

## AbstractGateway (`Shopware\PayPalSDK\Gateway\AbstractGateway`)

Basis für alle fachlichen Gateways. Intern: Token holen → Request bauen → Response deserialisieren.

```php
new OrderGateway(
    ClientInterface $client = new Psr18Client(),
    TokenGatewayInterface $tokenGateway = new TokenGateway(),
    RequestServiceInterface $requestService = new RequestService(),
)
```

---

## OrderGateway (`Shopware\PayPalSDK\Gateway\OrderGateway`)

Basis-URL: `POST /v2/checkout/orders`

| Methode | HTTP | Pfad | Beschreibung |
|---------|------|------|-------------|
| `createOrder(Order, ApiContextInterface): Order` | POST | `/v2/checkout/orders` | Order erstellen |
| `getOrder(string $orderId, ApiContextInterface): Order` | GET | `/v2/checkout/orders/{id}` | Order abrufen |
| `authorizeOrder(string $orderId, ApiContextInterface): Order` | POST | `/v2/checkout/orders/{id}/authorize` | Order autorisieren |
| `captureOrder(string $orderId, ApiContextInterface): Order` | POST | `/v2/checkout/orders/{id}/capture` | Order capturen |
| `patchOrder(string $orderId, PatchCollection, ApiContextInterface): void` | PATCH | `/v2/checkout/orders/{id}` | Order-Felder patchen |
| `addTracker(Tracker, string $orderId, ApiContextInterface): Order` | POST | `/v2/checkout/orders/{id}/track` | Tracking hinzufügen |
| `removeTracker(Tracker, string $orderId, ApiContextInterface): void` | PATCH | `/v2/checkout/orders/{id}/trackers/{captureId}-{trackingNumber}` | Tracking stornieren (status=CANCELLED) |

Wichtige Structs:
- `Shopware\PayPalSDK\Struct\V2\Order` — Haupt-Order-Objekt
- `Shopware\PayPalSDK\Struct\V2\Order\Tracker`
- `Shopware\PayPalSDK\Struct\V2\Patch` / `PatchCollection`
- `Order::INTENT_CAPTURE` / `Order::INTENT_AUTHORIZE`

---

## PaymentGateway (`Shopware\PayPalSDK\Gateway\PaymentGateway`)

Basis-URL: `/v2/payments`

| Methode | HTTP | Pfad | Rückgabe |
|---------|------|------|---------|
| `getCapture(string $captureId, ApiContextInterface): Capture` | GET | `/v2/payments/captures/{id}` | Capture-Details |
| `getAuthorization(string $authorizationId, ApiContextInterface): Authorization` | GET | `/v2/payments/authorizations/{id}` | Authorization-Details |
| `getRefund(string $refundId, ApiContextInterface): Refund` | GET | `/v2/payments/refunds/{id}` | Refund-Details |
| `refundCapture(string $captureId, Refund, ApiContextInterface): Refund` | POST | `/v2/payments/captures/{id}/refund` | Refund auf Capture |
| `captureAuthorization(string $authorizationId, Capture, ApiContextInterface): Capture` | POST | `/v2/payments/authorizations/{id}/capture` | Auth. capturen |
| `voidAuthorization(string $authorizationId, ApiContextInterface): void` | POST | `/v2/payments/authorizations/{id}/void` | Auth. void |
| `findEligibleMethods(FindEligibleMethods, ApiContextInterface): EligibleMethodsData` | POST | `/v2/payments/find-eligible-methods` | Zahlungsmethoden-Eligibility |

Structs: `Struct\V2\Order\PurchaseUnit\Payments\{Authorization, Capture, Refund}`, `Struct\V2\{EligibleMethodsData, FindEligibleMethods}`

---

## PaymentV1Gateway (`Shopware\PayPalSDK\Gateway\PaymentV1Gateway`)

Basis-URL: `/v1/payments` — Alte PayPal Payments API (Legacy)

| Methode | HTTP | Pfad |
|---------|------|------|
| `getAuthorization(string $authorizationId, ApiContextInterface): Authorization` | GET | `/v1/payments/authorization/{id}` |
| `getCapture(string $captureId, ApiContextInterface): Capture` | GET | `/v1/payments/capture/{id}` |
| `getOrder(string $orderId, ApiContextInterface): Order` | GET | `/v1/payments/orders/{id}` |
| `getPayment(string $paymentId, ApiContextInterface): Payment` | GET | `/v1/payments/payment/{id}` |
| `getSale(string $saleId, ApiContextInterface): Sale` | GET | `/v1/payments/sale/{id}` |

Structs: `Struct\V1\{Capture, Payment}`, `Struct\V1\Payment\Transaction\RelatedResource\{Authorization, Order, Sale}`

---

## WebhookGateway (`Shopware\PayPalSDK\Gateway\WebhookGateway`)

Basis-URL: `/v1/notifications/webhooks`

| Methode | HTTP | Pfad | Beschreibung |
|---------|------|------|-------------|
| `createWebhook(Webhook, ApiContextInterface): Webhook` | POST | `/v1/notifications/webhooks` | Webhook anlegen |
| `getWebhook(string $webhookId, ApiContextInterface): Webhook` | GET | `/v1/notifications/webhooks/{id}` | Webhook abrufen |
| `getWebhookList(ApiContextInterface): WebhookList` | GET | `/v1/notifications/webhooks` | Alle Webhooks |
| `updateWebhook(string $webhookId, PatchCollection, ApiContextInterface): void` | PATCH | `/v1/notifications/webhooks/{id}` | Webhook patchen |
| `deleteWebhook(string $webhookId, ApiContextInterface): void` | DELETE | `/v1/notifications/webhooks/{id}` | Webhook löschen |

Structs: `Struct\V1\{Webhook, WebhookList}`, `Struct\V1\PatchCollection`

---

## CustomerGateway (`Shopware\PayPalSDK\Gateway\CustomerGateway`)

Basis-URLs: `/v1/customer`, `/v2/customer`, `/v3/customer`

| Methode | HTTP | Pfad | Beschreibung |
|---------|------|------|-------------|
| `getMerchantIntegrations(string $partnerId, string $merchantId, ApiContextInterface): MerchantIntegrations` | GET | `/v1/customer/partners/{partnerId}/merchant-integrations/{merchantId}` | Merchant-Integration abrufen |
| `getMerchantTracking(string $partnerId, string $trackingId, ApiContextInterface): MerchantTracking` | GET | `/v1/customer/partners/{partnerId}/merchant-integrations?tracking_id=` | Onboarding-Tracking |
| `getCredentials(string $partnerId, ApiContextInterface): Credentials` | GET | `/v1/customer/partners/{partnerId}/merchant-integrations/credentials` | Credentials abrufen |
| `createPartnerReferral(Referral, ApiContextInterface): Referral` | POST | `/v2/customer/partner-referrals` | Partner-Referral erstellen |
| `getDisputes(ApiContextInterface): Disputes` | GET | `/v1/customer/disputes` | Alle Disputes |
| `getDispute(string $disputeId, ApiContextInterface): DisputeItem` | GET | `/v1/customer/disputes/{id}` | Einzelner Dispute |
| `getManagedAccounts(ApiContextInterface): ManagedAccounts` | GET | `/v3/customer/managed-accounts` | Managed Accounts (filter via queryParams) |
| `getManagedAccount(string $merchantId, ApiContextInterface): ManagedAccount` | GET | `/v3/customer/managed-accounts/{merchantId}` | Einzelner Managed Account |
| `createWalletDomain(WalletDomain, ApiContextInterface): WalletDomain` | POST | `/v1/customer/wallet-domains` | Apple-Pay-Domain registrieren |
| `getWalletDomains(ApiContextInterface, int $page = 1, int $pageSize = 99): WalletDomains` | GET | `/v1/customer/wallet-domains?page=&page_size=` | Wallet-Domains auflisten |
| `deleteWalletDomain(WalletDomain, ApiContextInterface): WalletDomain` | POST | `/v1/customer/unregister-wallet-domain` | Domain deregistrieren |

Anmerkung: `getMerchantIntegrations`, `getMerchantTracking`, `getCredentials`, `createPartnerReferral`, `getManagedAccounts`, `getManagedAccount` rufen intern `$context->withThirdParty(false)` auf.

Structs: `Struct\V1\{MerchantIntegrations, MerchantTracking, Disputes, WalletDomain, WalletDomains}`, `Struct\V1\MerchantIntegrations\Credentials`, `Struct\V2\Referral`, `Struct\V3\{ManagedAccount, ManagedAccounts}`

---

## ReportingGateway (`Shopware\PayPalSDK\Gateway\ReportingGateway`)

Basis-URL: `/v1/reporting`

| Methode | HTTP | Pfad | Beschreibung |
|---------|------|------|-------------|
| `listTransactions(TransactionSearch, ApiContextInterface): Transactions` | GET | `/v1/reporting/transactions` | Transaktionen abrufen (Parameter aus `TransactionSearch`-Struct) |
| `listBalances(?BalanceSearch, ApiContextInterface): Balances` | GET | `/v1/reporting/balances` | Kontostände abrufen |

Structs: `Struct\V1\Reporting\{Transactions, TransactionSearch, Balances, BalanceSearch}`

---

## Struct-Übersicht nach API-Bereich

### V1 — Legacy PayPal API

| Struct | Verwendung |
|--------|-----------|
| `V1\Token` | OAuth-Token mit `getAccessToken()`, `getTokenType()`, `getExpiresIn()`, `getExpireDateTime()` |
| `V1\ClientToken` | Client-Token für Browser |
| `V1\Payment` | Legacy-Payment-Objekt |
| `V1\Capture` | V1-Capture |
| `V1\Refund` | V1-Refund |
| `V1\Patch` / `V1\PatchCollection` | PATCH-Operationen |
| `V1\Webhook` / `V1\WebhookList` | Webhook-Entitäten |
| `V1\Disputes` / `V1\Disputes\Item` | Dispute-Entitäten (inkl. Evidence, Adjudication, Offer, Extensions) |
| `V1\MerchantIntegrations` | Onboarding-Informationen |
| `V1\MerchantTracking` | Onboarding-Tracking |
| `V1\Shipping` | Versandinfo |
| `V1\Plan` / `V1\Subscription` | Subscription-API (Billing-Plan, Subscriber, BillingInfo) |
| `V1\WalletDomain` / `V1\WalletDomains` | Apple Pay Wallet-Domain |
| `V1\Reporting\TransactionSearch` | Filter für Transaktions-Report |
| `V1\Reporting\Transactions` | Transaktions-Response |
| `V1\Reporting\BalanceSearch` | Filter für Balance-Report |
| `V1\Reporting\Balances` | Balance-Response |
| `V1\Common\{Address, Amount, Details, Money, Link, Value}` | Shared Value-Objects |
| `ConstantsV1` | V1-String-Konstanten |

### V2 — Aktuelle PayPal Orders & Payments API

| Struct | Verwendung |
|--------|-----------|
| `V2\Order` | Haupt-Order (intent, purchaseUnits, paymentSource, status) |
| `V2\Order\Tracker` | Shipment-Tracker |
| `V2\Order\PurchaseUnit` | Purchase-Unit (amount, payee, items, shipping, payments) |
| `V2\Order\PurchaseUnit\Amount` | Betrag mit Breakdown |
| `V2\Order\PurchaseUnit\Amount\Breakdown` | Aufschlüsselung (item_total, shipping, etc.) |
| `V2\Order\PurchaseUnit\Payee` | Payee (email, merchant_id) |
| `V2\Order\PurchaseUnit\PaymentInstruction` | Plattform-Gebühren |
| `V2\Order\PurchaseUnit\Payments\Authorization` | Autorisierungs-Objekt |
| `V2\Order\PurchaseUnit\Payments\Authorization\*` | Seller-Protection, ExpirationTime etc. |
| `V2\Order\PurchaseUnit\Payments\Capture` | Capture-Objekt |
| `V2\Order\PurchaseUnit\Payments\Capture\*` | SellerReceivableBreakdown, FinalCapture |
| `V2\Order\PurchaseUnit\Payments\Refund` | Refund-Objekt |
| `V2\Order\PurchaseUnit\Shipping` | Versand (address, trackers) |
| `V2\Order\PurchaseUnit\Shipping\Tracker` | Tracker mit STATUS_CANCELLED |
| `V2\Order\PurchaseUnit\SupplementaryData` | Card- / Risk-Daten |
| `V2\Order\PaymentSource` | Zahlungsquelle (PayPal, Card, Klarna, SEPA, Vault etc.) |
| `V2\Order\PaymentSource\Card` | Card-Zahlung inkl. AuthenticationResult |
| `V2\Order\PaymentSource\Klarna` | Klarna-Zahlung |
| `V2\Order\PaymentSource\PayUponInvoice` | Rechnungskauf |
| `V2\Order\PaymentSource\Token` | Vault-Token |
| `V2\Order\PaymentSource\Common\Attributes` | Vault-Attribut (customer, vault) |
| `V2\Patch` / `V2\PatchCollection` | PATCH-Operationen (op: add/replace/remove/copy/move/test) |
| `V2\Referral` | Partner-Referral (Onboarding-Link) |
| `V2\Referral\BusinessEntity` | Business-Informationen |
| `V2\Referral\Operation\ApiIntegrationPreference` | Integrations-Einstellungen |
| `V2\FindEligibleMethods` | Eligibility-Query |
| `V2\EligibleMethodsData` | Eligibility-Response |
| `V2\EligibleMethodsData\EligibleMethods\AdvancedCards` | Advanced-Cards-Eligibility |
| `V2\Common\*` | Shared V2-Value-Objects |
| `ConstantsV2` | V2-String-Konstanten |

### V3 — Neue PayPal APIs

| Struct | Verwendung |
|--------|-----------|
| `V3\ManagedAccount` | Managed-Account für Partner-Onboarding |
| `V3\ManagedAccount\BusinessEntity` | Business-Entity-Infos |
| `V3\ManagedAccount\IndividualOwner` | Einzelpersonen-Inhaber (BirthDetails, IdentificationDocument) |
| `V3\ManagedAccounts` | Liste von Managed-Accounts |
| `V3\PaymentToken` | Vault-Payment-Token |
| `V3\PaymentToken\Metadata` | Token-Metadaten |
| `V3\Common\{Email, Name, PhoneNumber}` | Shared V3-Value-Objects |

### AgenticCommerce V1 — PayPal Agentic Commerce API

Neue API für KI-gestützte Kaufabwicklung. Namespace: `Shopware\PayPalSDK\Struct\AgenticCommerce\V1\`

| Struct | Verwendung |
|--------|-----------|
| `PayPalCart` | Warenkorb-Objekt |
| `CartItem` / `CartItemCollection` | Warenkorb-Positionen |
| `CartTotals` | Summen |
| `Customer` | Kunden-Info |
| `ShippingAddress` / `BillingAddress` | Adressen |
| `ShippingOption` / `ShippingOptionCollection` | Versandoptionen |
| `PaymentMethod` | Zahlungsmethode |
| `CheckoutField` / `CheckoutFieldCollection` | Checkout-Felder |
| `ValidationIssue` / `ValidationIssueCollection` | Validierungsfehler |
| `ResolutionOption` / `ResolutionOptionCollection` | Lösungsoptionen |
| `AgentError` / `AgentErrorDetail` | Agent-Fehler |
| `AppliedCoupon` / `Coupon` | Gutschein-Objekte |
| `GiftOptions` | Geschenk-Optionen |
| `Value\*` | Typed-Value-Objekte (AgeVerification, GiftMessage, etc.) |
| `Context\*` | Error-Contexts (BusinessRuleError, DataError, InventoryIssue, etc.) |
| `Referral\*` | Referral-spezifische Structs |
| `Builder\MetaDataBuilder` | Fluent Builder für MetaData |
| `Builder\ResolutionBuilder` | Fluent Builder für Resolution |
| `Builder\ValidationIssueBuilder` | Fluent Builder für ValidationIssue |

---

## Error-Structs

| Struct | Beschreibung |
|--------|-------------|
| `Struct\Error\Error` | PayPal-Error-Response |
| `Struct\Error\Detail` / `DetailCollection` | Error-Detail-Einträge |

---

## Exceptions

| Klasse | Wann |
|--------|------|
| `ApiException` | Allgemeine HTTP-Fehler ≥ 400 |
| `OAuthApiException extends ApiException` | OAuth-Endpunkt liefert Fehler |
| `ErrorApiException extends ApiException` | PayPal-Error-Response mit `name`/`details[]` |

`ExceptionFactory::createFromResponse(ResponseInterface): ApiException` — erzeugt korrekte Subklasse.

---

## RequestService

`Shopware\PayPalSDK\RequestService` implementiert `RequestServiceInterface`:

- `createRequest(string $method, string $path, ApiContextInterface): RequestInterface`
  - Wählt Basis-URL nach `$ctx->isSandbox()`
  - Setzt `Content-Type: application/json` für POST/PUT/PATCH
  - Setzt `PayPal-Auth-Assertion`-Header bei Third-Party-Calls
- `withBody(RequestInterface, array|\JsonSerializable): RequestInterface`
- `handleResponse(ResponseInterface): ?array` — wirft `ApiException` bei ≥ 400

Third-Party-Assertion: JWT-ähnlicher Header `base64({"alg":"none"}).base64({"iss":"clientId","payer_id":"merchantId"}).`

---

## Vollständiges Third-Party-Beispiel

```php
use Shopware\PayPalSDK\Context\ApiContext;
use Shopware\PayPalSDK\Context\CredentialsOAuthContext;
use Shopware\PayPalSDK\Gateway\OrderGateway;

// Partner ruft im Namen eines Merchants:
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

## Util-Klassen

| Klasse | Beschreibung |
|--------|-------------|
| `Util\TokenArrayCache` | PSR-16-In-Memory-Cache für Tokens |
| `Util\CaseConverter` | camelCase ↔ snake_case für JSON-Serialisierung |
| `Util\QueryParameterFormatter` | Baut Query-Parameter aus Struct-Properties (`withStructQueryParameters()`) |
