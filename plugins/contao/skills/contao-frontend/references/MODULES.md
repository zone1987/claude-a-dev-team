# Contao 5 — Frontend modules

## Contents

- [Overview](#overview)
- [Basic components](#basic-components)
- [Implementation example](#implementation-example)
- [Service tag options](#service-tag-options)
- [Registration methods](#registration-methods)
- [PageModel access](#pagemodel-access)
- [Difference: frontend module vs. content element](#difference-frontend-module-vs-content-element)

## Overview

Frontend modules generate dynamic content for complex functionality that is
shared across multiple pages. Examples: news lists, navigation elements,
member forms.

They work as fragment controllers that render into the main content, and
are created in much the same way as content elements.

---

## Basic components

1. **Fragment controller** — a class extending `AbstractFrontendModuleController`
2. **Service tag** `contao.frontend_module`
3. **DCA configuration** in `tl_module` (palette)
4. **Twig template** — naming convention: `frontend_module/<type>.html.twig`
5. **Translations** for backend labels

---

## Implementation example

### Controller

```php
// src/Controller/FrontendModule/MyNewsListController.php
namespace App\Controller\FrontendModule;

use Contao\CoreBundle\Controller\FrontendModule\AbstractFrontendModuleController;
use Contao\CoreBundle\DependencyInjection\Attribute\AsFrontendModule;
use Contao\CoreBundle\Twig\FragmentTemplate;
use Contao\ModuleModel;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;

#[AsFrontendModule(category: 'news')]
class MyNewsListController extends AbstractFrontendModuleController
{
    protected function getResponse(FragmentTemplate $template, ModuleModel $model, Request $request): Response
    {
        $template->set('items', $this->loadNews($model));
        return $template->getResponse();
    }

    private function loadNews(ModuleModel $model): array
    {
        // Database query or similar
        return [];
    }
}
```

### DCA palette

```php
// contao/dca/tl_module.php
$GLOBALS['TL_DCA']['tl_module']['palettes']['my_news_list'] = '
    {title_legend},name,headline,type;
    {config_legend},numberOfItems;
    {template_legend},customTpl;
    {protected_legend:hide},protected;
    {expert_legend:hide},guests,cssID;
';
```

### Template

```twig
{# templates/frontend_module/my_news_list.html.twig #}
{% extends "@Contao/frontend_module/_base.html.twig" %}

{% block content %}
    <ul>
        {% for item in items %}
            <li>{{ item.headline }}</li>
        {% endfor %}
    </ul>
{% endblock %}
```

### Translations

```yaml
# translations/contao_default.en.yaml
FMD:
    my_news_list:
        - My News List
        - Displays a list of news items.
```

---

## Service tag options

| Option | Type | Purpose |
|--------|-----|-------|
| `type` | string | Identifies the template and DCA palette (optional) |
| `category` | string | Groups the module in the type dropdown |
| `template` | string | Overrides the generated template name |
| `renderer` | string | Default: `forward`; `inline` or `esi` are also possible |
| `method` | string | Specifies the controller method to call |

---

## Registration methods

**Via PHP attribute (recommended):**
```php
#[AsFrontendModule(category: 'news', type: 'my_news_list')]
```

**Via YAML service tag:**
```yaml
App\Controller\FrontendModule\MyNewsListController:
    tags:
        - name: contao.frontend_module
          type: my_news_list
          category: news
```

---

## PageModel access

As with content elements, the current page is available via `$this->getPageModel()`:

```php
protected function getResponse(FragmentTemplate $template, ModuleModel $model, Request $request): Response
{
    $page = $this->getPageModel();
    $template->set('currentAlias', $page->alias);
    return $template->getResponse();
}
```

---

## Difference: frontend module vs. content element

| Aspect | Frontend module | Content element |
|--------|----------------|-----------------|
| Table | `tl_module` | `tl_content` |
| Base class | `AbstractFrontendModuleController` | `AbstractContentElementController` |
| Model type | `ModuleModel` | `ContentModel` |
| Attribute | `#[AsFrontendModule]` | `#[AsContentElement]` |
| Template path | `frontend_module/<type>` | `content_element/<type>` |
| Placement | Page layout/article modules | Article (content area) |

---

*Source: https://docs.contao.org/5.x/dev/framework/front-end-modules/*  
*https://docs.contao.org/5.x/dev/getting-started/content-elements-modules/*
