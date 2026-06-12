---
name: panther-client
description: >
  Vollstandige Client-API von Symfony Panther: request/get/post, click/clickLink,
  submit/submitForm, back/forward/reload/restart, alle waitFor*-Varianten (waitFor,
  waitForStaleness, waitForVisibility, waitForInvisibility, waitForElementToContain,
  waitForElementToNotContain, waitForAttributeToContain, waitForAttributeToNotContain,
  waitForEnabled, waitForDisabled) mit Timeout/Interval-Parametern, executeScript,
  executeAsyncScript, takeScreenshot, ping, quit, start, getWebDriver, getPageSource,
  getCurrentURL, getTitle, refreshCrawler, manage, getKeyboard, getMouse, getCookieJar,
  navigate, switchTo, findElement, findElements, createChromeClient, createFirefoxClient,
  createSeleniumClient.
  Complete Panther Client API: all methods, signatures, defaults, JavaScript execution,
  screenshots, WebDriver access, window management.
  Trigger: "panther client api", "panther waitfor", "panther executescript", "panther screenshot",
  "panther getpagesource", "panther getcurrenturl", "panther ping", "panther quit",
  "panther createchromeclient", "panther createfirefoxclient", "panther refreshcrawler",
  "panther navigate", "panther manage", "panther getkeyboard", "panther getmouse",
  "panther webdriver", "client methoden panther", "panther waitforvisibility".
---

# Panther Client — Vollstandige API

```php
use Symfony\Component\Panther\Client;

$client = Client::createChromeClient();
$client->request('GET', '/');
$crawler = $client->waitFor('.app-loaded');
$client->takeScreenshot('/tmp/screen.png');
```

## Wichtigste Methoden-Gruppen

- **Navigation**: `request`, `get`, `back`, `forward`, `reload`, `restart`
- **Warten**: `waitFor`, `waitForStaleness`, `waitForVisibility`, `waitForInvisibility`, `waitForElementToContain`, `waitForElementToNotContain`, `waitForAttributeToContain`, `waitForAttributeToNotContain`, `waitForEnabled`, `waitForDisabled`, `wait`
- **JavaScript**: `executeScript`, `executeAsyncScript`
- **Zustand**: `getPageSource`, `getCurrentURL`, `getTitle`, `refreshCrawler`, `ping`
- **WebDriver-Zugriff**: `getWebDriver`, `manage`, `navigate`, `switchTo`
- **Eingabe**: `getKeyboard`, `getMouse`
- **Formulare/Links**: `click`, `clickLink`, `submit`, `submitForm`

Alle waitFor-Methoden: `timeoutInSecond = 30`, `intervalInMillisecond = 250`.

## Vertiefung

- [references/deep/client.md](references/deep/client.md) — Jede Methode mit vollstandiger Signatur, Parameterbeschreibung, Ruckgabetyp und Beispiel
- [references/deep/expected-conditions.md](references/deep/expected-conditions.md) — PantherWebDriverExpectedCondition: alle 5 statischen Methoden + Vergleich mit Standard-WebDriverExpectedCondition
- [references/deep/webdriver-checkbox.md](references/deep/webdriver-checkbox.md) — WebDriverCheckbox: interne Klasse fur Checkbox/Radio-Interaktion
