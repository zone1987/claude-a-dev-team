# Panther — JavaScript, console logs and screenshots

## Contents

- [Executing JavaScript](#executing-javascript)
- [Reading browser console logs](#reading-browser-console-logs)
- [Creating screenshots](#creating-screenshots)
- [Testing real-time applications (Mercure, WebSocket)](#testing-real-time-applications-mercure-websocket)
- [Sources](#sources)

## Executing JavaScript

Panther implements the `JavaScriptExecutor` interface from php-webdriver.

### executeScript — synchronous JavaScript

```php
// Return value: primitive, array or null
$result = $client->executeScript('return document.title;');
// => string

// Pass in a DOM element and get it back
$element = $client->getCrawler()->filter('.my-class')->getElement(0);
$result = $client->executeScript('arguments[0].style.border = "2px solid red"; return arguments[0];', [$element]);

// Side effects without a return value
$client->executeScript('window.scrollTo(0, document.body.scrollHeight);');

// Multiple arguments
$client->executeScript(
    'arguments[0].setAttribute(arguments[1], arguments[2]);',
    [$element, 'data-testid', 'my-element']
);
```

### executeAsyncScript — asynchronous JavaScript

The script receives a callback as its last argument, which it must invoke.
Panther waits until the callback is invoked (timeout: WebDriver default = 0ms,
so set `manage()->timeouts()->setScriptTimeout()` beforehand).

```php
// Set the timeout for async scripts
$client->manage()->timeouts()->setScriptTimeout(5); // seconds

// Wait for an asynchronous operation
$result = $client->executeAsyncScript(
    'var callback = arguments[arguments.length - 1];
     setTimeout(function() { callback("done"); }, 1000);'
);
// => "done"

// Perform a fetch request inside the browser
$data = $client->executeAsyncScript(
    'var cb = arguments[arguments.length - 1];
     fetch("/api/data").then(r => r.json()).then(data => cb(data));'
);
```

---

## Reading browser console logs

Chrome supports structured performance and browser logs via the
`goog:loggingPrefs` capability. Firefox does not support this natively.

### Configuration

```php
use Symfony\Component\Panther\PantherTestCase;

class LogTest extends PantherTestCase
{
    public function testConsoleLogs(): void
    {
        $client = self::createPantherClient(
            [],
            [],
            [
                'capabilities' => [
                    'goog:loggingPrefs' => [
                        'browser'     => 'ALL',   // console.log, console.warn, console.error etc.
                        'performance' => 'ALL',   // network timing, paint events etc.
                        // Further valid categories: 'driver', 'client', 'server'
                    ],
                ],
            ]
        );

        $client->request('GET', '/');

        // Read browser console logs
        $consoleLogs = $client->getWebDriver()->manage()->getLog('browser');
        // Format: [['level' => 'WARNING', 'message' => '...', 'source' => 'javascript', 'timestamp' => 1234567890000], ...]

        foreach ($consoleLogs as $log) {
            echo $log['level'] . ': ' . $log['message'] . "\n";
        }

        // Read performance logs
        $performanceLogs = $client->getWebDriver()->manage()->getLog('performance');
        // Contains Chrome DevTools Protocol events as JSON in 'message'
    }
}
```

### Log level constants

| Level | Meaning |
|---|---|
| `'OFF'` | No logs |
| `'SEVERE'` | Errors only (console.error, JS exceptions) |
| `'WARNING'` | Errors and warnings |
| `'INFO'` | General information |
| `'DEBUG'` | Debug information |
| `'ALL'` | All logs |

---

## Creating screenshots

### Manual screenshot

```php
// Write a PNG file
$client->takeScreenshot('/var/screenshots/my-test.png');

// Return value: path to the file (string)
$path = $client->takeScreenshot('/tmp/screenshot.png');

// With a dynamic file name
$client->takeScreenshot(sprintf('/var/screenshots/%s.png', date('Y-m-d_H-i-s')));
```

### Automatic error screenshots

Requires `ServerExtension` in `phpunit.dist.xml` and `PANTHER_ERROR_SCREENSHOT_DIR`:

```xml
<!-- phpunit.dist.xml -->
<extensions>
    <bootstrap class="Symfony\Component\Panther\ServerExtension"/>
</extensions>
<php>
    <server name="PANTHER_ERROR_SCREENSHOT_DIR" value="var/screenshots"/>
    <server name="PANTHER_ERROR_SCREENSHOT_ATTACH" value="1"/>
</php>
```

File name format on error:
```
{DIR}/{YYYY-MM-DD_HH-II-SS}_{error|failure}_{Namespace-ClassName_methodName}-{clientIndex}.png
```

Example:
```
var/screenshots/2024-01-15_14-30-00_failure_App-Tests-HomepageTest_testMyApp-0.png
```

`PANTHER_ERROR_SCREENSHOT_ATTACH=1` additionally prints `[[ATTACHMENT|/path]]` to
stdout (GitLab CI artifact format).

### Saving a screenshot manually with a name inside the test

```php
public function testWithScreenshot(): void
{
    $client = static::createPantherClient();
    $client->request('GET', '/dashboard');

    // Capture the state before the action
    $client->takeScreenshot('/var/screenshots/before_click.png');

    $client->clickLink('Submit');
    $client->waitFor('.success-message');

    // Capture the state after the action
    $client->takeScreenshot('/var/screenshots/after_click.png');

    $this->assertSelectorTextContains('.success-message', 'Done');
}
```

---

## Testing real-time applications (Mercure, WebSocket)

For real-time features you need several independent browser sessions.

### Creating a second Panther client

```php
use Symfony\Component\Panther\PantherTestCase;

class ChatTest extends PantherTestCase
{
    public function testRealTimeChat(): void
    {
        // First client (primary, also stored in self::$pantherClient)
        $client1 = self::createPantherClient();
        $client1->request('GET', '/chat');

        // Second client (shares the same ChromeDriver/GeckoDriver process,
        // but creates a new WebDriver session => new browser window/tab)
        $client2 = self::createAdditionalPantherClient();
        $client2->request('GET', '/chat');

        // Client2 posts a message
        $client2->submitForm('Post message', ['message' => 'Hallo Welt!']);

        // Client1 waits for the message via Mercure/WebSocket
        $client1->waitFor('.message');
        $this->assertSelectorTextContains('.message', 'Hallo Welt!');
    }
}
```

Note: `createAdditionalPantherClient()` returns a new `Client`
that uses the same `BrowserManager` (ChromeDriver process) but has its own
WebDriver session. Both clients are registered automatically by `ServerExtension`
and on failure you get a screenshot of each one.

### Three or more clients

```php
$client1 = self::createPantherClient();
$client2 = self::createAdditionalPantherClient();
$client3 = self::createAdditionalPantherClient(); // yet another client

$client1->request('GET', '/board');
$client2->request('GET', '/board');
$client3->request('GET', '/board');

$client1->clickLink('Start game');
$client2->waitFor('.game-started');
$client3->waitFor('.game-started');

$this->assertSelectorIsVisible('.game-started');
```

### Waiting for asynchronous updates

```php
// Standard wait (DOM change)
$client1->waitFor('.new-message');

// Wait for visibility
$client1->waitForVisibility('.notification-badge');

// Wait for text content
$client1->waitForElementToContain('.message-count', '3');

// Explicit timeout (seconds, the default is determined by WebDriverWait)
use Facebook\WebDriver\WebDriverExpectedCondition;
$client1->getWebDriver()->wait(10)->until(
    WebDriverExpectedCondition::presenceOfElementLocated(
        \Facebook\WebDriver\WebDriverBy::cssSelector('.live-update')
    )
);
```

---

## Sources

- https://symfony.com/doc/current/testing/end_to_end.html
- https://github.com/symfony/panther/blob/main/src/Client.php
- https://github.com/symfony/panther/blob/main/src/PantherTestCaseTrait.php
- https://github.com/symfony/panther/blob/main/src/ServerExtensionLegacy.php
- https://github.com/php-webdriver/php-webdriver (JavaScriptExecutor interface)
