# PHP SDK — HTTP Clients

## ClientFactory

`Shopware\App\SDK\HttpClient\ClientFactory` — factory for authenticated clients back to the shop Admin API.

```php
__construct(
    CacheInterface $cache = new NullCache(),    // PSR-16 for OAuth token caching
    ClientInterface $client = new Psr18Client(), // PSR-18 (auto-discovered)
    LoggerInterface $logger = new NullLogger()
)
```

| Method | Returns | Description |
|--------|---------|-------------|
| `createClient(ShopInterface $shop)` | `ClientInterface` | PSR-18 `AuthenticatedClient` wrapping `LoggerClient` |
| `createSimpleClient(ShopInterface $shop)` | `SimpleHttpClient` | convenience JSON client |

```php
$factory = new ClientFactory($psr16Cache);

// PSR-18 client
$psr18 = $factory->createClient($shop);
$response = $psr18->sendRequest($request);

// Simple client
$client = $factory->createSimpleClient($shop);
$result = $client->get('/api/product');
$data   = $result->json();
```

## AuthenticatedClient

`Shopware\App\SDK\HttpClient\AuthenticatedClient` implements PSR-18 `ClientInterface`.

Automatically fetches and caches OAuth2 `client_credentials` token from `{shopUrl}/api/oauth/token`.

- **Token grace period:** `TOKEN_EXPIRE_DIFF = 30` seconds — token refreshed 30s before expiry
- Injects `Authorization: Bearer {token}` into every outgoing request
- Throws `AuthenticationFailedException` if OAuth endpoint returns non-200

## LoggerClient

`Shopware\App\SDK\HttpClient\LoggerClient` implements PSR-18 `ClientInterface`.

Decorates any PSR-18 client with PSR-3 logging:
- **Info level:** request method + URI + headers
- **Debug level:** request + response bodies

## SimpleHttpClient

`Shopware\App\SDK\HttpClient\SimpleHttpClient\SimpleHttpClient`

Convenience HTTP client — automatically serialises/deserialises JSON, sets `Content-Type: application/json` and `Accept: application/json`.

```php
__construct(ClientInterface $client)
```

All methods return `SimpleHttpClientResponse`.

| Method | Body handling |
|--------|--------------|
| `get(string $url, array $headers = [])` | No body |
| `post(string $url, array $body = [], array $headers = [])` | JSON-encoded |
| `patch(string $url, array $body = [], array $headers = [])` | JSON-encoded |
| `put(string $url, array $body = [], array $headers = [])` | JSON-encoded |
| `delete(string $url, array $body = [], array $headers = [])` | JSON-encoded |

Headers passed per-call **override** the defaults.

## SimpleHttpClientResponse

```php
getContent(): string         // raw body string, stream rewound after read
json(): array                // decoded JSON; throws \RuntimeException if not array
getStatusCode(): int
getHeader(string $name): string
getRawResponse(): ResponseInterface
ok(): bool                   // status 200–299
```

## NullCache

`Shopware\App\SDK\HttpClient\NullCache` — no-op PSR-16 implementation. All reads return `$default`, all writes return `true`. Use in development or when token caching is not needed.

## AuthenticationFailedException

`Shopware\App\SDK\HttpClient\Exception\AuthenticationFailedException` extends `\RuntimeException`

```php
__construct(string $shopId, ResponseInterface $response, ?\Throwable $previous = null)
getResponse(): ResponseInterface
```

## Test: MockClient

`Shopware\App\SDK\Test\MockClient` implements PSR-18 `ClientInterface`.

```php
__construct(array $responses)  // array<ResponseInterface>
sendRequest(RequestInterface $request): ResponseInterface  // pops first response
isEmpty(): bool
```

```php
$mock = new MockClient([
    new Response(200, [], json_encode(['data' => []])),
    new Response(204),
]);
$factory = new ClientFactory(new NullCache(), $mock);
```
