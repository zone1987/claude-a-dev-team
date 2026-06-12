# Contao 5 — Twig-Template-System

## Übersicht

Contao verwendet seit Version 4.12 nativ das **Twig-Template-System** von Symfony.
In Contao 5 sind die meisten Content Elements ausschließlich Twig-basiert.
PHP-Templates (Legacy) werden in Contao 5 noch unterstützt, ab Contao 6 entfallen sie.

---

## Getting Started: Twig-Grundlagen

### Kernsyntax

```twig
{# Variablenausgabe #}
{{ name }}

{# Kontrollstrukturen #}
{% for item in items %}
    <li>{{ item }}</li>
{% endfor %}

{# Filter #}
{{ age|round }}
{{ text|capitalize }}

{# String-Verkettung #}
{{ firstName ~ ' ' ~ lastName }}

{# Kommentare #}
{# Dies ist ein Kommentar #}
```

### Twig-Extensions installieren

```bash
composer require twig/intl-extra
```

```twig
{{ '1000000'|format_currency('EUR') }}
{# €1,000,000.00 #}
```

### Custom Twig-Filter erstellen

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

## Architektur: ContaoFilesystemLoader

### Namespaces

Twig-Templates werden über **Namespaces** (mit `@`-Präfix) identifiziert:

```
$twig->render("@Foo/bar/baz.html.twig", $params);
```

### Managed Namespace `@Contao`

Der **Managed Namespace** ist Contaos Kernmechanismus: Mehrere Bundles können
dasselbe Template unabhängig voneinander erweitern, ohne sich gegenseitig zu kennen.

Der `ContaoFilesystemLoader` ordnet Templates diesen Namespaces zu:

| Verzeichnis | Namespace | Priorität |
|-------------|-----------|-----------|
| Bundle-Template-Verzeichnis: `/vendor/foo/bar/src/Resources/contao/templates` | `@Contao_FooBarBundle` | 1 |
| App-Template-Verzeichnis: `/contao/templates`, `/src/Resources/contao/templates` | `@Contao_App` | 2 |
| Globales Template-Verzeichnis: `/templates` | `@Contao_Global` | 3 |
| Theme-Verzeichnisse: `/templates/<theme>` | `@Contao_Theme_<theme>` | 4 |

### Template-Vererbungshierarchie

Beim Kompilieren ersetzt Contao `@Contao`-Referenzen in `extends`, `include`, `embed`
und `use`-Tags durch den jeweiligen Bundle-Namespace:

```twig
{% extends "@Contao/content_element/text.html.twig" %}
{# wird zu: #}
{% extends "@Contao_ContaoCoreBundle/content_element/text.html.twig" %}
```

Dadurch entsteht eine Vererbungskette, in der alle Bundles unabhängig voneinander
denselben Template-Slot belegen können.

**Debug-Befehl:** `debug:contao-twig` zeigt die gesamte Hierarchie an.

### Bundle-Template-Pfad konfigurieren

Ab Symfony 6.1 (AbstractBundle):
```php
class FooBarBundle extends AbstractBundle
{
    // Pfad wird automatisch erkannt
}
```

Für ältere Versionen (Bundle-Klasse):
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

## Naming & Struktur

### Twig Root

Das oberste Template-Verzeichnis ist der **Twig-Root** — alle Unterverzeichnisse
gehören zum Template-Namen.

```
templates/          ← Twig root
├── content_element/
│   ├── text.html.twig        → "content_element/text"
│   └── image.html.twig       → "content_element/image"
└── frontend_module/
    └── news_list.html.twig   → "frontend_module/news_list"
```

### `.twig-root` Marker (für Bundles)

In Bundles wird der Twig-Root via `.twig-root`-Datei markiert:

```
vendor/…/FooBundle/contao/templates/
├── bar/
│   └── baz.html.twig          → "@Contao/baz.html.twig" (legacy ohne Verzeichnis)
└── my_root/
    ├── .twig-root             ← Marker
    └── content_element/
        └── foobar.html.twig   → "@Contao/content_element/foobar.html.twig"
```

### Standard-Verzeichnisse

| Kategorie | Verzeichnis | Beispiel |
|-----------|-------------|---------|
| Wiederverwendbare Komponenten | `component/` | `component/_list.html.twig` |
| Content Elements | `content_element/` | `content_element/gallery.html.twig` |
| Frontend-Module | `frontend_module/` | `frontend_module/feed_reader.html.twig` |
| Backend-Elemente | `backend/` | `backend/module_wildcard.html.twig` |

### Namenskonventionen

- `snake_case` für alle Namen
- Dateiendung inkludieren: `name.html.twig` oder `name.svg.twig`
- Keine doppelten Verzeichnisnamen in Dateinamen
- Partielle Templates mit `_`-Präfix (nur intern verwenden)

---

## Variant Templates

Variant-Templates sind spezialisierte Versionen eines Basis-Templates, die
Redakteure pro Element auswählen können.

**Beispiel:** Highlight-Variante für `content_element/text.html.twig`:

```twig
{# templates/content_element/text/highlight.html.twig #}
{% extends "@Contao/content_element/text.html.twig" %}

{% block text %}
    <div style="border: 5px solid red; padding: 1em;">{{ parent() }}</div>
{% endblock %}
```

Variants liegen in einem Unterverzeichnis, das nach dem Basis-Template benannt ist
(ohne Dateiendung). Sie erscheinen automatisch im Backend-Dropdown.

### Template Finder

```php
// Factory via DI injizieren
$finder = $this->finderFactory->create();

$finder = $finder
    ->identifier('content_element/text')
    ->extension('html.twig')
    ->withVariants()
;

// Für DCA-Listener:
$options = $finder->asTemplateOptions();
```

---

## Templates erstellen

### Extends (Vererbung)

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
        Angepasster Inhalt
    {% endblock %}
{% endembed %}
```

### Horizontal Reuse (`use`)

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

### Contao Components

Komponenten sind wiederverwendbare Template-Logik für den `{% use %}`-Import.
Konventionen:
- In einem einzelnen Block namens `<name>_component` eingehüllt
- Im `component/`-Verzeichnis gespeichert

---

## Output Encoding

Twig implementiert **Output-Encoding** (sicherer als Contaos historisches Input-Encoding):

```twig
{# HTML-Kontext (automatisch) #}
{{ color }}

{# Explizite CSS-Kodierung #}
<style>.box { background: {{ color|e('css') }} }</style>

{# HTML-Kontext #}
<div class="box">{{ color|e('html') }}</div>
```

### Rohausgabe (Vorsicht!)

```twig
{# NUR für vertrauenswürdige HTML-Inhalte (z.B. TinyMCE-Ausgabe) #}
{{ my_content|raw }}
```

**Warnung:** `|raw` auf unvertrauenswürdige Daten führt zu schwerwiegenden
XSS-Sicherheitslücken!

### Double-Encoding verhindern

Contao verwendet eigene `contao_html`- und `contao_html_attr`-Escaper, die
`htmlspecialchars(double_encode: false)` nutzen. Gelten nur für `@Contao`-Namespaces.

Ab Contao 5.3.19/5.4.7: Double-Encoding explizit einschalten wenn nötig:
```twig
{{ my_data|e('html', double_encode = true) }}
```

---

## Debugging

### PhpStorm: ide-twig.json

In Entwicklungsumgebungen erstellt `ContaoFilesystemLoaderWarmer` eine `var/ide-twig.json`
für Template-Autocompletion und Navigation.

### debug:contao-twig Befehl

```bash
bin/console debug:contao-twig
bin/console debug:contao-twig --theme my_theme
bin/console debug:contao-twig content_element/te
bin/console debug:contao-twig content_element/text --tree
```

`--tree` zeigt Ergebnisse hierarchisch an. `--theme <slug>` inkludiert Theme-Templates.

### Dump in Templates

```twig
{# Alles dumpen #}
{{ dump() }}

{# Bestimmte Variablen #}
{{ dump(a, b) }}

{# Via Tag (in Symfony Web Debug Toolbar) #}
{% dump a, b %}
```

**Sicherheitshinweis:** Nur in Entwicklungsumgebungen verwenden!

### Twig-Cache-Dateien

Kompilierte Templates in `var/cache/dev/twig/`. XDebug-Breakpoints setzbar.
Dateien via Kommentar `/* @Contao/<name>.html.twig */` finden.

---

## Legacy PHP-Templates

### Instanziierung

```php
use Contao\FrontendTemplate;

$template = new FrontendTemplate('my_front_end_template');
$template->someData = 'foobar';
$buffer = $template->parse();
```

### Template-Ordner (Suchreihenfolge)

1. `templates/<THEME>/` — Theme-spezifische Überschreibungen
2. `templates/` — Eigene Überschreibungen
3. `contao/templates/` — Anwendungs-spezifische Templates
4. `<BUNDLE>/contao/templates/` — Bundle-Templates

### Template-Vererbung (Legacy PHP)

```php
<?php $this->block('head'); ?>
    <?php $this->parent(); ?>
    <style>.thing { color: orange; }</style>
<?php $this->endblock(); ?>
```

Child-Template:
```php
<?php $this->extend('fe_page'); ?>

<?php $this->block('head'); ?>
    <?php $this->parent(); ?>
    <link rel="stylesheet" href="style_2.css">
<?php $this->endblock(); ?>
```

### Template-Daten setzen

```php
$template->foobar = 'foobar';
// oder:
$template->setData([
    'myVariable' => 'foobar',
    'myOtherVariable' => 'Lorem Ipsum',
]);
```

### Lazy-Variablen (Performance)

```php
// Wird nur ausgeführt wenn $template->foo in template benutzt wird:
$template->foo = function(): string {
    return expensiveOperation();
};

// Einmalig ausführen und cachen:
$template->foo = Template::once(function(): string {
    return expensiveOperation();
});
```

### Legacy-Templates in Twig überschreiben/erweitern

Twig-Template mit gleichem Namen erstellen (`.html.twig` statt `.html5`):

```twig
{# templates/fe_page.html.twig #}
{% extends "@Contao/fe_page.html5" %}

{% block head %}
    {{ parent() }}
    <style>.thing { color: orange; }</style>
{% endblock %}
```

---

## Quick Reference: Häufige Aufgaben

### Dynamischer Template-Name

```php
protected function getResponse(FragmentTemplate $template, ContentModel $model, Request $request): Response
{
    $template->setName('content_element/custom_name');
    return $template->getResponse();
}
```

### Base Template mit Custom Attributen

```twig
{# content_element/_base.html.twig erweitern #}
{% extends "@Contao/content_element/_base.html.twig" %}

{% block attributes %}
    {{ parent() }}
    data-element="{{ model.id }}"
{% endblock %}
```

### HTML-Attribute via attrs()

```twig
<div {{ attrs()
    .set('class', 'my-class')
    .set('id', 'el-' ~ element.id)
    .setIfExists('data-foo', foo)
}}>
```

### Bild/Figure rendern

```twig
{% set figure = figure(model.singleSRC, {width: 800}) %}
{% if figure %}
    {{ figure.build()|render }}
{% endif %}
```

### Translations

```twig
{{ 'MSC.goBack'|trans({}, 'contao_default') }}

{# Trans-Tag mit Default-Domain #}
{% trans_default_domain 'contao_default' %}
{{ 'MSC.goBack'|trans }}
```

---

## Versions-Kompatibilität

| Contao-Version | Status |
|----------------|--------|
| 5.x | Twig Standard, PHP-Templates noch supportet |
| 4.13 LTS | Twig nativ seit 4.12; Directory-Struktur supported |
| 4.9 LTS | Kein natives Twig; nicht mehr unterstützt |

**Für Contao 4.13 + 5 gleichzeitig:**

```php
// Template explizit angeben für neue Verzeichnisstruktur:
#[AsContentElement(category: 'bar', template: 'content_element/foo')]
class FooController extends AbstractContentElement { ... }
```

---

*Quelle: https://docs.contao.org/5.x/dev/framework/templates/*  
*https://docs.contao.org/5.x/dev/framework/templates/getting-started/*  
*https://docs.contao.org/5.x/dev/framework/templates/architecture/*  
*https://docs.contao.org/5.x/dev/framework/templates/creating-templates/*  
*https://docs.contao.org/5.x/dev/framework/templates/debugging/*  
*https://docs.contao.org/5.x/dev/framework/templates/legacy/*  
*https://docs.contao.org/5.x/dev/framework/templates/quick-reference/*
