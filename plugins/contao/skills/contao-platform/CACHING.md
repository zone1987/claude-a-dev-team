# Contao Caching (5.x)

## Contents

- [Overview](#overview)
- [3 caching methods](#3-caching-methods)
- [Cache tag system](#cache-tag-system)
- [Fragment rendering](#fragment-rendering)
- [Complete example](#complete-example)
- [Best Practices](#best-practices)

## Overview

Contao implements HTTP caching via **FOSHttpCacheBundle** with Symfony's HttpCache reverse proxy.

| Cache type | Audience | Header |
|-----------|-----------|--------|
| Private cache | Single user | `Cache-Control: private` |
| Shared cache | Multiple users via reverse proxy | `Cache-Control: public` |

---

## 3 caching methods

### 1. Cache Expiration

```php
$response->headers->addCacheControlDirective('private');
$response->headers->addCacheControlDirective('max-age', 60);
```

### 2. Cache Validation

- Date-based: `Last-Modified` / `If-Not-Modified-Since` → `304 Not Modified`
- Key-based: `ETag` / `If-None-Match` → `304 Not Modified`

### 3. Cache Invalidation (tag-based)

For shared caches. Maximum: 1 year cache lifetime.

---

## Cache tag system

### Tagging a response

```php
// In any service (inject fos_http_cache.http.symfony_response_tagger)
$this->responseTagger->addTags(['news-42']);
```

In fragment controllers (extending `AbstractFragmentController`):

```php
$this->tagResponse(['news-42']);
```

### Invalidating tags

```php
// Inject fos_http_cache.cache_manager
$this->cacheManager->invalidateTags(['news-42']);
```

### Automatic back end invalidation

When editing DB records, Contao automatically invalidates:

| Tag | When |
|-----|------|
| `contao.db.<table>.<id>` | A single record |
| `contao.db.<table>` | The entire table (if there is no parent) |
| Parent and child table tags | Hierarchical relationships |

---

## Fragment rendering

### Inline fragments (default)

Content is rendered within the main request. Cache time = minimum of page and fragment.

Template responses automatically include `Contao-Merge-Cache-Control` for correct cache merging.

### Edge Side Includes (ESI)

Separate cache times for fragment and page:

```
Page: 24h cache
Fragment: 1 week cache
```

Supported by the Symfony reverse proxy, Varnish, and major CDNs. Falls back to inline when not supported.

> **Warning:** ESI is only useful when the fragment is cacheable. Uncacheable fragments served via ESI degrade performance.

---

## Complete example

```php
use Contao\CoreBundle\Controller\ContentElement\AbstractContentElementController;

class MyContentElementController extends AbstractContentElementController
{
    protected function getResponse(
        FragmentTemplate $template,
        ContentModel $model,
        Request $request
    ): Response {
        $this->tagResponse(['news-42']);

        $response = $template->getResponse();
        $response->setPublic();
        $response->setMaxAge(3600);
        return $response;
    }
}
```

---

## Best Practices

- Fragment caching only pays off for expensive, cacheable fragments
- Avoid ESI for simple fragments
- For simple updates, prefer client-side JavaScript
- Follow the DB tag naming convention in the front end for automatic coordination

---

*Source: https://docs.contao.org/5.x/dev/framework/caching/*
