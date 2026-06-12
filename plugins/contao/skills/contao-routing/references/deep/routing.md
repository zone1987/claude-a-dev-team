# Contao 5 — Routing

## Übersicht

Contaos Routing-System baut auf Symfonys Routing-Framework auf. Dieses Dokument
deckt Custom Routes, Request-Attribute, Content Routing und Legacy-URL-Parameter ab.

---

## Custom Routes implementieren

Die Managed Edition lädt Controller automatisch aus `src/Controller/`. Ab Contao 5.3
werden attributbasierte Routen ohne manuelle Konfiguration entdeckt.

### Minimaler Controller

```php
// src/Controller/ExampleController.php
namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;

#[Route('/example', name: ExampleController::class)]
class ExampleController
{
    public function __invoke(Request $request): Response
    {
        return new Response('Hello World!');
    }
}
```

### routes.yaml (falls kein Autoconfigure)

```yaml
# config/routes.yaml
app.controller:
    resource: ../src/Controller
    type: attribute
```

---

## Request-Attribute

Contao unterstützt spezielle Request-Attribute für erweiterte Funktionalität:

### `_scope` — Request-Scope

Steuert, ob ein Request im `frontend`- oder `backend`-Scope verarbeitet wird:

```php
#[Route('/my-route', defaults: ['_scope' => 'frontend'])]
class MyController { ... }
```

- `frontend`: Löst Contao-spezifische Frontend-Verarbeitung aus (Locale-Erkennung, CSRF)
- `backend`: Backend-Scope mit Backend-Authentication

### `_token_check` — CSRF-Schutz

Aktiviert Cross-Site-Request-Forgery-Schutz auf Custom Controllern:

```php
#[Route('/form-handler', defaults: ['_token_check' => true])]
class FormController { ... }
```

### `_bypass_maintenance` — Wartungsmodus umgehen

Erlaubt Routen, den Frontend-Wartungsmodus zu umgehen:

```php
#[Route('/status', defaults: ['_bypass_maintenance' => true])]
class StatusController { ... }
```

### PageModel-Attribut

Stellt Zugriff auf die aktuelle Seite bereit. Seit Contao 5.4 bietet der
`PageFinder`-Service eine Alternative:

```php
use Contao\PageModel;
use Contao\CoreBundle\Routing\PageFinder;

class MyController
{
    public function __construct(private readonly PageFinder $pageFinder) {}

    public function __invoke(Request $request): Response
    {
        $page = $this->pageFinder->findPageForRequest($request);
        // oder direkt aus Request-Attribut:
        $page = $request->attributes->get('pageModel');
    }
}
```

---

## Content Routing (ab Contao 5.3)

Content Routing ermöglicht URL-Generierung für eigene Objekte, Models und
Datenbankeinträge. Es erweitert Symfonys Routing speziell für Frontend-Content.

### ContentUrlGenerator Service

```php
use Contao\CoreBundle\Routing\ContentUrlGenerator;
use Symfony\Component\Routing\Generator\UrlGeneratorInterface;

class MyService
{
    public function __construct(
        private readonly ContentUrlGenerator $contentUrlGenerator,
    ) {}

    public function getUrl(object $content): string
    {
        return $this->contentUrlGenerator->generate(
            $content,
            [],
            UrlGeneratorInterface::ABSOLUTE_URL
        );
    }
}
```

### Twig-Integration

```twig
<a href="{{ content_url(item) }}">{{ item.title }}</a>
```

### ContentUrlResolver Interface implementieren

Eigene Resolver müssen `ContentUrlResolverInterface` implementieren und mit
`contao.content_url_resolver` getaggt sein:

```php
// src/Routing/FoobarContentUrlResolver.php
namespace App\Routing;

use Contao\CoreBundle\Routing\Content\ContentUrlResolverInterface;
use Contao\CoreBundle\Routing\Content\ContentUrlResult;
use Contao\PageModel;

class FoobarContentUrlResolver implements ContentUrlResolverInterface
{
    public function resolve(object $content): ContentUrlResult|null
    {
        if (!$content instanceof FoobarModel) {
            return null;
        }

        // Option 1: Externe URL
        // return ContentUrlResult::url('https://example.com');

        // Option 2: Redirect zu anderem Content
        // return ContentUrlResult::redirect($otherModel);

        // Option 3: Seite auflösen
        return ContentUrlResult::resolve(
            PageModel::findByPk($content->jumpTo)
        );
    }

    public function getParametersForContent(object $content, PageModel $pageModel): array
    {
        return ['foobarId' => (int) $content->id];
    }
}
```

```yaml
# config/services.yaml
App\Routing\FoobarContentUrlResolver:
    tags:
        - name: contao.content_url_resolver
```

---

## Legacy URL-Parameter

Für Legacy-Seitentypen können beliebige Parameter über die URL nach dem Seiten-Alias
übergeben werden (via optionalen `{parameters}`-Routen-Segment).

### Der "Auto Item"

Wenn eine ungerade Anzahl URL-Fragmente auf einen Seiten-Alias folgt, wird das
erste Fragment zum "Auto Item" (`auto_item`).

URL: `https://example.com/news/detail/some-news`
→ Auto Item: `some-news`

```php
use Contao\Input;

$autoItem = Input::get('auto_item');
```

**Wichtige Warnung:** `Input::get('auto_item')` auf jeder Anfrage ausführen (z.B. in
Layout-Modulen oder Hooks) markiert den Parameter als "verwendet" und verhindert
404-Fehler. Stattdessen dritten Parameter nutzen:

```php
// Nicht als "gelesen" markieren:
$autoItem = Input::get('auto_item', false, true);
```

### Key-Value-Parameter

Gerade Anzahl URL-Fragmente → Key/Value-Paare:

URL: `https://example.com/foo/bar/lorem/ipsum/dolor/sit`
→ Parameter: `lorem=ipsum`, `dolor=sit`

```php
$lorem = Input::get('lorem'); // 'ipsum'
$dolor = Input::get('dolor'); // 'sit'
```

### Kombination Auto Item + Key/Value

URL: `https://example.com/foo/bar/some-news/lorem/ipsum/dolor/sit`
→ Auto Item: `some-news`, plus `lorem=ipsum`, `dolor=sit`

---

## Weiterführende Ressourcen

- Symfony Routing Dokumentation: https://symfony.com/doc/current/routing.html
- Page Controllers: `contao-page-controllers`-Skill
- Backend Routes: `contao-backend-routes`-Skill

---

*Quelle: https://docs.contao.org/5.x/dev/framework/routing/*  
*https://docs.contao.org/5.x/dev/framework/routing/content-routing/*  
*https://docs.contao.org/5.x/dev/framework/routing/legacy-parameters/*
