# Contao 5 — Twig Template System

## Contents

- [Overview](#overview)
- [Getting Started: Twig Basics](#getting-started-twig-basics)
- [Architecture: ContaoFilesystemLoader](#architecture-contaofilesystemloader)
- [Naming & Structure](#naming-structure)
- [Variant Templates](#variant-templates)
- [Creating Templates](#creating-templates)
- [Output Encoding](#output-encoding)
- [Debugging](#debugging)
- [Legacy PHP Templates](#legacy-php-templates)
- [Quick Reference: Common Tasks](#quick-reference-common-tasks)
- [Version Compatibility](#version-compatibility)

## Overview

Since version 4.12, Contao natively uses Symfony's **Twig template system**.
In Contao 5, most content elements are exclusively Twig-based.
PHP templates (legacy) are still supported in Contao 5; they are dropped as of Contao 6.

---

## Getting Started: Twig Basics

### Core syntax

```twig
{# Variable output #}
{{ name }}

{# Control structures #}
{% for item in items %}
    <li>{{ item }}</li>
{% endfor %}

{# Filters #}
{{ age|round }}
{{ text|capitalize }}

{# String concatenation #}
{{ firstName ~ ' ' ~ lastName }}

{# Comments #}
{# This is a comment #}
```

### Installing Twig extensions

```bash
composer require twig/intl-extra
```

```twig
{{ '1000000'|format_currency('EUR') }}
{# €1,000,000.00 #}
```

### Creating a custom Twig filter

```php
// src/Twig/AppExtension.php
namespace App\Twig;

use Twig\Extension\AbstractExtension;
use Twig\TwigFilter;

class AppExtension extends AbstractExtension
{
    public function getFilters(): array
    {
        return [
            new TwigFilter('rot13', [$this, 'rotateString']),
        ];
    }

    public function rotateString(string $value): string
    {
        return str_rot13($value);
    }
}
```

---

## Architecture: ContaoFilesystemLoader

### Namespaces

Twig templates are identified through **namespaces** (with an `@` prefix):

```
$twig->render("@Foo/bar/baz.html.twig", $params);
```

### Managed namespace `@Contao`

The **managed namespace** is Contao's core mechanism: several bundles can extend
the same template independently of each other without knowing about each other.

The `ContaoFilesystemLoader` assigns templates to these namespaces:

| Directory | Namespace | Priority |
|-------------|-----------|-----------|
| Bundle template directory: `/vendor/foo/bar/src/Resources/contao/templates` | `@Contao_FooBarBundle` | 1 |
| App template directory: `/contao/templates`, `/src/Resources/contao/templates` | `@Contao_App` | 2 |
| Global template directory: `/templates` | `@Contao_Global` | 3 |
| Theme directories: `/templates/<theme>` | `@Contao_Theme_<theme>` | 4 |

### Template inheritance hierarchy

While compiling, Contao replaces `@Contao` references in `extends`, `include`, `embed`
and `use` tags with the respective bundle namespace:

```twig
{% extends "@Contao/content_element/text.html.twig" %}
{# becomes: #}
{% extends "@Contao_ContaoCoreBundle/content_element/text.html.twig" %}
```

This creates an inheritance chain in which all bundles can occupy the same
template slot independently of each other.

**Debug command:** `debug:contao-twig` shows the entire hierarchy.

### Configuring the bundle template path

As of Symfony 6.1 (AbstractBundle):
```php
class FooBarBundle extends AbstractBundle
{
    // path is detected automatically
}
```

For older versions (bundle class):
```php
class FooBarBundle extends Bundle
{
    public function getPath(): string
    {
        return dirname(__DIR__);
    }
}
```

---

## Naming & Structure

### Twig root

The topmost template directory is the **Twig root** — all subdirectories
are part of the template name.

```
templates/          ← Twig root
├── content_element/
│   ├── text.html.twig        → "content_element/text"
│   └── image.html.twig       → "content_element/image"
└── frontend_module/
    └── news_list.html.twig   → "frontend_module/news_list"
```

### `.twig-root` marker (for bundles)

In bundles, the Twig root is marked with a `.twig-root` file:

```
vendor/…/FooBundle/contao/templates/
├── bar/
│   └── baz.html.twig          → "@Contao/baz.html.twig" (legacy without directory)
└── my_root/
    ├── .twig-root             ← marker
    └── content_element/
        └── foobar.html.twig   → "@Contao/content_element/foobar.html.twig"
```

### Standard directories

| Category | Directory | Example |
|-----------|-------------|---------|
| Reusable components | `component/` | `component/_list.html.twig` |
| Content elements | `content_element/` | `content_element/gallery.html.twig` |
| Frontend modules | `frontend_module/` | `frontend_module/feed_reader.html.twig` |
| Backend elements | `backend/` | `backend/module_wildcard.html.twig` |

### Naming conventions

- `snake_case` for all names
- Include the file extension: `name.html.twig` or `name.svg.twig`
- No duplicate directory names in file names
- Partial templates with a `_` prefix (use internally only)

---

## Variant Templates

Variant templates are specialised versions of a base template that
editors can select per element.

**Example:** highlight variant for `content_element/text.html.twig`:

```twig
{# templates/content_element/text/highlight.html.twig #}
{% extends "@Contao/content_element/text.html.twig" %}

{% block text %}
    <div style="border: 5px solid red; padding: 1em;">{{ parent() }}</div>
{% endblock %}
```

Variants live in a subdirectory named after the base template
(without the file extension). They appear in the backend dropdown automatically.

### Template finder

```php
// inject the factory via DI
$finder = $this->finderFactory->create();

$finder = $finder
    ->identifier('content_element/text')
    ->extension('html.twig')
    ->withVariants()
;

// For DCA listeners:
$options = $finder->asTemplateOptions();
```

---

## Creating Templates

### Extends (inheritance)

```twig
{# templates/content_element/my_element.html.twig #}
{% extends "@Contao/content_element/_base.html.twig" %}

{% block content %}
    <p>{{ text }}</p>
{% endblock %}
```

### Include

```twig
{% include "@Contao/component/_action_button.html.twig" with {label: 'Click me'} %}
```

### Embed

```twig
{% embed "@Contao/component/_card.html.twig" %}
    {% block card_body %}
        Customised content
    {% endblock %}
{% endembed %}
```

### Horizontal reuse (`use`)

```twig
{% use "@Contao/component/_stylesheet.html.twig" %}

{% with {file: asset('styles.css')} %}
    {{ block('stylesheet_component') }}
{% endwith %}
```

### Macros

```twig
{% macro input(name, value, type='text') %}
    <input type="{{ type }}" name="{{ name }}" value="{{ value }}">
{% endmacro %}

{{ _self.input('username', user.name) }}
```

### Contao components

Components are reusable template logic for the `{% use %}` import.
Conventions:
- Wrapped in a single block named `<name>_component`
- Stored in the `component/` directory

---

## Output Encoding

Twig implements **output encoding** (safer than Contao's historic input encoding):

```twig
{# HTML context (automatic) #}
{{ color }}

{# Explicit CSS encoding #}
<style>.box { background: {{ color|e('css') }} }</style>

{# HTML context #}
<div class="box">{{ color|e('html') }}</div>
```

### Raw output (careful!)

```twig
{# ONLY for trusted HTML content (e.g. TinyMCE output) #}
{{ my_content|raw }}
```

**Warning:** `|raw` on untrusted data leads to severe
XSS security holes!

### Preventing double encoding

Contao uses its own `contao_html` and `contao_html_attr` escapers, which use
`htmlspecialchars(double_encode: false)`. They apply to `@Contao` namespaces only.

As of Contao 5.3.19/5.4.7, enable double encoding explicitly when needed:
```twig
{{ my_data|e('html', double_encode = true) }}
```

---

## Debugging

### PhpStorm: ide-twig.json

In development environments, the `ContaoFilesystemLoaderWarmer` creates a `var/ide-twig.json`
for template autocompletion and navigation.

### debug:contao-twig command

```bash
bin/console debug:contao-twig
bin/console debug:contao-twig --theme my_theme
bin/console debug:contao-twig content_element/te
bin/console debug:contao-twig content_element/text --tree
```

`--tree` shows the results hierarchically. `--theme <slug>` includes theme templates.

### Dump in templates

```twig
{# Dump everything #}
{{ dump() }}

{# Specific variables #}
{{ dump(a, b) }}

{# Via tag (in the Symfony Web Debug Toolbar) #}
{% dump a, b %}
```

**Security note:** use in development environments only!

### Twig cache files

Compiled templates live in `var/cache/dev/twig/`. XDebug breakpoints can be set.
Find the files via the comment `/* @Contao/<name>.html.twig */`.

---

## Legacy PHP Templates

### Instantiation

```php
use Contao\FrontendTemplate;

$template = new FrontendTemplate('my_front_end_template');
$template->someData = 'foobar';
$buffer = $template->parse();
```

### Template folders (search order)

1. `templates/<THEME>/` — theme-specific overrides
2. `templates/` — own overrides
3. `contao/templates/` — application-specific templates
4. `<BUNDLE>/contao/templates/` — bundle templates

### Template inheritance (legacy PHP)

```php
<?php $this->block('head'); ?>
    <?php $this->parent(); ?>
    <style>.thing { color: orange; }</style>
<?php $this->endblock(); ?>
```

Child template:
```php
<?php $this->extend('fe_page'); ?>

<?php $this->block('head'); ?>
    <?php $this->parent(); ?>
    <link rel="stylesheet" href="style_2.css">
<?php $this->endblock(); ?>
```

### Setting template data

```php
$template->foobar = 'foobar';
// or:
$template->setData([
    'myVariable' => 'foobar',
    'myOtherVariable' => 'Lorem Ipsum',
]);
```

### Lazy variables (performance)

```php
// Executed only when $template->foo is used in the template:
$template->foo = function(): string {
    return expensiveOperation();
};

// Execute once and cache:
$template->foo = Template::once(function(): string {
    return expensiveOperation();
});
```

### Overriding/extending legacy templates in Twig

Create a Twig template with the same name (`.html.twig` instead of `.html5`):

```twig
{# templates/fe_page.html.twig #}
{% extends "@Contao/fe_page.html5" %}

{% block head %}
    {{ parent() }}
    <style>.thing { color: orange; }</style>
{% endblock %}
```

---

## Quick Reference: Common Tasks

### Dynamic template name

```php
protected function getResponse(FragmentTemplate $template, ContentModel $model, Request $request): Response
{
    $template->setName('content_element/custom_name');
    return $template->getResponse();
}
```

### Base template with custom attributes

```twig
{# extending content_element/_base.html.twig #}
{% extends "@Contao/content_element/_base.html.twig" %}

{% block attributes %}
    {{ parent() }}
    data-element="{{ model.id }}"
{% endblock %}
```

### HTML attributes via attrs()

```twig
<div {{ attrs()
    .set('class', 'my-class')
    .set('id', 'el-' ~ element.id)
    .setIfExists('data-foo', foo)
}}>
```

### Rendering an image/figure

```twig
{% set figure = figure(model.singleSRC, {width: 800}) %}
{% if figure %}
    {{ figure.build()|render }}
{% endif %}
```

### Translations

```twig
{{ 'MSC.goBack'|trans({}, 'contao_default') }}

{# Trans tag with a default domain #}
{% trans_default_domain 'contao_default' %}
{{ 'MSC.goBack'|trans }}
```

---

## Version Compatibility

| Contao version | Status |
|----------------|--------|
| 5.x | Twig is the standard, PHP templates still supported |
| 4.13 LTS | Twig native since 4.12; directory structure supported |
| 4.9 LTS | No native Twig; no longer supported |

**For Contao 4.13 and 5 at the same time:**

```php
// Specify the template explicitly for the new directory structure:
#[AsContentElement(category: 'bar', template: 'content_element/foo')]
class FooController extends AbstractContentElement { ... }
```

---

*Source: https://docs.contao.org/5.x/dev/framework/templates/*  
*https://docs.contao.org/5.x/dev/framework/templates/getting-started/*  
*https://docs.contao.org/5.x/dev/framework/templates/architecture/*  
*https://docs.contao.org/5.x/dev/framework/templates/creating-templates/*  
*https://docs.contao.org/5.x/dev/framework/templates/debugging/*  
*https://docs.contao.org/5.x/dev/framework/templates/legacy/*  
*https://docs.contao.org/5.x/dev/framework/templates/quick-reference/*
