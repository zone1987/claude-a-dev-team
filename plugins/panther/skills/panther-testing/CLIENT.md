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

- [CLIENT-DETAIL.md](CLIENT-DETAIL.md) — Jede Methode mit vollstandiger Signatur, Parameterbeschreibung, Ruckgabetyp und Beispiel
- [CLIENT-EXPECTED-CONDITIONS.md](CLIENT-EXPECTED-CONDITIONS.md) — PantherWebDriverExpectedCondition: alle 5 statischen Methoden + Vergleich mit Standard-WebDriverExpectedCondition
- [CLIENT-WEBDRIVER-CHECKBOX.md](CLIENT-WEBDRIVER-CHECKBOX.md) — WebDriverCheckbox: interne Klasse fur Checkbox/Radio-Interaktion
