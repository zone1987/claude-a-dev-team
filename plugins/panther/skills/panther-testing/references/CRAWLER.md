# Panther Crawler — Complete API

```php
$crawler = $client->request('GET', '/');
$title   = $crawler->filter('h1')->text();
$links   = $crawler->filter('nav a')->links();
$form    = $crawler->selectButton('Anmelden')->form();
```

## Most important method groups

- **Filtering**: `filter($css)`, `filterXPath($xpath)`, `matches($css)`
- **Traversal**: `eq($pos)`, `first()`, `last()`, `children($css?)`, `siblings()`, `nextAll()`, `previousAll()`, `ancestors()`, `closest($css)`
- **Reading values**: `attr($name, $default?)`, `text($default?)` (normalized only!), `html($default?)` (= outerHTML), `nodeName()`
- **Iteration**: `each(callable)`, `reduce(callable)`, `count()`, `slice($offset, $length?)`
- **Extraction**: `extract(array $attributes)` — `evaluate()` throws an exception in PantherCrawler
- **Links/images**: `links()`, `images()`, `selectLink($text)`, `selectImage($alt)`, `link()`, `image()`
- **Forms**: `selectButton($text)`, `form($values?, $method?)`, `getElement(int $position)` (WebDriverElement)

## Deep dive

- [CRAWLER-DETAIL.md](CRAWLER-DETAIL.md) — every method with its complete signature, return type, DomCrawler basics and examples
