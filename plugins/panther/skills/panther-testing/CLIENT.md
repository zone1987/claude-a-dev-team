# Panther Client — Complete API

```php
use Symfony\Component\Panther\Client;

$client = Client::createChromeClient();
$client->request('GET', '/');
$crawler = $client->waitFor('.app-loaded');
$client->takeScreenshot('/tmp/screen.png');
```

## Most Important Method Groups

- **Navigation**: `request`, `get`, `back`, `forward`, `reload`, `restart`
- **Waiting**: `waitFor`, `waitForStaleness`, `waitForVisibility`, `waitForInvisibility`, `waitForElementToContain`, `waitForElementToNotContain`, `waitForAttributeToContain`, `waitForAttributeToNotContain`, `waitForEnabled`, `waitForDisabled`, `wait`
- **JavaScript**: `executeScript`, `executeAsyncScript`
- **State**: `getPageSource`, `getCurrentURL`, `getTitle`, `refreshCrawler`, `ping`
- **WebDriver access**: `getWebDriver`, `manage`, `navigate`, `switchTo`
- **Input**: `getKeyboard`, `getMouse`
- **Forms/Links**: `click`, `clickLink`, `submit`, `submitForm`

All waitFor methods: `timeoutInSecond = 30`, `intervalInMillisecond = 250`.

## In Depth

- [CLIENT-DETAIL.md](CLIENT-DETAIL.md) — Every method with complete signature, parameter description, return type and example
- [CLIENT-EXPECTED-CONDITIONS.md](CLIENT-EXPECTED-CONDITIONS.md) — PantherWebDriverExpectedCondition: all 5 static methods + comparison with the standard WebDriverExpectedCondition
- [CLIENT-WEBDRIVER-CHECKBOX.md](CLIENT-WEBDRIVER-CHECKBOX.md) — WebDriverCheckbox: internal class for checkbox/radio interaction
