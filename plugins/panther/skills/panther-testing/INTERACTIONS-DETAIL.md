# Panther — complete interactions reference

## Contents

- [1. Click methods](#1-click-methods)
- [2. Form interactions](#2-form-interactions)
- [3. Form-Objekt — Vollstandige Interaktions-API](#3-form-objekt-vollstandige-interaktions-api)
- [4. FormField-Klassen — Methoden-Tabellen](#4-formfield-klassen-methoden-tabellen)
- [5. Mouse-API](#5-mouse-api)
- [6. Drag & Drop](#6-drag-drop)
- [7. Keyboard-API](#7-keyboard-api)
- [8. Element-Methoden (WebDriverElement)](#8-element-methoden-webdriverelement)
- [9. File-Upload (vollstandig)](#9-file-upload-vollstandig)
- [10. Complete interaction example](#10-complete-interaction-example)

## 1. Click methods

### client->click

```php
public function click(
    \Symfony\Component\DomCrawler\Link $link,
    array $serverParameters = []
): Crawler
```

Clicks a `Link` object (from `$crawler->link()`).

```php
$link = $crawler->filter('a.next-page')->link();
$crawler = $client->click($link);
```

### client->clickLink

```php
public function clickLink(string $linkText): Crawler
```

Clicks a link by its text.

```php
$client->clickLink('Weiter');
$client->clickLink('Abmelden');
```

---

## 2. Form interactions

### client->submitForm

```php
public function submitForm(
    string $buttonText,          // text, id or name of the submit button
    array  $fieldValues  = [],   // Feldbelegung: ['feldname' => 'wert']
    string $method       = null, // HTTP-Methode uberschreiben
    array  $serverParameters = []
): Crawler
```

Kurzform fur schnelle Form-Interaktionen:

```php
$client->submitForm('Anmelden', [
    'login[email]'    => 'user@example.com',
    'login[password]' => 'geheim123',
]);

$client->submitForm('Suchen', ['q' => 'symfony panther'], 'GET');
```

### client->submit

```php
public function submit(
    \Symfony\Component\DomCrawler\Form $form,
    array $values            = [],
    array $serverParameters  = []
): Crawler
```

Submits a `Form` object (from `$crawler->form()`).

```php
$form = $crawler->selectButton('Bestellen')->form();
$form['quantity']->setValue('3');
$form['address']->setValue('Musterstrasse 1');
$client->submit($form);
```

---

## 3. Form-Objekt — Vollstandige Interaktions-API

### Setting fields via array syntax

```php
$form = $crawler->selectButton('Speichern')->form();

// Input/Textarea
$form['username'] = 'symfonyfan';               // Kurzschreibweise
$form['username']->setValue('symfonyfan');      // explizit

// Select
$form['country']->select('DE');
$form['lang']->select(['de', 'en']);            // Multi-Select

// Checkbox
$form['newsletter']->tick();
$form['marketing']->untick();

// Radio
$form['gender']->select('m');

// Datei-Upload
$form['avatar']->upload('/absolute/path/to/photo.jpg');
```

### setValues (Bulk-Setzen)

```php
$form->setValues([
    'registration[username]' => 'symfonyfan',
    'registration[email]'    => 'fan@symfony.com',
    'registration[terms]'    => '1',
]);
```

### Verschachtelte Arrays (PHP-Formulare)

```php
// The form has: <input name="multi[]" value="a"> and <input name="multi[]" value="b">
$form->setValues(['multi' => ['x', 'y']]);

// Mit expliziten Indizes
$form->setValues(['grid' => [
    0             => 'Wert A',
    'dimensional' => 'Wert B',
]]);

// Mehrere Checkboxen per value
$form->setValues(['interests' => ['php', 'symfony']]);
```

### Validierung deaktivieren

```php
// At form level (from the base class, works)
$form->disableValidation();
```

Note: `$form['country']->disableValidation()` (at ChoiceFormField level) in Panther
is NOT implemented and throws `LogicException`. Source: `src/DomCrawler/Field/ChoiceFormField.php:disableValidation()`.

---

## 4. FormField-Klassen — Methoden-Tabellen

### InputFormField

Zustandig fur: `<input type="text">`, `<input type="email">`, `<input type="number">`,
`<input type="hidden">`, `<input type="password">`, `<input type="search">`, etc.

| Methode                  | Signatur                       | Beschreibung                      |
|--------------------------|--------------------------------|-----------------------------------|
| `setValue`               | `setValue(string $value): void` | Sets the field value             |
| `getValue`               | `getValue(): string`           | Reads the current value           |

### TextareaFormField

Zustandig fur: `<textarea>`

| Methode     | Signatur                        | Beschreibung              |
|-------------|---------------------------------|---------------------------|
| `setValue`  | `setValue(string $value): void` | Sets the content           |
| `getValue`  | `getValue(): string`            | Reads the current content  |

### ChoiceFormField

Zustandig fur: `<select>`, `<input type="radio">`, `<input type="checkbox">`

| Methode       | Signatur                                          | Beschreibung                                    |
|---------------|---------------------------------------------------|-------------------------------------------------|
| `select`      | `select(string\|array $value): void`              | Wahlt Option(en)                               |
| `tick`        | `tick(): void`                                    | Sets checkbox = checked                        |
| `untick`      | `untick(): void`                                  | Sets checkbox = unchecked                      |
| `getValue`    | `getValue(): string\|array`                       | Returns the selected value / selected values |
| `isDisabled`  | `isDisabled(): bool`                              | True if the field is disabled                   |
| `availableOptionValues` | `availableOptionValues(): array` | Returns all available option values as a string array |

### FileFormField

Zustandig fur: `<input type="file">`

| Methode       | Signatur                                  | Beschreibung                                                |
|---------------|-------------------------------------------|-------------------------------------------------------------|
| `upload`      | `upload(?string $path): void`             | Sets the absolute file path for the upload (inherited)      |
| `setFilePath` | `setFilePath(string $path): void`         | Sets the file path directly via `sendKeys()` on the element |
| `setValue`    | `setValue(?string $value): void`          | Wie `upload`, normalisiert Pfad via `realpath()`            |
| `getValue`    | `getValue(): array\|string\|null`         | Returns the upload array `['name','type','tmp_name','error','size']` |

Source: `src/DomCrawler/Field/FileFormField.php`

---

## 5. Mouse-API

`$client->getMouse()` gibt `\Symfony\Component\Panther\WebDriver\WebDriverMouse` zuruck —
Panther's own class, which wraps `BaseWebDriverMouse` and adds CSS-selector-based helper
methods. All `*To` methods take a CSS selector, convert it to coordinates and
delegate to the underlying `BaseWebDriverMouse`.

Source: `src/WebDriver/WebDriverMouse.php`

### clickTo

```php
public function clickTo(string $cssSelector): self
```

Linksklick auf Element per CSS-Selektor. Kein Offset-Parameter.

```php
$client->getMouse()->clickTo('#submit-btn');
$client->getMouse()->clickTo('.card:first-child');
```

### doubleClickTo

```php
public function doubleClickTo(string $cssSelector): self
```

Doppelklick auf Element. Kein Offset-Parameter.

```php
$client->getMouse()->doubleClickTo('.editable-cell');
```

### contextClickTo

```php
public function contextClickTo(string $cssSelector): self
```

Rechtsklick (Kontextmenu) auf Element. Kein Offset-Parameter.

```php
$client->getMouse()->contextClickTo('#file-icon');
```

### mouseMoveTo

```php
public function mouseMoveTo(string $cssSelector, mixed $xOffset = null, mixed $yOffset = null): self
```

Moves the mouse over an element (triggering hover effects). `$xOffset`/`$yOffset` are passed to
`BaseWebDriverMouse::mouseMove()` (pixel offset relative to the element center).

```php
$client->getMouse()->mouseMoveTo('.dropdown-trigger');
$client->getMouse()->mouseMoveTo('.map', 150, 80); // Offset click
$client->waitForVisibility('.dropdown-menu');
$client->clickLink('Einstellungen');
```

### mouseDownTo / mouseUpTo

```php
public function mouseDownTo(string $cssSelector): self
public function mouseUpTo(string $cssSelector): self
```

Maustaste drucken / loslassen (fur Drag & Drop). Kein Offset-Parameter.

### click / contextClick / doubleClick / mouseDown / mouseUp / mouseMove (niedrigstufig)

Die niedrigstufigen Methoden nehmen `WebDriverCoordinates` statt CSS-Selektor:

```php
public function click(WebDriverCoordinates $where): self
public function contextClick(WebDriverCoordinates $where): self
public function doubleClick(WebDriverCoordinates $where): self
public function mouseDown(WebDriverCoordinates $where): self
public function mouseUp(WebDriverCoordinates $where): self
public function mouseMove(WebDriverCoordinates $where, $xOffset = null, $yOffset = null): self
```

---

## 6. Drag & Drop

Panther supports drag & drop via the WebDriverActions API:

```php
use Facebook\WebDriver\Interactions\WebDriverActions;

$driver  = $client->getWebDriver();
$actions = new WebDriverActions($driver);

$source = $client->findElement(\Facebook\WebDriver\WebDriverBy::cssSelector('#draggable'));
$target = $client->findElement(\Facebook\WebDriver\WebDriverBy::cssSelector('#droppable'));

$actions->dragAndDrop($source, $target)->perform();

// Mit Offset
$actions->dragAndDropBy($source, 100, 50)->perform();

// Manuell (press-move-release)
$actions
    ->clickAndHold($source)
    ->moveToElement($target)
    ->release()
    ->perform();
```

---

## 7. Keyboard-API

`$client->getKeyboard()` gibt ein `\Facebook\WebDriver\WebDriverKeyboard` zuruck.

### sendKeys

```php
$client->getKeyboard()->sendKeys(string $keys): void
```

Sends keyboard input to the currently focused element.

```php
$crawler->filter('input[name=search]')->getElement(0)->click();
$client->getKeyboard()->sendKeys('symfony panther');
$client->getKeyboard()->sendKeys(\Facebook\WebDriver\WebDriverKeys::ENTER);
```

### WebDriverKeys-Konstanten (Auswahl)

```php
use Facebook\WebDriver\WebDriverKeys;

WebDriverKeys::ENTER         // Enter/Return
WebDriverKeys::TAB           // Tab
WebDriverKeys::ESCAPE        // Escape
WebDriverKeys::BACKSPACE     // Backspace
WebDriverKeys::DELETE        // Delete
WebDriverKeys::SPACE         // Leerzeichen
WebDriverKeys::ARROW_UP      // Pfeil hoch
WebDriverKeys::ARROW_DOWN    // Pfeil runter
WebDriverKeys::ARROW_LEFT    // Pfeil links
WebDriverKeys::ARROW_RIGHT   // Pfeil rechts
WebDriverKeys::HOME          // Pos1
WebDriverKeys::END           // Ende
WebDriverKeys::PAGE_UP       // Bild hoch
WebDriverKeys::PAGE_DOWN     // Bild runter
WebDriverKeys::F1 ... F12    // Funktionstasten
WebDriverKeys::CONTROL       // Strg
WebDriverKeys::SHIFT         // Shift
WebDriverKeys::ALT           // Alt
WebDriverKeys::META          // Meta/Windows/Cmd
WebDriverKeys::NULL_KEY      // Modifier freigeben
```

### Tastenkombinationen

```php
use Facebook\WebDriver\Interactions\WebDriverActions;

$actions = new WebDriverActions($client->getWebDriver());

// Strg+A (Alles markieren)
$actions->keyDown(null, WebDriverKeys::CONTROL)
        ->sendKeys(null, 'a')
        ->keyUp(null, WebDriverKeys::CONTROL)
        ->perform();

// Direkt auf Element
$el = $client->findElement(WebDriverBy::cssSelector('input'));
$actions->keyDown($el, WebDriverKeys::SHIFT)
        ->sendKeys($el, 'hello')
        ->keyUp($el, WebDriverKeys::SHIFT)
        ->perform();
```

---

## 8. Element-Methoden (WebDriverElement)

Nach `$crawler->filter('...')->getElement(0)` verfugbar
(Signatur: `getElement(int $position): ?WebDriverElement`):

```php
$el = $crawler->filter('#my-input')->getElement(0);

$el->click(): void
$el->sendKeys(string $value): self      // Text eingeben
$el->clear(): self                      // Inhalt loschen
$el->submit(): void                     // Submit the parent form
$el->getText(): string                  // Sichtbarer Text
$el->getAttribute(string $name): ?string
$el->isEnabled(): bool
$el->isSelected(): bool
$el->isDisplayed(): bool
$el->getTagName(): string
$el->getLocation(): WebDriverPoint      // {x, y} Position
$el->getSize(): WebDriverDimension      // {width, height}
$el->getRect(): WebDriverRect           // {x, y, width, height}
$el->getCSSValue(string $property): string
$el->findElement(WebDriverBy $by): WebDriverElement
$el->findElements(WebDriverBy $by): array
$el->takeScreenshot(): string           // Screenshot nur dieses Elements
```

---

## 9. File-Upload (vollstandig)

### Uber Crawler/Form (empfohlen)

```php
$form = $crawler->selectButton('Hochladen')->form();
$form['profile_picture']->upload('/absolute/path/to/image.jpg');
$client->submit($form);
```

### Uber WebDriverElement (fur Custom-Inputs)

```php
$fileInput = $client->findElement(
    \Facebook\WebDriver\WebDriverBy::cssSelector('input[type=file]')
);
$fileInput->sendKeys('/absolute/path/to/document.pdf');
```

### Mehrere Dateien (Multi-Upload)

```php
// Upload-Feld fur mehrere Dateien (<input type="file" multiple>)
$form['attachments[]']->upload('/path/file1.pdf');
// Zweite Datei per WebDriver (direkt)
$el = $crawler->filter('input[name="attachments[]"]')->getElement(0);
$el->sendKeys('/path/file2.pdf');
```

---

## 10. Complete interaction example

```php
use Symfony\Component\Panther\PantherTestCase;
use Facebook\WebDriver\WebDriverKeys;
use Facebook\WebDriver\Interactions\WebDriverActions;

class ProductTest extends PantherTestCase
{
    public function testComplexInteraction(): void
    {
        $client = static::createPantherClient();
        $client->request('GET', '/products/new');

        // Fill in the form fields
        $form = $client->getCrawler()->selectButton('Speichern')->form();
        $form['product[name]']->setValue('Neues Produkt');
        $form['product[description]']->setValue("Zeile 1\nZeile 2");
        $form['product[category]']->select('electronics');
        $form['product[active]']->tick();
        $form['product[image]']->upload('/tmp/product.jpg');

        // Hover and click
        $client->getMouse()->mouseMoveTo('.help-tooltip');
        $client->waitForVisibility('.tooltip-content');

        // Keyboard shortcut
        $actions = new WebDriverActions($client->getWebDriver());
        $actions->keyDown(null, WebDriverKeys::CONTROL)
                ->sendKeys(null, 's')
                ->keyUp(null, WebDriverKeys::CONTROL)
                ->perform();

        // Or: submit the form directly
        $client->submit($form);

        // Warten auf Erfolgsmeldung
        $client->waitForElementToContain('.flash-success', 'gespeichert');
        $this->assertSelectorWillExist('.product-detail');
        $this->assertSelectorTextContains('h1', 'Neues Produkt');

        // Screenshot for documentation
        $client->takeScreenshot('/tmp/product-saved.png');
    }
}
```

---

Quellen:
- https://symfony.com/doc/current/testing/end_to_end.html
- https://symfony.com/doc/current/components/dom_crawler.html
- https://github.com/php-webdriver/php-webdriver
- https://github.com/symfony/panther
