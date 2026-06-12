# Panther — Vollstandige Interaktions-Referenz

## 1. Klick-Methoden

### client->click

```php
public function click(
    \Symfony\Component\DomCrawler\Link $link,
    array $serverParameters = []
): Crawler
```

Klickt auf ein `Link`-Objekt (aus `$crawler->link()`).

```php
$link = $crawler->filter('a.next-page')->link();
$crawler = $client->click($link);
```

### client->clickLink

```php
public function clickLink(string $linkText): Crawler
```

Klickt auf einen Link anhand seines Textes.

```php
$client->clickLink('Weiter');
$client->clickLink('Abmelden');
```

---

## 2. Formular-Interaktionen

### client->submitForm

```php
public function submitForm(
    string $buttonText,          // Text, id oder name des Submit-Buttons
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

Sendet ein `Form`-Objekt (aus `$crawler->form()`).

```php
$form = $crawler->selectButton('Bestellen')->form();
$form['quantity']->setValue('3');
$form['address']->setValue('Musterstrasse 1');
$client->submit($form);
```

---

## 3. Form-Objekt — Vollstandige Interaktions-API

### Felder uber Array-Syntax setzen

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
// Formular hat: <input name="multi[]" value="a"> und <input name="multi[]" value="b">
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
// Auf Form-Ebene (aus Basis-Klasse, funktioniert)
$form->disableValidation();
```

Hinweis: `$form['country']->disableValidation()` (auf ChoiceFormField-Ebene) ist in Panther
NICHT implementiert und wirft `LogicException`. Quelle: `src/DomCrawler/Field/ChoiceFormField.php:disableValidation()`.

---

## 4. FormField-Klassen — Methoden-Tabellen

### InputFormField

Zustandig fur: `<input type="text">`, `<input type="email">`, `<input type="number">`,
`<input type="hidden">`, `<input type="password">`, `<input type="search">`, etc.

| Methode                  | Signatur                       | Beschreibung                      |
|--------------------------|--------------------------------|-----------------------------------|
| `setValue`               | `setValue(string $value): void` | Setzt den Feldwert               |
| `getValue`               | `getValue(): string`           | Liest den aktuellen Wert          |

### TextareaFormField

Zustandig fur: `<textarea>`

| Methode     | Signatur                        | Beschreibung              |
|-------------|---------------------------------|---------------------------|
| `setValue`  | `setValue(string $value): void` | Setzt den Inhalt           |
| `getValue`  | `getValue(): string`            | Liest den aktuellen Inhalt |

### ChoiceFormField

Zustandig fur: `<select>`, `<input type="radio">`, `<input type="checkbox">`

| Methode       | Signatur                                          | Beschreibung                                    |
|---------------|---------------------------------------------------|-------------------------------------------------|
| `select`      | `select(string\|array $value): void`              | Wahlt Option(en)                               |
| `tick`        | `tick(): void`                                    | Setzt Checkbox = checked                       |
| `untick`      | `untick(): void`                                  | Setzt Checkbox = unchecked                     |
| `getValue`    | `getValue(): string\|array`                       | Gibt ausgewahlten Wert / ausgewahlte Werte zuruck |
| `isDisabled`  | `isDisabled(): bool`                              | True wenn das Feld disabled ist                 |
| `availableOptionValues` | `availableOptionValues(): array` | Gibt alle verfugbaren Optionswerte als string-Array zuruck |

### FileFormField

Zustandig fur: `<input type="file">`

| Methode       | Signatur                                  | Beschreibung                                                |
|---------------|-------------------------------------------|-------------------------------------------------------------|
| `upload`      | `upload(?string $path): void`             | Setzt den absoluten Dateipfad fur den Upload (geerbt)       |
| `setFilePath` | `setFilePath(string $path): void`         | Setzt Dateipfad direkt via `sendKeys()` auf das Element     |
| `setValue`    | `setValue(?string $value): void`          | Wie `upload`, normalisiert Pfad via `realpath()`            |
| `getValue`    | `getValue(): array\|string\|null`         | Gibt Upload-Array `['name','type','tmp_name','error','size']` zuruck |

Quelle: `src/DomCrawler/Field/FileFormField.php`

---

## 5. Mouse-API

`$client->getMouse()` gibt `\Symfony\Component\Panther\WebDriver\WebDriverMouse` zuruck —
Panthers eigene Klasse, die `BaseWebDriverMouse` wrappt und CSS-Selektor-basierte Hilfsmethoden
hinzufugt. Alle `*To`-Methoden nehmen einen CSS-Selektor, konvertieren ihn zu Koordinaten und
delegieren an die zugrundeliegende `BaseWebDriverMouse`.

Quelle: `src/WebDriver/WebDriverMouse.php`

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

Bewegt die Maus uber ein Element (Hover-Effekte triggern). `$xOffset`/`$yOffset` werden an
`BaseWebDriverMouse::mouseMove()` weitergegeben (Pixel-Offset relativ zur Element-Mitte).

```php
$client->getMouse()->mouseMoveTo('.dropdown-trigger');
$client->getMouse()->mouseMoveTo('.map', 150, 80); // Offset-Klick
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

Panther unterstutzt Drag & Drop uber die WebDriverActions-API:

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

Sendet Tastatureingaben an das aktuell fokussierte Element.

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
$el->submit(): void                     // Eltern-Formular abschicken
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

## 10. Vollstandiges Interaktions-Beispiel

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

        // Formular-Felder befüllen
        $form = $client->getCrawler()->selectButton('Speichern')->form();
        $form['product[name]']->setValue('Neues Produkt');
        $form['product[description]']->setValue("Zeile 1\nZeile 2");
        $form['product[category]']->select('electronics');
        $form['product[active]']->tick();
        $form['product[image]']->upload('/tmp/product.jpg');

        // Hover und Klick
        $client->getMouse()->mouseMoveTo('.help-tooltip');
        $client->waitForVisibility('.tooltip-content');

        // Keyboard shortcut
        $actions = new WebDriverActions($client->getWebDriver());
        $actions->keyDown(null, WebDriverKeys::CONTROL)
                ->sendKeys(null, 's')
                ->keyUp(null, WebDriverKeys::CONTROL)
                ->perform();

        // Oder: Formular direkt absenden
        $client->submit($form);

        // Warten auf Erfolgsmeldung
        $client->waitForElementToContain('.flash-success', 'gespeichert');
        $this->assertSelectorWillExist('.product-detail');
        $this->assertSelectorTextContains('h1', 'Neues Produkt');

        // Screenshot zur Dokumentation
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
