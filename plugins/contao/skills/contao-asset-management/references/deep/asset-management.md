# Contao 5 — Asset Management

## Übersicht

Contao verwendet globale Arrays zum Speichern von Asset-Referenzen während des
Seitenlayout-Aufbaus. Zusätzlich steht die Symfony Asset Component zur Verfügung.

---

## Globale Arrays

| Array | Beschreibung |
|-------|-------------|
| `$GLOBALS['TL_BODY']` | HTML-Code vor `</body>` |
| `$GLOBALS['TL_CSS']` | CSS-Asset-Pfade für `<head>` |
| `$GLOBALS['TL_HEAD']` | HTML-Code für `<head>` |
| `$GLOBALS['TL_JAVASCRIPT']` | JavaScript-Asset-Pfade für `<head>` |
| `$GLOBALS['TL_MOOTOOLS']` | HTML-Code vor `</body>` |

**Hinweis:** Im Backend funktionieren nur `TL_CSS`, `TL_JAVASCRIPT` und `TL_MOOTOOLS`.

---

## CSS & JavaScript Assets hinzufügen

```php
$GLOBALS['TL_CSS'][] = 'bundles/myextension/frontend.css';
$GLOBALS['TL_JAVASCRIPT'][] = 'bundles/myextension/scripts.js';
```

### Pipe-Optionen

Optionen werden mit `|` (Pipe) an den Dateipfad angehängt:

| Option | Beispiel | Beschreibung |
|--------|---------|-------------|
| Static | `\|static` | Asset kann mit anderen statischen Assets kombiniert werden |
| Media | `\|print` | CSS `media`-Attribut |
| Async | `\|async` | JavaScript `async`-Attribut |
| Version | `\|1` | Hängt `?v=…` Parameter an |

**Kombinations-Beispiele:**
```php
$GLOBALS['TL_CSS'][] = 'files/theme/css/print.css|print|static|1';
$GLOBALS['TL_JAVASCRIPT'][] = 'bundles/myextension/scripts.js|2|async|static';
```

### Static

Ermöglicht Kombination mit anderen statischen Assets (wenn im Seitenlayout aktiviert):

```php
$GLOBALS['TL_CSS'][] = 'bundles/myextension/frontend.css|static';
```

### Media

CSS-Media-Attribut setzen:

```php
$GLOBALS['TL_CSS'][] = 'files/theme/css/print.css|print';
// → <link rel="stylesheet" href="…" media="print">
```

### Async

JavaScript asynchron laden:

```php
$GLOBALS['TL_JAVASCRIPT'][] = 'bundles/myextension/scripts.js|async';
```

### Version (Cache-Busting)

```php
$cssTimestamp = filemtime($this->rootDir.'/bundles/myextension/frontend.css');
$GLOBALS['TL_CSS'][] = 'bundles/myextension/frontend.css|'.$cssTimestamp;
```

---

## Template-Hilfsfunktionen (generateStyleTag etc.)

Die `\Contao\Template`-Klasse bietet statische Hilfsfunktionen:

### generateStyleTag

```php
$GLOBALS['TL_HEAD'][] = \Contao\Template::generateStyleTag(
    'bundles/myextension/print.css',
    'print',
    null // mtime für Cache-Busting
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

## Twig: Assets einbinden

### `add`-Tag

```twig
{# Stylesheet #}
{% use "@Contao/component/_stylesheet.html.twig" %}

{% with {file: asset('styles.css')} %}
    {{ block('stylesheet_component') }}
{% endwith %}
```

### Lazy Loading

```twig
{% use "@Contao/component/_stylesheet.html.twig" %}

{% with {file: asset('styles.css'), lazy: true} %}
    {{ block('stylesheet_component') }}
{% endwith %}
```

Rendert:
```html
<link rel="preload" as="style" href="…" onload="this.onload=null;this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="…"></noscript>
```

---

## Symfony Asset Component

### Zugriff in Templates

**Twig:**
```twig
<script src="{{ asset('foobar.js', 'fooexample') }}"></script>
<script src="{{ asset('js/tablesort.min.js', 'contao-components/tablesort') }}"></script>
```

**PHP-Templates:**
```php
<script src="<?= $this->asset('foobar.js', 'fooexample') ?>"></script>
```

**Insert Tags:**
```
<script src="{{asset::jquery.js::contao-components/jquery}}"></script>
```

### Asset-Auflösung

**contao-components-Pakete** verwenden Paket-Versionen für Cache-Busting:
- Pfad: `assets/jquery/jquery.js`
- Zugriff: `{{asset::jquery.js::contao-components/jquery}}`
- Generiert: `jquery.js?v=1.1.0`

**Bundle-Assets** aus `public/` oder `src/Resources/public/`:
- Registriert unter Kleinschreibungs-Bundle-Kurzname
- `FooExampleBundle` → `web/bundles/fooexample/`
- Mit `manifest.json`: Verwendet Manifest-Version-Strategie (Webpack Encore)

---

*Quelle: https://docs.contao.org/5.x/dev/framework/asset-management/*
