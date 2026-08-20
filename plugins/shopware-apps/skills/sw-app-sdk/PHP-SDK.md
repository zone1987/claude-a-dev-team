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
| `PHP-SDK-01-OVERVIEW.md` | Package metadata, architecture map, bootstrap pattern |
| `PHP-SDK-02-REGISTRATION.md` | AppConfiguration, RegistrationService, full handshake flow |
| `PHP-SDK-03-SHOP-REPOSITORY.md` | ShopInterface, ShopRepositoryInterface, DynamoDBRepository |
| `PHP-SDK-04-AUTHENTICATION.md` | RequestVerifier, DualSignatureRequestVerifier, ResponseSigner |
| `PHP-SDK-05-CONTEXT-RESOLVER.md` | ContextResolver — all assemble* methods |
| `PHP-SDK-06-ACTION-STRUCTS.md` | Every action struct (Webhook/ActionButton/Payment/Tax/Gateway) |
| `PHP-SDK-07-DOMAIN-OBJECTS.md` | Cart, Order, SalesChannelContext, full field lists |
| `PHP-SDK-08-RESPONSES.md` | ActionButtonResponse, PaymentResponse, GatewayResponse, TaxProviderResponseBuilder |
| `PHP-SDK-09-HTTP-CLIENT.md` | AuthenticatedClient, ClientFactory, SimpleHttpClient |
| `PHP-SDK-10-EVENTS-EXCEPTIONS.md` | All PSR-14 events, all exception classes |

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
