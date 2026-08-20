# Panther Client — Complete API Reference

`Symfony\Component\Panther\Client`

Implements `Symfony\Component\BrowserKit\AbstractBrowser` and, beyond that, the
`Facebook\WebDriver\WebDriver` interface.

## Contents

- [Static Factory Methods](#static-factory-methods)
- [Lifecycle](#lifecycle)
- [Navigation](#navigation)
- [Waiting Methods (all with timeout/interval)](#waiting-methods-all-with-timeoutinterval)
- [JavaScript Execution](#javascript-execution)
- [State Queries](#state-queries)
- [WebDriver Access](#webdriver-access)
- [Input Devices](#input-devices)
- [Forms and Links](#forms-and-links)
- [Window Management](#window-management)
- [Element Lookup (low-level)](#element-lookup-low-level)
- [CookieJar](#cookiejar)
- [Complete Example](#complete-example)

## Static Factory Methods

### createChromeClient

```php
public static function createChromeClient(
    ?string $chromeDriverBinary = null,   // path to chromedriver binary; null = auto-detect
    ?array  $arguments          = null,   // Chrome browser arguments, e.g. ['--window-size=1920,1080']
    array   $options            = [],     // manager options (capabilities, chromedriver_arguments)
    ?string $baseUri            = null    // base URI (e.g. 'http://localhost:9080')
): self
```

Example:
```php
$client = Client::createChromeClient(
    null,
    ['--window-size=1500,4000', '--disable-gpu'],
    ['capabilities' => ['acceptInsecureCerts' => true]],
    'http://127.0.0.1:9080'
);
```

### createFirefoxClient

```php
public static function createFirefoxClient(
    ?string $geckodriverBinary = null,    // path to geckodriver; null = auto-detect
    ?array  $arguments         = null,   // Firefox arguments
    array   $options           = [],     // manager options (capabilities)
    ?string $baseUri           = null
): self
```

Example:
```php
use Facebook\WebDriver\WebDriverDimension;
$client = Client::createFirefoxClient();
$client->manage()->window()->setSize(new WebDriverDimension(1500, 4000));
```

### createSeleniumClient

```php
public static function createSeleniumClient(
    ?string                    $host         = null,  // Selenium Hub URL, e.g. 'http://127.0.0.1:4444/wd/hub'
    ?WebDriverCapabilities     $capabilities = null,  // desired capabilities
    ?string                    $baseUri      = null,
    array                      $options      = []
): self
```

---

## Lifecycle

### start

```php
public function start(): void
```

Starts the WebDriver process (ChromeDriver/GeckoDriver) and opens the browser.
Called automatically when needed.

### quit

```php
public function quit(bool $quitBrowserManager = true): void
```

Terminates the browser. With `$quitBrowserManager = false`, only the session is closed,
the ChromeDriver process keeps running.

### restart

```php
public function restart(): void
```

Terminates the browser and starts it again. Clears history and cookies.

### close

```php
public function close(): WebDriver
```

Closes the current browser tab (not the entire browser).

### ping

```php
public function ping(int $timeout = 1000): bool
```

Checks whether the WebDriver connection is still active.
- `$timeout`: timeout in milliseconds (default: 1000)
- Returns: `true` if connected, `false` otherwise
- Useful in long tests to detect a session timeout

---

## Navigation

### request

```php
public function request(
    string  $method,                  // HTTP method: 'GET', 'POST', etc.
    string  $uri,                     // URL or path (relative to baseUri)
    array   $parameters    = [],      // query/POST parameters
    array   $files         = [],      // file uploads
    array   $server        = [],      // server parameters / HTTP headers
    ?string $content       = null,    // request body as string
    bool    $changeHistory = true     // update history
): PantherCrawler
```

### get

```php
public function get(string $url): self
```

Short variant for GET requests. Returns the client itself (fluent interface).

### back

```php
public function back(): PantherCrawler
```

Navigates one page back (browser history). Returns the crawler of the new page.

### forward

```php
public function forward(): PantherCrawler
```

Navigates one page forward.

### reload

```php
public function reload(): PantherCrawler
```

Reloads the current page. Equivalent to F5.

### navigate

```php
public function navigate(): WebDriverNavigationInterface
```

Returns the WebDriver `navigate()` object for methods such as `navigateTo($url)`,
`back()`, `forward()`, `refresh()`.

---

## Waiting Methods (all with timeout/interval)

All waitFor methods share the same signature structure:
- `$locator`: CSS selector (e.g. `'#my-id'`, `'.my-class'`, `'button[type=submit]'`)
- `$timeoutInSecond`: max. wait time in seconds (default: `30`)
- `$intervalInMillisecond`: polling interval in ms (default: `250`)
- Returns: `PantherCrawler` with the element that was found

### waitFor

```php
public function waitFor(
    string $locator,
    int    $timeoutInSecond        = 30,
    int    $intervalInMillisecond  = 250
): PantherCrawler
```

Waits until at least one element matching the selector is present in the DOM.

### waitForStaleness

```php
public function waitForStaleness(
    string $locator,
    int    $timeoutInSecond       = 30,
    int    $intervalInMillisecond = 250
): PantherCrawler
```

Waits until the element is removed from the DOM (stale).

### waitForVisibility

```php
public function waitForVisibility(
    string $locator,
    int    $timeoutInSecond       = 30,
    int    $intervalInMillisecond = 250
): PantherCrawler
```

Waits until the element is visible (not `display:none`/`visibility:hidden`).

### waitForInvisibility

```php
public function waitForInvisibility(
    string $locator,
    int    $timeoutInSecond       = 30,
    int    $intervalInMillisecond = 250
): PantherCrawler
```

Waits until the element becomes invisible or is removed from the DOM.

### waitForElementToContain

```php
public function waitForElementToContain(
    string $locator,
    string $text,
    int    $timeoutInSecond       = 30,
    int    $intervalInMillisecond = 250
): PantherCrawler
```

Waits until the element contains `$text` as its text content.

### waitForElementToNotContain

```php
public function waitForElementToNotContain(
    string $locator,
    string $text,
    int    $timeoutInSecond       = 30,
    int    $intervalInMillisecond = 250
): PantherCrawler
```

Waits until the element NO LONGER contains `$text`.

### waitForAttributeToContain

```php
public function waitForAttributeToContain(
    string $locator,
    string $attribute,
    string $text,
    int    $timeoutInSecond       = 30,
    int    $intervalInMillisecond = 250
): PantherCrawler
```

Waits until the element's `$attribute` attribute contains `$text`.

```php
$client->waitForAttributeToContain('.price', 'data-old-price', '25');
```

### waitForAttributeToNotContain

```php
public function waitForAttributeToNotContain(
    string $locator,
    string $attribute,
    string $text,
    int    $timeoutInSecond       = 30,
    int    $intervalInMillisecond = 250
): PantherCrawler
```

### waitForEnabled

```php
public function waitForEnabled(
    string $locator,
    int    $timeoutInSecond       = 30,
    int    $intervalInMillisecond = 250
): PantherCrawler
```

Waits until a button/input element loses its `disabled` state.

### waitForDisabled

```php
public function waitForDisabled(
    string $locator,
    int    $timeoutInSecond       = 30,
    int    $intervalInMillisecond = 250
): PantherCrawler
```

Waits until an element becomes `disabled`.

### wait (low-level)

```php
public function wait(
    int $timeoutInSecond        = 30,
    int $intervalInMillisecond  = 250
): \Facebook\WebDriver\WebDriverWait
```

Returns a `WebDriverWait` object for custom conditions:

```php
use Facebook\WebDriver\WebDriverExpectedCondition;

$client->wait(10, 500)->until(
    WebDriverExpectedCondition::titleContains('Dashboard')
);
```

---

## JavaScript Execution

### executeScript

```php
public function executeScript(
    string $script,       // JS code as string
    array  $arguments = [] // arguments passed to JS (as `arguments[0]`, etc.)
): mixed
```

Synchronous JS. Returns the value of the JS `return` statement.

```php
// Scroll to top
$client->executeScript('window.scrollTo(0, 0);');

// Read element value
$value = $client->executeScript('return arguments[0].value;', [$element]);

// Read localStorage
$token = $client->executeScript('return localStorage.getItem("token");');
```

### executeAsyncScript

```php
public function executeAsyncScript(
    string $script,
    array  $arguments = []
): mixed
```

Asynchronous JS. The script must call `arguments[arguments.length - 1]` as the callback.

```php
$result = $client->executeAsyncScript(
    'setTimeout(() => arguments[0]("done"), 1000);'
);
```

---

## State Queries

### getPageSource

```php
public function getPageSource(): string
```

Returns the complete HTML source of the current page (after JS rendering).

### getCurrentURL

```php
public function getCurrentURL(): string
```

Returns the browser's current URL (after redirects).

### getTitle

```php
public function getTitle(): string
```

Returns the content of the current page's `<title>` tag.

### refreshCrawler

```php
public function refreshCrawler(): PantherCrawler
```

Refreshes the crawler based on the current DOM state (after JS changes).
Returns a new `PantherCrawler`.

### getCrawler

```php
public function getCrawler(): PantherCrawler
```

Returns the most recently created crawler (without a DOM refresh).

### takeScreenshot

```php
public function takeScreenshot(?string $saveAs = null): string
```

Creates a screenshot of the browser window.
- `$saveAs`: file path to save to (PNG). If `null`, no file is saved.
- Returns: PNG data as a Base64-encoded string.

```php
$client->takeScreenshot('/tmp/before-click.png');
$client->click($link);
$client->takeScreenshot('/tmp/after-click.png');
```

---

## WebDriver Access

### getWebDriver

```php
public function getWebDriver(): \Facebook\WebDriver\WebDriver
```

Returns the raw `WebDriver` instance for all WebDriver methods that are not exposed
directly in Panther.

```php
$driver = $client->getWebDriver();
$driver->manage()->window()->maximize();
$logs = $driver->manage()->getLog('browser');
```

### manage

```php
public function manage(): \Facebook\WebDriver\WebDriverOptions
```

Access to browser management (cookies, logs, window, timeouts):

```php
$options = $client->manage();
$options->window()->maximize();
$options->window()->setSize(new WebDriverDimension(1920, 1080));
$options->timeouts()->implicitlyWait(5);
$options->timeouts()->pageLoadTimeout(30);
$cookies = $options->getCookies();
$options->addCookie(['name' => 'foo', 'value' => 'bar']);
$options->deleteCookieNamed('foo');
$options->deleteAllCookies();
```

### switchTo

```php
public function switchTo(): \Facebook\WebDriver\WebDriverTargetLocator
```

Switches the context (frame, window, alert):

```php
$client->switchTo()->frame(0);          // switch into frame
$client->switchTo()->defaultContent();  // back to the main document
$client->switchTo()->alert()->accept(); // confirm alert
$client->switchTo()->window($handle);   // another tab/window
```

### navigate

```php
public function navigate(): \Facebook\WebDriver\WebDriverNavigationInterface
```

```php
$client->navigate()->to('https://example.com');
$client->navigate()->back();
$client->navigate()->forward();
$client->navigate()->refresh();
```

---

## Input Devices

### getMouse

```php
public function getMouse(): \Symfony\Component\Panther\WebDriver\WebDriverMouse
```

Returns Panther's own `WebDriverMouse` object (wraps `BaseWebDriverMouse` and adds
CSS selector methods such as `clickTo`, `doubleClickTo`, `contextClickTo`, `mouseMoveTo`,
`mouseDownTo`, `mouseUpTo`). See the `panther-interactions` skill for details.

Source: `src/Client.php:getMouse()` + `src/WebDriver/WebDriverMouse.php`

### getKeyboard

```php
public function getKeyboard(): \Facebook\WebDriver\WebDriverKeyboard
```

Returns the `WebDriverKeyboard` object. See the `panther-interactions` skill for details.

---

## Forms and Links

### click

```php
public function click(
    \Symfony\Component\DomCrawler\Link $link,
    array $serverParameters = []
): \Symfony\Component\DomCrawler\Crawler
```

Clicks a `Link` object (from `$crawler->selectLink(...)->link()`).

### clickLink

```php
// inherited from BrowserKit AbstractBrowser
public function clickLink(string $linkText): Crawler
```

Clicks a link by its text.

```php
$client->clickLink('Zur Startseite');
```

### submit

```php
public function submit(
    \Symfony\Component\DomCrawler\Form $form,
    array $values         = [],
    array $serverParameters = []
): \Symfony\Component\DomCrawler\Crawler
```

### submitForm

```php
// inherited from BrowserKit AbstractBrowser
public function submitForm(
    string $buttonText,
    array  $fieldValues = [],
    string $method      = null,
    array  $serverParameters = []
): Crawler
```

```php
$client->submitForm('Anmelden', [
    'email'    => 'user@example.com',
    'password' => 'secret',
]);
```

---

## Window Management

### getWindowHandle

```php
public function getWindowHandle(): string
```

Returns the handle of the current browser window/tab.

### getWindowHandles

```php
public function getWindowHandles(): array
```

Returns all open window/tab handles.

---

## Element Lookup (low-level)

### findElement

```php
public function findElement(\Facebook\WebDriver\WebDriverBy $locator): \Facebook\WebDriver\WebDriverElement
```

### findElements

```php
public function findElements(\Facebook\WebDriver\WebDriverBy $locator): array
```

```php
use Facebook\WebDriver\WebDriverBy;

$el    = $client->findElement(WebDriverBy::cssSelector('.my-class'));
$items = $client->findElements(WebDriverBy::cssSelector('li'));
```

---

## CookieJar

### getCookieJar

```php
public function getCookieJar(): \Symfony\Component\Panther\Cookie\CookieJar
```

Panther's own `CookieJar` class (wraps WebDriver cookies). Methods:

Source: `src/Client.php:getCookieJar()` + `src/Cookie/CookieJar.php`

```php
$jar = $client->getCookieJar();
$jar->all();                    // array<Cookie>
$jar->get(string $name): ?Cookie
$jar->set(Cookie $cookie): void
$jar->allValues(string $uri): array   // ['name' => 'value', ...]
$jar->allRawValues(string $uri): array
$jar->expire(string $name): void
$jar->clear(): void
```

---

## Complete Example

```php
use Symfony\Component\Panther\Client;
use Symfony\Component\Panther\PantherTestCase;

class CheckoutTest extends PantherTestCase
{
    public function testCheckout(): void
    {
        $client = static::createPantherClient([
            'port' => 9080,
        ]);

        // Load page
        $client->request('GET', '/shop/cart');

        // Wait for a dynamically loaded element
        $crawler = $client->waitFor('.cart-items', 10, 500);

        // Screenshot before purchase
        $client->takeScreenshot('/tmp/cart-before.png');

        // Fill in the form and submit it
        $client->submitForm('Zur Kasse', ['coupon' => 'SAVE10']);

        // Wait until the redirect has completed
        $client->waitFor('.payment-form');

        // Assertions
        $this->assertSelectorTextContains('.total', '90,00');
        $this->assertPageTitleContains('Kasse');
        $this->assertSelectorAttributeContains('.step', 'data-step', '2');

        // JavaScript
        $token = $client->executeScript('return window.__CSRF_TOKEN__;');
        $this->assertNotEmpty($token);

        // Check browser logs
        $logs = $client->getWebDriver()->manage()->getLog('browser');
        $errors = array_filter($logs, fn($log) => $log['level'] === 'SEVERE');
        $this->assertEmpty($errors, 'Keine JS-Fehler erwartet');

        // Check connection
        $this->assertTrue($client->ping());

        $client->quit();
    }
}
```

---

Sources:
- https://raw.githubusercontent.com/symfony/panther/main/src/Client.php
- https://symfony.com/doc/current/testing/end_to_end.html
- https://github.com/php-webdriver/php-webdriver
