# Panther — BrowserKit clients as a WebDriver alternative

## Contents

- [Overview: which client to choose?](#overview-which-client-to-choose)
- [HttpBrowserClient (Goutte replacement)](#httpbrowserclient-goutte-replacement)
- [Symfony KernelBrowser (createClient)](#symfony-kernelbrowser-createclient)
- [Combining all three clients](#combining-all-three-clients)
- [PantherTestCaseTrait with other TestCase classes](#panthertestcasetrait-with-other-testcase-classes)
- [The web server is shared automatically](#the-web-server-is-shared-automatically)
- [Performance trade-off](#performance-trade-off)
- [Sources](#sources)

## Overview: which client to choose?

| Client | Method | JavaScript | Speed | Usage |
|---|---|---|---|---|
| `PantherClient` (Chrome) | `createPantherClient()` | complete | slow | E2E tests with JS dependencies |
| `PantherClient` (Firefox) | `createPantherClient(['browser' => static::FIREFOX])` | complete | slow | Cross-browser tests |
| `HttpBrowserClient` | `createHttpBrowserClient()` | none | very fast | Forms, links, API calls without JS |
| Symfony `KernelBrowser` | `createClient()` | none | fastest | Symfony integration tests in-process |

The first three use the PHP built-in web server; `createClient()` runs
directly in the PHPUnit process without an HTTP connection.

---

## HttpBrowserClient (Goutte replacement)

`HttpBrowserClient` is based on `symfony/http-client` and `symfony/browser-kit`.
It sends real HTTP requests, but does not execute any JavaScript.

### Creation

```php
use Symfony\Component\Panther\PantherTestCase;

class FormTest extends PantherTestCase
{
    public function testContactForm(): void
    {
        // Starts the built-in web server if it is not already running
        $client = static::createHttpBrowserClient();

        $client->request('GET', '/contact');
        $client->submitForm('Absenden', [
            'contact[name]'    => 'Max Mustermann',
            'contact[email]'   => 'max@example.com',
            'contact[message]' => 'Hallo Welt',
        ]);

        $this->assertResponseIsSuccessful();
        $this->assertSelectorTextContains('.flash-success', 'Nachricht gesendet');
    }
}
```

### Signature of createHttpBrowserClient()

```php
protected static function createHttpBrowserClient(
    array $options = [],       // web server options (same as createPantherClient)
    array $kernelOptions = []  // Symfony kernel options
): HttpBrowserClient
```

### http_client_options

```php
$client = static::createHttpBrowserClient(
    options: [
        'http_client_options' => [
            // symfony/http-client options:
            'timeout'          => 30,
            'verify_peer'      => false,    // do not check the SSL certificate
            'verify_host'      => false,
            'headers'          => [
                'X-Test-Mode' => 'true',
            ],
            'max_redirects'    => 20,
            'proxy'            => 'http://proxy.example.com:8080',
        ],
    ]
);
```

---

## Symfony KernelBrowser (createClient)

`createClient()` returns a `KernelBrowser` (from `symfony/framework-bundle`).
It does not open an HTTP connection — requests are processed directly by the Symfony
kernel. Fastest option, no network latency.

```php
use Symfony\Component\Panther\PantherTestCase;

class ApiTest extends PantherTestCase
{
    public function testApiEndpoint(): void
    {
        $client = static::createClient();
        // Identical to WebTestCase::createClient()

        $client->request('GET', '/api/products', [], [], [
            'HTTP_ACCEPT' => 'application/json',
        ]);

        $this->assertResponseIsSuccessful();
        $data = json_decode($client->getResponse()->getContent(), true);
        $this->assertArrayHasKey('products', $data);
    }
}
```

Note: `createClient()` is only available when `PantherTestCase` extends
`KernelTestCase` (which is the case for `Symfony\Component\Panther\PantherTestCase`,
provided `symfony/framework-bundle` is installed).

---

## Combining all three clients

```php
use Symfony\Component\Panther\PantherTestCase;

class FullStackTest extends PantherTestCase
{
    public function testFullFlow(): void
    {
        // 1. Create data via KernelBrowser (fastest)
        $symfonyClient = static::createClient();
        $symfonyClient->request('POST', '/api/products', [], [], [
            'CONTENT_TYPE' => 'application/json',
        ], json_encode(['name' => 'Test-Produkt', 'price' => 9.99]));
        $this->assertResponseStatusCodeSame(201);

        // 2. HTTP browser for the server-side-rendering check
        $httpClient = static::createHttpBrowserClient();
        $httpClient->request('GET', '/products');
        $this->assertSelectorTextContains('.product-list', 'Test-Produkt');

        // 3. Panther for JavaScript-based interaction
        $pantherClient = static::createPantherClient();
        $pantherClient->request('GET', '/products');
        $pantherClient->clickLink('Test-Produkt');
        $pantherClient->waitFor('.product-detail');
        $this->assertSelectorTextContains('.product-detail h1', 'Test-Produkt');
    }
}
```

---

## PantherTestCaseTrait with other TestCase classes

For projects that use other base classes (e.g. `LiipFunctionalTestBundle`),
there is the `PantherTestCaseTrait`:

```php
use Liip\FunctionalTestBundle\Test\WebTestCase;
use Symfony\Component\Panther\PantherTestCaseTrait;

class ProductTest extends WebTestCase
{
    use PantherTestCaseTrait;

    public function testWithFixturesAndPanther(): void
    {
        // Load fixtures (LiipFunctionalTestBundle)
        $this->loadFixtures([
            \App\DataFixtures\ProductFixtures::class,
        ]);

        // Use the Panther client
        $client = self::createPantherClient();
        $client->request('GET', '/products');

        $this->assertSelectorTextContains('.product-list', 'Fixture-Produkt');
    }
}
```

Another example with `ApiTestCase` (e.g. from `api-platform/core`):

```php
use ApiPlatform\Symfony\Bundle\Test\ApiTestCase;
use Symfony\Component\Panther\PantherTestCaseTrait;

class ProductApiE2ETest extends ApiTestCase
{
    use PantherTestCaseTrait;

    public function testApiAndBrowser(): void
    {
        // API Platform client for API tests
        $apiClient = static::createClient();
        $response = $apiClient->request('GET', '/api/products');
        $this->assertResponseIsSuccessful();

        // Panther for frontend tests
        $browser = self::createPantherClient();
        $browser->request('GET', '/products');
        $browser->waitFor('.product-grid');
        $this->assertSelectorExists('.product-card');
    }
}
```

---

## The web server is shared automatically

All three `create*Client()` methods use the same PHP built-in web server process.
The first call starts it, further calls within the same test class
use the running instance.

```php
public function testSharedServer(): void
{
    // Starts the web server on port 9080
    $http = static::createHttpBrowserClient();

    // Uses the same web server (no restart)
    $panther = static::createPantherClient();

    // Both talk to http://127.0.0.1:9080
    $http->request('GET', '/');
    $panther->request('GET', '/');
}
```

---

## Performance trade-off

| Criterion | KernelBrowser | HttpBrowserClient | PantherClient |
|---|---|---|---|
| Startup time | < 10ms | ~100ms (server) | ~2-5s (browser) |
| Request time | < 1ms | ~5-50ms | ~100-500ms |
| JavaScript | no | no | complete |
| Real network stack | no | yes | yes |
| Real browser rendering | no | no | yes |
| CSS animations | no | no | yes |
| Screenshots | no | no | yes |
| Recommended for | Unit/integration tests | Forms, links, SSR | SPA, JavaScript, E2E |

---

## Sources

- https://symfony.com/doc/current/testing/end_to_end.html
- https://github.com/symfony/panther/blob/main/src/PantherTestCaseTrait.php
- https://symfony.com/doc/current/components/browser_kit.html
- https://symfony.com/doc/current/components/http_client.html
