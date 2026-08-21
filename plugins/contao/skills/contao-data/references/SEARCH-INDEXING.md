# Contao Search Indexing (5.x)

## Contents

- [Overview](#overview)
- [Triggering indexing](#triggering-indexing)
- [Disabling the default indexer](#disabling-the-default-indexer)
- [Custom Indexer](#custom-indexer)
- [Excluding pages from the index dynamically](#excluding-pages-from-the-index-dynamically)

## Overview

Contao provides a built-in site search with:
- Word splitting across all languages
- Highlighting support
- Simple relevance sorting

For advanced features (autocomplete, facets, language analysis), external search engines can be integrated via a custom indexer.

---

## Triggering indexing

### 1. CLI crawler

```bash
vendor/bin/contao-console contao:crawl
# Options via --help
```

Based on Escargot. The domain must be set in the CLI configuration.

### 2. SearchIndexListener (automatic)

Listens on `kernel.terminate` and indexes responses on every request.

| Advantages | Disadvantages |
|---------|-----------|
| Automatic background indexing | May affect performance |
| Index updates on editor changes | Timing differs (php-fpm: after the response, mod_php/fcgi: before the response) |
| Deletes URIs on non-2xx responses | — |

### Configuration

```yaml
# config/config.yaml
contao:
    search:
        listener:
            index: true    # Update the index entry on every request
            delete: false  # Delete the entry on unsuccessful requests
```

Both set to `false` → disables the listener completely.

---

## Disabling the default indexer

```yaml
contao:
    search:
        default_indexer:
            enable: false
```

---

## Custom Indexer

### Registration

```yaml
# config/services.yaml
services:
    App\Search\ExampleSearchIndexer:
        tags:
            - { name: 'contao.search_indexer' }
```

### IndexerInterface – 3 mandatory methods

```php
interface IndexerInterface
{
    public function index(Document $document): void;    // Index a document
    public function delete(Document $document): void;   // Remove a document
    public function clear(): void;                      // Clear the entire index
}
```

### Document access

The `Document` object provides:
- HTTP status code
- HTTP headers
- Response body
- JSON-LD helpers

### Extracting JSON-LD from the response

```php
// Extract Schema.org metadata from the response
$jsonLdScriptsData = $document->extractJsonLdScripts('https://schema.org', 'Product');
```

**Example JSON-LD in the HTML:**
```html
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "Product",
    "description": "Description",
    "name": "Product name",
    "offers": {
        "@type": "Offer",
        "availability": "http://schema.org/InStock",
        "price": "55.00",
        "priceCurrency": "USD"
    }
}
</script>
```

---

## Excluding pages from the index dynamically

### Via the generatePage hook

```php
// src/EventListener/GeneratePageListener.php
namespace App\EventListener;

use Contao\CoreBundle\DependencyInjection\Attribute\AsHook;
use Contao\PageModel;

#[AsHook('generatePage')]
class GeneratePageListener
{
    public function __invoke(PageModel $pageModel): void
    {
        if (/* condition */) {
            $pageModel->noSearch = true;
        }
    }
}
```

Alternatively: fetch `pageModel` from the request attributes in your own kernel event listeners.

---

*Source: https://docs.contao.org/5.x/dev/framework/search-indexing/*
