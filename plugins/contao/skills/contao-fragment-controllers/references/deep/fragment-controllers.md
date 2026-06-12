# Contao 5 — Fragment Controllers

## Übersicht

Fragment Controllers ermöglichen das Bauen flexibler Seiten-Komponenten mit
Symfony's Controller-Architektur. Contao-Seiten bestehen aus hierarchischen
Komponenten: Layouts → Sektionen → Module/Artikel → Content Elements.

Ein **Fragment** ist ein Seitenteil, der als Symfony-Sub-Request verarbeitet wird.
Jedes Fragment hat eigene Parameter und HTTP-Header, aber keine eigene URL.

---

## Konzept

```
Page
├── Layout
│   └── Section (e.g. main, header, footer)
│       └── Article
│           ├── Content Element  ← Fragment
│           └── Front End Module ← Fragment
```

Jeder Fragment-Controller ist ein PHP-Controller, der aus dem `Request`-Objekt
liest und eine `Response` zurückgibt — ohne eigene Route.

---

## Eingebaute Fragment-Typen

Contao stellt zwei eingebaute Fragment-Typen bereit:

| Typ | Registry-Global | Basis-Klasse |
|-----|-----------------|-------------|
| Front-End-Module | `$GLOBALS['FE_MOD']` | `AbstractFrontendModuleController` |
| Content Elements | `$GLOBALS['TL_CTE']` | `AbstractContentElementController` |

Beide Basis-Klassen übernehmen: Template-Vorbereitung, Response-Generierung,
Caching-Header.

---

## Legacy-Klassen erweitern

Bestehende Contao-Framework-Klassen können erweitert werden. Dabei muss die
`__invoke`-Methode implementiert werden:

```php
// src/Controller/FrontendModule/CustomNewsListController.php
namespace App\Controller\FrontendModule;

use Contao\CoreBundle\DependencyInjection\Attribute\AsFrontendModule;
use Contao\ModuleNewsList;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;

#[AsFrontendModule('custom_news_list', category: 'news')]
class CustomNewsListController extends ModuleNewsList
{
    public function __invoke(Request $request): Response
    {
        // Eigene Logik vor/nach dem Standard-Verhalten
        $this->customizeOutput();

        return new Response($this->generate());
    }

    private function customizeOutput(): void
    {
        // Anpassungen
    }
}
```

**Wichtig:** Klassen, die Legacy-Contao-Framework-Klassen erweitern, benötigen
**manuelle Service-Registrierung** in `config/services.yaml` — sie werden nicht
automatisch über Autoconfigure entdeckt.

```yaml
# config/services.yaml
App\Controller\FrontendModule\CustomNewsListController:
    public: true
    tags:
        - name: contao.frontend_module
          type: custom_news_list
          category: news
```

---

## Sub-Requests und Caching

- Jedes Fragment verarbeitet sich als eigenständiger Symfony-Sub-Request
- Sub-Requests können die Cache-Zeit der Eltern-Response beeinflussen
- ESI-Renderer ermöglicht separate Caching-Entscheidungen pro Fragment

**Renderer-Optionen:**
- `forward` (Standard): Sub-Request im selben PHP-Prozess
- `inline`: Inline-Rendering ohne Sub-Request-Overhead
- `esi`: Edge Side Includes für unabhängiges CDN-Caching

---

## Custom Fragment-Typen

Das Contao-Fragment-Registry unterstützt beliebige eigene Fragment-Typen
über `FragmentRegistry` und `RegisterFragmentsPass`. Dies erfordert fortgeschrittene
Symfony-Kenntnisse.

**Verfügbar seit:** Contao 4.5

---

## Unterschied Fragment-Controller vs. Page-Controller

| Aspekt | Fragment Controller | Page Controller |
|--------|---------------------|----------------|
| Eigene URL | Nein | Ja (via Seitenstruktur) |
| Einbettung | In Artikel/Layout | Eigenständige Seite |
| Sub-Request | Ja | Nein (Haupt-Request) |

---

*Quelle: https://docs.contao.org/5.x/dev/guides/fragment-controllers/*  
*https://docs.contao.org/5.x/dev/framework/content-elements/*  
*https://docs.contao.org/5.x/dev/framework/front-end-modules/*
