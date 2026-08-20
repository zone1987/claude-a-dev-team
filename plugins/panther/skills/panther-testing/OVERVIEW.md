# Symfony Panther — Overview and Architecture

Panther is a browser-testing and web-crawling library for PHP that drives real browsers
(Chrome, Firefox) via the W3C WebDriver protocol. It implements the
`BrowserInterface` and returns the same `Crawler` type as Symfony's `WebTestCase`.

## Architecture: three client types

| Client                  | Base              | JavaScript | Speed           | Usage                                |
|-------------------------|-------------------|:----------:|:---------------:|--------------------------------------|
| `PantherClient` (Chrome/Firefox) | WebDriver | Yes   | slow            | E2E, JS apps, real interactions      |
| `HttpBrowserClient`     | BrowserKit/cURL   | No         | fast            | HTTP-only tests, forms without JS    |
| `KernelBrowserClient`   | Symfony Kernel    | No         | very fast       | Unit/functional, Symfony apps only   |

## Short example

```php
use Symfony\Component\Panther\PantherTestCase;

class E2ETest extends PantherTestCase
{
    public function testHomepage(): void
    {
        $client = static::createPantherClient();          // real browser (Chrome)
        $client->request('GET', '/');
        $this->assertSelectorTextContains('h1', 'Welcome');

        $http = static::createHttpBrowserClient();        // headless HTTP
        $http->request('GET', '/api/ping');
        $this->assertSelectorExists('body');
    }
}
```

## Differentiation

- **WebTestCase / KernelBrowser**: no real browser, no JS, but full kernel access.
- **HttpBrowser (BrowserKit)**: real HTTP stack, no JS, no kernel access.
- **Goutte**: obsolete, its successor is `HttpBrowser`.
- **Panther (WebDriver)**: the only client with JS, real DOM, screenshots, waitFor.

## Deep dive

- [ARCHITECTURE.md](ARCHITECTURE.md) — Complete architecture, comparison table, decision tree
