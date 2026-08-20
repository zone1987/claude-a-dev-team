# Contao Caching (5.x)

## Contents

- [Überblick](#überblick)
- [3 Caching-Methoden](#3-caching-methoden)
- [Cache-Tag-System](#cache-tag-system)
- [Fragment-Rendering](#fragment-rendering)
- [Vollständiges Beispiel](#vollständiges-beispiel)
- [Best Practices](#best-practices)

## Überblick

Contao implementiert HTTP-Caching via **FOSHttpCacheBundle** mit Symfonys HttpCache Reverse Proxy.

| Cache-Typ | Zielgruppe | Header |
|-----------|-----------|--------|
| Private Cache | Einzelnutzer | `Cache-Control: private` |
| Shared Cache | Mehrere Nutzer über Reverse Proxy | `Cache-Control: public` |

---

## 3 Caching-Methoden

### 1. Cache Expiration

```php
$response->headers->addCacheControlDirective('private');
$response->headers->addCacheControlDirective('max-age', 60);
```

### 2. Cache Validation

- Datumsbasiert: `Last-Modified` / `If-Not-Modified-Since` → `304 Not Modified`
- Schlüsselbasiert: `ETag` / `If-None-Match` → `304 Not Modified`

### 3. Cache Invalidation (Tag-basiert)

Für Shared Caches. Maximum: 1 Jahr Cache-Lebensdauer.

---

## Cache-Tag-System

### Response taggen

```php
// In beliebigen Services (inject fos_http_cache.http.symfony_response_tagger)
$this->responseTagger->addTags(['news-42']);
```

In Fragment-Controllern (erben von `AbstractFragmentController`):

```php
$this->tagResponse(['news-42']);
```

### Tags invalidieren

```php
// Inject fos_http_cache.cache_manager
$this->cacheManager->invalidateTags(['news-42']);
```

### Automatische Backend-Invalidierung

Beim Bearbeiten von DB-Datensätzen invalidiert Contao automatisch:

| Tag | Wann |
|-----|------|
| `contao.db.<table>.<id>` | Einzelnen Datensatz |
| `contao.db.<table>` | Gesamte Tabelle (wenn kein Parent) |
| Parent- und Child-Table-Tags | Hierarchische Beziehungen |

---

## Fragment-Rendering

### Inline-Fragments (Standard)

Content wird innerhalb des Haupt-Requests gerendert. Cache-Zeit = Minimum aus Seite + Fragment.

Template-Responses inkludieren automatisch `Contao-Merge-Cache-Control` für korrektes Cache-Merging.

### Edge Side Includes (ESI)

Separate Cache-Zeiten für Fragment und Seite:

```
Seite: 24h Cache
Fragment: 1 Woche Cache
```

Unterstützt von Symfony Reverse Proxy, Varnish, und großen CDNs. Fallback auf Inline wenn nicht unterstützt.

> **Warnung:** ESI nur sinnvoll wenn Fragment cacheable ist. Unkachebare Fragmente per ESI verschlechtern die Performance.

---

## Vollständiges Beispiel

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

- Fragment-Caching lohnt nur bei teuren, cacheable Fragmenten
- ESI vermeiden für einfache Fragmente
- Für einfache Updates lieber Client-seitiges JavaScript nutzen
- DB-Tag-Namenskonvention im Frontend einhalten für automatische Koordination

---

*Quelle: https://docs.contao.org/5.x/dev/framework/caching/*
