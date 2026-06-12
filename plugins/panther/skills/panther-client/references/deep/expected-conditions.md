# PantherWebDriverExpectedCondition — Vollstandige Referenz

`Symfony\Component\Panther\WebDriver\PantherWebDriverExpectedCondition`

Panther-eigene Expected-Conditions, die uber die Standard-Conditions von
`Facebook\WebDriver\WebDriverExpectedCondition` hinausgehen. Alle Methoden
sind `static` und geben ein `callable` zuruck, das `WebDriverWait::until()`
erwartet.

Quelle: `src/WebDriver/PantherWebDriverExpectedCondition.php`

---

## Methoden-Ubersicht

Alle Methoden geben `callable(WebDriver $driver): bool|null` zuruck.
Gibt `null` zuruck wenn eine `StaleElementReferenceException` auftritt (Element wurde
aus dem DOM entfernt — Polling wird fortgesetzt).

### elementTextNotContains

```php
public static function elementTextNotContains(
    WebDriverBy $by,
    string      $text
): callable
```

Wartet bis das per `$by` gefundene Element `$text` NICHT mehr im sichtbaren Text enthalt.

Genutzt von `Client::waitForElementToNotContain()`.

```php
use Facebook\WebDriver\WebDriverBy;
use Symfony\Component\Panther\WebDriver\PantherWebDriverExpectedCondition;

$client->wait(10, 250)->until(
    PantherWebDriverExpectedCondition::elementTextNotContains(
        WebDriverBy::cssSelector('.status'),
        'Loading'
    )
);
```

---

### elementEnabled

```php
public static function elementEnabled(WebDriverBy $by): callable
```

Wartet bis das Element `isEnabled() === true` (kein `disabled`-Attribut).

Genutzt von `Client::waitForEnabled()`.

```php
$client->wait(30, 250)->until(
    PantherWebDriverExpectedCondition::elementEnabled(
        WebDriverBy::cssSelector('button[type=submit]')
    )
);
```

---

### elementDisabled

```php
public static function elementDisabled(WebDriverBy $by): callable
```

Wartet bis das Element `isEnabled() === false` (`disabled`-Attribut gesetzt).

Genutzt von `Client::waitForDisabled()`.

---

### elementAttributeContains

```php
public static function elementAttributeContains(
    WebDriverBy $by,
    string      $attribute,
    string      $text
): callable
```

Wartet bis das Attribut `$attribute` des Elements `$text` enthalt.
Gibt `null` zuruck (nicht `false`) wenn das Attribut `null` ist (Element hat Attribut nicht).

Genutzt von `Client::waitForAttributeToContain()`.

```php
$client->wait(10, 250)->until(
    PantherWebDriverExpectedCondition::elementAttributeContains(
        WebDriverBy::cssSelector('.btn'),
        'class',
        'active'
    )
);
```

---

### elementAttributeNotContains

```php
public static function elementAttributeNotContains(
    WebDriverBy $by,
    string      $attribute,
    string      $text
): callable
```

Wartet bis das Attribut `$attribute` des Elements `$text` NICHT mehr enthalt.
Gibt `null` wenn das Attribut selbst `null` ist.

Genutzt von `Client::waitForAttributeToNotContain()`.

---

## Vergleich: Standard vs. Panther Expected Conditions

`Facebook\WebDriver\WebDriverExpectedCondition` liefert (Auswahl):

| Methode | Beschreibung |
|---|---|
| `presenceOfElementLocated($by)` | Element im DOM vorhanden (auch unsichtbar) |
| `visibilityOfElementLocated($by)` | Element sichtbar |
| `invisibilityOfElementLocated($by)` | Element unsichtbar oder nicht im DOM |
| `stalenessOf($element)` | Element wurde aus dem DOM entfernt |
| `elementTextContains($by, $text)` | Element enthalt Text |
| `titleContains($title)` | Seiten-Titel enthalt String |
| `titleIs($title)` | Seiten-Titel ist exakt gleich |
| `urlContains($url)` | Aktuelle URL enthalt String |
| `urlIs($url)` | Aktuelle URL ist exakt gleich |
| `numberOfWindowsToBe($n)` | Exakt n Fenster/Tabs offen |

`PantherWebDriverExpectedCondition` erganzt:

| Methode | Beschreibung |
|---|---|
| `elementTextNotContains($by, $text)` | Element enthalt Text NICHT |
| `elementEnabled($by)` | Element ist enabled |
| `elementDisabled($by)` | Element ist disabled |
| `elementAttributeContains($by, $attr, $text)` | Attribut enthalt Text |
| `elementAttributeNotContains($by, $attr, $text)` | Attribut enthalt Text NICHT |

---

## Direkte Nutzung mit wait()

```php
use Facebook\WebDriver\WebDriverExpectedCondition;
use Symfony\Component\Panther\WebDriver\PantherWebDriverExpectedCondition;

// Standard-Condition
$client->wait(10)->until(
    WebDriverExpectedCondition::titleContains('Dashboard')
);

// Panther-eigene Condition
$client->wait(30, 500)->until(
    PantherWebDriverExpectedCondition::elementEnabled(
        \Facebook\WebDriver\WebDriverBy::cssSelector('input[name=submit]')
    ),
    'Submit button did not become enabled within 30 seconds'
);
```

Hinweis: Die hohere Ebene sind die `waitFor*`-Methoden von `Client`, die diese Conditions
intern verwenden. Die direkte `wait()->until()`-Nutzung ist nur notwendig fur nicht direkt
exponierte Conditions.
