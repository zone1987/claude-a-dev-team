---
name: sw-app-php-sdk
description: >
  Exhaustive reference for `shopware/app-php-sdk` (PHP 8.1+, PSR-based, framework-agnostic).
  Use when: implementing the Shopware App registration handshake (HMAC/JWT), verifying request
  signatures, resolving shop context, handling AppLifecycle (activate/deactivate/delete),
  dispatching action-button/webhook/payment/tax/gateway contexts, building authenticated HTTP
  clients back to the shop, writing custom ShopRepository implementations, or understanding
  the complete class surface of the PHP SDK.
---

# sw-app-php-sdk — Shopware App PHP SDK Reference

## When to Apply

- Implementing `/register` + `/register/callback` endpoints in PHP
- Verifying `shopware-shop-signature` HMAC or storefront JWT headers
- Implementing `ShopRepositoryInterface` (MySQL, Redis, DynamoDB …)
- Deserialising Shopware POST payloads into typed PHP objects (webhook, payment, tax …)
- Signing outgoing responses (`ResponseSigner`)
- Creating authenticated PSR-18 clients back to the shop Admin API
- Handling all App lifecycle hooks with PSR-14 events
- Using Gateway Commands (Checkout / Context Gateway)
- Implementing in-app purchase validation against SBP JWKS

## Reference Files

| File | Content |
|------|---------|
| `references/deep/01-overview.md` | Package metadata, architecture map, bootstrap pattern |
| `references/deep/02-registration.md` | AppConfiguration, RegistrationService, full handshake flow |
| `references/deep/03-shop-repository.md` | ShopInterface, ShopRepositoryInterface, DynamoDBRepository |
| `references/deep/04-authentication.md` | RequestVerifier, DualSignatureRequestVerifier, ResponseSigner |
| `references/deep/05-context-resolver.md` | ContextResolver — all assemble* methods |
| `references/deep/06-action-structs.md` | Every action struct (Webhook/ActionButton/Payment/Tax/Gateway) |
| `references/deep/07-domain-objects.md` | Cart, Order, SalesChannelContext, full field lists |
| `references/deep/08-responses.md` | ActionButtonResponse, PaymentResponse, GatewayResponse, TaxProviderResponseBuilder |
| `references/deep/09-http-client.md` | AuthenticatedClient, ClientFactory, SimpleHttpClient |
| `references/deep/10-events-exceptions.md` | All PSR-14 events, all exception classes |

## Quick Bootstrap (Symfony-agnostic PSR)

```php
use Shopware\App\SDK\AppConfiguration;
use Shopware\App\SDK\AppLifecycle;
use Shopware\App\SDK\Registration\RegistrationService;
use Shopware\App\SDK\Shop\ShopResolver;
use Shopware\App\SDK\Context\ContextResolver;
use Shopware\App\SDK\Authentication\ResponseSigner;
use Shopware\App\SDK\HttpClient\ClientFactory;

$cfg  = new AppConfiguration('MyApp', 'secret', 'https://app.example.com/register/callback');
$repo = new MyShopRepository();           // implements ShopRepositoryInterface

$lifecycle = new AppLifecycle(
    new RegistrationService($cfg, $repo),
    new ShopResolver($repo),
    $repo
);

// Route dispatch (pseudo-code)
match($path) {
    '/register'          => $lifecycle->register($request),
    '/register/callback' => $lifecycle->registerConfirm($request),
    '/activate'          => $lifecycle->activate($request),
    '/deactivate'        => $lifecycle->deactivate($request),
    '/delete'            => $lifecycle->delete($request),
};
```
