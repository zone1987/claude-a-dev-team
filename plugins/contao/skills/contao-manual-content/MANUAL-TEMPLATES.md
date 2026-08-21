# Templates, from the editor's side

How a template is customised in the backend, in both systems Contao 5 ships: Twig, which is the
standard, and the legacy PHP templates. Every customisation made under **Layout > Templates** is
update-safe.

**Before overriding anything**: a CSS id or class does not need a template. Both can be entered in
the element's **Expert settings**.

## Contents

- [Which system applies](#which-system-applies)
- [Twig syntax](#twig-syntax)
- [Where a Twig template lives](#where-a-twig-template-lives)
- [Reusing a Twig template](#reusing-a-twig-template)
- [Seeing what data a template has](#seeing-what-data-a-template-has)
- [Legacy PHP templates](#legacy-php-templates)
- [Assets from a template](#assets-from-a-template)
- [Source](#source)

## Which system applies

Twig has been available since Contao 4.12 and became the core standard at 5.0. **From Contao 5.7
every `.html5` template has a Twig equivalent**, and Twig fully replaces the HTML5 templates.

**Precedence**: the Twig version is used by default, but a `.html5` template of the same name in the
`templates` directory **takes precedence over it**. So `news_full.html.twig` applies as long as no
`news_full.html5` exists in `templates`.

The fallback to PHP templates exists for a transition period. The manual is explicit that HTML5
templates and the legacy content elements (prefix `ce_`) should be avoided, and the option used only
in exceptional cases.

**File extension**: a Twig template ends in `.twig`, with the output type before it. HTML output
therefore uses `.html.twig`.

## Twig syntax

Three identifiers carry everything:

| Identifier | Purpose |
|---|---|
| `{# … #}` | comment |
| `{{ … }}` | output a variable |
| `{% … %}` | a command or control structure |

A single-line comment, and a multi-line one that comments code out so it does not execute:

```twig
{# my comment #}

{# commented out code - the code will not be executed
{{ variable }}
#}
```

Output, a condition, and a loop:

```twig
<p>output: {{ name_of_variable }}</p>

{% if my_variable %}
<p>The variable has the following content:</p>
<p>{{ my_variable }}</p>
{% endif %}

<ul>
    {% for item in items %}
        <li>{{ item }}</li>
    {% endfor %}
</ul>
```

A filter is applied with a pipe:

```twig
{{ name_of_variable|name_of_filter }}
```

Twig ships many filters, and custom ones can be added as the developer documentation describes. For
the language itself, the manual points at the official Twig documentation, section "Twig for template
designers".

## Where a Twig template lives

Custom templates go in `/templates`, which is what makes them selectable in the backend when an
element is configured. **Use debug mode while creating, moving or renaming**, so it is visible which
template actually applies.

| Kind | Path | Note |
|---|---|---|
| Global | `/templates/content_element/text.html.twig` | selecting `text [content_element/text.html.twig]` creates the folder automatically |
| Global variant | `/templates/content_element/text/tip.html.twig` | a subfolder named after the base template |
| Theme specific | `/templates/themeA/content_element/text.html.twig` | linked through the Theme Manager |
| Theme specific variant | `/templates/themeA/content_element/text/highlight.html.twig` | needs a global variant of the same name |

Two constraints the manual states outright: a theme folder name **must not contain an underscore**,
and a theme-specific variant cannot exist without a global variant of the same name.

## Reusing a Twig template

Contao's approach is reuse rather than replacement. The precedence order, highest last:

1. templates from the core
2. templates from an extension
3. templates from an application
4. global templates
5. global variant templates

`debug:contao-twig` prints the resolved hierarchy.

### Extend, and adapt a block

`{% extends %}` inherits: instead of overwriting the whole template, individual blocks of the base
template are adapted. A block is opened with `{% block name %}` and closed with `{% endblock %}`;
`{{ parent() }}` outputs the original content.

```twig
{# /templates/content_element/text.html.twig #}
{% extends "@Contao/content_element/text.html.twig" %}
{% block text %}
    <p>Introductory text for all text elements</p>
    {{ parent() }}
{% endblock %}
```

A variant that appends instead:

```twig
{# /templates/content_element/text/tip.html.twig #}
{% extends "@Contao/content_element/text.html.twig" %}
{% block text %}
    {{ parent() }}
    <p>Here is an additional closing text for the "Tip" variant</p>
{% endblock %}
```

### Adapt HTML attributes

`attrs()` modifies attributes coming from a parent template:

```twig
{% set text_attributes = attrs().addClass('description').mergeWith(text_attributes|default) %}
```

### Horizontal reuse

`{{ block }}` outputs a block several times within a template. Blocks become available by being
defined directly, by a parent template, or through `{% use %}`.

**The difference that matters**: `{% extends %}` prints every block of the parent to the front end,
while `{% use %}` only makes the blocks available to the template.

For more, the manual points at Include, Embed, Macros and Components in the developer documentation.

## Seeing what data a template has

`dump()` shows the available variables and their contents. **Only with debug mode enabled**, because
the data can carry safety-critical information about the system.

As a function, output goes into the page:

```twig
{{ dump() }}      {# all available data #}
{{ dump(a) }}     {# the data of variable a #}
{{ dump(a, b) }}  {# the data of a and b #}
```

As a tag, output goes to the toolbar:

```twig
{% dump %}
{% dump(a) %}
```

In an extended template, `dump()` has to sit **inside a block**:

```twig
{# /templates/content_element/text.html.twig #}
{% extends "@Contao/content_element/text.html.twig" %}
{% block text %}
    {{ dump(headline) }}
{% endblock %}
```

## Legacy PHP templates

A PHP template holds HTML and PHP. In debug mode the template name appears as an HTML comment in the
source, so it is visible which one is in use.

### Where it lives, and what it is called

- Templates go in `/templates` to be available in the backend.
- One in the main directory is marked **global**.
- A subdirectory linked to a theme through the Theme Manager marks its files with that theme's name.
  **A template in an unlinked subdirectory is ignored.**
- The file name carries a prefix for its type: `ce_` for **c**ontent **e**lement. Editing
  `ce_text.html5` affects every text element; `ce_text_specific.html5` applies to one element only.

### Inheritance

Only content wrapped in `$this->block('name')` and `$this->endblock()` can be customised. A template
declares its base with `$this->extend('name')`, then supplies new block content;
`$this->parent()` gives the original.

Adding a meta tag:

```php
<?php $this->extend('fe_page'); ?>

<?php $this->block('meta'); ?>
  <?php $this->parent(); ?>
  <meta name="author" content="John Doe">
<?php $this->endblock(); ?>
```

Configuring TinyMCE to paste as text:

```php
<?php $this->extend('be_tinyMCE'); ?>

<?php $this->block('custom'); ?>
  paste_as_text: true,
<?php $this->endblock(); ?>
```

### Mixing templates

`insert()` puts one template inside another, with variables as an optional second argument:

```php
<?php $this->insert('template_name', array('key'=>'value')); ?>

<?php $this->insert('template_name', $this->getData()); ?>
```

The second form passes every variable of the current template. A worked example, source template
`image_copyright.html5`:

```php
<small>Photographed by <?php echo $this->name; ?>, licensed as <?php echo $this->license; ?></small>
```

Used from `ce_image_copyright.html5`:

```php
<?php $this->extend('ce_image'); ?>

<?php $this->block('content'); ?>
  <?php $this->parent(); ?>

  <?php $this->insert('image_copyright', array('name'=>'Donna Evans', 'license'=>'Creative Commons')); ?>

<?php $this->endblock(); ?>
```

## Assets from a template

Rather than loading CSS and JavaScript through the page layout everywhere, a template can carry its
own. Two ways, and the second offers more control.

Direct HTML references, with the files in a public directory under `/files`:

```html
<link href="files/myfolder/custom.css" rel="stylesheet">
<script src="files/myfolder/custom.js"></script>
```

Through the PHP global arrays, which puts them in the HTML head:

```php
<?php
// will be output inside <head>
$GLOBALS['TL_CSS'][] = 'files/myfolder/custom.css|static';
$GLOBALS['TL_JAVASCRIPT'][] = 'files/myfolder/custom.js|static';
?>
```

Appending `|static` combines the file with the assets already coming from the page layout.

## Display template data, legacy PHP system

**Source:** https://docs.contao.org/5.x/manual/en/layout/templates/php/template-data/

This page describes the mechanism for dumping all available PHP template data to inspect the template context.

The available template context varies depending on the template source. Usually, the complete data can be accessed via `$this->…`.

All available template data can be dumped to see what is there:

```php
<?php $this->dumpTemplateVars() ?>
```

This statement uses the Symfony VarDumper component to display the data. In debug mode, the output will therefore be redirected to the Symfony Debug Toolbar.

**Note:** if template inheritance is used, the template data is only displayed in debug mode or if the statement is enclosed between `$this->block(…)` and `$this->endblock()` statements.

---

Two notes for the caller: the requested `content-slider` URL carries `hidden: true` and `type: redirect` upstream (target `/en/article-management/content-elements/legacy-element/`), so it is a legacy element page that may not resolve at the given path. The `contao-manager-error` page lives under `installation/contao-manager/` in the source tree but is published at the requested `/installation/contao-manager-error` URL via an explicit `url:` override, so that URL is correct.agentId: a669a580ce1a9fa8e (use SendMessage with to: 'a669a580ce1a9fa8e', summary: '<5-10 word recap>' to continue this agent)
<usage>subagent_tokens: 138223
tool_uses: 17
duration_ms: 343322</usage>

## Source

Distilled from the [Contao 5 user manual](https://docs.contao.org/5.x/manual/en/layout/templates/),
the eleven pages under `layout/templates/`, retrieved 2026-08-21:

- https://docs.contao.org/5.x/manual/en/layout/templates/
- https://docs.contao.org/5.x/manual/en/layout/templates/twig/
- https://docs.contao.org/5.x/manual/en/layout/templates/twig/syntax/
- https://docs.contao.org/5.x/manual/en/layout/templates/twig/manage/
- https://docs.contao.org/5.x/manual/en/layout/templates/twig/reuse/
- https://docs.contao.org/5.x/manual/en/layout/templates/twig/data/
- https://docs.contao.org/5.x/manual/en/layout/templates/php/
- https://docs.contao.org/5.x/manual/en/layout/templates/php/manage-template/
- https://docs.contao.org/5.x/manual/en/layout/templates/php/template-assets/
- https://docs.contao.org/5.x/manual/en/layout/templates/php/template-inheritance/
- https://docs.contao.org/5.x/manual/en/layout/templates/php/template-insertion/

The developer-side view of the same system, `ContaoFilesystemLoader` and the component pattern
included, is `TEMPLATES.md` in the `contao-frontend` skill.
