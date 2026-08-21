# Contao 5 — Getting Started

## Contents

- [Overview](#overview)
- [Directory structure (Managed Edition)](#directory-structure-managed-edition)
- [Configuration files](#configuration-files)
- [Autoloading and services](#autoloading-and-services)
- [DCA basics (getting started)](#dca-basics-getting-started)
- [Hooks overview (getting started)](#hooks-overview-getting-started)
- [Translations when getting started](#translations-when-getting-started)
- [Content elements & modules (getting started)](#content-elements-modules-getting-started)
- [Further skills](#further-skills)

## Overview

Contao is an open source CMS implemented as a Symfony bundle that can either be integrated
into existing Symfony applications or run as a standalone Managed Edition.
This section covers getting started for new developers.

---

## Directory structure (Managed Edition)

After installation via `composer create-project contao/managed-edition`, the project
contains the following core directories:

| Directory | Purpose |
|-------------|-------|
| `assets/` | Framework and third-party JS/CSS |
| `config/` | Application configuration |
| `files/` | Files managed by the Contao file manager |
| `public/` | Public entry points, symlinks to resources |
| `system/` | Legacy compatibility folder (Contao 3) |
| `templates/` | Custom Contao and Twig templates |
| `var/` | Transient files (cache, logs) |
| `vendor/` | Composer dependencies including Contao |

### Directories for your own development

| Directory | Purpose |
|-------------|-------|
| `config/` | Application configuration |
| `contao/` | Contao-specific configuration, DCAs, translations |
| `src/` | Your own PHP code (controllers, event listeners, services) |
| `templates/` | Custom and overridden templates |
| `translations/` | Symfony translations (as of version 5.3) |

---

## Configuration files

### `config/` directory

| File | Purpose |
|-------|-------|
| `.env` | Default environment variables (is committed) |
| `.env.local` | Environment-specific overrides (in `.gitignore`) |
| `config.yaml` | Bundle and extension configuration |
| `config_dev.yaml` | Development environment settings |
| `config_prod.yaml` | Production environment settings |
| `parameters.yaml` | Database and SMTP credentials |
| `routes.yaml` | Application-specific routes |
| `services.yaml` | Service definitions |

### `contao/` directory

| File/directory | Purpose |
|-------------------|-------|
| `contao/config/config.php` | Registers modules, content elements, models, hooks, crons |
| `contao/dca/` | Data Container Array customisations |
| `contao/languages/` | Translation files by language |
| `contao/languages/de/` | German translations |
| `contao/languages/en/` | English translations (fallback) |

---

## Autoloading and services

### PSR-4 autoloading

Configured by default in `composer.json`:

```json
{
    "autoload": {
        "psr-4": {
            "App\\": "src/"
        }
    }
}
```

### Service configuration (`config/services.yaml`)

```yaml
services:
    _defaults:
        autowire: true
        autoconfigure: true

    App\:
        resource: ../src
```

With `autowire: true` and `autoconfigure: true`, hooks, callbacks and content
elements are detected and registered automatically – no manual tag entry is necessary.

**Caution:** classes that extend legacy Contao framework classes require manual
service registration, because they are not discovered through autoconfigure.

### Route configuration (`config/routes.yaml`)

```yaml
app.controller:
    resource: ../src/Controller
    type: attribute
```

---

## DCA basics (getting started)

DCA customisations belong in `contao/dca/<tablename>.php`. Example: adding a `location`
field to news entries:

```php
// contao/dca/tl_news.php
use Contao\CoreBundle\DataContainer\PaletteManipulator;

$GLOBALS['TL_DCA']['tl_news']['fields']['location'] = [
    'label' => ['Location', 'Location of the news entry, if applicable.'],
    'inputType' => 'text',
    'eval' => ['tl_class' => 'w50', 'maxlength' => 255],
    'sql' => ['type' => 'string', 'length' => 255, 'default' => ''],
];

PaletteManipulator::create()
    ->addField('location', 'author_legend', PaletteManipulator::POSITION_APPEND)
    ->applyToPalette('default', 'tl_news')
    ->applyToPalette('internal', 'tl_news')
;
```

**Important:** after changes to Contao configurations, the Symfony application
cache must be rebuilt for the production environment. In the development environment
changes take effect immediately.

---

## Hooks overview (getting started)

Hooks allow injecting your own logic at specific execution points of the framework.
Registration via the `#[AsHook]` attribute:

```php
// src/EventListener/ParseArticlesListener.php
namespace App\EventListener;

use Contao\CoreBundle\DependencyInjection\Attribute\AsHook;
use Contao\FrontendTemplate;
use Contao\Module;
use Contao\UserModel;

#[AsHook('parseArticles')]
class ParseArticlesListener
{
    public function __invoke(FrontendTemplate $template, array $newsEntry, Module $module): void
    {
        $author = UserModel::findById($newsEntry['author']);
        $template->set('author', $author->row());
    }
}
```

Dependency injection works in hooks through the constructor:

```php
#[AsHook('updatePersonalData')]
class UpdatePersonalDataListener
{
    public function __construct(private readonly ExternalMemberService $externalMemberService)
    {
    }

    public function __invoke(FrontendUser $member, array $data, Module $module): void
    {
        $this->externalMemberService->updateMemberData($data);
    }
}
```

---

## Translations when getting started

Translations are placed in `contao/languages/<language>/`. Example for
changing an existing label:

```php
// contao/languages/en/default.php
$GLOBALS['TL_LANG']['MSC']['more'] = 'more';
```

As of Contao 5.3 the Symfony translations format with the `contao_` prefix is also possible:

```yaml
# translations/contao_default.en.yaml
MSC:
    more: more
```

---

## Content elements & modules (getting started)

A simple content element requires:
1. Controller class (PHP)
2. DCA palette
3. Twig template

Short example:

```php
// src/Controller/ContentElement/MyContentElementController.php
#[AsContentElement(category: 'texts')]
class MyContentElementController extends AbstractContentElementController
{
    protected function getResponse(FragmentTemplate $template, ContentModel $model, Request $request): Response
    {
        $template->set('text', $model->text);
        return $template->getResponse();
    }
}
```

```php
// contao/dca/tl_content.php
$GLOBALS['TL_DCA']['tl_content']['palettes']['my_content_element'] = '
    {type_legend},type,headline;{text_legend},text,url;
';
```

```twig
{# templates/content_element/my_content_element.html.twig #}
{% extends "@Contao/content_element/_base.html.twig" %}
{% block content %}
    {{ text }}
{% endblock %}
```

The `contao/maker-bundle` can generate files automatically via `make:contao:content-element`
or `make:contao:frontend-module`.

---

## Further skills

- `contao-initial-setup` — Managed Edition vs. Symfony application, installation
- `contao-core-concepts` — all core concepts at a glance
- `contao-extension-bundle` — creating and publishing a bundle
- `contao-content-elements` — complete content element documentation
- `contao-templates` — Twig template system

---

*Source: https://docs.contao.org/5.x/dev/getting-started/*  
*https://docs.contao.org/5.x/dev/getting-started/starting-development/*  
*https://docs.contao.org/5.x/dev/getting-started/dca/*  
*https://docs.contao.org/5.x/dev/getting-started/hooks/*  
*https://docs.contao.org/5.x/dev/getting-started/content-elements-modules/*  
*https://docs.contao.org/5.x/dev/getting-started/translations/*
