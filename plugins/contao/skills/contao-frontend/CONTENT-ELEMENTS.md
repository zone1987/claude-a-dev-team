# Contao 5 — Content Elements

## Contents

- [Overview](#overview)
- [Basic components](#basic-components)
- [Minimal implementation](#minimal-implementation)
- [Service tag options](#service-tag-options)
- [Registration methods](#registration-methods)
- [PageModel access](#pagemodel-access)
- [Nested fragments (as of Contao 5.3)](#nested-fragments-as-of-contao-53)
- [Wrapper elements (legacy)](#wrapper-elements-legacy)
- [Content elements for custom tables](#content-elements-for-custom-tables)
- [Maker Bundle](#maker-bundle)

## Overview

Content elements are the fundamental content building blocks in Contao. They are
implemented as fragment controllers, receive data via a content model and
return a response that is rendered into the main content.

---

## Basic components

Every content element consists of:

1. **Fragment controller** — a class extending `AbstractContentElementController`
2. **Service tag** `contao.content_element` with:
   - **type**: identifies the template and the DCA palette (derived from the class name)
   - **category**: groups elements in dropdowns (default: `miscellaneous`)
   - **template**: optional custom template path
3. **DCA palette** in `tl_content`
4. **Twig template** (`content_element/<type>.html.twig`)
5. **Translations** for backend labels

---

## Minimal implementation

### Controller

```php
// src/Controller/ContentElement/ExampleElementController.php
namespace App\Controller\ContentElement;

use Contao\ContentModel;
use Contao\CoreBundle\Controller\ContentElement\AbstractContentElementController;
use Contao\CoreBundle\DependencyInjection\Attribute\AsContentElement;
use Contao\CoreBundle\Twig\FragmentTemplate;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;

#[AsContentElement(category: 'texts')]
class ExampleElementController extends AbstractContentElementController
{
    protected function getResponse(FragmentTemplate $template, ContentModel $model, Request $request): Response
    {
        $template->set('text', $model->text);
        $template->set('url', $model->url);
        return $template->getResponse();
    }
}
```

### DCA palette

```php
// contao/dca/tl_content.php
$GLOBALS['TL_DCA']['tl_content']['palettes']['example_element'] = '
    {type_legend},type,headline;
    {text_legend},text,url;
';
```

### Template

```twig
{# templates/content_element/example_element.html.twig #}
{% extends "@Contao/content_element/_base.html.twig" %}

{% block content %}
    {{ text }}
    {% if url %}
        <a href="{{ url }}">Read more</a>
    {% endif %}
{% endblock %}
```

### Translations

```yaml
# translations/contao_default.en.yaml
CTE:
    example_element:
        - My Content Element
        - A Content Element for testing purposes.
```

---

## Service tag options

| Option | Type | Description |
|--------|-----|-------------|
| `name` | string | Must be `contao.content_element` |
| `type` | string | Custom type identifier (mandatory when overriding) |
| `category` | string | Groups the element in the selector |
| `template` | string | Overrides the default template path |
| `renderer` | string | `inline`, `esi` or `forward` (default) |
| `method` | string | Controller method to call |
| `nestedFragments` | bool/array | Enables nested child elements |

---

## Registration methods

**Via PHP attribute (recommended):**
```php
#[AsContentElement(category: 'texts', template: 'content_element/my_element')]
```

**Via annotation:**
```php
/** @ContentElement("my_element", category="texts") */
```

**Via YAML service tag:**
```yaml
# config/services.yaml
App\Controller\ContentElement\ExampleElementController:
    tags:
        - name: contao.content_element
          type: example_element
          category: texts
```

---

## PageModel access

Inside the controller, the current page is available via `$this->getPageModel()`
as follows:

```php
protected function getResponse(FragmentTemplate $template, ContentModel $model, Request $request): Response
{
    $page = $this->getPageModel();
    // $page is a \Contao\PageModel object
    $template->set('pageTitle', $page->pageTitle);
    return $template->getResponse();
}
```

---

## Nested fragments (as of Contao 5.3)

Nested fragments allow a parent element to contain child content elements.

**Controller:**
```php
#[AsContentElement(nestedFragments: ['allowedTypes' => ['image', 'video']])]
class GalleryController extends AbstractContentElementController
{
    // ...
}
```

**Template:**
```twig
{% for fragment in nested_fragments %}
    {{ content_element(fragment) }}
{% endfor %}
```

---

## Wrapper elements (legacy)

Legacy wrapper elements (start/stop/single/separator) are registered in `$GLOBALS['TL_WRAPPERS']`
as follows:

```php
// contao/config/config.php
$GLOBALS['TL_WRAPPERS']['start'][] = 'my_start_element';
$GLOBALS['TL_WRAPPERS']['stop'][] = 'my_stop_element';
$GLOBALS['TL_WRAPPERS']['single'][] = 'my_single_element';
```

**Important:** the backend output should differ from the frontend output in order to
avoid rendering problems.

---

## Content elements for custom tables

Content elements can also be used as child records of custom tables:

```php
// contao/dca/tl_example.php
$GLOBALS['TL_DCA']['tl_example'] = [
    'config' => [
        'ctable' => ['tl_content'],
    ],
    'list' => [
        'operations' => [
            'edit' => [
                'href' => 'table=tl_content',
                'icon' => 'edit.svg',
            ],
        ],
    ],
];
```

Backend module:
```php
$GLOBALS['BE_MOD']['content']['example'] = [
    'tables' => ['tl_example', 'tl_content'],
];
```

Rendering in the frontend:
```php
use Contao\ContentModel;
use Contao\Controller;

$models = ContentModel::findPublishedByPidAndTable($recordId, 'tl_example');
foreach ($models as $model) {
    echo Controller::getContentElement($model);
}
```

**Performance tip:** use anonymous functions for lazy evaluation — content is only
loaded from the database when it is actually accessed.

---

## Maker Bundle

The `contao/maker-bundle` can generate files automatically:

```bash
bin/console make:contao:content-element
```

---

*Source: https://docs.contao.org/5.x/dev/framework/content-elements/*  
*https://docs.contao.org/5.x/dev/getting-started/content-elements-modules/*  
*https://docs.contao.org/5.x/dev/guides/using-content-elements/*
