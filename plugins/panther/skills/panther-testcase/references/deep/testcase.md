# PantherTestCase — Vollstandige Referenz

## Klassen-Hierarchie

```
PHPUnit\Framework\TestCase
  └── Symfony\Bundle\FrameworkBundle\Test\WebTestCase  (nur bei Symfony-Apps)
        └── Symfony\Component\Panther\PantherTestCase
```

Ohne Symfony-App direkt:
```
PHPUnit\Framework\TestCase
  + Symfony\Component\Panther\PantherTestCaseTrait (als Trait)
```

## Konstanten

```php
PantherTestCase::CHROME   = 'chrome'
PantherTestCase::FIREFOX  = 'firefox'
PantherTestCase::SELENIUM = 'selenium'
```

## Client-Factory-Methoden

### createPantherClient

```php
protected static function createPantherClient(
    array $options = [],
    array $kernelOptions = [],
    array $managerOptions = []
): \Symfony\Component\Panther\Client
```

**$options — Schlussel-Referenz:**

| Schlussel             | Typ       | Default     | Beschreibung                                         |
|-----------------------|-----------|-------------|------------------------------------------------------|
| `webServerDir`        | string    | `./public/` | Document-Root des integrierten PHP-Servers           |
| `hostname`            | string    | `127.0.0.1` | Hostname des Testservers                             |
| `port`                | int       | `9080`      | Port des Testservers                                 |
| `router`              | string    | —           | Pfad zum PHP-Router-Script                           |
| `external_base_uri`   | string\|null | null    | URI eines externen Servers (verhindert internen Start)|
| `readinessPath`       | string    | `''`        | Pfad fur Health-Check vor Teststart; leer = Basis-URL wird gepruft |
| `env`                 | array     | `[]`        | Zusatzliche Umgebungsvariablen fur den Server        |
| `browser`             | string    | `chrome`    | `'chrome'`, `'firefox'`, `'selenium'`                |

**$managerOptions — Wichtige Schlussel:**

| Schlussel                 | Beschreibung                                                   |
|---------------------------|----------------------------------------------------------------|
| `capabilities`            | `WebDriverCapabilities`-Objekt oder Array mit Browser-Caps     |
| `chromedriver_arguments`  | `array` — z. B. `['--log-path=...', '--log-level=DEBUG']`      |
| `host`                    | Selenium-Hub-URL (nur bei `browser = 'selenium'`)              |

**Beispiele:**

```php
// Standard (Chrome, headless)
$client = static::createPantherClient();

// Firefox
$client = static::createPantherClient(['browser' => static::FIREFOX]);

// Externer Server (kein integrierter PHP-Server)
$client = static::createPantherClient([
    'external_base_uri' => 'https://my-staging.example.com',
]);

// Selenium Grid
use Facebook\WebDriver\Remote\DesiredCapabilities;
$client = static::createPantherClient(
    options: ['browser' => static::SELENIUM],
    managerOptions: [
        'host'         => 'http://selenium-hub:4444',
        'capabilities' => DesiredCapabilities::firefox(),
    ]
);

// Benutzerdefinierter Port und WebRoot
$client = static::createPantherClient([
    'hostname'      => '127.0.0.1',
    'port'          => 8080,
    'webServerDir'  => './public',
]);

// Browser-Console-Logging
$client = static::createPantherClient(
    [],
    [],
    [
        'capabilities' => [
            'goog:loggingPrefs' => [
                'browser'     => 'ALL',
                'performance' => 'ALL',
            ],
        ],
    ]
);
$client->request('GET', '/');
$logs = $client->getWebDriver()->manage()->getLog('browser');
```

### createAdditionalPantherClient

```php
protected static function createAdditionalPantherClient(): \Symfony\Component\Panther\Client
```

Erzeugt eine zweite, isolierte Browser-Instanz. Beide Instanzen teilen denselben Test-Server.
Assertions werden immer auf dem **primaren** Client ausgefuhrt.

```php
public function testRealTimeChat(): void
{
    $client1 = static::createPantherClient();
    $client1->request('GET', '/chat');

    $client2 = static::createAdditionalPantherClient();
    $client2->request('GET', '/chat');
    $client2->submitForm('Senden', ['message' => 'Hallo!']);

    // Warten bis Nachricht in Client 1 sichtbar
    $client1->waitFor('.message');

    // Assertion lauft auf $client1 (primarerer Browser)
    $this->assertSelectorTextContains('.message', 'Hallo!');
}
```

### createHttpBrowserClient

```php
protected static function createHttpBrowserClient(
    array $options = [],
    array $kernelOptions = []
): \Symfony\Component\BrowserKit\HttpBrowser
```

Optionen: dieselbe Schlussel-Tabelle wie `createPantherClient`, plus:

| Schlussel             | Beschreibung                              |
|-----------------------|-------------------------------------------|
| `http_client_options` | Array fur `HttpClient::create()` Optionen |

### createClient (Symfony WebTestCase)

```php
protected static function createClient(
    array $options = [],
    array $server = []
): \Symfony\Bundle\FrameworkBundle\KernelBrowser
```

Nur verfugbar wenn Symfony `WebTestCase` erweitert wird.

### startWebServer / stopWebServer

```php
public static function startWebServer(array $options = []): void
public static function stopWebServer(): void
public static function isWebServerStarted(): bool
```

## Alle Assertions — Vollstandige Referenz

### Page-Title-Assertions

```php
assertPageTitleSame(string $expectedTitle, string $message = ''): void
```
Pruft, ob der Seitentitel exakt ubereinstimmt.

```php
assertPageTitleContains(string $expectedTitle, string $message = ''): void
```
Pruft, ob der Seitentitel den Wert enthalt.

---

### Selector-Existenz

```php
assertSelectorExists(string $selector, string $message = ''): void
```
Schlagt fehl wenn kein Element mit CSS-Selektor gefunden wird.

```php
assertSelectorNotExists(string $selector, string $message = ''): void
```
Schlagt fehl wenn mindestens ein Element gefunden wird.

---

### Selector-Text

```php
assertSelectorTextContains(string $selector, string $text, string $message = ''): void
```
Pruft ob `.textContent` des ersten passenden Elements `$text` enthalt.

```php
assertSelectorTextNotContains(string $selector, string $text, string $message = ''): void
```
Pruft dass `.textContent` `$text` NICHT enthalt.

---

### Sichtbarkeit

```php
assertSelectorIsVisible(string $locator): void
```
Pruft ob das Element angezeigt wird (nicht `display:none`, `visibility:hidden`).

```php
assertSelectorIsNotVisible(string $locator): void
```
Pruft ob das Element versteckt ist.

```php
assertSelectorWillBeVisible(string $locator): void
```
Wartet (max. 30s, 250ms Intervall) bis das Element sichtbar wird, dann Assertion.

```php
assertSelectorWillNotBeVisible(string $locator): void
```
Wartet bis das Element verschwindet.

---

### Enabled/Disabled

```php
assertSelectorIsEnabled(string $locator): void
```
Pruft ob Element (Button, Input, etc.) nicht disabled ist.

```php
assertSelectorIsDisabled(string $locator): void
```
Pruft ob Element disabled ist.

```php
assertSelectorWillBeEnabled(string $locator): void
```
Wartet bis Element enabled wird.

```php
assertSelectorWillBeDisabled(string $locator): void
```
Wartet bis Element disabled wird.

---

### Existenz (waitFor-Varianten)

```php
assertSelectorWillExist(string $locator): void
```
Wartet bis der CSS-Selektor mindestens ein Element im DOM findet.

```php
assertSelectorWillNotExist(string $locator): void
```
Wartet bis das Element aus dem DOM entfernt wird (Staleness).

---

### Text (waitFor-Varianten)

```php
assertSelectorWillContain(string $locator, string $text): void
```
Wartet bis das Element den Text enthalt.

```php
assertSelectorWillNotContain(string $locator, string $text): void
```
Wartet bis das Element den Text NICHT mehr enthalt.

---

### Attribute

```php
assertSelectorAttributeContains(string $locator, string $attribute, ?string $text = null): void
```
Pruft ob das Attribut `$attribute` des Elements `$text` enthalt (oder vorhanden ist wenn `$text = null`).

```php
assertSelectorAttributeNotContains(string $locator, string $attribute, string $text): void
```
Pruft dass das Attribut `$text` NICHT enthalt.

```php
assertSelectorAttributeWillContain(string $locator, string $attribute, string $text): void
```
Wartet bis das Attribut `$text` enthalt.

```php
assertSelectorAttributeWillNotContain(string $locator, string $attribute, string $text): void
```
Wartet bis das Attribut `$text` NICHT mehr enthalt.

---

## PantherTestCaseTrait (ohne Symfony)

```php
use Symfony\Component\Panther\PantherTestCaseTrait;
use Liip\FunctionalTestBundle\Test\WebTestCase;

class MyTest extends WebTestCase
{
    use PantherTestCaseTrait;

    public function testWithFixtures(): void
    {
        $this->loadFixtures([]);
        $client = static::createPantherClient();
        $client->request('GET', '/');
    }
}
```

## Multi-Domain-Tests

```php
use PHPUnit\Framework\Attributes\RunInSeparateProcess;

class MultiDomainTest extends PantherTestCase
{
    #[RunInSeparateProcess]
    public function testExternalDomain(): void
    {
        $client = static::createPantherClient([
            'external_base_uri' => 'http://other-domain.localhost:8080',
        ]);
        $client->request('GET', '/');
    }
}
```

## Interaktiver Debug-Modus

```bash
PANTHER_NO_HEADLESS=1 vendor/bin/phpunit --debug
```

Wenn ein Test fehlschlagt, wird der Browser geoffnet und pausiert, bis Enter gedruckt wird.
Erfordert die PHPUnit-Extension in `phpunit.dist.xml`.

---

Quellen:
- https://symfony.com/doc/current/testing/end_to_end.html
- `src/PantherTestCaseTrait.php` (`$defaultOptions`, `createPantherClient`, `createAdditionalPantherClient`, `createHttpBrowserClient`, `startWebServer`)
- `src/WebTestAssertionsTrait.php` (alle assert*-Methoden)
- `src/PantherTestCase.php` (Konstanten CHROME/FIREFOX/SELENIUM)
- `src/WebDriver/PantherWebDriverExpectedCondition.php` (wait-Conditions)
