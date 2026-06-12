---
name: panther-overview
description: >
  Was ist Symfony Panther, Architektur (echte Browser via WebDriver + headless HTTP via
  BrowserKit/HttpBrowser), wann welchen Client verwenden, Abgrenzung zu WebTestCase/Goutte.
  What is Panther, architecture, real browser vs. headless, when to use which client.
  Trigger: "was ist panther", "panther vs webtest", "panther architektur", "panther overview",
  "panther architecture", "panther vs goutte", "panther browser vs http", "symfony e2e testing",
  "panther client types", "which panther client", "panther real browser", "panther headless".
---

# Symfony Panther — Uberblick und Architektur

Panther ist eine Browser-Testing- und Web-Crawling-Bibliothek fur PHP, die echte Browser
(Chrome, Firefox) uber das W3C-WebDriver-Protokoll steuert. Sie implementiert die
`BrowserInterface` und liefert denselben `Crawler`-Typ wie Symfonys `WebTestCase`.

## Architektur: Drei Client-Typen

| Client                  | Basis             | JavaScript | Geschwindigkeit | Einsatz                              |
|-------------------------|-------------------|:----------:|:---------------:|--------------------------------------|
| `PantherClient` (Chrome/Firefox) | WebDriver | Ja    | langsam         | E2E, JS-Apps, echte Interaktionen    |
| `HttpBrowserClient`     | BrowserKit/cURL   | Nein       | schnell         | HTTP-only-Tests, Formulare ohne JS   |
| `KernelBrowserClient`   | Symfony Kernel    | Nein       | sehr schnell    | Unit/Functional, nur Symfony-Apps    |

## Kurzbeispiel

```php
use Symfony\Component\Panther\PantherTestCase;

class E2ETest extends PantherTestCase
{
    public function testHomepage(): void
    {
        $client = static::createPantherClient();          // echter Browser (Chrome)
        $client->request('GET', '/');
        $this->assertSelectorTextContains('h1', 'Welcome');

        $http = static::createHttpBrowserClient();        // headless HTTP
        $http->request('GET', '/api/ping');
        $this->assertSelectorExists('body');
    }
}
```

## Abgrenzung

- **WebTestCase / KernelBrowser**: kein echter Browser, kein JS, aber vollstandiger Kernel-Zugriff.
- **HttpBrowser (BrowserKit)**: echter HTTP-Stack, kein JS, kein Kernel-Zugriff.
- **Goutte**: veraltet, Nachfolger ist `HttpBrowser`.
- **Panther (WebDriver)**: einziger Client mit JS, Real-DOM, Screenshots, waitFor.

## Vertiefung

- [references/deep/architecture.md](references/deep/architecture.md) — Vollstandige Architektur, Vergleichstabelle, Entscheidungsbaum
