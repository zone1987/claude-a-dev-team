# Contao Response Context (5.x)

## Contents

- [Overview](#overview)
- [Workflow (4 steps)](#workflow-4-steps)
- [Creating a ResponseContext (page controller)](#creating-a-responsecontext-page-controller)
- [Core capabilities](#core-capabilities)
- [Planned extensions](#planned-extensions)

## Overview

The response context solves a fundamental problem of a CMS versus standard Symfony: in Symfony, controllers manage the entire response object. In Contao, fragments (frontend modules, news readers etc.) have to modify page elements without knowing the overall context.

**Core idea:** through the response context, fragments can modify capabilities such as the page title – without direct knowledge of their execution environment (HTML page, ESI fragment, AJAX, e-mail).

---

## Workflow (4 steps)

1. The page controller determines the context based on the URL
2. The controller defines a `ResponseContext` with capabilities and renders fragments
3. Fragments access the `ResponseContext` and modify capabilities
4. The page controller applies the changes and finalizes the response

---

## Creating a ResponseContext (page controller)

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

        // Render fragments …

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

> **Tip:** use `addLazy()` instead of `add()` to avoid instantiating unused services.

---

## Core capabilities

### HtmlHeadBag

Manages the dynamic `<head>` area:

| Method | Purpose |
|---------|-------|
| `setTitle($title)` | Override the page title |
| `setMetaDescription($desc)` | Set the meta description |
| `setMetaRobots($robots)` | Configure robot directives |
| `setCanonicalUri($uri)` | Set the canonical URL |
| `setKeepParamsForCanonical($params)` | Override query parameters for the canonical URL |
| `addKeepParamsForCanonical($params)` | Add parameters to the canonical URL |

### JsonLdManager

Manages JSON-LD schema data:

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

Modifies content security policies for the current request when CSP is enabled.
Complete documentation: the Contao CSP skill (`contao-csp`).

---

## Planned extensions

Future capabilities: `<script>` tags, `<link>` tags, `<meta>` tags, extended HTML head management.

---

*Source: https://docs.contao.org/5.x/dev/framework/response-context/*
