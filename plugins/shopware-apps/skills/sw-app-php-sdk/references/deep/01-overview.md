# PHP SDK — Overview & Architecture

## Package

| Key | Value |
|-----|-------|
| Composer name | `shopware/app-php-sdk` |
| Namespace root | `Shopware\App\SDK\` → `src/` |
| PHP requirement | `^8.1` |
| License | MIT |

## Runtime Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `lcobucci/jwt` | `^4.0\|\|^5.0` | JWT parsing/signing (storefront token, in-app-purchase JWT) |
| `phpseclib/phpseclib` | `^3.0.50` | RSA cryptography backing for JWT |
| `strobotti/php-jwk` | `^1.4` | JWKS key-set parsing (in-app purchases) |
| `php-http/discovery` | `^1.17` | Auto-discovers PSR-18 client and PSR-17 factories |
| `psr/http-client` | — | PSR-18 HTTP client interface |
| `psr/http-factory` | — | PSR-17 request/response factories |
| `psr/http-message` | — | PSR-7 message interfaces |
| `psr/simple-cache` | `^3.0` | PSR-16 token caching |
| `psr/event-dispatcher` | `^1.0` | PSR-14 lifecycle events |
| `lcobucci/clock` | `^3` | PSR-20 clock abstraction |

**Optional:** `async-aws/dynamo-db` — for the DynamoDB repository adapter.

## Source Directory Map

```
src/
├── AppConfiguration.php          — central config value-object
├── AppLifecycle.php              — entry point for all lifecycle HTTP endpoints
├── Adapter/DynamoDB/             — DynamoDB ShopRepository adapter
├── Authentication/               — HMAC + JWT verifiers and response signer
├── Context/                      — ContextResolver + all action structs + domain objects
│   ├── ActionButton/
│   ├── Cart/
│   ├── Gateway/Checkout/
│   ├── Gateway/Context/
│   ├── Gateway/InAppFeatures/
│   ├── InAppPurchase/
│   ├── Module/
│   ├── Order/
│   ├── Payment/
│   ├── Response/Customer/
│   ├── SalesChannelContext/
│   ├── Storefront/
│   ├── TaxProvider/
│   ├── Trait/
│   └── Webhook/
├── Event/                        — PSR-14 lifecycle event classes
├── Exception/                    — typed exception classes
├── Framework/Collection.php      — generic typed collection
├── Gateway/Checkout/Command/     — checkout gateway command objects
├── Gateway/Context/Command/      — context gateway command objects
├── HttpClient/                   — authenticated + logging PSR-18 clients
├── Registration/                 — RegistrationService + secret generator
├── Response/                     — static response factories
├── Shop/                         — ShopInterface + ShopRepositoryInterface + ShopResolver
├── TaxProvider/                  — TaxProviderResponseBuilder
└── Test/                         — MockShop, MockShopRepository, MockClient, JWKSHelper
```

## Bootstrap Pattern (PSR, framework-agnostic)

```php
use Shopware\App\SDK\AppConfiguration;
use Shopware\App\SDK\AppLifecycle;
use Shopware\App\SDK\Registration\RegistrationService;
use Shopware\App\SDK\Shop\ShopResolver;
use Shopware\App\SDK\Context\ContextResolver;
use Shopware\App\SDK\Authentication\ResponseSigner;
use Shopware\App\SDK\HttpClient\ClientFactory;

$cfg       = new AppConfiguration('MyApp', 'app-secret', 'https://yourapp.com/register/callback');
$repo      = new YourShopRepository();  // implements ShopRepositoryInterface
$lifecycle = new AppLifecycle(new RegistrationService($cfg, $repo), new ShopResolver($repo), $repo);
$resolver  = new ContextResolver();
$signer    = new ResponseSigner();
$factory   = new ClientFactory($psr16Cache);

// Registration endpoints
$lifecycle->register($request);         // GET  /register
$lifecycle->registerConfirm($request);  // POST /register/callback

// Lifecycle webhooks
$lifecycle->activate($request);         // POST app.activated
$lifecycle->deactivate($request);       // POST app.deactivated
$lifecycle->delete($request);           // POST app.deleted

// Resolve shop + context for any other request
$shop    = (new ShopResolver($repo))->resolveShop($request);
$webhook = $resolver->assembleWebhook($request, $shop);

// Signed HTTP client back to shop
$client = $factory->createSimpleClient($shop);
$client->get('/api/product');
```

## Collection<T>

`Shopware\App\SDK\Framework\Collection<TElement>` — generic collection implementing `Countable`, `IteratorAggregate`, `\JsonSerializable`.

Key methods: `all()`, `add($el)`, `set($key, $el)`, `get($key)`, `first()`, `last()`, `remove($key)`, `has($key)`, `map(\Closure)`, `filter(\Closure): self`, `count()`, `keys()`, `jsonSerialize()`.
