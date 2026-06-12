# Contao 5 — Page Controllers

## Übersicht

Page Controllers sind spezialisierte Controller-Implementierungen in Contao, die
Anfragen für spezifische Seitentypen innerhalb der Seitenstruktur verarbeiten.
Sie vereinen die Möglichkeit, eine Seite in Contaos Seitenstruktur zu definieren,
mit vollständiger Routing-Kontrolle.

**Typischer Use-Case:** RSS-Feed-Seite, bei der die URL-Struktur (z.B. `/feed/records.xml`)
frei im Backend konfigurierbar ist, unabhängig vom globalen URL-Suffix der Site.

---

## Registrierungsmethoden

1. **PHP-Attribut** `#[AsPage]` (empfohlen)
2. **Annotation** `@Page`
3. **YAML-Konfiguration** via `config/services.yaml`

---

## Konfigurationsparameter

| Parameter | Zweck |
|-----------|-------|
| `type` | Wird automatisch aus dem Klassenname abgeleitet; anpassbar |
| `path` | URL-Struktur (absolut oder relativ zum Alias) |
| `urlSuffix` | Überschreibt site-weites Suffix (z.B. `.csv` statt `.html`) |
| `contentComposition` | Boolean: Backend-Inhaltsbearbeitung aktivieren/deaktivieren |

---

## Minimales Beispiel

```php
// src/Controller/Page/RssFeedPageController.php
namespace App\Controller\Page;

use Contao\CoreBundle\DependencyInjection\Attribute\AsPage;
use Contao\PageModel;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;

#[AsPage(type: 'rss_feed', path: '/{alias}.xml', urlSuffix: '.xml')]
class RssFeedPageController
{
    public function __invoke(Request $request, PageModel $pageModel): Response
    {
        // $pageModel enthält die Contao-Seiten-Konfiguration
        $xml = $this->generateFeed($pageModel);

        return new Response($xml, 200, ['Content-Type' => 'application/rss+xml']);
    }

    private function generateFeed(PageModel $pageModel): string
    {
        // ...
        return '<rss></rss>';
    }
}
```

---

## URL-Generierung

Für moderne Page Controller mit Pflicht-Pfad-Parametern empfiehlt die Dokumentation
Symfonys `UrlGeneratorInterface`:

```php
use Symfony\Component\Routing\Generator\UrlGeneratorInterface;

class MyService
{
    public function __construct(private readonly UrlGeneratorInterface $router)
    {
    }

    public function getUrl(PageModel $page): string
    {
        return $this->router->generate($page->type, [
            'alias' => $page->alias,
        ], UrlGeneratorInterface::ABSOLUTE_URL);
    }
}
```

### Ab Contao 5.3: Array-Parameter-Übergabe

Ab Version 5.3 können statt direkter UrlGenerator-Aufrufe Arrays mit Parametern
an `getFrontendUrl()`-Methoden übergeben werden:

```php
$url = $pageModel->getFrontendUrl(['foobarId' => 42]);
```

---

## contentComposition

Wenn `contentComposition: true` gesetzt ist, können Redakteure im Backend Inhalte
auf dieser Seite bearbeiten (Artikel/Content Elements hinzufügen). Standard ist `false`
für vollständig controller-gesteuerte Seiten.

```php
#[AsPage(type: 'special', contentComposition: true)]
class SpecialPageController
{
    // ...
}
```

---

## Seitentypen im Backend

Damit der Seitentyp im Backend auswählbar ist, müssen Translations vorhanden sein:

```yaml
# translations/contao_default.en.yaml
PTY:
    rss_feed:
        - RSS Feed
        - A page that renders an RSS feed.
```

---

## Unterschied: Page Controller vs. normaler Controller

| Aspekt | Page Controller | Normaler Controller |
|--------|----------------|---------------------|
| URL | Über Contao-Seitenstruktur konfiguriert | Route fest im Code |
| Seitenstruktur | Erscheint als Seitentyp | Nicht sichtbar |
| PageModel | Automatisch verfügbar | Über PageFinder |
| Locale | Aus Seiten-Konfiguration | Symfony-Standard |

---

*Quelle: https://docs.contao.org/5.x/dev/framework/page-controllers/*
