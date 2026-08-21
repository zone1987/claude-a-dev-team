# Contao 5 — Fragment Controllers

## Contents

- [Overview](#overview)
- [Concept](#concept)
- [Built-in fragment types](#built-in-fragment-types)
- [Extending legacy classes](#extending-legacy-classes)
- [Sub-requests and caching](#sub-requests-and-caching)
- [Custom fragment types](#custom-fragment-types)
- [Difference between fragment controller and page controller](#difference-between-fragment-controller-and-page-controller)

## Overview

Fragment controllers make it possible to build flexible page components with
Symfony's controller architecture. Contao pages consist of hierarchical
components: layouts → sections → modules/articles → content elements.

A **fragment** is a part of a page that is processed as a Symfony sub-request.
Each fragment has its own parameters and HTTP headers, but no URL of its own.

---

## Concept

```
Page
├── Layout
│   └── Section (e.g. main, header, footer)
│       └── Article
│           ├── Content Element  ← Fragment
│           └── Front End Module ← Fragment
```

Every fragment controller is a PHP controller that reads from the `Request` object
and returns a `Response` — without a route of its own.

---

## Built-in fragment types

Contao provides two built-in fragment types:

| Type | Registry global | Base class |
|-----|-----------------|-------------|
| Frontend modules | `$GLOBALS['FE_MOD']` | `AbstractFrontendModuleController` |
| Content elements | `$GLOBALS['TL_CTE']` | `AbstractContentElementController` |

Both base classes handle: template preparation, response generation,
caching headers.

---

## Extending legacy classes

Existing Contao framework classes can be extended. In doing so, the
`__invoke` method must be implemented:

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
        // Custom logic before/after the default behavior
        $this->customizeOutput();

        return new Response($this->generate());
    }

    private function customizeOutput(): void
    {
        // Customizations
    }
}
```

**Important:** classes that extend legacy Contao framework classes require
**manual service registration** in `config/services.yaml` — they are not
discovered automatically via autoconfigure.

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

## Sub-requests and caching

- Each fragment is processed as an independent Symfony sub-request
- Sub-requests can influence the cache lifetime of the parent response
- The ESI renderer allows separate caching decisions per fragment

**Renderer options:**
- `forward` (default): sub-request in the same PHP process
- `inline`: inline rendering without sub-request overhead
- `esi`: edge side includes for independent CDN caching

---

## Custom fragment types

The Contao fragment registry supports arbitrary custom fragment types
via `FragmentRegistry` and `RegisterFragmentsPass`. This requires advanced
Symfony knowledge.

**Available since:** Contao 4.5

---

## Difference between fragment controller and page controller

| Aspect | Fragment controller | Page controller |
|--------|---------------------|----------------|
| Own URL | No | Yes (via the page structure) |
| Embedding | In an article/layout | Standalone page |
| Sub-request | Yes | No (main request) |

---

*Source: https://docs.contao.org/5.x/dev/guides/fragment-controllers/*  
*https://docs.contao.org/5.x/dev/framework/content-elements/*  
*https://docs.contao.org/5.x/dev/framework/front-end-modules/*
