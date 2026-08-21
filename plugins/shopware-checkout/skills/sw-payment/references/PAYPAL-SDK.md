# shopware/paypal-sdk — PayPal REST API SDK

A PSR-18 based PHP SDK by Shopware AG for talking directly to the **PayPal REST APIs** —
**not** the Shopware payment handler itself (no Shopware framework dependency).

```php
$context = new CredentialsOAuthContext($clientId, $clientSecret, sandbox: true);
$client  = new Client($context); // PSR-18 HttpClient + PSR-16 Token-Cache
$order   = $client->getOrderGateway()->create($orderStruct);
```

- **Auth**: `CredentialsOAuthContext` (client ID/secret) or `AuthorizationCodeOAuthContext` (onboarding);
  the OAuth2 token is cached via PSR-16. Sandbox vs. live is chosen through the context. Marketplace via `PayPal-Auth-Assertion`.
- **Gateways** (API areas): Orders (V2), Payments (V1/V2), Webhooks, Customer/Disputes/Managed Accounts, Reporting, Token.
- Struct namespaces V1/V2/V3/AgenticCommerce; a dedicated exception hierarchy.

For a Shopware **payment handler** (checkout integration) → `sw-payment-handler`/`sw-payment-app`.

→ Full reference (all gateways/methods, HTTP paths, structs, exceptions): [PAYPAL-SDK-GATEWAYS.md](PAYPAL-SDK-GATEWAYS.md)
