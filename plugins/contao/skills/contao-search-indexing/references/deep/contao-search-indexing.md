# Contao Search Indexing (5.x)

## Überblick

Contao bietet eine eingebaute Seitensuche mit:
- Worttrennung über alle Sprachen
- Highlighting-Unterstützung
- Einfache Relevanzsortierung

Für erweiterte Funktionen (Autocomplete, Facetten, Sprachanalyse) können externe Suchmaschinen via Custom Indexer integriert werden.

---

## Index-Auslösung

### 1. CLI-Crawler

```bash
vendor/bin/contao-console contao:crawl
# Optionen via --help
```

Basiert auf Escargot. Domain muss in der CLI-Konfiguration gesetzt sein.

### 2. SearchIndexListener (automatisch)

Lauscht auf `kernel.terminate` und indiziert Responses bei jedem Request.

| Vorteile | Nachteile |
|---------|-----------|
| Automatische Hintergrund-Indizierung | Kann Performance beeinflussen |
| Index-Updates bei Redakteur-Änderungen | Timing unterscheidet sich (php-fpm: nach Response, mod_php/fcgi: vor Response) |
| Löscht URIs bei nicht-2xx-Responses | — |

### Konfiguration

```yaml
# config/config.yaml
contao:
    search:
        listener:
            index: true    # Indexeintrag bei jedem Request aktualisieren
            delete: false  # Eintrag bei nicht-erfolgreichen Requests löschen
```

Beide auf `false` → Listener komplett deaktivieren.

---

## Standard-Indexer deaktivieren

```yaml
contao:
    search:
        default_indexer:
            enable: false
```

---

## Custom Indexer

### Registrierung

```yaml
# config/services.yaml
services:
    App\Search\ExampleSearchIndexer:
        tags:
            - { name: 'contao.search_indexer' }
```

### IndexerInterface – 3 Pflichtmethoden

```php
interface IndexerInterface
{
    public function index(Document $document): void;    // Dokument indizieren
    public function delete(Document $document): void;   // Dokument entfernen
    public function clear(): void;                      // Gesamten Index leeren
}
```

### Document-Zugriff

Das `Document`-Objekt bietet:
- HTTP-Statuscode
- HTTP-Header
- Response-Body
- JSON-LD-Helfer

### JSON-LD aus Response extrahieren

```php
// Schema.org-Metadaten aus Response extrahieren
$jsonLdScriptsData = $document->extractJsonLdScripts('https://schema.org', 'Product');
```

**Beispiel JSON-LD im HTML:**
```html
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "Product",
    "description": "Beschreibung",
    "name": "Produktname",
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

## Seiten dynamisch aus dem Index ausschließen

### Via generatePage-Hook

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
        if (/* Bedingung */) {
            $pageModel->noSearch = true;
        }
    }
}
```

Alternativ: `pageModel` aus Request-Attributen in eigenen Kernel-Event-Listenern holen.

---

*Quelle: https://docs.contao.org/5.x/dev/framework/search-indexing/*
