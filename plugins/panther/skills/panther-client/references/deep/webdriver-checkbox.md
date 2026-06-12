# WebDriverCheckbox — Vollstandige Referenz

`Symfony\Component\Panther\WebDriver\WebDriverCheckbox`

Hilfsklasse fur Checkboxen und Radio-Buttons. Implementiert `Facebook\WebDriver\WebDriverSelectInterface`
analog zu `WebDriverSelect` (fur `<select>`) — damit konnen Checkbox-Gruppen und Radio-Gruppen
uber dieselbe Schnittstelle angesteuert werden wie Select-Felder.

Quelle: `src/WebDriver/WebDriverCheckbox.php`

Hinweis: Diese Klasse ist `internal` (nicht Teil der public API von Panther) und wird intern
von `ChoiceFormField` und `Form` verwendet, wenn `<input type="checkbox">` oder
`<input type="radio">` vorliegt.

---

## Konstruktor

```php
public function __construct(WebDriverElement $element)
```

`$element` muss ein `<input type="checkbox">` oder `<input type="radio">` mit einem
`name`-Attribut sein. Wirft sonst:
- `UnexpectedTagNameException` wenn kein `<input>`
- `WebDriverException` wenn Typ nicht checkbox/radio
- `WebDriverException` wenn kein `name`-Attribut

---

## isMultiple

```php
public function isMultiple(): bool
```

`true` fur Checkboxen (mehrere konnen gleichzeitig selektiert sein),
`false` fur Radio-Buttons (gegenseitig exklusiv).

---

## getOptions

```php
public function getOptions(): array  // WebDriverElement[]
```

Gibt alle verwandten Elemente (gleicher Name im gleichen Form) zuruck.

---

## getAllSelectedOptions

```php
public function getAllSelectedOptions(): array  // WebDriverElement[]
```

Gibt alle aktuell selektierten Elemente zuruck. Stoppt beim ersten fur Radio-Buttons.

---

## getFirstSelectedOption

```php
public function getFirstSelectedOption(): WebDriverElement
```

Wirft `NoSuchElementException` wenn nichts selektiert.

---

## selectByIndex / selectByValue / selectByVisibleText / selectByVisiblePartialText

```php
public function selectByIndex(int $index): void
public function selectByValue(string $value): void
public function selectByVisibleText(string $text): void
public function selectByVisiblePartialText(string $text): void
```

Selektiert das Element am gegebenen Index / mit gegebenem `value`-Attribut /
mit gegebenem Label-Text.

---

## deselectAll / deselectByIndex / deselectByValue / deselectByVisibleText / deselectByVisiblePartialText

Nur fur Checkboxen (`isMultiple() === true`). Wirft `UnsupportedOperationException` bei Radio-Buttons.

```php
public function deselectAll(): void
public function deselectByIndex(int $index): void
public function deselectByValue(string $value): void
public function deselectByVisibleText(string $text): void
public function deselectByVisiblePartialText(string $text): void
```

---

## Nutzung uber ChoiceFormField (empfohlen)

Direkte Nutzung von `WebDriverCheckbox` ist selten notig. Stattdessen uber `Form`:

```php
$form = $crawler->selectButton('Speichern')->form();

// Checkbox ticken
$form['newsletter']->tick();     // ChoiceFormField::tick() -> WebDriverCheckbox intern

// Checkbox un-ticken
$form['newsletter']->untick();

// Radio auswahlen
$form['payment_method']->select('paypal');

// Checkbox-Gruppe (mehrere) auswahlen
$form['interests']->select(['php', 'symfony']);
```
