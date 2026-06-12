# Contao 5 — Backend-Routen & Backend-Assets

## Übersicht

Contao erlaubt eigene Backend-Controller und -Routen ohne ausschließliche
DCA-Konfiguration. Dieser Skill deckt Backend-Routen, Menü-Integration und
das Einbinden von Assets im Backend ab.

---

## Backend-Controller aufsetzen

### AbstractBackendController

```php
// src/Controller/BackendController.php
namespace App\Controller;

use Contao\CoreBundle\Controller\AbstractBackendController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;

#[Route(
    '%contao.backend.route_prefix%/my-backend-route',
    name: self::class,
    defaults: ['_scope' => 'backend']
)]
class BackendController extends AbstractBackendController
{
    public function __invoke(): Response
    {
        return $this->render('my_backend_route.html.twig', [
            'foo' => 'bar',
        ]);
    }
}
```

**Schlüsselanforderung:** `_scope => 'backend'` im Route-Default für korrekte
Registrierung im Contao-Backend-Scope.

**Wichtig:** Controller müssen in `config/routes.yaml` **vor** den `ContaoCoreBundle`-Routen
importiert werden:

```yaml
# config/routes.yaml
app.controller:
    resource: ../src/Controller
    type: attribute
```

---

## Backend-Template

Templates erweitern das Basis-Backend-Layout:

```twig
{# templates/my_backend_route.html.twig #}
{% extends "@Contao/be_main" %}

{% block headline %}
    My Backend Module
{% endblock %}

{% block main_content %}
    <div class="tl_listing_container">
        <p>Main Content: {{ foo }}</p>
    </div>
{% endblock %}
```

---

## Menü-Integration

Ein Event-Listener fügt den Menüeintrag hinzu:

```php
// src/EventListener/BackendMenuListener.php
namespace App\EventListener;

use App\Controller\BackendController;
use Contao\CoreBundle\Event\MenuEvent;
use Symfony\Component\EventDispatcher\Attribute\AsEventListener;

#[AsEventListener(ContaoCoreEvents::BACKEND_MENU_BUILD, priority: -255)]
class BackendMenuListener
{
    public function __invoke(MenuEvent $event): void
    {
        $factory = $event->getFactory();
        $tree = $event->getTree();

        if ('mainMenu' !== $tree->getName()) {
            return;
        }

        $node = $factory->createItem('my-backend-route', [
            'route' => BackendController::class,
        ]);
        $node->setLabel('My Module');
        $node->setLinkAttribute('title', 'My Module');
        $node->setLinkAttribute('class', 'my-module');
        $node->setCurrent($this->isCurrent($event));

        // An vorhandene Kategorie hängen:
        if ($contentNode = $tree->getChild('content')) {
            $contentNode->addChild($node);
        }
    }

    private function isCurrent(MenuEvent $event): bool
    {
        // Prüfen ob aktueller Request zu diesem Menüpunkt gehört
        return false;
    }
}
```

**Niedrige Priorität** (`-255`) stellt sicher, dass Kern-Menüs zuerst geladen werden
und Parent-Nodes verfügbar sind.

---

## Backend-Assets global hinzufügen

Für universelle Backend-Asset-Einbindung einen Event-Listener nutzen, der auf
Backend-Main-Requests prüft:

```php
// src/EventListener/AddBackendAssetsListener.php
namespace App\EventListener;

use Contao\CoreBundle\Routing\ScopeMatcher;
use Symfony\Component\EventDispatcher\Attribute\AsEventListener;
use Symfony\Component\HttpKernel\Event\RequestEvent;

#[AsEventListener]
class AddBackendAssetsListener
{
    public function __construct(
        private readonly ScopeMatcher $scopeMatcher,
    ) {}

    public function __invoke(RequestEvent $event): void
    {
        if (!$this->scopeMatcher->isBackendMainRequest($event)) {
            return;
        }

        $GLOBALS['TL_CSS'][] = 'bundles/myextension/backend.css';
        $GLOBALS['TL_JAVASCRIPT'][] = 'bundles/myextension/backend.js';
    }
}
```

---

## Backend-Assets für spezifische DCA-Views

Für bestimmte DataContainer-Views den `onload`-DCA-Callback nutzen:

```php
// src/EventListener/DataContainer/ContentOnLoadCallbackListener.php
namespace App\EventListener\DataContainer;

use Contao\CoreBundle\DependencyInjection\Attribute\AsCallback;

#[AsCallback(table: 'tl_content', target: 'config.onload')]
class ContentOnLoadCallbackListener
{
    public function __invoke(): void
    {
        $GLOBALS['TL_CSS'][] = 'bundles/myextension/content-editor.css';
        $GLOBALS['TL_JAVASCRIPT'][] = 'bundles/myextension/content-editor.js';
    }
}
```

**Alternative:** Assets können auch in `config/config.yaml` konfiguriert werden:

```yaml
# config/config.yaml
contao:
    backend:
        stylesheets:
            - bundles/myextension/backend.css
        javascript:
            - bundles/myextension/backend.js
```

---

## ContaoCoreEvents Konstanten

Wichtige Event-Konstanten für Backend-Events:

```php
use Contao\CoreBundle\ContaoCoreEvents;

// Verfügbare Events (Auswahl):
ContaoCoreEvents::BACKEND_MENU_BUILD    // Backend-Menü aufbauen
ContaoCoreEvents::SLUG_VALID_CHARACTERS // Slug-Validierung
ContaoCoreEvents::PREVIEW_URL_CREATE    // Preview-URL erzeugen
ContaoCoreEvents::PREVIEW_URL_CONVERT   // Preview-URL konvertieren
```

---

## Backend-Route mit Daten

Vollständiges Beispiel mit Datenbankabfragen und Formular-Handling:

```php
#[Route(
    '%contao.backend.route_prefix%/vendor-export',
    name: self::class,
    defaults: ['_scope' => 'backend'],
    methods: ['GET', 'POST']
)]
class VendorExportController extends AbstractBackendController
{
    public function __construct(
        private readonly VendorRepository $vendors,
    ) {}

    public function __invoke(Request $request): Response
    {
        if ($request->isMethod('POST') && $this->isTokenValid('backend', $request)) {
            return $this->exportCsv();
        }

        return $this->render('backend/vendor_export.html.twig', [
            'vendors' => $this->vendors->findAll(),
        ]);
    }

    private function exportCsv(): Response
    {
        // CSV-Export-Logik
        $response = new Response('...csv data...');
        $response->headers->set('Content-Type', 'text/csv');
        $response->headers->set('Content-Disposition', 'attachment; filename="vendors.csv"');
        return $response;
    }
}
```

---

## Contao-Backend-URL-Prefix

Der Route-Präfix `%contao.backend.route_prefix%` ergibt standardmäßig `/contao`.
Er kann in `config/config.yaml` geändert werden:

```yaml
contao:
    backend:
        route_prefix: /admin
```

---

*Quelle: https://docs.contao.org/5.x/dev/guides/back-end-routes/*  
*https://docs.contao.org/5.x/dev/guides/adding-back-end-assets/*
