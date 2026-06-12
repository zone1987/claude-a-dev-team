# Contao Response Context (5.x)

## Überblick

Der Response Context löst ein fundamentales Problem von CMS vs. Standard-Symfony: In Symfony verwalten Controller das komplette Response-Objekt. In Contao müssen Fragmente (Frontend-Module, News-Reader etc.) Seitenelemente modifizieren ohne den Gesamtkontext zu kennen.

**Kernidee:** Fragmente können über den Response Context Fähigkeiten wie Seitentitel modifizieren – ohne direkte Kenntnis ihrer Ausführungsumgebung (HTML-Seite, ESI-Fragment, AJAX, E-Mail).

---

## Workflow (4 Schritte)

1. Page Controller ermittelt Kontext anhand der URL
2. Controller definiert `ResponseContext` mit Fähigkeiten und rendert Fragmente
3. Fragmente greifen auf `ResponseContext` zu und modifizieren Fähigkeiten
4. Page Controller wendet Änderungen an und finalisiert die Response

---

## ResponseContext erstellen (Page Controller)

```php
namespace App\Controller\Page;

use Contao\CoreBundle\Routing\ResponseContext\HtmlHeadBag\HtmlHeadBag;
use Contao\CoreBundle\Routing\ResponseContext\ResponseContext;
use Contao\CoreBundle\Routing\ResponseContext\ResponseContextAccessor;

class ExamplePageController
{
    public function __construct(
        private readonly ResponseContextAccessor $responseContextAccessor
    ) {}

    public function __invoke(Request $request, PageModel $pageModel): Response
    {
        $responseContext = new ResponseContext();
        $responseContext->add(new HtmlHeadBag());
        $this->responseContextAccessor->setResponseContext($responseContext);

        // Fragmente rendern …

        $myHtmlContent = sprintf(
            '<html><head><title>%s</title></head><body>Content</body></html>',
            $responseContext->get(HtmlHeadBag::class)->getTitle()
        );

        $response = new Response($myHtmlContent);
        $this->responseContextAccessor->finalizeCurrentContext($response);
        return $response;
    }
}
```

> **Tipp:** `addLazy()` statt `add()` verwenden um ungenutzte Services nicht zu instanziieren.

---

## Core-Fähigkeiten

### HtmlHeadBag

Verwaltet dynamischen `<head>`-Bereich:

| Methode | Zweck |
|---------|-------|
| `setTitle($title)` | Seitentitel überschreiben |
| `setMetaDescription($desc)` | Meta-Description setzen |
| `setMetaRobots($robots)` | Robot-Direktiven konfigurieren |
| `setCanonicalUri($uri)` | Kanonische URL setzen |
| `setKeepParamsForCanonical($params)` | Query-Parameter für Canonical überschreiben |
| `addKeepParamsForCanonical($params)` | Parameter zum Canonical hinzufügen |

### JsonLdManager

Verwaltet JSON-LD Schema-Daten:

```php
use Contao\CoreBundle\Routing\ResponseContext\JsonLd\JsonLdManager;
use Spatie\SchemaOrg\ImageObject;

$schemaManager = new JsonLdManager(new ResponseContext());
$graph = $schemaManager->getGraphForSchema(JsonLdManager::SCHEMA_ORG);
$graph->add(
    (new ImageObject())->name('Name')->caption('Caption')
);
$schemaManager->collectFinalScriptFromGraphs();
```

### CspHandler

Modifiziert Content Security Policies für den aktuellen Request wenn CSP aktiviert ist.
Vollständige Dokumentation: Contao-CSP-Skill (`contao-csp`).

---

## Geplante Erweiterungen

Zukünftige Fähigkeiten: `<script>`-Tags, `<link>`-Tags, `<meta>`-Tags, erweitertes HTML-Head-Management.

---

*Quelle: https://docs.contao.org/5.x/dev/framework/response-context/*
