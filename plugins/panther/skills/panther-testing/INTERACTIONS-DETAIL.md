# Panther — complete interactions reference

## Contents

- [1. Click methods](#1-click-methods)
- [2. Form interactions](#2-form-interactions)
- [3. Form object — complete interactions API](#3-form-object--complete-interactions-api)
- [4. FormField classes — method tables](#4-formfield-classes--method-tables)
- [5. Mouse-API](#5-mouse-api)
- [6. Drag & Drop](#6-drag-drop)
- [7. Keyboard-API](#7-keyboard-api)
- [8. Element methods (WebDriverElement)](#8-element-methods-webdriverelement)
- [9. File upload (complete)](#9-file-upload-complete)
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
$client->clickLink('Next');
$client->clickLink('Log out');
```

---

## 2. Form interactions

### client->submitForm

```php
public function submitForm(
    string $buttonText,          // text, id or name of the submit button
    array  $fieldValues  = [],   // field values: ['fieldname' => 'value']
    string $method       = null, // override the HTTP method
    array  $serverParameters = []
): Crawler
```

Shorthand for quick form interactions:

```php
$client->submitForm('Sign in', [
    'login[email]'    => 'user@example.com',
    'login[password]' => 'secret123',
]);

$client->submitForm('Search', ['q' => 'symfony panther'], 'GET');
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
$form = $crawler->selectButton('Order')->form();
$form['quantity']->setValue('3');
$form['address']->setValue('Example Street 1');
$client->submit($form);
```

---

## 3. Form object — complete interactions API

### Setting fields via array syntax

```php
$form = $crawler->selectButton('Save')->form();

// Input/Textarea
$form['username'] = 'symfonyfan';               // shorthand
$form['username']->setValue('symfonyfan');      // explicit

// Select
$form['country']->select('DE');
$form['lang']->select(['de', 'en']);            // multi-select

// Checkbox
$form['newsletter']->tick();
$form['marketing']->untick();

// Radio
$form['gender']->select('m');

// File upload
$form['avatar']->upload('/absolute/path/to/photo.jpg');
```

### setValues (bulk assignment)

```php
$form->setValues([
    'registration[username]' => 'symfonyfan',
    'registration[email]'    => 'fan@symfony.com',
    'registration[terms]'    => '1',
]);
```

### Nested arrays (PHP forms)

```php
// The form has: <input name="multi[]" value="a"> and <input name="multi[]" value="b">
$form->setValues(['multi' => ['x', 'y']]);

// With explicit indices
$form->setValues(['grid' => [
    0             => 'Value A',
    'dimensional' => 'Value B',
]]);

// Multiple checkboxes by value
$form->setValues(['interests' => ['php', 'symfony']]);
```

### Disabling validation

```php
// At form level (from the base class, works)
$form->disableValidation();
```

Note: `$form['country']->disableValidation()` (at ChoiceFormField level) in Panther
is NOT implemented and throws `LogicException`. Source: `src/DomCrawler/Field/ChoiceFormField.php:disableValidation()`.

---

## 4. FormField classes — method tables

### InputFormField

Responsible for: `<input type="text">`, `<input type="email">`, `<input type="number">`,
`<input type="hidden">`, `<input type="password">`, `<input type="search">`, etc.

| Method                   | Signature                      | Description                       |
|--------------------------|--------------------------------|-----------------------------------|
| `setValue`               | `setValue(string $value): void` | Sets the field value             |
| `getValue`               | `getValue(): string`           | Reads the current value           |

### TextareaFormField

Responsible for: `<textarea>`

| Method      | Signature                       | Description               |
|-------------|---------------------------------|---------------------------|
| `setValue`  | `setValue(string $value): void` | Sets the content           |
| `getValue`  | `getValue(): string`            | Reads the current content  |

### ChoiceFormField

Responsible for: `<select>`, `<input type="radio">`, `<input type="checkbox">`

| Method        | Signature                                         | Description                                     |
|---------------|---------------------------------------------------|-------------------------------------------------|
| `select`      | `select(string\|array $value): void`              | Selects option(s)                              |
| `tick`        | `tick(): void`                                    | Sets checkbox = checked                        |
| `untick`      | `untick(): void`                                  | Sets checkbox = unchecked                      |
| `getValue`    | `getValue(): string\|array`                       | Returns the selected value / selected values |
| `isDisabled`  | `isDisabled(): bool`                              | True if the field is disabled                   |
| `availableOptionValues` | `availableOptionValues(): array` | Returns all available option values as a string array |

### FileFormField

Responsible for: `<input type="file">`

| Method        | Signature                                 | Description                                                 |
|---------------|-------------------------------------------|-------------------------------------------------------------|
| `upload`      | `upload(?string $path): void`             | Sets the absolute file path for the upload (inherited)      |
| `setFilePath` | `setFilePath(string $path): void`         | Sets the file path directly via `sendKeys()` on the element |
| `setValue`    | `setValue(?string $value): void`          | Like `upload`, normalizes the path via `realpath()`         |
| `getValue`    | `getValue(): array\|string\|null`         | Returns the upload array `['name','type','tmp_name','error','size']` |

Source: `src/DomCrawler/Field/FileFormField.php`

---

## 5. Mouse-API

`$client->getMouse()` returns `\Symfony\Component\Panther\WebDriver\WebDriverMouse` —
Panther's own class, which wraps `BaseWebDriverMouse` and adds CSS-selector-based helper
methods. All `*To` methods take a CSS selector, convert it to coordinates and
delegate to the underlying `BaseWebDriverMouse`.

Source: `src/WebDriver/WebDriverMouse.php`

### clickTo

```php
public function clickTo(string $cssSelector): self
```

Left-click on an element by CSS selector. No offset parameter.

```php
$client->getMouse()->clickTo('#submit-btn');
$client->getMouse()->clickTo('.card:first-child');
```

### doubleClickTo

```php
public function doubleClickTo(string $cssSelector): self
```

Double-click on an element. No offset parameter.

```php
$client->getMouse()->doubleClickTo('.editable-cell');
```

### contextClickTo

```php
public function contextClickTo(string $cssSelector): self
```

Right-click (context menu) on an element. No offset parameter.

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
$client->clickLink('Settings');
```

### mouseDownTo / mouseUpTo

```php
public function mouseDownTo(string $cssSelector): self
public function mouseUpTo(string $cssSelector): self
```

Press / release the mouse button (for drag & drop). No offset parameter.

### click / contextClick / doubleClick / mouseDown / mouseUp / mouseMove (low-level)

The low-level methods take `WebDriverCoordinates` instead of a CSS selector:

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

// With offset
$actions->dragAndDropBy($source, 100, 50)->perform();

// Manual (press-move-release)
$actions
    ->clickAndHold($source)
    ->moveToElement($target)
    ->release()
    ->perform();
```

---

## 7. Keyboard-API

`$client->getKeyboard()` returns a `\Facebook\WebDriver\WebDriverKeyboard`.

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

### WebDriverKeys constants (selection)

```php
use Facebook\WebDriver\WebDriverKeys;

WebDriverKeys::ENTER         // Enter/Return
WebDriverKeys::TAB           // Tab
WebDriverKeys::ESCAPE        // Escape
WebDriverKeys::BACKSPACE     // Backspace
WebDriverKeys::DELETE        // Delete
WebDriverKeys::SPACE         // Space
WebDriverKeys::ARROW_UP      // Arrow up
WebDriverKeys::ARROW_DOWN    // Arrow down
WebDriverKeys::ARROW_LEFT    // Arrow left
WebDriverKeys::ARROW_RIGHT   // Arrow right
WebDriverKeys::HOME          // Home
WebDriverKeys::END           // End
WebDriverKeys::PAGE_UP       // Page up
WebDriverKeys::PAGE_DOWN     // Page down
WebDriverKeys::F1 ... F12    // Function keys
WebDriverKeys::CONTROL       // Ctrl
WebDriverKeys::SHIFT         // Shift
WebDriverKeys::ALT           // Alt
WebDriverKeys::META          // Meta/Windows/Cmd
WebDriverKeys::NULL_KEY      // Release modifier
```

### Key combinations

```php
use Facebook\WebDriver\Interactions\WebDriverActions;

$actions = new WebDriverActions($client->getWebDriver());

// Ctrl+A (select all)
$actions->keyDown(null, WebDriverKeys::CONTROL)
        ->sendKeys(null, 'a')
        ->keyUp(null, WebDriverKeys::CONTROL)
        ->perform();

// Directly on an element
$el = $client->findElement(WebDriverBy::cssSelector('input'));
$actions->keyDown($el, WebDriverKeys::SHIFT)
        ->sendKeys($el, 'hello')
        ->keyUp($el, WebDriverKeys::SHIFT)
        ->perform();
```

---

## 8. Element methods (WebDriverElement)

Available after `$crawler->filter('...')->getElement(0)`
(signature: `getElement(int $position): ?WebDriverElement`):

```php
$el = $crawler->filter('#my-input')->getElement(0);

$el->click(): void
$el->sendKeys(string $value): self      // Type text
$el->clear(): self                      // Clear the content
$el->submit(): void                     // Submit the parent form
$el->getText(): string                  // Visible text
$el->getAttribute(string $name): ?string
$el->isEnabled(): bool
$el->isSelected(): bool
$el->isDisplayed(): bool
$el->getTagName(): string
$el->getLocation(): WebDriverPoint      // {x, y} position
$el->getSize(): WebDriverDimension      // {width, height}
$el->getRect(): WebDriverRect           // {x, y, width, height}
$el->getCSSValue(string $property): string
$el->findElement(WebDriverBy $by): WebDriverElement
$el->findElements(WebDriverBy $by): array
$el->takeScreenshot(): string           // Screenshot of this element only
```

---

## 9. File upload (complete)

### Via Crawler/Form (recommended)

```php
$form = $crawler->selectButton('Upload')->form();
$form['profile_picture']->upload('/absolute/path/to/image.jpg');
$client->submit($form);
```

### Via WebDriverElement (for custom inputs)

```php
$fileInput = $client->findElement(
    \Facebook\WebDriver\WebDriverBy::cssSelector('input[type=file]')
);
$fileInput->sendKeys('/absolute/path/to/document.pdf');
```

### Multiple files (multi-upload)

```php
// Upload field for multiple files (<input type="file" multiple>)
$form['attachments[]']->upload('/path/file1.pdf');
// Second file via WebDriver (directly)
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
        $form = $client->getCrawler()->selectButton('Save')->form();
        $form['product[name]']->setValue('New product');
        $form['product[description]']->setValue("Line 1\nLine 2");
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

        // Wait for the success message
        $client->waitForElementToContain('.flash-success', 'saved');
        $this->assertSelectorWillExist('.product-detail');
        $this->assertSelectorTextContains('h1', 'New product');

        // Screenshot for documentation
        $client->takeScreenshot('/tmp/product-saved.png');
    }
}
```

---

Sources:
- https://symfony.com/doc/current/testing/end_to_end.html
- https://symfony.com/doc/current/components/dom_crawler.html
- https://github.com/php-webdriver/php-webdriver
- https://github.com/symfony/panther
