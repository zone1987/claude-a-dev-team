# PantherTestCase — Complete reference

## Contents

- [Class hierarchy](#class-hierarchy)
- [Constants](#constants)
- [Client factory methods](#client-factory-methods)
- [All assertions — complete reference](#all-assertions-complete-reference)
- [PantherTestCaseTrait (without Symfony)](#panthertestcasetrait-without-symfony)
- [Multi-domain tests](#multi-domain-tests)
- [Interactive debug mode](#interactive-debug-mode)

## Class hierarchy

```
PHPUnit\Framework\TestCase
  └── Symfony\Bundle\FrameworkBundle\Test\WebTestCase  (only for Symfony apps)
        └── Symfony\Component\Panther\PantherTestCase
```

Without a Symfony app, directly:
```
PHPUnit\Framework\TestCase
  + Symfony\Component\Panther\PantherTestCaseTrait (as a trait)
```

## Constants

```php
PantherTestCase::CHROME   = 'chrome'
PantherTestCase::FIREFOX  = 'firefox'
PantherTestCase::SELENIUM = 'selenium'
```

## Client factory methods

### createPantherClient

```php
protected static function createPantherClient(
    array $options = [],
    array $kernelOptions = [],
    array $managerOptions = []
): \Symfony\Component\Panther\Client
```

**$options — key reference:**

| Key                   | Type      | Default     | Description                                          |
|-----------------------|-----------|-------------|------------------------------------------------------|
| `webServerDir`        | string    | `./public/` | Document root of the integrated PHP server           |
| `hostname`            | string    | `127.0.0.1` | Hostname of the test server                          |
| `port`                | int       | `9080`      | Port of the test server                              |
| `router`              | string    | —           | Path to the PHP router script                        |
| `external_base_uri`   | string\|null | null    | URI of an external server (prevents the internal start)|
| `readinessPath`       | string    | `''`        | Path for the health check before the test starts; empty = the base URL is checked |
| `env`                 | array     | `[]`        | Additional environment variables for the server      |
| `browser`             | string    | `chrome`    | `'chrome'`, `'firefox'`, `'selenium'`                |

**$managerOptions — important keys:**

| Key                       | Description                                                    |
|---------------------------|----------------------------------------------------------------|
| `capabilities`            | `WebDriverCapabilities` object or array with browser caps      |
| `chromedriver_arguments`  | `array` — e.g. `['--log-path=...', '--log-level=DEBUG']`       |
| `host`                    | Selenium hub URL (only when `browser = 'selenium'`)            |

**Examples:**

```php
// Default (Chrome, headless)
$client = static::createPantherClient();

// Firefox
$client = static::createPantherClient(['browser' => static::FIREFOX]);

// External server (no integrated PHP server)
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

// Custom port and web root
$client = static::createPantherClient([
    'hostname'      => '127.0.0.1',
    'port'          => 8080,
    'webServerDir'  => './public',
]);

// Browser console logging
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

Creates a second, isolated browser instance. Both instances share the same test server.
Assertions are always executed on the **primary** client.

```php
public function testRealTimeChat(): void
{
    $client1 = static::createPantherClient();
    $client1->request('GET', '/chat');

    $client2 = static::createAdditionalPantherClient();
    $client2->request('GET', '/chat');
    $client2->submitForm('Senden', ['message' => 'Hallo!']);

    // Wait until the message is visible in client 1
    $client1->waitFor('.message');

    // The assertion runs on $client1 (the primary browser)
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

Options: the same key table as `createPantherClient`, plus:

| Key                   | Description                               |
|-----------------------|-------------------------------------------|
| `http_client_options` | Array for `HttpClient::create()` options  |

### createClient (Symfony WebTestCase)

```php
protected static function createClient(
    array $options = [],
    array $server = []
): \Symfony\Bundle\FrameworkBundle\KernelBrowser
```

Only available when Symfony's `WebTestCase` is extended.

### startWebServer / stopWebServer

```php
public static function startWebServer(array $options = []): void
public static function stopWebServer(): void
public static function isWebServerStarted(): bool
```

## All assertions — complete reference

### Page title assertions

```php
assertPageTitleSame(string $expectedTitle, string $message = ''): void
```
Checks whether the page title matches exactly.

```php
assertPageTitleContains(string $expectedTitle, string $message = ''): void
```
Checks whether the page title contains the value.

---

### Selector existence

```php
assertSelectorExists(string $selector, string $message = ''): void
```
Fails when no element is found with the CSS selector.

```php
assertSelectorNotExists(string $selector, string $message = ''): void
```
Fails when at least one element is found.

---

### Selector text

```php
assertSelectorTextContains(string $selector, string $text, string $message = ''): void
```
Checks whether the `.textContent` of the first matching element contains `$text`.

```php
assertSelectorTextNotContains(string $selector, string $text, string $message = ''): void
```
Checks that `.textContent` does NOT contain `$text`.

---

### Visibility

```php
assertSelectorIsVisible(string $locator): void
```
Checks whether the element is displayed (not `display:none`, `visibility:hidden`).

```php
assertSelectorIsNotVisible(string $locator): void
```
Checks whether the element is hidden.

```php
assertSelectorWillBeVisible(string $locator): void
```
Waits (max. 30s, 250ms interval) until the element becomes visible, then asserts.

```php
assertSelectorWillNotBeVisible(string $locator): void
```
Waits until the element disappears.

---

### Enabled/Disabled

```php
assertSelectorIsEnabled(string $locator): void
```
Checks whether the element (button, input, etc.) is not disabled.

```php
assertSelectorIsDisabled(string $locator): void
```
Checks whether the element is disabled.

```php
assertSelectorWillBeEnabled(string $locator): void
```
Waits until the element becomes enabled.

```php
assertSelectorWillBeDisabled(string $locator): void
```
Waits until the element becomes disabled.

---

### Existence (waitFor variants)

```php
assertSelectorWillExist(string $locator): void
```
Waits until the CSS selector finds at least one element in the DOM.

```php
assertSelectorWillNotExist(string $locator): void
```
Waits until the element is removed from the DOM (staleness).

---

### Text (waitFor variants)

```php
assertSelectorWillContain(string $locator, string $text): void
```
Waits until the element contains the text.

```php
assertSelectorWillNotContain(string $locator, string $text): void
```
Waits until the element no longer contains the text.

---

### Attributes

```php
assertSelectorAttributeContains(string $locator, string $attribute, ?string $text = null): void
```
Checks whether the element's `$attribute` attribute contains `$text` (or is present when `$text = null`).

```php
assertSelectorAttributeNotContains(string $locator, string $attribute, string $text): void
```
Checks that the attribute does NOT contain `$text`.

```php
assertSelectorAttributeWillContain(string $locator, string $attribute, string $text): void
```
Waits until the attribute contains `$text`.

```php
assertSelectorAttributeWillNotContain(string $locator, string $attribute, string $text): void
```
Waits until the attribute no longer contains `$text`.

---

## PantherTestCaseTrait (without Symfony)

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

## Multi-domain tests

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

## Interactive debug mode

```bash
PANTHER_NO_HEADLESS=1 vendor/bin/phpunit --debug
```

When a test fails, the browser is opened and pauses until Enter is pressed.
Requires the PHPUnit extension in `phpunit.dist.xml`.

---

Sources:
- https://symfony.com/doc/current/testing/end_to_end.html
- `src/PantherTestCaseTrait.php` (`$defaultOptions`, `createPantherClient`, `createAdditionalPantherClient`, `createHttpBrowserClient`, `startWebServer`)
- `src/WebTestAssertionsTrait.php` (all assert* methods)
- `src/PantherTestCase.php` (constants CHROME/FIREFOX/SELENIUM)
- `src/WebDriver/PantherWebDriverExpectedCondition.php` (wait conditions)
