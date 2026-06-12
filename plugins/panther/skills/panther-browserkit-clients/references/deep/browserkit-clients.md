# Panther — BrowserKit-Clients als WebDriver-Alternative

## Uebersicht: Welchen Client waehlen?

| Client | Methode | JavaScript | Geschwindigkeit | Einsatz |
|---|---|---|---|---|
| `PantherClient` (Chrome) | `createPantherClient()` | vollstaendig | langsam | E2E-Tests mit JS-Abhaengigkeiten |
| `PantherClient` (Firefox) | `createPantherClient(['browser' => static::FIREFOX])` | vollstaendig | langsam | Cross-Browser-Tests |
| `HttpBrowserClient` | `createHttpBrowserClient()` | keines | sehr schnell | Formulare, Links, API-Calls ohne JS |
| Symfony `KernelBrowser` | `createClient()` | keines | am schnellsten | Symfony-Integrationstests in-process |

Die ersten drei nutzen den PHP Built-In-Webserver; `createClient()` laeuft
direkt im PHPUnit-Prozess ohne HTTP-Verbindung.

---

## HttpBrowserClient (Goutte-Ersatz)

`HttpBrowserClient` basiert auf `symfony/http-client` und `symfony/browser-kit`.
Er sendet echte HTTP-Requests, fuehrt aber kein JavaScript aus.

### Erstellung

```php
use Symfony\Component\Panther\PantherTestCase;

class FormTest extends PantherTestCase
{
    public function testContactForm(): void
    {
        // Startet Built-In-Webserver wenn noch nicht laufend
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

### Signature von createHttpBrowserClient()

```php
protected static function createHttpBrowserClient(
    array $options = [],       // Web-Server-Optionen (gleiche wie createPantherClient)
    array $kernelOptions = []  // Symfony-Kernel-Optionen
): HttpBrowserClient
```

### http_client_options

```php
$client = static::createHttpBrowserClient(
    options: [
        'http_client_options' => [
            // symfony/http-client Optionen:
            'timeout'          => 30,
            'verify_peer'      => false,    // SSL-Zertifikat nicht pruefen
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

`createClient()` gibt einen `KernelBrowser` zurueck (aus `symfony/framework-bundle`).
Er fuehrt keine HTTP-Verbindung auf — Requests werden direkt durch den Symfony-Kernel
verarbeitet. Schnellste Option, keine Netzwerk-Latenz.

```php
use Symfony\Component\Panther\PantherTestCase;

class ApiTest extends PantherTestCase
{
    public function testApiEndpoint(): void
    {
        $client = static::createClient();
        // Identisch zu WebTestCase::createClient()

        $client->request('GET', '/api/products', [], [], [
            'HTTP_ACCEPT' => 'application/json',
        ]);

        $this->assertResponseIsSuccessful();
        $data = json_decode($client->getResponse()->getContent(), true);
        $this->assertArrayHasKey('products', $data);
    }
}
```

Hinweis: `createClient()` ist nur verfuegbar wenn `PantherTestCase` von
`KernelTestCase` erbt (was bei `Symfony\Component\Panther\PantherTestCase` der Fall
ist, sofern `symfony/framework-bundle` installiert ist).

---

## Alle drei Clients kombinieren

```php
use Symfony\Component\Panther\PantherTestCase;

class FullStackTest extends PantherTestCase
{
    public function testFullFlow(): void
    {
        // 1. Daten ueber KernelBrowser anlegen (am schnellsten)
        $symfonyClient = static::createClient();
        $symfonyClient->request('POST', '/api/products', [], [], [
            'CONTENT_TYPE' => 'application/json',
        ], json_encode(['name' => 'Test-Produkt', 'price' => 9.99]));
        $this->assertResponseStatusCodeSame(201);

        // 2. HTTP-Browser fuer Server-Side-Rendering-Check
        $httpClient = static::createHttpBrowserClient();
        $httpClient->request('GET', '/products');
        $this->assertSelectorTextContains('.product-list', 'Test-Produkt');

        // 3. Panther fuer JavaScript-basierte Interaktion
        $pantherClient = static::createPantherClient();
        $pantherClient->request('GET', '/products');
        $pantherClient->clickLink('Test-Produkt');
        $pantherClient->waitFor('.product-detail');
        $this->assertSelectorTextContains('.product-detail h1', 'Test-Produkt');
    }
}
```

---

## PantherTestCaseTrait mit anderen TestCase-Klassen

Fuer Projekte die andere Basis-Klassen nutzen (z.B. `LiipFunctionalTestBundle`),
gibt es den `PantherTestCaseTrait`:

```php
use Liip\FunctionalTestBundle\Test\WebTestCase;
use Symfony\Component\Panther\PantherTestCaseTrait;

class ProductTest extends WebTestCase
{
    use PantherTestCaseTrait;

    public function testWithFixturesAndPanther(): void
    {
        // Fixtures laden (LiipFunctionalTestBundle)
        $this->loadFixtures([
            \App\DataFixtures\ProductFixtures::class,
        ]);

        // Panther-Client nutzen
        $client = self::createPantherClient();
        $client->request('GET', '/products');

        $this->assertSelectorTextContains('.product-list', 'Fixture-Produkt');
    }
}
```

Weiteres Beispiel mit `ApiTestCase` (z.B. von `api-platform/core`):

```php
use ApiPlatform\Symfony\Bundle\Test\ApiTestCase;
use Symfony\Component\Panther\PantherTestCaseTrait;

class ProductApiE2ETest extends ApiTestCase
{
    use PantherTestCaseTrait;

    public function testApiAndBrowser(): void
    {
        // API-Platform-Client fuer API-Tests
        $apiClient = static::createClient();
        $response = $apiClient->request('GET', '/api/products');
        $this->assertResponseIsSuccessful();

        // Panther fuer Frontend-Tests
        $browser = self::createPantherClient();
        $browser->request('GET', '/products');
        $browser->waitFor('.product-grid');
        $this->assertSelectorExists('.product-card');
    }
}
```

---

## Webserver wird automatisch geteilt

Alle drei `create*Client()`-Methoden nutzen denselben PHP Built-In-Webserver-Prozess.
Der erste Aufruf startet ihn, weitere Aufrufe innerhalb derselben Test-Klasse
nutzen die laufende Instanz.

```php
public function testSharedServer(): void
{
    // Startet Webserver auf Port 9080
    $http = static::createHttpBrowserClient();

    // Nutzt denselben Webserver (kein Neustart)
    $panther = static::createPantherClient();

    // Beide sprechen http://127.0.0.1:9080 an
    $http->request('GET', '/');
    $panther->request('GET', '/');
}
```

---

## Performance-Abwaegung

| Kriterium | KernelBrowser | HttpBrowserClient | PantherClient |
|---|---|---|---|
| Startzeit | < 10ms | ~100ms (Server) | ~2-5s (Browser) |
| Request-Zeit | < 1ms | ~5-50ms | ~100-500ms |
| JavaScript | nein | nein | vollstaendig |
| Echte Netzwerk-Stack | nein | ja | ja |
| Echte Browser-Rendering | nein | nein | ja |
| CSS-Animationen | nein | nein | ja |
| Screenshots | nein | nein | ja |
| Empfohlen fuer | Unit/Integrationstests | Formulare, Links, SSR | SPA, JavaScript, E2E |

---

## Quellen

- https://symfony.com/doc/current/testing/end_to_end.html
- https://github.com/symfony/panther/blob/main/src/PantherTestCaseTrait.php
- https://symfony.com/doc/current/components/browser_kit.html
- https://symfony.com/doc/current/components/http_client.html
