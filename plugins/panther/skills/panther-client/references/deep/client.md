# Panther Client — Vollstandige API-Referenz

`Symfony\Component\Panther\Client`

Implementiert `Symfony\Component\BrowserKit\AbstractBrowser` und daruber hinaus das
`Facebook\WebDriver\WebDriver`-Interface.

## Static Factory Methods

### createChromeClient

```php
public static function createChromeClient(
    ?string $chromeDriverBinary = null,   // Pfad zu chromedriver-Binary; null = auto-detect
    ?array  $arguments          = null,   // Chrome-Browser-Argumente, z. B. ['--window-size=1920,1080']
    array   $options            = [],     // Manager-Optionen (capabilities, chromedriver_arguments)
    ?string $baseUri            = null    // Basis-URI (z. B. 'http://localhost:9080')
): self
```

Beispiel:
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
    ?string $geckodriverBinary = null,    // Pfad zu geckodriver; null = auto-detect
    ?array  $arguments         = null,   // Firefox-Argumente
    array   $options           = [],     // Manager-Optionen (capabilities)
    ?string $baseUri           = null
): self
```

Beispiel:
```php
use Facebook\WebDriver\WebDriverDimension;
$client = Client::createFirefoxClient();
$client->manage()->window()->setSize(new WebDriverDimension(1500, 4000));
```

### createSeleniumClient

```php
public static function createSeleniumClient(
    ?string                    $host         = null,  // Selenium Hub URL, z. B. 'http://127.0.0.1:4444/wd/hub'
    ?WebDriverCapabilities     $capabilities = null,  // Gewunschte Capabilities
    ?string                    $baseUri      = null,
    array                      $options      = []
): self
```

---

## Lebenszyklus

### start

```php
public function start(): void
```

Startet den WebDriver-Prozess (ChromeDriver/GeckoDriver) und offnet den Browser.
Wird automatisch aufgerufen wenn notig.

### quit

```php
public function quit(bool $quitBrowserManager = true): void
```

Beendet den Browser. Mit `$quitBrowserManager = false` wird nur die Session geschlossen,
der ChromeDriver-Prozess lauft weiter.

### restart

```php
public function restart(): void
```

Beendet und startet den Browser neu. Loscht History und Cookies.

### close

```php
public function close(): WebDriver
```

Schliesst den aktuellen Browser-Tab (nicht den gesamten Browser).

### ping

```php
public function ping(int $timeout = 1000): bool
```

Pruft ob die WebDriver-Verbindung noch aktiv ist.
- `$timeout`: Timeout in Millisekunden (Default: 1000)
- Ruckgabe: `true` wenn verbunden, `false` sonst
- Nutzlich bei langen Tests um Session-Timeout zu erkennen

---

## Navigation

### request

```php
public function request(
    string  $method,                  // HTTP-Methode: 'GET', 'POST', etc.
    string  $uri,                     // URL oder Pfad (relativ zur baseUri)
    array   $parameters    = [],      // Query-/POST-Parameter
    array   $files         = [],      // Datei-Uploads
    array   $server        = [],      // Server-Parameter / HTTP-Header
    ?string $content       = null,    // Request-Body als String
    bool    $changeHistory = true     // History aktualisieren
): PantherCrawler
```

### get

```php
public function get(string $url): self
```

Kurze Variante fur GET-Requests. Gibt den Client selbst zuruck (Fluent Interface).

### back

```php
public function back(): PantherCrawler
```

Navigiert eine Seite zuruck (Browser-History). Gibt Crawler der neuen Seite zuruck.

### forward

```php
public function forward(): PantherCrawler
```

Navigiert eine Seite vor.

### reload

```php
public function reload(): PantherCrawler
```

Ladt die aktuelle Seite neu. Entspricht F5.

### navigate

```php
public function navigate(): WebDriverNavigationInterface
```

Gibt das WebDriver-`navigate()`-Objekt zuruck fur Methoden wie `navigateTo($url)`,
`back()`, `forward()`, `refresh()`.

---

## Warte-Methoden (alle mit Timeout/Interval)

Alle waitFor-Methoden haben dieselbe Signatur-Struktur:
- `$locator`: CSS-Selektor (z. B. `'#my-id'`, `'.my-class'`, `'button[type=submit]'`)
- `$timeoutInSecond`: Max. Wartezeit in Sekunden (Default: `30`)
- `$intervalInMillisecond`: Polling-Intervall in ms (Default: `250`)
- Ruckgabe: `PantherCrawler` mit dem gefundenen Element

### waitFor

```php
public function waitFor(
    string $locator,
    int    $timeoutInSecond        = 30,
    int    $intervalInMillisecond  = 250
): PantherCrawler
```

Wartet bis mindestens ein Element mit dem Selektor im DOM vorhanden ist.

### waitForStaleness

```php
public function waitForStaleness(
    string $locator,
    int    $timeoutInSecond       = 30,
    int    $intervalInMillisecond = 250
): PantherCrawler
```

Wartet bis das Element aus dem DOM entfernt wird (stale).

### waitForVisibility

```php
public function waitForVisibility(
    string $locator,
    int    $timeoutInSecond       = 30,
    int    $intervalInMillisecond = 250
): PantherCrawler
```

Wartet bis das Element sichtbar ist (nicht `display:none`/`visibility:hidden`).

### waitForInvisibility

```php
public function waitForInvisibility(
    string $locator,
    int    $timeoutInSecond       = 30,
    int    $intervalInMillisecond = 250
): PantherCrawler
```

Wartet bis das Element unsichtbar oder aus dem DOM entfernt wird.

### waitForElementToContain

```php
public function waitForElementToContain(
    string $locator,
    string $text,
    int    $timeoutInSecond       = 30,
    int    $intervalInMillisecond = 250
): PantherCrawler
```

Wartet bis das Element `$text` als Textinhalt enthalt.

### waitForElementToNotContain

```php
public function waitForElementToNotContain(
    string $locator,
    string $text,
    int    $timeoutInSecond       = 30,
    int    $intervalInMillisecond = 250
): PantherCrawler
```

Wartet bis das Element `$text` NICHT mehr enthalt.

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

Wartet bis das Attribut `$attribute` des Elements `$text` enthalt.

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

Wartet bis ein Button/Input-Element den `disabled`-Status verliert.

### waitForDisabled

```php
public function waitForDisabled(
    string $locator,
    int    $timeoutInSecond       = 30,
    int    $intervalInMillisecond = 250
): PantherCrawler
```

Wartet bis ein Element `disabled` wird.

### wait (niedrigstufig)

```php
public function wait(
    int $timeoutInSecond        = 30,
    int $intervalInMillisecond  = 250
): \Facebook\WebDriver\WebDriverWait
```

Gibt ein `WebDriverWait`-Objekt zuruck fur benutzerdefinierte Bedingungen:

```php
use Facebook\WebDriver\WebDriverExpectedCondition;

$client->wait(10, 500)->until(
    WebDriverExpectedCondition::titleContains('Dashboard')
);
```

---

## JavaScript-Ausfuhrung

### executeScript

```php
public function executeScript(
    string $script,       // JS-Code als String
    array  $arguments = [] // An JS ubergebene Argumente (als `arguments[0]`, etc.)
): mixed
```

Synchrones JS. Ruckgabewert des JS-`return`-Statements.

```php
// Scroll to top
$client->executeScript('window.scrollTo(0, 0);');

// Element-Wert lesen
$value = $client->executeScript('return arguments[0].value;', [$element]);

// localStorage lesen
$token = $client->executeScript('return localStorage.getItem("token");');
```

### executeAsyncScript

```php
public function executeAsyncScript(
    string $script,
    array  $arguments = []
): mixed
```

Asynchrones JS. Das Script muss `arguments[arguments.length - 1]` als Callback aufrufen.

```php
$result = $client->executeAsyncScript(
    'setTimeout(() => arguments[0]("done"), 1000);'
);
```

---

## Zustandsabfragen

### getPageSource

```php
public function getPageSource(): string
```

Gibt den vollstandigen HTML-Quelltext der aktuellen Seite zuruck (nach JS-Rendering).

### getCurrentURL

```php
public function getCurrentURL(): string
```

Gibt die aktuelle URL des Browsers zuruck (nach Redirects).

### getTitle

```php
public function getTitle(): string
```

Gibt den `<title>`-Tag-Inhalt der aktuellen Seite zuruck.

### refreshCrawler

```php
public function refreshCrawler(): PantherCrawler
```

Aktualisiert den Crawler auf Basis des aktuellen DOM-Zustands (nach JS-Anderungen).
Gibt neuen `PantherCrawler` zuruck.

### getCrawler

```php
public function getCrawler(): PantherCrawler
```

Gibt den zuletzt erzeugten Crawler zuruck (ohne DOM-Refresh).

### takeScreenshot

```php
public function takeScreenshot(?string $saveAs = null): string
```

Erstellt einen Screenshot des Browserfensters.
- `$saveAs`: Dateipfad zum Speichern (PNG). Wenn `null`, wird kein File gespeichert.
- Ruckgabe: PNG-Daten als Base64-kodierter String.

```php
$client->takeScreenshot('/tmp/before-click.png');
$client->click($link);
$client->takeScreenshot('/tmp/after-click.png');
```

---

## WebDriver-Zugriff

### getWebDriver

```php
public function getWebDriver(): \Facebook\WebDriver\WebDriver
```

Gibt die rohe `WebDriver`-Instanz zuruck fur alle nicht direkt in Panther exponierten
WebDriver-Methoden.

```php
$driver = $client->getWebDriver();
$driver->manage()->window()->maximize();
$logs = $driver->manage()->getLog('browser');
```

### manage

```php
public function manage(): \Facebook\WebDriver\WebDriverOptions
```

Zugriff auf Browser-Management (Cookies, Logs, Window, Timeouts):

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

Wechselt den Kontext (Frame, Window, Alert):

```php
$client->switchTo()->frame(0);          // in Frame wechseln
$client->switchTo()->defaultContent();  // zuruck zum Hauptdokument
$client->switchTo()->alert()->accept(); // Alert bestatigen
$client->switchTo()->window($handle);   // anderen Tab/Window
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

## Eingabegerate

### getMouse

```php
public function getMouse(): \Symfony\Component\Panther\WebDriver\WebDriverMouse
```

Gibt Panthers eigenes `WebDriverMouse`-Objekt zuruck (wrappt `BaseWebDriverMouse` und fugt
CSS-Selektor-Methoden wie `clickTo`, `doubleClickTo`, `contextClickTo`, `mouseMoveTo`,
`mouseDownTo`, `mouseUpTo` hinzu). Siehe `panther-interactions` Skill fur Details.

Quelle: `src/Client.php:getMouse()` + `src/WebDriver/WebDriverMouse.php`

### getKeyboard

```php
public function getKeyboard(): \Facebook\WebDriver\WebDriverKeyboard
```

Gibt das `WebDriverKeyboard`-Objekt zuruck. Siehe `panther-interactions` Skill fur Details.

---

## Formulare und Links

### click

```php
public function click(
    \Symfony\Component\DomCrawler\Link $link,
    array $serverParameters = []
): \Symfony\Component\DomCrawler\Crawler
```

Klickt auf ein `Link`-Objekt (aus `$crawler->selectLink(...)->link()`).

### clickLink

```php
// Vererbt von BrowserKit AbstractBrowser
public function clickLink(string $linkText): Crawler
```

Klickt auf einen Link anhand seines Textes.

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
// Vererbt von BrowserKit AbstractBrowser
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

## Fenster-Management

### getWindowHandle

```php
public function getWindowHandle(): string
```

Gibt den Handle des aktuellen Browser-Fensters/Tabs zuruck.

### getWindowHandles

```php
public function getWindowHandles(): array
```

Gibt alle offenen Fenster/Tab-Handles zuruck.

---

## Element-Suche (niedrigstufig)

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

Panthers eigene `CookieJar`-Klasse (wrappt WebDriver-Cookies). Methoden:

Quelle: `src/Client.php:getCookieJar()` + `src/Cookie/CookieJar.php`

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

## Vollstandiges Beispiel

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

        // Seite laden
        $client->request('GET', '/shop/cart');

        // Auf dynamisch geladenes Element warten
        $crawler = $client->waitFor('.cart-items', 10, 500);

        // Screenshot vor Kauf
        $client->takeScreenshot('/tmp/cart-before.png');

        // Formular ausfüllen und abschicken
        $client->submitForm('Zur Kasse', ['coupon' => 'SAVE10']);

        // Warten bis Weiterleitung abgeschlossen
        $client->waitFor('.payment-form');

        // Assertions
        $this->assertSelectorTextContains('.total', '90,00');
        $this->assertPageTitleContains('Kasse');
        $this->assertSelectorAttributeContains('.step', 'data-step', '2');

        // JavaScript
        $token = $client->executeScript('return window.__CSRF_TOKEN__;');
        $this->assertNotEmpty($token);

        // Browser-Logs prufen
        $logs = $client->getWebDriver()->manage()->getLog('browser');
        $errors = array_filter($logs, fn($log) => $log['level'] === 'SEVERE');
        $this->assertEmpty($errors, 'Keine JS-Fehler erwartet');

        // Verbindung prufen
        $this->assertTrue($client->ping());

        $client->quit();
    }
}
```

---

Quellen:
- https://raw.githubusercontent.com/symfony/panther/main/src/Client.php
- https://symfony.com/doc/current/testing/end_to_end.html
- https://github.com/php-webdriver/php-webdriver
