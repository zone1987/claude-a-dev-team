---
name: panther-crawler
description: >
  Vollstandige Crawler-API von Symfony Panther (DomCrawler): filter/filterXPath,
  selectButton/selectLink/selectImage, form/getElement(int), attr/text/html/nodeName,
  each/eq/first/last/slice/reduce/count/extract, links/images/getUri,
  Traversal (children/siblings/nextAll/previousAll/ancestors/closest).
  Einschraenkungen: innerText(), outerHtml(), evaluate(), registerNamespace(), parents(),
  addHtmlContent() und alle add*-Methoden sind in PantherCrawler NICHT implementiert.
  Formular-Objekt (Form-Klasse) mit getValues/setValues/getFiles/getMethod.
  Complete Panther/DomCrawler Crawler API with all traversal, filtering, and form methods.
  Trigger: "panther crawler", "domcrawler api", "panther filter", "panther filterxpath",
  "panther form crawler", "panther selectbutton", "panther text attr html", "crawler eq first last",
  "crawler each reduce", "crawler extract", "crawler links images", "panther getUri",
  "domcrawler filter", "panther siblings", "panther ancestors".
---

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

- [references/deep/crawler.md](references/deep/crawler.md) — Jede Methode mit vollstandiger Signatur, Ruckgabetyp, DomCrawler-Grundlagen und Beispielen
