# Contao 5 — Backend routes & backend assets

## Contents

- [Overview](#overview)
- [Setting up a backend controller](#setting-up-a-backend-controller)
- [Backend template](#backend-template)
- [Menu integration](#menu-integration)
- [Adding backend assets globally](#adding-backend-assets-globally)
- [Backend assets for specific DCA views](#backend-assets-for-specific-dca-views)
- [ContaoCoreEvents constants](#contaocoreevents-constants)
- [Backend route with data](#backend-route-with-data)
- [Contao backend URL prefix](#contao-backend-url-prefix)

## Overview

Contao allows custom backend controllers and routes without relying exclusively on
DCA configuration. This skill covers backend routes, menu integration and
including assets in the backend.

---

## Setting up a backend controller

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

**Key requirement:** `_scope => 'backend'` in the route defaults for correct
registration in the Contao backend scope.

**Important:** controllers must be imported in `config/routes.yaml` **before** the
`ContaoCoreBundle` routes:

```yaml
# config/routes.yaml
app.controller:
    resource: ../src/Controller
    type: attribute
```

---

## Backend template

Templates extend the base backend layout:

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

## Menu integration

An event listener adds the menu entry:

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

        // Attach to an existing category:
        if ($contentNode = $tree->getChild('content')) {
            $contentNode->addChild($node);
        }
    }

    private function isCurrent(MenuEvent $event): bool
    {
        // Check whether the current request belongs to this menu item
        return false;
    }
}
```

**A low priority** (`-255`) ensures that core menus are loaded first
and parent nodes are available.

---

## Adding backend assets globally

For universal backend asset inclusion, use an event listener that checks for
backend main requests:

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

## Backend assets for specific DCA views

For particular DataContainer views, use the `onload` DCA callback:

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

**Alternative:** assets can also be configured in `config/config.yaml`:

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

## ContaoCoreEvents constants

Important event constants for backend events:

```php
use Contao\CoreBundle\ContaoCoreEvents;

// Available events (selection):
ContaoCoreEvents::BACKEND_MENU_BUILD    // Build the backend menu
ContaoCoreEvents::SLUG_VALID_CHARACTERS // Slug validation
ContaoCoreEvents::PREVIEW_URL_CREATE    // Create a preview URL
ContaoCoreEvents::PREVIEW_URL_CONVERT   // Convert a preview URL
```

---

## Backend route with data

Complete example with database queries and form handling:

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
        // CSV export logic
        $response = new Response('...csv data...');
        $response->headers->set('Content-Type', 'text/csv');
        $response->headers->set('Content-Disposition', 'attachment; filename="vendors.csv"');
        return $response;
    }
}
```

---

## Contao backend URL prefix

The route prefix `%contao.backend.route_prefix%` resolves to `/contao` by default.
It can be changed in `config/config.yaml`:

```yaml
contao:
    backend:
        route_prefix: /admin
```

---

*Source: https://docs.contao.org/5.x/dev/guides/back-end-routes/*  
*https://docs.contao.org/5.x/dev/guides/adding-back-end-assets/*
