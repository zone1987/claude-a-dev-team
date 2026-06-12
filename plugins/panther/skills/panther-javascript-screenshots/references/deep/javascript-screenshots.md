# Panther — JavaScript, Console-Logs und Screenshots

## JavaScript ausfuehren

Panther implementiert das `JavaScriptExecutor`-Interface von php-webdriver.

### executeScript — synchrones JavaScript

```php
// Rueckgabewert: primitiv, Array oder null
$result = $client->executeScript('return document.title;');
// => string

// DOM-Element uebergeben und zurueck bekommen
$element = $client->getCrawler()->filter('.my-class')->getElement(0);
$result = $client->executeScript('arguments[0].style.border = "2px solid red"; return arguments[0];', [$element]);

// Seiteneffekte ohne Rueckgabewert
$client->executeScript('window.scrollTo(0, document.body.scrollHeight);');

// Mehrere Argumente
$client->executeScript(
    'arguments[0].setAttribute(arguments[1], arguments[2]);',
    [$element, 'data-testid', 'my-element']
);
```

### executeAsyncScript — asynchrones JavaScript

Das Skript erhaelt als letztes Argument einen Callback, den es aufrufen muss.
Panther wartet bis der Callback aufgerufen wird (Timeout: WebDriver-Standard = 0ms,
daher `manage()->timeouts()->setScriptTimeout()` vorher setzen).

```php
// Timeout fuer async Scripts setzen
$client->manage()->timeouts()->setScriptTimeout(5); // Sekunden

// Warten auf asynchronen Vorgang
$result = $client->executeAsyncScript(
    'var callback = arguments[arguments.length - 1];
     setTimeout(function() { callback("done"); }, 1000);'
);
// => "done"

// Fetch-Request innerhalb des Browsers ausfuehren
$data = $client->executeAsyncScript(
    'var cb = arguments[arguments.length - 1];
     fetch("/api/data").then(r => r.json()).then(data => cb(data));'
);
```

---

## Browser-Console-Logs auslesen

Chrome unterstuetzt strukturierte Performance- und Browser-Logs via
`goog:loggingPrefs`-Capability. Firefox unterstuetzt dies nicht native.

### Konfiguration

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
                        'performance' => 'ALL',   // Netzwerk-Timing, Paint-Ereignisse etc.
                        // Weitere gueltige Kategorien: 'driver', 'client', 'server'
                    ],
                ],
            ]
        );

        $client->request('GET', '/');

        // Browser-Console-Logs lesen
        $consoleLogs = $client->getWebDriver()->manage()->getLog('browser');
        // Format: [['level' => 'WARNING', 'message' => '...', 'source' => 'javascript', 'timestamp' => 1234567890000], ...]

        foreach ($consoleLogs as $log) {
            echo $log['level'] . ': ' . $log['message'] . "\n";
        }

        // Performance-Logs lesen
        $performanceLogs = $client->getWebDriver()->manage()->getLog('performance');
        // Enthaelt Chrome DevTools Protocol Events als JSON in 'message'
    }
}
```

### Log-Level-Konstanten

| Level | Bedeutung |
|---|---|
| `'OFF'` | Keine Logs |
| `'SEVERE'` | Nur Fehler (console.error, JS-Exceptions) |
| `'WARNING'` | Fehler und Warnungen |
| `'INFO'` | Allgemeine Infos |
| `'DEBUG'` | Debug-Informationen |
| `'ALL'` | Alle Logs |

---

## Screenshots erstellen

### Manueller Screenshot

```php
// PNG-Datei schreiben
$client->takeScreenshot('/var/screenshots/my-test.png');

// Rueckgabewert: Pfad zur Datei (string)
$path = $client->takeScreenshot('/tmp/screenshot.png');

// Mit dynamischem Dateinamen
$client->takeScreenshot(sprintf('/var/screenshots/%s.png', date('Y-m-d_H-i-s')));
```

### Automatische Fehler-Screenshots

Erfordert `ServerExtension` in `phpunit.dist.xml` und `PANTHER_ERROR_SCREENSHOT_DIR`:

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

Dateiname-Format bei Fehler:
```
{DIR}/{YYYY-MM-DD_HH-II-SS}_{error|failure}_{Namespace-ClassName_methodName}-{clientIndex}.png
```

Beispiel:
```
var/screenshots/2024-01-15_14-30-00_failure_App-Tests-HomepageTest_testMyApp-0.png
```

`PANTHER_ERROR_SCREENSHOT_ATTACH=1` gibt ausserdem `[[ATTACHMENT|/pfad]]` auf
stdout aus (GitLab-CI-Artifact-Format).

### Screenshot im Test manuell mit Namen speichern

```php
public function testWithScreenshot(): void
{
    $client = static::createPantherClient();
    $client->request('GET', '/dashboard');

    // Zustand vor Aktion festhalten
    $client->takeScreenshot('/var/screenshots/before_click.png');

    $client->clickLink('Submit');
    $client->waitFor('.success-message');

    // Zustand nach Aktion festhalten
    $client->takeScreenshot('/var/screenshots/after_click.png');

    $this->assertSelectorTextContains('.success-message', 'Done');
}
```

---

## Real-Time-Applikationen testen (Mercure, WebSocket)

Fuer Real-Time-Features benoetigt man mehrere unabhaengige Browser-Sessions.

### Einen zweiten Panther-Client erstellen

```php
use Symfony\Component\Panther\PantherTestCase;

class ChatTest extends PantherTestCase
{
    public function testRealTimeChat(): void
    {
        // Erster Client (primaer, wird auch in self::$pantherClient gespeichert)
        $client1 = self::createPantherClient();
        $client1->request('GET', '/chat');

        // Zweiter Client (teilt denselben ChromeDriver/GeckoDriver-Prozess,
        // erstellt aber eine neue WebDriver-Session => neues Browser-Fenster/Tab)
        $client2 = self::createAdditionalPantherClient();
        $client2->request('GET', '/chat');

        // Client2 postet eine Nachricht
        $client2->submitForm('Post message', ['message' => 'Hallo Welt!']);

        // Client1 wartet auf die Nachricht via Mercure/WebSocket
        $client1->waitFor('.message');
        $this->assertSelectorTextContains('.message', 'Hallo Welt!');
    }
}
```

Hinweis: `createAdditionalPantherClient()` gibt einen neuen `Client` zurueck,
der denselben `BrowserManager` (ChromeDriver-Prozess) nutzt, aber eine eigene
WebDriver-Session hat. Beide Clients werden automatisch von `ServerExtension`
registriert und bei Fehler bekommt man einen Screenshot von jedem.

### Drei oder mehr Clients

```php
$client1 = self::createPantherClient();
$client2 = self::createAdditionalPantherClient();
$client3 = self::createAdditionalPantherClient(); // noch ein weiterer Client

$client1->request('GET', '/board');
$client2->request('GET', '/board');
$client3->request('GET', '/board');

$client1->clickLink('Start game');
$client2->waitFor('.game-started');
$client3->waitFor('.game-started');

$this->assertSelectorIsVisible('.game-started');
```

### Warten auf asynchrone Updates

```php
// Standard-Wait (DOM-Aenderung)
$client1->waitFor('.new-message');

// Auf Sichtbarkeit warten
$client1->waitForVisibility('.notification-badge');

// Auf Text-Inhalt warten
$client1->waitForElementToContain('.message-count', '3');

// Expliziter Timeout (Sekunden, Default ist durch WebDriverWait bestimmt)
use Facebook\WebDriver\WebDriverExpectedCondition;
$client1->getWebDriver()->wait(10)->until(
    WebDriverExpectedCondition::presenceOfElementLocated(
        \Facebook\WebDriver\WebDriverBy::cssSelector('.live-update')
    )
);
```

---

## Quellen

- https://symfony.com/doc/current/testing/end_to_end.html
- https://github.com/symfony/panther/blob/main/src/Client.php
- https://github.com/symfony/panther/blob/main/src/PantherTestCaseTrait.php
- https://github.com/symfony/panther/blob/main/src/ServerExtensionLegacy.php
- https://github.com/php-webdriver/php-webdriver (JavaScriptExecutor Interface)
