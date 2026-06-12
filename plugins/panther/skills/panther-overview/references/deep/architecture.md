# Symfony Panther — Architektur & Entscheidungsbaum

## Was ist Panther?

Symfony Panther ist eine Browser-Testing- und Web-Crawling-Bibliothek fur PHP. Sie steuert
echte Browser (Chrome, Firefox) uber das W3C-WebDriver-Protokoll (via `php-webdriver/webdriver`)
und kann alternativ uber `BrowserKit/HttpBrowser` rein HTTP-basiert ohne Browser arbeiten.
Panther implementiert `Symfony\Component\BrowserKit\AbstractBrowser` und liefert stets einen
`Symfony\Component\DomCrawler\Crawler` (bzw. `PantherCrawler`), sodass Tests nahtlos zwischen
den Client-Typen wechseln konnen.

## Architektur-Diagramm (vereinfacht)

```
PantherTestCase / PantherTestCaseTrait
        |
        |-- createPantherClient()      --> WebDriver-Client (Chrome/Firefox/Selenium)
        |       \--> php-webdriver/webdriver --> ChromeDriver/GeckoDriver --> Browser
        |
        |-- createHttpBrowserClient()  --> BrowserKit/HttpBrowser (cURL)
        |       \--> symfony/http-client --> HTTP-Stack (kein Browser)
        |
        \-- createClient()             --> Symfony KernelBrowser (nur Symfony-Apps)
                \--> Symfony Kernel (in-process)
```

## Client-Vergleich (vollstandig)

| Kriterium               | PantherClient (WebDriver) | HttpBrowserClient     | KernelBrowserClient      |
|-------------------------|---------------------------|-----------------------|--------------------------|
| Basistechnologie        | W3C WebDriver             | BrowserKit + cURL     | Symfony Kernel           |
| JavaScript-Unterstutzung | Ja                       | Nein                  | Nein                     |
| Echter Browser          | Ja (Chrome / Firefox)     | Nein                  | Nein                     |
| Geschwindigkeit         | Langsam                   | Mittel                | Sehr schnell             |
| Screenshots             | Ja (`takeScreenshot`)     | Nein                  | Nein                     |
| waitFor-Methoden        | Ja                        | Nein                  | Nein                     |
| PHP-Kernel-Zugriff      | Nein                      | Nein                  | Ja                       |
| Symfony-Requirement     | Nein (jede PHP-App)       | Nein (jede PHP-App)   | Ja                       |
| Cookies                 | Ja (WebDriver CookieJar)  | Ja (BrowserKit)       | Ja (BrowserKit)          |
| HTTP-Redirects          | Ja (automatisch)          | Ja (konfigurierbar)   | Ja (konfigurierbar)      |
| SSL-Probleme umgehen    | Ja (via Capabilities)     | Ja (via HttpClient)   | N/A                      |
| Multi-Browser-Instanzen | Ja                        | Nein                  | Nein                     |
| Headless-Modus          | Ja (Standard)             | N/A                   | N/A                      |

## Entscheidungsbaum: Welchen Client verwenden?

```
Brauche ich JavaScript-Rendering oder echte Browser-Interaktionen?
  JA  --> PantherClient (createPantherClient)
  NEIN
    |
    Ist es eine Symfony-App und brauche ich Kernel/Service-Zugriff?
      JA  --> KernelBrowserClient (createClient)
      NEIN --> HttpBrowserClient (createHttpBrowserClient)
```

## Typische Einsatzfalle

### PantherClient (WebDriver)
- Single-Page Applications (SPA) mit Vue/React/Svelte
- Formulare mit JavaScript-Validierung
- Infinite Scroll, dynamisches Laden
- WebSocket / SSE / Real-Time-Tests
- Drag & Drop, Hover-Effekte
- Screenshot-Vergleiche
- Tests, die mehrere Browser-Instanzen erfordern (Chat-Tests)

### HttpBrowserClient
- REST-API-Endpunkte (JSON-Responses)
- Server-Side-Rendered-Seiten ohne JS
- Performance-Tests (viele Requests)
- Web-Crawling / Scraping

### KernelBrowserClient
- Unit-nahe Funktionaltests (schnell)
- Tests mit Datenbank-Reset
- Tests die Services, Repositories etc. direkt mocken

## Abgrenzung zu anderen Tools

| Tool               | Verhaltnis zu Panther                                              |
|--------------------|--------------------------------------------------------------------|
| **Goutte**         | Veraltet. Nachfolger ist `HttpBrowserClient` via `BrowserKit`.    |
| **WebTestCase**    | Symfony-intern, nur `KernelBrowser`, kein JS. Panther erweitert es.|
| **Playwright**     | Node.js-basiert, kein PHP. Fur PHP-Apps: Panther bevorzugen.      |
| **Selenium IDE**   | Grafisches Werkzeug, Panther nutzt Selenium-Grid-Protokoll.       |
| **Cypress**        | JavaScript-only, kein PHP. Fur PHP-Apps: Panther bevorzugen.      |
| **Behat/Mink**     | BDD-Framework, kann Panther als Treiber nutzen.                   |

## Dependency-Graph (Composer)

```
symfony/panther
  ├── php-webdriver/webdriver        # W3C WebDriver-Protokoll
  ├── symfony/browser-kit            # AbstractBrowser, CookieJar, History
  ├── symfony/dom-crawler            # Crawler, Form, FormFields
  ├── symfony/http-client            # fur HttpBrowserClient
  ├── symfony/process                # PHP-Built-in-Server starten
  └── dbrekelmans/bdi (optional)     # automatische Treiber-Installation
```

## PantherCrawler vs. DomCrawler

`PantherCrawler` ist eine Erweiterung von `DomCrawler\Crawler` mit WebDriver-spezifischen
Methoden:
- `getElement()` gibt ein `WebDriverElement` zuruck (kein `\DOMElement`)
- Keine XML-Unterstutzung (nur HTML)
- `text()` gibt sichtbaren Text zuruck (wie `innerText` im Browser)
- `html()` gibt das aktuelle (evtl. JS-modifizierte) HTML zuruck

## Versionierung

Panther folgt dem Symfony-Release-Zyklus. Ab v2.0 ist PHP 8.1+ Minimum.
Aktuelle stable: v2.4.x (Stand 2026-01).

---

Quellen:
- https://symfony.com/doc/current/testing/end_to_end.html
- https://github.com/symfony/panther
- https://symfony.com/doc/current/components/browser_kit.html
