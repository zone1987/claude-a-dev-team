# Panther Crawler — Vollstandige API-Referenz

`Symfony\Component\Panther\DomCrawler\Crawler` erweitert
`Symfony\Component\DomCrawler\Crawler`.

## Konstruktion / Erzeugung

```php
// Aus Client-Request
$crawler = $client->request('GET', '/');

// Aus waitFor
$crawler = $client->waitFor('.dynamic-element');

// Direkt (ohne Browser, fur Unit-Tests)
use Symfony\Component\DomCrawler\Crawler;
$crawler = new Crawler('<html><body><p class="msg">Hallo</p></body></html>');
```

---

## Filtern (Auswahl)

### filter

```php
public function filter(string $selector): static
```

Filtert nach CSS-Selektor. Erfordert `symfony/css-selector` (wird automatisch mit Panther installiert).

```php
$paragraphs = $crawler->filter('article > p');
$links      = $crawler->filter('nav a[href]');
$inputs     = $crawler->filter('form input:not([type=hidden])');
```

### filterXPath

```php
public function filterXPath(string $xpath): static
```

Filtert nach XPath-Ausdruck.

```php
$nodes = $crawler->filterXPath('//div[@class="content"]/p');
$texts = $crawler->filterXPath('descendant-or-self::h2');
```

### matches

```php
public function matches(string $selector): bool
```

Pruft ob der aktuelle Knoten den CSS-Selektor erfullt.

```php
if ($crawler->filter('button')->first()->matches('[disabled]')) { ... }
```

### registerNamespace

```php
public function registerNamespace(string $prefix, string $namespace): void
// NICHT implementiert in PantherCrawler — wirft LogicException ("not supported")
```

Quelle: `src/DomCrawler/Crawler.php:registerNamespace()`

### setDefaultNamespacePrefix

```php
public function setDefaultNamespacePrefix(string $prefix): void
// NICHT implementiert in PantherCrawler — wirft LogicException ("not supported")
```

Quelle: `src/DomCrawler/Crawler.php:setDefaultNamespacePrefix()`

---

## Traversal (Baum-Navigation)

### eq

```php
public function eq(int $position): static
```

Element an Position `$position` (0-basiert).

```php
$thirdRow = $crawler->filter('tr')->eq(2);
```

### first

```php
public function first(): static
```

Erstes gefundenes Element.

### last

```php
public function last(): static
```

Letztes gefundenes Element.

### slice

```php
public function slice(int $offset = 0, int $length = null): static
```

Teilmenge der gefundenen Elemente.

```php
$firstThree = $crawler->filter('li')->slice(0, 3);
$fromSecond = $crawler->filter('li')->slice(1);
```

### children

```php
public function children(?string $selector = null): static
```

Direkte Kind-Knoten, optional gefiltert nach CSS-Selektor.

```php
$items     = $crawler->filter('ul')->children();
$listItems = $crawler->filter('ul')->children('li.active');
```

### siblings

```php
public function siblings(): static
```

Alle Geschwister-Knoten (ohne den Knoten selbst).

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

Nachster Vorfahre der den CSS-Selektor erfullt (inkl. aktueller Knoten). Gibt `null` zuruck wenn nicht gefunden.

```php
$form = $crawler->filter('input[name=email]')->closest('form');
```

---

## Werte lesen

### text

```php
public function text(
    ?string $default = null,
    bool    $normalizeWhitespace = true
): string
```

Gibt den sichtbaren Textinhalt des Knotens zuruck (wie `innerText` im Browser).
- `$default`: Ruckgabewert wenn kein Knoten gefunden
- `$normalizeWhitespace`: Whitespace normalisieren und trimmen (Default: `true`)

Wichtig: In `PantherCrawler` muss `$normalizeWhitespace = true` sein (Default). Der Wert
`false` wirft `InvalidArgumentException` ("Panther only supports getting normalized text.").

Quelle: `src/DomCrawler/Crawler.php:text()`

```php
$title = $crawler->filter('h1')->text();
// FEHLER: $crawler->filter('pre')->text(null, false); // => InvalidArgumentException
```

### html

```php
public function html(?string $default = null): string
```

Gibt das HTML des Knotens zuruck. Fur das `<html>`-Root-Element: vollstandiger Seitenquelltext
via `$webDriver->getPageSource()`. Fur alle anderen Elemente: `outerHTML` des Elements
(inkl. eigener Tags). Es gibt KEINE separate `outerHtml()`-Methode in `PantherCrawler`.

Quelle: `src/DomCrawler/Crawler.php:html()`

```php
$html = $crawler->filter('.content')->html();
// z. B.: '<div class="content"><p>Hello</p></div>'

$pageSource = $crawler->filter('html')->html();
// vollstandiger Seitenquelltext
```

### attr

```php
public function attr(
    string  $attribute,
    ?string $default = null
): ?string
```

Gibt den Attributwert des ersten Knotens zuruck.

```php
$href  = $crawler->filter('a.primary')->attr('href');
$cls   = $crawler->filter('div')->attr('class', 'no-class');
$val   = $crawler->filter('input[name=token]')->attr('value');
```

### nodeName

```php
public function nodeName(): string
```

Gibt den HTML-Tag-Namen in Kleinbuchstaben zuruck.

```php
$tag = $crawler->filter('.container > *')->first()->nodeName(); // 'div', 'p', etc.
```

---

## Iteration

### each

```php
public function each(callable $closure): array
```

Ruft `$closure(Crawler $node, int $index)` fur jeden Knoten auf.
Gibt Array der Ruckgabewerte zuruck.

```php
$texts = $crawler->filter('li')->each(fn(Crawler $node, int $i) => $node->text());
// ['Item 1', 'Item 2', 'Item 3']
```

### reduce

```php
public function reduce(callable $closure): static
```

Behalt nur Knoten fur die `$closure(Crawler $node, int $index)` `true` zuruckgibt.

```php
$evenRows = $crawler->filter('tr')->reduce(fn(Crawler $node, int $i) => $i % 2 === 0);
```

### count

```php
public function count(): int
```

Anzahl der gefundenen Knoten.

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

Extrahiert Attributwerte fur alle gefundenen Knoten.
Sonderattribute: `'_name'` (Tag-Name), `'_text'` (Textinhalt).

```php
$data = $crawler->filter('a')->extract(['href', '_text']);
// [['https://...', 'Link-Text'], ['https://...', 'Anderer Text']]

$classes = $crawler->filter('div')->extract(['class']);
// [['container'], ['wrapper'], ...]

$meta = $crawler->filterXPath('//body/*')->extract(['_name', '_text', 'class']);
```

### evaluate

`PantherCrawler::evaluate()` ist NICHT implementiert und wirft immer eine
`LogicException` ("not supported"). Diese Methode stammt aus der Basis-Klasse
`DomCrawler\Crawler`, ist aber im WebDriver-Modus nicht verwendbar.

Quelle: `src/DomCrawler/Crawler.php:evaluate()` — wirft via `ExceptionThrower`

```php
// NICHT nutzbar mit PantherCrawler:
// $crawler->evaluate('//span'); // => LogicException
```

Stattdessen: `filterXPath()` verwenden.

---

## Links

### links

```php
public function links(): array
```

Gibt alle `Link`-Objekte aus `<a>`-Elementen im Crawler zuruck.

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

Gibt ein `Link`-Objekt (`Symfony\Component\Panther\DomCrawler\Link`) fur den aktuellen Knoten
zuruck. Nur `'get'` ist als Methode zugelassen — andere Werte werfen `InvalidArgumentException`.

Quelle: `src/DomCrawler/Crawler.php:link()`

```php
$link = $crawler->filter('a.cta')->first()->link();
$client->click($link);
```

### selectLink

```php
public function selectLink(string $value): static
```

Findet `<a>`, `<area>` und `<link>` Elemente anhand von Text-Inhalt, `id` oder `title`-Attribut.

```php
$loginLink = $crawler->selectLink('Anmelden');
$client->click($loginLink->link());
```

### getUri

```php
public function getUri(): string
```

Gibt die absolute URI des aktuellen Link-/Image-Elements zuruck.

---

## Bilder

### images

```php
public function images(): array
```

Gibt alle `Image`-Objekte aus `<img>`-Elementen zuruck.

### image

```php
public function image(): Image
```

Gibt ein `Image`-Objekt fur den aktuellen Knoten zuruck.

### selectImage

```php
public function selectImage(string $value): static
```

Findet `<img>` nach `alt`-Text.

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

Findet `<button>`, `<input type="submit">`, `<input type="button">`, `<input type="image">`
anhand von: Text-Inhalt, `id`, `name`, `alt` (fur Images) oder `value`-Attribut.

```php
$buttonCrawler = $crawler->selectButton('Anmelden');
$buttonCrawler = $crawler->selectButton('submit-btn');  // per id
```

### form

```php
public function form(
    array   $values = [],   // Formularwerte vorbelegen
    ?string $method = null  // HTTP-Methode uberschreiben
): Form
```

Erstellt ein `Form`-Objekt fur das Formular, das den Button enthalt (oder das aktuelle Form-Element).

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

Gibt das `WebDriverElement` an Index `$position` (0-basiert) zuruck, oder `null` wenn
die Position nicht existiert. Nur bei WebDriver-Clients verfugbar.

Quelle: `src/DomCrawler/Crawler.php:getElement()`

```php
$el = $crawler->filter('.upload-zone')->getElement(0);
if (null !== $el) {
    $el->sendKeys('/path/to/file.pdf');
}

// Erstes Element — Standard-Verwendung
$input = $crawler->filter('input[name=email]')->getElement(0);
```

---

## Form-Klasse — Vollstandige API

`Symfony\Component\DomCrawler\Form`

### Factory

```php
$form = $crawler->selectButton('Submit')->form();
$form = $crawler->filter('form.login')->form();
$form = $crawler->filter('form')->form(['username' => 'admin']);
```

### Werte-Methoden

```php
$form->getValues(): array              // flaches Array aller Formularwerte
$form->setValues(array $values): self  // mehrere Werte setzen
$form->getPhpValues(): array           // verschachteltes Array (fur PHP-Arrays im Form)
$form->getPhpFiles(): array            // verschachteltes Array der Datei-Uploads
$form->getFiles(): array               // flaches Array der Datei-Uploads
```

### Informations-Methoden

```php
$form->getUri(): string     // vollstandige URI (inkl. Query-String bei GET)
$form->getMethod(): string  // 'GET' oder 'POST'
$form->getName(): string    // name-Attribut des Formulars
```

### Validierung

```php
$form->disableValidation(): self  // Nur auf Form-Ebene; ChoiceFormField::disableValidation() wirft LogicException
```

Quelle: `src/DomCrawler/Field/ChoiceFormField.php:disableValidation()` — nicht implementiert

### Felder-Zugriff

```php
// Einzelne Felder direkt uber Array-Syntax
$form['username']->setValue('admin');
$form['role']->select('ADMIN');
$form['active']->tick();

// ACHTUNG: $form['country']->disableValidation() ist in Panther NICHT verfugbar
// (wirft LogicException). Stattdessen: direkt per value selectieren.
$form['country']->select('DE');
```

---

## FormField-Typen — Vollstandige Methoden

### InputFormField (`<input type="text|email|number|...">`)

```php
setValue(string $value): void   // Setzt den Eingabewert
getValue(): string              // Gibt den aktuellen Wert zuruck
```

### TextareaFormField (`<textarea>`)

```php
setValue(string $value): void
getValue(): string
```

### ChoiceFormField (`<select>`, `<input type="radio">`, `<input type="checkbox">`)

```php
select(string|array $value): void
// Wahlt eine Option in <select> oder setzt Radio/Checkbox
// Fur Multi-Select: $value als Array ['opt1', 'opt2']

tick(): void   // Setzt Checkbox auf checked (true)
untick(): void // Entfernt Checkbox-Haken

getValue(): string|array        // Aktuell ausgewahlter Wert
isDisabled(): bool              // Pruft ob Feld disabled ist

availableOptionValues(): array
// Gibt alle verfugbaren value-Attribute der Options zuruck
```

Hinweis: `addChoice()` aus der Basis-Klasse ist in `PantherCrawler::ChoiceFormField`
NICHT implementiert und wirft `LogicException` ("not supported").
Quelle: `src/DomCrawler/Field/ChoiceFormField.php:addChoice()`

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
upload(?string $path): void       // Setzt Dateipfad (geerbt, ruft setValue() intern)
setFilePath(string $path): void   // Setzt Pfad direkt via sendKeys() auf das Element
setValue(?string $value): void    // Normalisiert Pfad via realpath(), ruft setFilePath()
getValue(): array|string|null     // Gibt Upload-Array: ['name','type','tmp_name','error','size']
```

Quelle: `src/DomCrawler/Field/FileFormField.php`

```php
$form['avatar']->upload('/var/www/tests/fixtures/avatar.jpg');
$form['document']->upload('/tmp/contract.pdf');
// oder direkt:
$form['avatar']->setFilePath('/absolute/path/photo.jpg');
```

---

## Inhalte hinzufugen

Hinweis: Die folgenden Methoden (geerbt von `DomCrawler\Crawler`) sind in `PantherCrawler`
ALLE NICHT implementiert und werfen `LogicException` ("not supported"):
`add()`, `addContent()`, `addHtmlContent()`, `addXmlContent()`, `addDocument()`,
`addNodeList()`, `addNodes()`, `addNode()`, `clear()`.

Quelle: `src/DomCrawler/Crawler.php` — alle diese Methoden delegieren an `ExceptionThrower`

Fur Panther-Tests wird der Crawler ausschliesslich vom `Client` via `request()`, `waitFor*()` oder
`refreshCrawler()` erzeugt. Direktes Befuellen ist nicht moeglich.

```php
// Richtig: Crawler uber Client erzeugen
$crawler = $client->request('GET', '/');

// NICHT moeglich:
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

| Einschrankung                 | Beschreibung                                         |
|-------------------------------|------------------------------------------------------|
| Kein XML-Crawling             | Nur HTML-Dokumente werden unterstutzt               |
| Keine DOM-Manipulation        | Crawler ist read-only (kein Schreiben ins DOM)       |
| Kein `\DOMElement`            | `getElement()` gibt `WebDriverElement`, nicht DOMElement |
| Keine Multi-Dimensionalen Arrays | Formularfelder mit `name[]`-Syntax haben Einschrankungen |
| Kein invalides `<select>`     | Standardmassig keine ungultigen Optionen wahlbar     |
| Bootstrap 5 Smooth Scroll     | Kann waitFor-Methoden storen — deaktivieren via `$enable-smooth-scroll: false` |

---

Quellen:
- https://symfony.com/doc/current/components/dom_crawler.html
- https://raw.githubusercontent.com/symfony/panther/main/src/Client.php
- https://symfony.com/doc/current/testing/end_to_end.html
