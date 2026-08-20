# Panther Crawler — Vollstandige API

```php
$crawler = $client->request('GET', '/');
$title   = $crawler->filter('h1')->text();
$links   = $crawler->filter('nav a')->links();
$form    = $crawler->selectButton('Anmelden')->form();
```

## Wichtigste Methoden-Gruppen

- **Filtern**: `filter($css)`, `filterXPath($xpath)`, `matches($css)`
- **Traversal**: `eq($pos)`, `first()`, `last()`, `children($css?)`, `siblings()`, `nextAll()`, `previousAll()`, `ancestors()`, `closest($css)`
- **Werte lesen**: `attr($name, $default?)`, `text($default?)` (nur normalisiert!), `html($default?)` (=outerHTML), `nodeName()`
- **Iteration**: `each(callable)`, `reduce(callable)`, `count()`, `slice($offset, $length?)`
- **Extraktion**: `extract(array $attributes)` — `evaluate()` wirft Exception in PantherCrawler
- **Links/Bilder**: `links()`, `images()`, `selectLink($text)`, `selectImage($alt)`, `link()`, `image()`
- **Formulare**: `selectButton($text)`, `form($values?, $method?)`, `getElement(int $position)` (WebDriverElement)

## Vertiefung

- [CRAWLER-DETAIL.md](CRAWLER-DETAIL.md) — Jede Methode mit vollstandiger Signatur, Ruckgabetyp, DomCrawler-Grundlagen und Beispielen
