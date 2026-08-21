# Contao 5 — Routing

## Contents

- [Overview](#overview)
- [Implementing custom routes](#implementing-custom-routes)
- [Request attributes](#request-attributes)
- [Content routing (as of Contao 5.3)](#content-routing-as-of-contao-53)
- [Legacy URL parameters](#legacy-url-parameters)
- [Further resources](#further-resources)

## Overview

Contao's routing system builds on Symfony's routing framework. This document
covers custom routes, request attributes, content routing and legacy URL parameters.

---

## Implementing custom routes

The Managed Edition loads controllers automatically from `src/Controller/`. As of Contao 5.3,
attribute-based routes are discovered without manual configuration.

### Minimal controller

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

### routes.yaml (if autoconfigure is unavailable)

```yaml
# config/routes.yaml
app.controller:
    resource: ../src/Controller
    type: attribute
```

---

## Request attributes

Contao supports special request attributes for extended functionality:

### `_scope` — request scope

Controls whether a request is processed in the `frontend` or `backend` scope:

```php
#[Route('/my-route', defaults: ['_scope' => 'frontend'])]
class MyController { ... }
```

- `frontend`: triggers Contao-specific frontend processing (locale detection, CSRF)
- `backend`: backend scope with backend authentication

### `_token_check` — CSRF protection

Enables cross-site request forgery protection on custom controllers:

```php
#[Route('/form-handler', defaults: ['_token_check' => true])]
class FormController { ... }
```

### `_bypass_maintenance` — bypassing maintenance mode

Allows routes to bypass the frontend maintenance mode:

```php
#[Route('/status', defaults: ['_bypass_maintenance' => true])]
class StatusController { ... }
```

### PageModel attribute

Provides access to the current page. Since Contao 5.4, the
`PageFinder` service offers an alternative:

```php
use Contao\PageModel;
use Contao\CoreBundle\Routing\PageFinder;

class MyController
{
    public function __construct(private readonly PageFinder $pageFinder) {}

    public function __invoke(Request $request): Response
    {
        $page = $this->pageFinder->findPageForRequest($request);
        // or directly from the request attribute:
        $page = $request->attributes->get('pageModel');
    }
}
```

---

## Content routing (as of Contao 5.3)

Content routing enables URL generation for custom objects, models and
database records. It extends Symfony's routing specifically for frontend content.

### ContentUrlGenerator service

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

### Twig integration

```twig
<a href="{{ content_url(item) }}">{{ item.title }}</a>
```

### Implementing the ContentUrlResolver interface

Custom resolvers must implement `ContentUrlResolverInterface` and be tagged with
`contao.content_url_resolver`:

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

        // Option 1: external URL
        // return ContentUrlResult::url('https://example.com');

        // Option 2: redirect to other content
        // return ContentUrlResult::redirect($otherModel);

        // Option 3: resolve a page
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

## Legacy URL parameters

For legacy page types, arbitrary parameters can be passed via the URL after the page
alias (via the optional `{parameters}` route segment).

### The "auto item"

If an odd number of URL fragments follows a page alias, the
first fragment becomes the "auto item" (`auto_item`).

URL: `https://example.com/news/detail/some-news`
→ auto item: `some-news`

```php
use Contao\Input;

$autoItem = Input::get('auto_item');
```

**Important warning:** calling `Input::get('auto_item')` on every request (e.g. in
layout modules or hooks) marks the parameter as "used" and prevents
404 errors. Use the third parameter instead:

```php
// Do not mark as "read":
$autoItem = Input::get('auto_item', false, true);
```

### Key-value parameters

An even number of URL fragments → key/value pairs:

URL: `https://example.com/foo/bar/lorem/ipsum/dolor/sit`
→ parameters: `lorem=ipsum`, `dolor=sit`

```php
$lorem = Input::get('lorem'); // 'ipsum'
$dolor = Input::get('dolor'); // 'sit'
```

### Combining auto item + key/value

URL: `https://example.com/foo/bar/some-news/lorem/ipsum/dolor/sit`
→ auto item: `some-news`, plus `lorem=ipsum`, `dolor=sit`

---

## Further resources

- Symfony routing documentation: https://symfony.com/doc/current/routing.html
- Page controllers: the `contao-page-controllers` skill
- Backend routes: the `contao-backend-routes` skill

---

*Source: https://docs.contao.org/5.x/dev/framework/routing/*  
*https://docs.contao.org/5.x/dev/framework/routing/content-routing/*  
*https://docs.contao.org/5.x/dev/framework/routing/legacy-parameters/*
