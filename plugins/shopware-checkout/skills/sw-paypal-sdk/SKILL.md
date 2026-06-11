---
name: sw-paypal-sdk
description: >
  PHP-SDK für die PayPal REST APIs (shopware/paypal-sdk). Gateways, OAuth-Kontexte, Structs.
  Trigger: "paypal-sdk", "PayPal SDK", "PayPal API PHP", "OrderGateway", "PaymentGateway",
  "WebhookGateway", "CustomerGateway", "ReportingGateway", "CredentialsOAuthContext",
  "ApiContext", "PayPal Order erstellen", "PayPal Capture", "PayPal Refund",
  "PayPal Webhook anlegen", "PayPal OAuth", "PayPal Sandbox", "shopware/paypal-sdk".
---

# shopware/paypal-sdk — PayPal REST API SDK

PSR-18-basiertes PHP-SDK der Shopware AG für direkte Kommunikation mit den **PayPal REST APIs** —
**nicht** der Shopware-Payment-Handler selbst (keine Shopware-Framework-Dependency).

```php
$context = new CredentialsOAuthContext($clientId, $clientSecret, sandbox: true);
$client  = new Client($context); // PSR-18 HttpClient + PSR-16 Token-Cache
$order   = $client->getOrderGateway()->create($orderStruct);
```

- **Auth**: `CredentialsOAuthContext` (Client-ID/Secret) oder `AuthorizationCodeOAuthContext` (Onboarding);
  OAuth2-Token per PSR-16 gecacht. Sandbox vs. Live über den Context. Marketplace via `PayPal-Auth-Assertion`.
- **Gateways** (API-Bereiche): Orders (V2), Payments (V1/V2), Webhooks, Customer/Disputes/Managed-Accounts, Reporting, Token.
- Struct-Namespaces V1/V2/V3/AgenticCommerce; eigene Exception-Hierarchie.

Für einen Shopware-**Payment-Handler** (Checkout-Integration) → `sw-payment-handler`/`sw-payment-app`.

→ Vollständige Referenz (alle Gateways/Methoden, HTTP-Pfade, Structs, Exceptions): [references/deep/paypal-sdk-gateways.md](references/deep/paypal-sdk-gateways.md)
