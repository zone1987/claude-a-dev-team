# WebDriverCheckbox — Complete Reference

`Symfony\Component\Panther\WebDriver\WebDriverCheckbox`

Helper class for checkboxes and radio buttons. Implements `Facebook\WebDriver\WebDriverSelectInterface`
analogous to `WebDriverSelect` (for `<select>`) — this allows checkbox groups and radio groups
to be controlled through the same interface as select fields.

Source: `src/WebDriver/WebDriverCheckbox.php`

Note: This class is `internal` (not part of Panther's public API) and is used internally
by `ChoiceFormField` and `Form` when an `<input type="checkbox">` or
`<input type="radio">` is present.

---

## Contents

- [Constructor](#constructor)
- [isMultiple](#ismultiple)
- [getOptions](#getoptions)
- [getAllSelectedOptions](#getallselectedoptions)
- [getFirstSelectedOption](#getfirstselectedoption)
- [selectByIndex / selectByValue / selectByVisibleText / selectByVisiblePartialText](#selectbyindex-selectbyvalue-selectbyvisibletext-selectbyvisiblepartialtext)
- [deselectAll / deselectByIndex / deselectByValue / deselectByVisibleText / deselectByVisiblePartialText](#deselectall-deselectbyindex-deselectbyvalue-deselectbyvisibletext-deselectbyvisiblepartialtext)
- [Usage via ChoiceFormField (recommended)](#usage-via-choiceformfield-recommended)

## Constructor

```php
public function __construct(WebDriverElement $element)
```

`$element` must be an `<input type="checkbox">` or `<input type="radio">` with a
`name` attribute. Otherwise it throws:
- `UnexpectedTagNameException` if not an `<input>`
- `WebDriverException` if the type is not checkbox/radio
- `WebDriverException` if there is no `name` attribute

---

## isMultiple

```php
public function isMultiple(): bool
```

`true` for checkboxes (several can be selected at the same time),
`false` for radio buttons (mutually exclusive).

---

## getOptions

```php
public function getOptions(): array  // WebDriverElement[]
```

Returns all related elements (same name within the same form).

---

## getAllSelectedOptions

```php
public function getAllSelectedOptions(): array  // WebDriverElement[]
```

Returns all currently selected elements. Stops at the first one for radio buttons.

---

## getFirstSelectedOption

```php
public function getFirstSelectedOption(): WebDriverElement
```

Throws `NoSuchElementException` if nothing is selected.

---

## selectByIndex / selectByValue / selectByVisibleText / selectByVisiblePartialText

```php
public function selectByIndex(int $index): void
public function selectByValue(string $value): void
public function selectByVisibleText(string $text): void
public function selectByVisiblePartialText(string $text): void
```

Selects the element at the given index / with the given `value` attribute /
with the given label text.

---

## deselectAll / deselectByIndex / deselectByValue / deselectByVisibleText / deselectByVisiblePartialText

Only for checkboxes (`isMultiple() === true`). Throws `UnsupportedOperationException` for radio buttons.

```php
public function deselectAll(): void
public function deselectByIndex(int $index): void
public function deselectByValue(string $value): void
public function deselectByVisibleText(string $text): void
public function deselectByVisiblePartialText(string $text): void
```

---

## Usage via ChoiceFormField (recommended)

Direct use of `WebDriverCheckbox` is rarely necessary. Use `Form` instead:

```php
$form = $crawler->selectButton('Speichern')->form();

// Tick checkbox
$form['newsletter']->tick();     // ChoiceFormField::tick() -> WebDriverCheckbox internally

// Un-tick checkbox
$form['newsletter']->untick();

// Select radio
$form['payment_method']->select('paypal');

// Select checkbox group (multiple)
$form['interests']->select(['php', 'symfony']);
```
