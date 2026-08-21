# Contao 5 — Asset Management

## Contents

- [Overview](#overview)
- [Global arrays](#global-arrays)
- [Adding CSS & JavaScript assets](#adding-css-javascript-assets)
- [Template helper functions (generateStyleTag etc.)](#template-helper-functions-generatestyletag-etc)
- [Twig: including assets](#twig-including-assets)
- [Symfony Asset Component](#symfony-asset-component)

## Overview

Contao uses global arrays to store asset references while the
page layout is being assembled. In addition, the Symfony Asset Component is available.

---

## Global arrays

| Array | Description |
|-------|-------------|
| `$GLOBALS['TL_BODY']` | HTML code before `</body>` |
| `$GLOBALS['TL_CSS']` | CSS asset paths for `<head>` |
| `$GLOBALS['TL_HEAD']` | HTML code for `<head>` |
| `$GLOBALS['TL_JAVASCRIPT']` | JavaScript asset paths for `<head>` |
| `$GLOBALS['TL_MOOTOOLS']` | HTML code before `</body>` |

**Note:** in the backend, only `TL_CSS`, `TL_JAVASCRIPT` and `TL_MOOTOOLS` work.

---

## Adding CSS & JavaScript assets

```php
$GLOBALS['TL_CSS'][] = 'bundles/myextension/frontend.css';
$GLOBALS['TL_JAVASCRIPT'][] = 'bundles/myextension/scripts.js';
```

### Pipe options

Options are appended to the file path with `|` (pipe):

| Option | Example | Description |
|--------|---------|-------------|
| Static | `\|static` | The asset can be combined with other static assets |
| Media | `\|print` | CSS `media` attribute |
| Async | `\|async` | JavaScript `async` attribute |
| Version | `\|1` | Appends a `?v=…` parameter |

**Combination examples:**
```php
$GLOBALS['TL_CSS'][] = 'files/theme/css/print.css|print|static|1';
$GLOBALS['TL_JAVASCRIPT'][] = 'bundles/myextension/scripts.js|2|async|static';
```

### Static

Enables combination with other static assets (if activated in the page layout):

```php
$GLOBALS['TL_CSS'][] = 'bundles/myextension/frontend.css|static';
```

### Media

Setting the CSS media attribute:

```php
$GLOBALS['TL_CSS'][] = 'files/theme/css/print.css|print';
// → <link rel="stylesheet" href="…" media="print">
```

### Async

Loading JavaScript asynchronously:

```php
$GLOBALS['TL_JAVASCRIPT'][] = 'bundles/myextension/scripts.js|async';
```

### Version (cache busting)

```php
$cssTimestamp = filemtime($this->rootDir.'/bundles/myextension/frontend.css');
$GLOBALS['TL_CSS'][] = 'bundles/myextension/frontend.css|'.$cssTimestamp;
```

---

## Template helper functions (generateStyleTag etc.)

The `\Contao\Template` class provides static helper functions:

### generateStyleTag

```php
$GLOBALS['TL_HEAD'][] = \Contao\Template::generateStyleTag(
    'bundles/myextension/print.css',
    'print',
    null // mtime for cache busting
);
// → <link rel="stylesheet" href="…" media="print">
```

### generateInlineStyle

```php
$GLOBALS['TL_HEAD'][] = \Contao\Template::generateInlineStyle($this->generateCss());
// → <style>…</style>
```

### generateScriptTag

```php
$GLOBALS['TL_BODY'][] = \Contao\Template::generateScriptTag(
    'bundles/myextension/scripts.js',
    false,  // $async
    null,   // $mtime
    null,   // $hash (integrity)
    null,   // $crossorigin
    null    // $referrerpolicy
);
```

### generateInlineScript

```php
$GLOBALS['TL_BODY'][] = \Contao\Template::generateInlineScript($this->generateJavaScript());
// → <script>…</script>
```

### generateFeedTag

```php
$GLOBALS['TL_HEAD'][] = \Contao\Template::generateFeedTag(
    'share/myfeed.xml',
    'rss',
    'My Feed'
);
```

---

## Twig: including assets

### The `add` tag

```twig
{# Stylesheet #}
{% use "@Contao/component/_stylesheet.html.twig" %}

{% with {file: asset('styles.css')} %}
    {{ block('stylesheet_component') }}
{% endwith %}
```

### Lazy loading

```twig
{% use "@Contao/component/_stylesheet.html.twig" %}

{% with {file: asset('styles.css'), lazy: true} %}
    {{ block('stylesheet_component') }}
{% endwith %}
```

Renders:
```html
<link rel="preload" as="style" href="…" onload="this.onload=null;this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="…"></noscript>
```

---

## Symfony Asset Component

### Access in templates

**Twig:**
```twig
<script src="{{ asset('foobar.js', 'fooexample') }}"></script>
<script src="{{ asset('js/tablesort.min.js', 'contao-components/tablesort') }}"></script>
```

**PHP templates:**
```php
<script src="<?= $this->asset('foobar.js', 'fooexample') ?>"></script>
```

**Insert tags:**
```
<script src="{{asset::jquery.js::contao-components/jquery}}"></script>
```

### Asset resolution

**contao-components packages** use package versions for cache busting:
- Path: `assets/jquery/jquery.js`
- Access: `{{asset::jquery.js::contao-components/jquery}}`
- Generates: `jquery.js?v=1.1.0`

**Bundle assets** from `public/` or `src/Resources/public/`:
- Registered under the lower-cased short bundle name
- `FooExampleBundle` → `web/bundles/fooexample/`
- With `manifest.json`: uses the manifest version strategy (Webpack Encore)

---

*Source: https://docs.contao.org/5.x/dev/framework/asset-management/*
