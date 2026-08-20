# PantherWebDriverExpectedCondition — Complete Reference

`Symfony\Component\Panther\WebDriver\PantherWebDriverExpectedCondition`

Panther's own expected conditions, which go beyond the standard conditions of
`Facebook\WebDriver\WebDriverExpectedCondition`. All methods
are `static` and return a `callable`, which is what `WebDriverWait::until()`
expects.

Source: `src/WebDriver/PantherWebDriverExpectedCondition.php`

---

## Contents

- [Method Overview](#method-overview)
- [Comparison: standard vs. Panther expected conditions](#comparison-standard-vs-panther-expected-conditions)
- [Direct usage with wait()](#direct-usage-with-wait)

## Method Overview

All methods return `callable(WebDriver $driver): bool|null`.
Returns `null` when a `StaleElementReferenceException` occurs (the element was
removed from the DOM — polling continues).

### elementTextNotContains

```php
public static function elementTextNotContains(
    WebDriverBy $by,
    string      $text
): callable
```

Waits until the element found via `$by` NO LONGER contains `$text` in its visible text.

Used by `Client::waitForElementToNotContain()`.

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

Waits until the element is `isEnabled() === true` (no `disabled` attribute).

Used by `Client::waitForEnabled()`.

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

Waits until the element is `isEnabled() === false` (`disabled` attribute set).

Used by `Client::waitForDisabled()`.

---

### elementAttributeContains

```php
public static function elementAttributeContains(
    WebDriverBy $by,
    string      $attribute,
    string      $text
): callable
```

Waits until the element's `$attribute` attribute contains `$text`.
Returns `null` (not `false`) when the attribute is `null` (the element does not have the attribute).

Used by `Client::waitForAttributeToContain()`.

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

Waits until the element's `$attribute` attribute NO LONGER contains `$text`.
Returns `null` when the attribute itself is `null`.

Used by `Client::waitForAttributeToNotContain()`.

---

## Comparison: standard vs. Panther expected conditions

`Facebook\WebDriver\WebDriverExpectedCondition` provides (selection):

| Method | Description |
|---|---|
| `presenceOfElementLocated($by)` | Element present in the DOM (even if invisible) |
| `visibilityOfElementLocated($by)` | Element visible |
| `invisibilityOfElementLocated($by)` | Element invisible or not in the DOM |
| `stalenessOf($element)` | Element was removed from the DOM |
| `elementTextContains($by, $text)` | Element contains text |
| `titleContains($title)` | Page title contains string |
| `titleIs($title)` | Page title is exactly equal |
| `urlContains($url)` | Current URL contains string |
| `urlIs($url)` | Current URL is exactly equal |
| `numberOfWindowsToBe($n)` | Exactly n windows/tabs open |

`PantherWebDriverExpectedCondition` adds:

| Method | Description |
|---|---|
| `elementTextNotContains($by, $text)` | Element does NOT contain text |
| `elementEnabled($by)` | Element is enabled |
| `elementDisabled($by)` | Element is disabled |
| `elementAttributeContains($by, $attr, $text)` | Attribute contains text |
| `elementAttributeNotContains($by, $attr, $text)` | Attribute does NOT contain text |

---

## Direct usage with wait()

```php
use Facebook\WebDriver\WebDriverExpectedCondition;
use Symfony\Component\Panther\WebDriver\PantherWebDriverExpectedCondition;

// Standard condition
$client->wait(10)->until(
    WebDriverExpectedCondition::titleContains('Dashboard')
);

// Panther's own condition
$client->wait(30, 500)->until(
    PantherWebDriverExpectedCondition::elementEnabled(
        \Facebook\WebDriver\WebDriverBy::cssSelector('input[name=submit]')
    ),
    'Submit button did not become enabled within 30 seconds'
);
```

Note: The higher-level API are the `waitFor*` methods of `Client`, which use these conditions
internally. Using `wait()->until()` directly is only necessary for conditions that are not
exposed directly.
