# Contao 5 — Page Controllers

## Contents

- [Overview](#overview)
- [Registration methods](#registration-methods)
- [Configuration parameters](#configuration-parameters)
- [Minimal example](#minimal-example)
- [URL generation](#url-generation)
- [contentComposition](#contentcomposition)
- [Page types in the backend](#page-types-in-the-backend)
- [Difference: page controller vs. regular controller](#difference-page-controller-vs-regular-controller)

## Overview

Page controllers are specialized controller implementations in Contao that handle
requests for specific page types within the page structure.
They combine the ability to define a page in Contao's page structure
with full routing control.

**Typical use case:** an RSS feed page whose URL structure (e.g. `/feed/records.xml`)
is freely configurable in the backend, independent of the site's global URL suffix.

---

## Registration methods

1. **PHP attribute** `#[AsPage]` (recommended)
2. **Annotation** `@Page`
3. **YAML configuration** via `config/services.yaml`

---

## Configuration parameters

| Parameter | Purpose |
|-----------|-------|
| `type` | Derived automatically from the class name; customizable |
| `path` | URL structure (absolute or relative to the alias) |
| `urlSuffix` | Overrides the site-wide suffix (e.g. `.csv` instead of `.html`) |
| `contentComposition` | Boolean: enable/disable backend content editing |

---

## Minimal example

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
        // $pageModel contains the Contao page configuration
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

## URL generation

For modern page controllers with mandatory path parameters, the documentation
recommends Symfony's `UrlGeneratorInterface`:

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

### As of Contao 5.3: passing parameters as an array

As of version 5.3, arrays of parameters can be passed to `getFrontendUrl()` methods
instead of calling the UrlGenerator directly:

```php
$url = $pageModel->getFrontendUrl(['foobarId' => 42]);
```

---

## contentComposition

When `contentComposition: true` is set, editors can edit content on this page
in the backend (adding articles/content elements). The default is `false`
for fully controller-driven pages.

```php
#[AsPage(type: 'special', contentComposition: true)]
class SpecialPageController
{
    // ...
}
```

---

## Page types in the backend

For the page type to be selectable in the backend, translations must exist:

```yaml
# translations/contao_default.en.yaml
PTY:
    rss_feed:
        - RSS Feed
        - A page that renders an RSS feed.
```

---

## Difference: page controller vs. regular controller

| Aspect | Page controller | Regular controller |
|--------|----------------|---------------------|
| URL | Configured via the Contao page structure | Route fixed in code |
| Page structure | Appears as a page type | Not visible |
| PageModel | Available automatically | Via PageFinder |
| Locale | From the page configuration | Symfony default |

---

*Source: https://docs.contao.org/5.x/dev/framework/page-controllers/*
