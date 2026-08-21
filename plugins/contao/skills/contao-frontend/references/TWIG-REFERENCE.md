# Contao 5.x Twig Reference — Functions, Filters, Globals, Tags

Contao extends Twig with its own functions, filters, globals and tags in addition to [Twig's own](https://twig.symfony.com/doc/3.x/#reference).

---

## Contents

- [1. Twig Functions](#1-twig-functions)
- [2. Twig Filters](#2-twig-filters)
- [3. Twig Globals](#3-twig-globals)
- [4. Twig Tags](#4-twig-tags)
- [5. Contao Twig Components](#5-contao-twig-components)

## 1. Twig Functions

### add_schema_org

Adds JSON-LD metadata to the current page.

```twig
{% do add_schema_org({
    '@type': 'Event',
    'identifier': '#/schema/events/' ~ id,
    'name': title,
    'startDate': startTime|date('Y-m-d\TH:i:sP'),
}) %}

{# Metadata from a FilesystemItem #}
{% do add_schema_org(file.schemaOrgData|default) %}

{# Metadata from a Figure #}
{% do add_schema_org(figure.schemaOrgData|default) %}
```

**Parameters:** `array $jsonLd` — Array with JSON-LD metadata  
**Returns:** `void` (via `{% do %}`)

---

### attrs()

Fluent management of HTML attributes through the `HtmlAttributes` class.

```twig
{# CSS classes #}
{% set el = attrs().addClass('my-div').addClass(cssClasses|default([])) %}
<div{{ el }}>…</div>

{# Remove classes #}
{{ attrs().removeClass('foo') }}

{# Add conditionally #}
{{ attrs().addClass('admin', isAdmin) }}

{# Styles #}
{{ attrs().addStyle('color: red') }}
{{ attrs().addStyle({'color': 'red', 'margin': '1em'}) }}
{{ attrs().removeStyle('color') }}

{# Set attributes #}
{{ attrs().set('id', 'my-id') }}
{{ attrs().unset('id') }}
{{ attrs().set('disabled', true, isDisabled) }}
{{ attrs().setIfExists('title', maybeTitle) }}

{# Merge #}
{{ attrs().mergeWith('disabled hidden') }}
{{ attrs().mergeWith({'aria-label': 'Close'}) }}
```

**Complete example:**
```twig
<button{{ attrs()
    .addClass(['btn', 'btn-primary'])
    .set('disabled', true, not isActive)
    .set('type', 'submit') }}>
    Speichern
</button>
```

---

### backend_icon() (as of 5.5)

Renders an icon in the back end.

```twig
{{ backend_icon('edit.svg', 'Datensatz bearbeiten') }}
{{ backend_icon('edit.svg', 'Edit', attrs().addClass('icon-sm')) }}
```

**Parameters:**
1. `string $icon` — Icon file name
2. `string $alt` — Alt text for `<img>`
3. `HtmlAttributes $attributes` (optional) — Additional HTML attributes on `<img>`

---

### contao_figure() [DEPRECATED]

Renders a figure for image processing. **Deprecated — will be removed in Contao 6.** Use `figure()` with `component/_figure.html.twig` instead.

**Parameters:**
1. `mixed $from` — `FilesModel`, `FilesystemItem`, `ImageInterface`, UUID/ID/path
2. `mixed $size` — Image size configuration
3. `array $configuration` — Additional `FigureBuilder` settings
4. `string $template` (optional) — Custom template

---

### contao_section()

Renders a layout section.

```twig
{{ contao_section('main') }}
{{ contao_section('left', 'block_section_custom') }}
```

**Parameters:**
1. `string $key` — Layout section ID
2. `string $template` (optional) — Custom template (default: `block_section`)

---

### contao_sections()

Renders the custom layout sections of a given position.

```twig
{{ contao_sections('top') }}
{{ contao_sections('bottom', 'block_sections_custom') }}
```

**Parameters:**
1. `string $key` — Position of the custom section
2. `string $template` (optional) — Custom template (default: `block_sections`)

---

### content_element() (as of 5.2)

Renders a content element by database reference or dynamically.

```twig
{# By ID #}
{{ content_element(8472) }}

{# Override the configuration #}
{{ content_element(5618, { perRow: 4 }) }}

{# Create dynamically #}
{{ content_element('text', { text: '<p>Hello World!</p>' }) }}

{# Via fragment reference #}
{{ content_element(fragment_reference) }}
```

**Parameters:**
- `int|string|FragmentReference $typeOrId` — Type, database ID or fragment reference
- `array $data` (optional) — Data/configuration overrides

---

### content_url() (as of 5.3)

Generates the URL for a model object (like Symfony's `path()`).

```twig
{% for item in items %}
    <a href="{{ content_url(item) }}">{{ item.title }}</a>
{% endfor %}

{# With parameters #}
{{ content_url(pageModel, {foo: 'bar'}) }}

{# Relative path instead of absolute URL #}
{{ content_url(item, [], true) }}
```

**Parameters:**
- `Model $content` — Contao model
- `array $parameters` (optional) — URL parameters
- `bool $relative` (optional) — `true` for an absolute path instead of an absolute URL

---

### csp_hash() (as of 5.3)

Adds CSP hashes for inline styles and scripts.

```twig
{# Secure inline JavaScript #}
{% set script %}
    alert('foo');
{% endset %}
<script>{{ script }}</script>
{% do csp_hash('script-src', script) %}

{# Secure an inline style #}
{% set style %}
    body { background-color: magenta; }
{% endset %}
<style>{{ style }}</style>
{% do csp_hash('style-src', style) %}
```

**Parameters:**
1. `string $directive` — CSP directive
2. `string $source` — Content to be hashed
3. `string $algorithm` (optional) — Hash algorithm (default: `sha256`)

---

### csp_nonce() (as of 5.3)

Adds CSP nonces for inline styles and scripts.

```twig
<script{{ attrs().setIfExists('nonce', csp_nonce('script-src')) }}>
    alert('foo');
</script>

<style{{ attrs().setIfExists('nonce', csp_nonce('style-src')) }}>
    body { background-color: magenta; }
</style>
```

**Parameters:** `string $directive` — CSP directive  
**Returns:** `string|null` (nonce value)

---

### csp_source() (as of 5.3)

Adds a source for a CSP directive. Useful for iframes and external media.

```twig
{# For iframes #}
{% set source = 'https://example.com/foobar' %}
{% do csp_source('frame-src', source) %}
<iframe src="{{ source }}">

{# For video elements #}
{% set source = 'https://example.com/foobar.mp4' %}
{% do csp_source('media-src', source) %}
<video controls><source src="{{ source }}"></video>

{# Multiple directives #}
{% do csp_source(['frame-src', 'media-src'], source) %}
```

**Parameters:**
- `string|array $directive` — CSP directive(s)
- `string $source` — Source URL

---

### figure()

Creates a Figure object for image processing via the Contao Image Studio.

```twig
{% use "@Contao/component/_figure.html.twig" %}

{% set image = figure('files/foo/bar.jpg', [1280, 720, 'crop']) %}

{% if image %}
    {% with {figure: image} %}{{ block('figure_component') }}{% endwith %}
{% endif %}
```

**Advanced configuration:**
```twig
{% set fig = figure(id, [200, 200, 'proportional'], {
    metadata: { alt: 'Bildbeschreibung', caption: 'Bildunterschrift' },
    enableLightbox: true,
    lightboxGroupIdentifier: 'my-gallery',
    lightboxSize: '_big_size',
    linkHref: 'https://contao.org',
    options: { attr: { class: 'foobar-container' } }
}) %}
```

**Access the image data:**
```twig
{% set resizedPath = figure(id, '_my_size').image.img.src %}
{% set originalPath = figure(id, '_my_size').image.filePath %}
```

**Parameters:**
- `mixed $from` — `FilesModel`, `FilesystemItem`, `ImageInterface`, UUID/ID/path
- `mixed $size` — Image size configuration, reference or size array
- `array $configuration` (optional) — `FigureBuilder` settings

**Returns:** `Figure|null`

---

### file_icon() (as of 5.7)

Renders an icon based on the file type in the back end.

```twig
{{ file_icon(download.file, 'Download', attrs().addClass('file-icon')) }}
```

**Parameters:**
1. `FilesystemItem $item` — Filesystem item
2. `string $alt` (optional) — Alt text
3. `HtmlAttributes $attributes` (optional) — Additional HTML attributes

---

### frontend_module() (as of 5.2)

Renders a front end module by database reference or dynamically.

```twig
{# By ID #}
{{ frontend_module(1701) }}

{# Override the configuration #}
{{ frontend_module(1864, { hardLimit: 0 }) }}

{# Dynamically #}
{{ frontend_module('newslist', {
    news_archives: [1, 2],
    news_template: 'news_latest',
    news_order: 'order_date_desc',
    numberOfItems: 10,
    imgSize: [0, 0, '_news_list'],
}) }}

{# Via fragment reference #}
{{ frontend_module(fragment_reference) }}
```

**Parameters:**
- `int|string|FragmentReference $typeOrId` — Type, database ID or fragment reference
- `array $data` (optional) — Configuration/overrides

---

### include()

Contao overrides Twig's default include function in order to support the Contao template hierarchy.

---

### insert_tag()

Renders an insert tag directly.

```twig
<a href="{{ insert_tag('link_url::10') }}">{{ insert_tag('link_title::10') }}</a>
<p>{{ insert_tag('insert_article::123')|raw }}</p>
```

**Parameters:** `string $insertTag` — Insert tag without curly braces  
**Returns:** `string`

---

### picture_config()

Creates an image configuration at runtime (without `contao.image.sizes` in the config).

```twig
{% use "@Contao/component/_figure.html.twig" %}

{% set special_size = picture_config({
    width: 400,
    height: 400,
    resizeMode: 'proportional',
    sizes: '0.75,1,1.5,2',
    items: [{
        width: 200,
        height: 100,
        media: '(max-width: 140px)',
    }]
}) %}

{% set image = figure('files/foo/bar.jpg', special_size) %}
{% with {figure: image} %}{{ block('figure_component') }}{% endwith %}
```

**Parameters:** `array $config` — The configuration matches the `contao.image.sizes` bundle configuration  
**Returns:** `PictureConfiguration`

---

### prefix_url()

Prefixes relative URLs with the base path (a replacement for `<base href="…">`).

```twig
<a href="{{ prefix_url(userGeneratedUrl|insert_tag) }}">Link</a>
```

**Parameters:** `string $url` — Relative URL  
**Returns:** `string` (path-absolute URL)

---

## 2. Twig Filters

### csp_inline_styles (as of 5.3)

Extracts all inline CSS style attributes of an HTML string and adds CSP hashes automatically.

```twig
{{ some_html|csp_inline_styles|raw }}
```

Configuration of the allowed styles: `contao.csp.allowed_inline_styles`.

---

### csp_unsafe_inline_style (as of 5.3.2)

Adds a CSP hash for an inline style and automatically adds `'unsafe-hashes'` to the directive.

**Warning:** Only pass trusted styles!

```twig
<div style="{{ 'color: red'|csp_unsafe_inline_style }}">

<div{{ attrs().addStyle({ color: 'red' })|csp_unsafe_inline_style }}>
```

---

### deserialize (as of 5.3.8)

Deserializes a string containing serialized data into an array. Internally: `Contao\StringUtil::deserialize()`.

```twig
{% set data = 'a:2:{i:0;s:3:"Foo";i:1;s:3:"Bar";}'|deserialize %}
{# data = ["Foo", "Bar"] #}

{{ (bar|deserialize).foo }}
```

---

### encode_email (as of 5.2)

Encodes an e-mail address with HTML entities. Internally: `Contao\StringUtil::encodeEmail()`.

```twig
{{ 'foobar@example.com'|encode_email }}
```

---

### escape

Contao overrides Twig's default escape filter in order to support `ChunkedText` from insert tags and prevents double encoding.

```twig
{# Default — no double encoding #}
{{ '&gt;'|e }}  {# Output: &gt; #}

{# Force double encoding #}
{{ '&gt;'|e('html', double_encode = true) }}
```

```twig
{# Selective escaping: only text outside of insert tags #}
{{ text|insert_tag_raw|escape('html') }}
```

---

### format_bytes

Converts bytes into a readable format.

```twig
{{ 134217728|format_bytes }}         {# "128.0 MiB" #}
{{ 135000000|format_bytes }}         {# "128.7 MiB" #}
{{ 135000000|format_bytes(2) }}      {# "128.75 MiB" #}
{{ 135000000|format_bytes(3) }}      {# "128.746 MiB" #}
```

**Parameters:** `int $decimalPlaces` (optional, default: `1`)

---

### highlight

Syntax highlighting via highlight.php.

```twig
{% set highlighted = code|highlight('php') %}
{% set code_attributes = attrs()
    .addClass('hljs')
    .addClass(highlighted.language) %}
<pre><code{{ code_attributes }}>
    {{- highlighted.value|raw -}}
</code></pre>

{# Short form via __toString() #}
<pre><code>{{ code|highlight('php')|raw }}</code></pre>
```

**Parameters:** `string $language` (optional, default: `plaintext`)  
**Returns:** `HighlightResult` with `.language` and `.value`

---

### highlight_auto

Automatic syntax highlighting via highlight.php (the language is auto-detected).

```twig
{% set highlighted = code|highlight_auto %}
<pre><code class="hljs {{ highlighted.language }}">
    {{- highlighted.value|raw -}}
</code></pre>

{# Restrict the languages #}
<pre><code>{{ code|highlight_auto(['C', 'C#', 'C++']) }}</code></pre>
```

**Returns:** `HighlightResult` (as with `highlight`)

---

### insert_tag

Replaces insert tags for text output (non-HTML, e.g. in HTML attributes).

```twig
{{ '{{date::Y}}'|insert_tag }}           {# "1970" #}
{{ '{{fragment::{{date::Y}}}}'|insert_tag }}  {# "1970" (no ESI tag) #}
```

---

### insert_tag_raw

Replaces insert tags for HTML output.

```twig
{{ '{{date::Y}}'|insert_tag_raw }}           {# "1970" #}
{{ '{{fragment::{{date::Y}}}}'|insert_tag_raw }}  {# <esi:include ...></esi:include> #}

{# Escaping: HTML tags outside = escaped, insert tag output = not escaped #}
{{ '<span> foo {{br}} bar </span>'|insert_tag_raw }}
{# Output: &lt;span&gt; foo <br> bar &lt;/span&gt; #}
```

---

### sanitize_html (as of 5.1)

Sanitizes HTML code with a configured Symfony sanitizer.

```twig
{# Default sanitizer — for external HTML code #}
{{ '<div title=test style=color:red onclick=alert(1)><script>alert(2)</script>{{date::Y}}'|sanitize_html }}
{# Output: <div title="test">&#123;&#123;date::Y&#125;&#125;</div> #}

{# Contao sanitizer (as of 5.7) — for HTML from the Contao back end (TinyMCE) #}
{{ html_from_backend|sanitize_html('contao') }}
```

---

## 3. Twig Globals

### contao (as of 5.3)

The `contao` Twig global provides access to useful functions and properties.

```twig
{# Current page (PageModel) #}
{{ contao.page.title }}
{% set page = contao.page %}

{# Is a back end user present in the front end session? #}
{% if contao.has_backend_user %}…{% endif %}

{# Is preview mode (show hidden elements) active? #}
{% if contao.is_preview_mode %}…{% endif %}

{# Request token for forms #}
{{ contao.request_token }}

{# Back end user in the front end (if present) #}
{% set user = contao.backend_user.username|default %}
```

**Properties:**

| Property | Type | Description |
|-------------|-----|--------------|
| `contao.page` | `PageModel\|null` | Current PageModel |
| `contao.has_backend_user` | `bool` | Back end user present in the session |
| `contao.is_preview_mode` | `bool` | Preview mode active |
| `contao.request_token` | `string` | CSRF request token |
| `contao.backend_user` | `BackendUser\|null` | Back end user (if present) |

---

## 4. Twig Tags

### {% add %}

Adds output to various sections of the document.

**Supported positions:**
- `head` — End of the `<head>` area
- `stylesheets` — Grouped with the other stylesheets
- `body` — End of the `<body>` area

```twig
{# Add a script to the head #}
{% add "my-analytics" to head %}
    <script>/* Analytics code */</script>
{% endadd %}

{# Add a stylesheet #}
{% add "my-styles" to stylesheets %}
    <link rel="stylesheet" href="{{ asset('css/custom.css') }}">
{% endadd %}

{# Body script with a named node (can be overridden) #}
{% add "tracking-script" to body %}
    <script src="{{ asset('js/tracking.js') }}"></script>
{% endadd %}
```

---

### {% slot %} (as of 5.6)

Defines layout sections for composed content. In page layouts, slots can take up content elements or modules.

```twig
{# Simple slot #}
{% slot main %}{% endslot %}

{# Slot with a wrapper (only when not empty) #}
{% slot main %}
    <main>{{ slot() }}</main>
{% endslot %}

{# Slot with fallback content #}
{% slot main %}
    […]
{% else %}
    This content is displayed when the slot is empty.
{% endslot %}
```

**Setting the slot content (PHP):**
```php
/** @var \Contao\CoreBundle\Twig\LayoutTemplate $template */
$template->setSlot('main', 'Trusted content for the <b>main</b> block.');
```

---

## 5. Contao Twig Components

Components are reusable template blocks that are imported with `{% use %}` and rendered with `block()`.

```twig
{# Use the _figure.html.twig component #}
{% use "@Contao/component/_figure.html.twig" %}

{% set image = figure('files/foo/bar.jpg', [800, 600, 'crop']) %}
{% if image %}
    {% with {figure: image} %}{{ block('figure_component') }}{% endwith %}
{% endif %}
```

**Customizing a component:**
```twig
{% use "@Contao/component/_picture.html.twig" %}
{% block image %}
    {% set img_attributes = attrs().addClass('my-image').mergeWith(img_attributes|default) %}
    <div>{{ parent() }}</div>
{% endblock %}
```

**Available core components** (under `@Contao/component/`):
- `_figure.html.twig` — Figure with image + caption
- `_picture.html.twig` — Responsive image
- `_image.html.twig` — Simple image

---

*Sources:*
- https://docs.contao.org/5.x/dev/reference/twig/
- https://docs.contao.org/5.x/dev/reference/twig/functions/
- https://docs.contao.org/5.x/dev/reference/twig/filters/
- https://docs.contao.org/5.x/dev/reference/twig/globals/
- https://docs.contao.org/5.x/dev/reference/twig/tags/
- https://docs.contao.org/5.x/dev/reference/twig/tags/add/
- https://docs.contao.org/5.x/dev/reference/twig/tags/slot/
