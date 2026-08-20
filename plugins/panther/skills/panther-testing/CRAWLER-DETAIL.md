# Panther Crawler — Complete API reference

`Symfony\Component\Panther\DomCrawler\Crawler` erweitert
`Symfony\Component\DomCrawler\Crawler`.

## Contents

- [Konstruktion / Erzeugung](#konstruktion-erzeugung)
- [Filtern (Auswahl)](#filtern-auswahl)
- [Traversal (Baum-Navigation)](#traversal-baum-navigation)
- [Reading values](#reading-values)
- [Iteration](#iteration)
- [Extraktion](#extraktion)
- [Links](#links)
- [Bilder](#bilder)
- [Formulare](#formulare)
- [Form class — complete API](#form-class--complete-api)
- [FormField types — complete methods](#formfield-types--complete-methods)
- [Inhalte hinzufugen](#inhalte-hinzufugen)
- [URI-Auflosung](#uri-auflosung)
- [Bekannte Einschrankungen (PantherCrawler)](#bekannte-einschrankungen-panthercrawler)

## Konstruktion / Erzeugung

```php
// Aus Client-Request
$crawler = $client->request('GET', '/');

// Aus waitFor
$crawler = $client->waitFor('.dynamic-element');

// Directly (without a browser, for unit tests)
use Symfony\Component\DomCrawler\Crawler;
$crawler = new Crawler('<html><body><p class="msg">Hallo</p></body></html>');
```

---

## Filtern (Auswahl)

### filter

```php
public function filter(string $selector): static
```

Filters by CSS selector. Requires `symfony/css-selector` (installed automatically with Panther).

```php
$paragraphs = $crawler->filter('article > p');
$links      = $crawler->filter('nav a[href]');
$inputs     = $crawler->filter('form input:not([type=hidden])');
```

### filterXPath

```php
public function filterXPath(string $xpath): static
```

Filters by XPath expression.

```php
$nodes = $crawler->filterXPath('//div[@class="content"]/p');
$texts = $crawler->filterXPath('descendant-or-self::h2');
```

### matches

```php
public function matches(string $selector): bool
```

Checks whether the current node matches the CSS selector.

```php
if ($crawler->filter('button')->first()->matches('[disabled]')) { ... }
```

### registerNamespace

```php
public function registerNamespace(string $prefix, string $namespace): void
// NOT implemented in PantherCrawler — throws LogicException ("not supported")
```

Source: `src/DomCrawler/Crawler.php:registerNamespace()`

### setDefaultNamespacePrefix

```php
public function setDefaultNamespacePrefix(string $prefix): void
// NOT implemented in PantherCrawler — throws LogicException ("not supported")
```

Source: `src/DomCrawler/Crawler.php:setDefaultNamespacePrefix()`

---

## Traversal (Baum-Navigation)

### eq

```php
public function eq(int $position): static
```

Element at position `$position` (0-based).

```php
$thirdRow = $crawler->filter('tr')->eq(2);
```

### first

```php
public function first(): static
```

First element found.

### last

```php
public function last(): static
```

Last element found.

### slice

```php
public function slice(int $offset = 0, int $length = null): static
```

Subset of the elements found.

```php
$firstThree = $crawler->filter('li')->slice(0, 3);
$fromSecond = $crawler->filter('li')->slice(1);
```

### children

```php
public function children(?string $selector = null): static
```

Direct child nodes, optionally filtered by CSS selector.

```php
$items     = $crawler->filter('ul')->children();
$listItems = $crawler->filter('ul')->children('li.active');
```

### siblings

```php
public function siblings(): static
```

All sibling nodes (excluding the node itself).

### nextAll

```php
public function nextAll(): static
```

Alle nachfolgenden Geschwister.

### previousAll

```php
public function previousAll(): static
```

Alle vorherigen Geschwister.

### ancestors

```php
public function ancestors(): static
```

Alle Vorfahren (parent, grandparent, ...).

### closest

```php
public function closest(string $selector): ?static
```

Nearest ancestor matching the CSS selector (including the current node). Returns `null` if none is found.

```php
$form = $crawler->filter('input[name=email]')->closest('form');
```

---

## Reading values

### text

```php
public function text(
    ?string $default = null,
    bool    $normalizeWhitespace = true
): string
```

Returns the visible text content of the node (like `innerText` in the browser).
- `$default`: return value if no node was found
- `$normalizeWhitespace`: normalize and trim whitespace (default: `true`)

Important: in `PantherCrawler`, `$normalizeWhitespace = true` is required (the default). The value
`false` throws `InvalidArgumentException` ("Panther only supports getting normalized text.").

Source: `src/DomCrawler/Crawler.php:text()`

```php
$title = $crawler->filter('h1')->text();
// FEHLER: $crawler->filter('pre')->text(null, false); // => InvalidArgumentException
```

### html

```php
public function html(?string $default = null): string
```

Returns the HTML of the node. For the `<html>` root element: the complete page source
via `$webDriver->getPageSource()`. For all other elements: the `outerHTML` of the element
(including its own tags). There is NO separate `outerHtml()` method in `PantherCrawler`.

Source: `src/DomCrawler/Crawler.php:html()`

```php
$html = $crawler->filter('.content')->html();
// z. B.: '<div class="content"><p>Hello</p></div>'

$pageSource = $crawler->filter('html')->html();
// complete page source
```

### attr

```php
public function attr(
    string  $attribute,
    ?string $default = null
): ?string
```

Returns the attribute value of the first node.

```php
$href  = $crawler->filter('a.primary')->attr('href');
$cls   = $crawler->filter('div')->attr('class', 'no-class');
$val   = $crawler->filter('input[name=token]')->attr('value');
```

### nodeName

```php
public function nodeName(): string
```

Returns the HTML tag name in lower case.

```php
$tag = $crawler->filter('.container > *')->first()->nodeName(); // 'div', 'p', etc.
```

---

## Iteration

### each

```php
public function each(callable $closure): array
```

Calls `$closure(Crawler $node, int $index)` for every node.
Returns an array of the return values.

```php
$texts = $crawler->filter('li')->each(fn(Crawler $node, int $i) => $node->text());
// ['Item 1', 'Item 2', 'Item 3']
```

### reduce

```php
public function reduce(callable $closure): static
```

Keeps only the nodes for which `$closure(Crawler $node, int $index)` returns `true`.

```php
$evenRows = $crawler->filter('tr')->reduce(fn(Crawler $node, int $i) => $i % 2 === 0);
```

### count

```php
public function count(): int
```

Number of nodes found.

```php
$itemCount = $crawler->filter('li')->count();
if ($crawler->filter('.error')->count() > 0) { ... }
```

### Iteration als DOMElement

```php
foreach ($crawler->filter('p') as $domElement) {
    echo $domElement->nodeName . ': ' . $domElement->textContent;
}
```

---

## Extraktion

### extract

```php
public function extract(array $attributes): array
```

Extracts attribute values for all nodes found.
Sonderattribute: `'_name'` (Tag-Name), `'_text'` (Textinhalt).

```php
$data = $crawler->filter('a')->extract(['href', '_text']);
// [['https://...', 'Link text'], ['https://...', 'Other text']]

$classes = $crawler->filter('div')->extract(['class']);
// [['container'], ['wrapper'], ...]

$meta = $crawler->filterXPath('//body/*')->extract(['_name', '_text', 'class']);
```

### evaluate

`PantherCrawler::evaluate()` is NOT implemented and always throws a
`LogicException` ("not supported"). This method comes from the base class
`DomCrawler\Crawler`, but is not usable in WebDriver mode.

Source: `src/DomCrawler/Crawler.php:evaluate()` — throws via `ExceptionThrower`

```php
// NOT usable with PantherCrawler:
// $crawler->evaluate('//span'); // => LogicException
```

Stattdessen: `filterXPath()` verwenden.

---

## Links

### links

```php
public function links(): array
```

Returns all `Link` objects from `<a>` elements in the crawler.

```php
$links = $crawler->filter('nav')->links();
foreach ($links as $link) {
    echo $link->getUri();  // absolute URI
}
```

### link

```php
public function link(string $method = 'get'): Link
```

Returns a `Link` object (`Symfony\Component\Panther\DomCrawler\Link`) for the current
node. Only `'get'` is allowed as the method — other values throw `InvalidArgumentException`.

Source: `src/DomCrawler/Crawler.php:link()`

```php
$link = $crawler->filter('a.cta')->first()->link();
$client->click($link);
```

### selectLink

```php
public function selectLink(string $value): static
```

Finds `<a>`, `<area>` and `<link>` elements by text content, `id` or `title` attribute.

```php
$loginLink = $crawler->selectLink('Anmelden');
$client->click($loginLink->link());
```

### getUri

```php
public function getUri(): string
```

Returns the absolute URI of the current link/image element.

---

## Bilder

### images

```php
public function images(): array
```

Returns all `Image` objects from `<img>` elements.

### image

```php
public function image(): Image
```

Returns an `Image` object for the current node.

### selectImage

```php
public function selectImage(string $value): static
```

Finds `<img>` by `alt` text.

```php
$img = $crawler->selectImage('Company Logo')->image();
echo $img->getUri();
```

---

## Formulare

### selectButton

```php
public function selectButton(string $value): static
```

Finds `<button>`, `<input type="submit">`, `<input type="button">`, `<input type="image">`
by: text content, `id`, `name`, `alt` (for images) or the `value` attribute.

```php
$buttonCrawler = $crawler->selectButton('Anmelden');
$buttonCrawler = $crawler->selectButton('submit-btn');  // per id
```

### form

```php
public function form(
    array   $values = [],   // Formularwerte vorbelegen
    ?string $method = null  // override the HTTP method
): Form
```

Creates a `Form` object for the form that contains the button (or the current form element).

```php
$form = $crawler->selectButton('Login')->form([
    'email'    => 'user@example.com',
    'password' => 'secret123',
]);
$client->submit($form);
```

### getElement (Panther-spezifisch)

```php
public function getElement(int $position): ?\Facebook\WebDriver\WebDriverElement
```

Returns the `WebDriverElement` at index `$position` (0-based), or `null` if
the position does not exist. Only available with WebDriver clients.

Source: `src/DomCrawler/Crawler.php:getElement()`

```php
$el = $crawler->filter('.upload-zone')->getElement(0);
if (null !== $el) {
    $el->sendKeys('/path/to/file.pdf');
}

// First element — standard usage
$input = $crawler->filter('input[name=email]')->getElement(0);
```

---

## Form class — complete API

`Symfony\Component\DomCrawler\Form`

### Factory

```php
$form = $crawler->selectButton('Submit')->form();
$form = $crawler->filter('form.login')->form();
$form = $crawler->filter('form')->form(['username' => 'admin']);
```

### Value methods

```php
$form->getValues(): array              // flat array of all form values
$form->setValues(array $values): self  // set multiple values
$form->getPhpValues(): array           // nested array (for PHP arrays in the form)
$form->getPhpFiles(): array            // nested array of the file uploads
$form->getFiles(): array               // flat array of the file uploads
```

### Information methods

```php
$form->getUri(): string     // complete URI (including the query string for GET)
$form->getMethod(): string  // 'GET' or 'POST'
$form->getName(): string    // name attribute of the form
```

### Validierung

```php
$form->disableValidation(): self  // Form level only; ChoiceFormField::disableValidation() throws LogicException
```

Source: `src/DomCrawler/Field/ChoiceFormField.php:disableValidation()` — not implemented

### Felder-Zugriff

```php
// Individual fields directly via array syntax
$form['username']->setValue('admin');
$form['role']->select('ADMIN');
$form['active']->tick();

// CAUTION: $form['country']->disableValidation() is NOT available in Panther
// (throws LogicException). Instead: select directly by value.
$form['country']->select('DE');
```

---

## FormField types — complete methods

### InputFormField (`<input type="text|email|number|...">`)

```php
setValue(string $value): void   // Sets the input value
getValue(): string              // Returns the current value
```

### TextareaFormField (`<textarea>`)

```php
setValue(string $value): void
getValue(): string
```

### ChoiceFormField (`<select>`, `<input type="radio">`, `<input type="checkbox">`)

```php
select(string|array $value): void
// Selects an option in <select> or sets radio/checkbox
// For multi-select: $value as an array ['opt1', 'opt2']

tick(): void   // Sets the checkbox to checked (true)
untick(): void // Removes the checkbox tick

getValue(): string|array        // Currently selected value
isDisabled(): bool              // Checks whether the field is disabled

availableOptionValues(): array
// Returns all available value attributes of the options
```

Note: `addChoice()` from the base class is NOT implemented in
`PantherCrawler::ChoiceFormField` and throws `LogicException` ("not supported").
Source: `src/DomCrawler/Field/ChoiceFormField.php:addChoice()`

Beispiele:
```php
// Select
$form['country']->select('DE');
$form['tags']->select(['php', 'symfony']);

// Checkbox
$form['newsletter']->tick();
$form['marketing']->untick();

// Radio
$form['gender']->select('m');

// Verfugbare Optionen abfragen
$options = $form['country']->availableOptionValues();
// ['DE', 'AT', 'CH', ...]
```

### FileFormField (`<input type="file">`)

```php
upload(?string $path): void       // Sets the file path (inherited, calls setValue() internally)
setFilePath(string $path): void   // Sets the path directly via sendKeys() on the element
setValue(?string $value): void    // Normalizes the path via realpath(), calls setFilePath()
getValue(): array|string|null     // Returns the upload array: ['name','type','tmp_name','error','size']
```

Source: `src/DomCrawler/Field/FileFormField.php`

```php
$form['avatar']->upload('/var/www/tests/fixtures/avatar.jpg');
$form['document']->upload('/tmp/contract.pdf');
// or directly:
$form['avatar']->setFilePath('/absolute/path/photo.jpg');
```

---

## Inhalte hinzufugen

Note: the following methods (inherited from `DomCrawler\Crawler`) are
ALL NOT implemented in `PantherCrawler` and throw `LogicException` ("not supported"):
`add()`, `addContent()`, `addHtmlContent()`, `addXmlContent()`, `addDocument()`,
`addNodeList()`, `addNodes()`, `addNode()`, `clear()`.

Source: `src/DomCrawler/Crawler.php` — all of these methods delegate to `ExceptionThrower`

For Panther tests the crawler is created exclusively by the `Client` via `request()`, `waitFor*()` or
`refreshCrawler()`. Populating it directly is not possible.

```php
// Correct: create the crawler via the client
$crawler = $client->request('GET', '/');

// NOT possible:
// $crawler = new PantherCrawler();
// $crawler->addHtmlContent('<html>...');  // => LogicException
```

---

## URI-Auflosung

```php
use Symfony\Component\DomCrawler\UriResolver;

UriResolver::resolve('/foo', 'http://localhost/bar/');
// 'http://localhost/foo'

UriResolver::resolve('?page=2', 'http://localhost/list#top');
// 'http://localhost/list?page=2'

UriResolver::resolve('../images/', 'http://localhost/a/b/');
// 'http://localhost/a/images/'
```

---

## Bekannte Einschrankungen (PantherCrawler)

| Limitation                    | Description                                          |
|-------------------------------|------------------------------------------------------|
| No XML crawling               | Only HTML documents are supported                    |
| No DOM manipulation           | The crawler is read-only (no writing into the DOM)   |
| No `\DOMElement`              | `getElement()` returns `WebDriverElement`, not DOMElement |
| No multi-dimensional arrays   | Form fields with `name[]` syntax have limitations |
| Kein invalides `<select>`     | Standardmassig keine ungultigen Optionen wahlbar     |
| Bootstrap 5 smooth scroll     | Can interfere with waitFor methods — disable via `$enable-smooth-scroll: false` |

---

Quellen:
- https://symfony.com/doc/current/components/dom_crawler.html
- https://raw.githubusercontent.com/symfony/panther/main/src/Client.php
- https://symfony.com/doc/current/testing/end_to_end.html
