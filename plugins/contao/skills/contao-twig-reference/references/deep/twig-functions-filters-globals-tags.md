# Contao 5.x Twig-Referenz — Funktionen, Filter, Globals, Tags

Contao erweitert Twig um eigene Funktionen, Filter, Globals und Tags zusätzlich zu [Twigs eigenen](https://twig.symfony.com/doc/3.x/#reference).

---

## 1. Twig-Funktionen

### add_schema_org

Fügt JSON-LD-Metadaten zur aktuellen Seite hinzu.

```twig
{% do add_schema_org({
    '@type': 'Event',
    'identifier': '#/schema/events/' ~ id,
    'name': title,
    'startDate': startTime|date('Y-m-d\TH:i:sP'),
}) %}

{# Metadaten aus FilesystemItem #}
{% do add_schema_org(file.schemaOrgData|default) %}

{# Metadaten aus Figure #}
{% do add_schema_org(figure.schemaOrgData|default) %}
```

**Parameter:** `array $jsonLd` — Array mit JSON-LD-Metadaten  
**Rückgabe:** `void` (via `{% do %}`)

---

### attrs()

Fluente Verwaltung von HTML-Attributen über die `HtmlAttributes`-Klasse.

```twig
{# CSS-Klassen #}
{% set el = attrs().addClass('my-div').addClass(cssClasses|default([])) %}
<div{{ el }}>…</div>

{# Klassen entfernen #}
{{ attrs().removeClass('foo') }}

{# Bedingt hinzufügen #}
{{ attrs().addClass('admin', isAdmin) }}

{# Stile #}
{{ attrs().addStyle('color: red') }}
{{ attrs().addStyle({'color': 'red', 'margin': '1em'}) }}
{{ attrs().removeStyle('color') }}

{# Attribute setzen #}
{{ attrs().set('id', 'my-id') }}
{{ attrs().unset('id') }}
{{ attrs().set('disabled', true, isDisabled) }}
{{ attrs().setIfExists('title', maybeTitle) }}

{# Zusammenführen #}
{{ attrs().mergeWith('disabled hidden') }}
{{ attrs().mergeWith({'aria-label': 'Close'}) }}
```

**Komplettes Beispiel:**
```twig
<button{{ attrs()
    .addClass(['btn', 'btn-primary'])
    .set('disabled', true, not isActive)
    .set('type', 'submit') }}>
    Speichern
</button>
```

---

### backend_icon() (ab 5.5)

Rendert ein Icon im Backend.

```twig
{{ backend_icon('edit.svg', 'Datensatz bearbeiten') }}
{{ backend_icon('edit.svg', 'Edit', attrs().addClass('icon-sm')) }}
```

**Parameter:**
1. `string $icon` — Icon-Dateiname
2. `string $alt` — Alt-Text für `<img>`
3. `HtmlAttributes $attributes` (optional) — Zusätzliche HTML-Attribute auf `<img>`

---

### contao_figure() [DEPRECATED]

Rendert eine Abbildung für Bildverarbeitung. **Veraltet — wird in Contao 6 entfernt.** Stattdessen `figure()` mit `component/_figure.html.twig` verwenden.

**Parameter:**
1. `mixed $from` — `FilesModel`, `FilesystemItem`, `ImageInterface`, UUID/ID/Pfad
2. `mixed $size` — Bildgrößenkonfiguration
3. `array $configuration` — Zusätzliche `FigureBuilder`-Einstellungen
4. `string $template` (optional) — Eigenes Template

---

### contao_section()

Rendert einen Layout-Abschnitt.

```twig
{{ contao_section('main') }}
{{ contao_section('left', 'block_section_custom') }}
```

**Parameter:**
1. `string $key` — Layout-Abschnitts-ID
2. `string $template` (optional) — Eigenes Template (Standard: `block_section`)

---

### contao_sections()

Rendert benutzerdefinierte Layout-Abschnitte einer bestimmten Position.

```twig
{{ contao_sections('top') }}
{{ contao_sections('bottom', 'block_sections_custom') }}
```

**Parameter:**
1. `string $key` — Position des benutzerdefinierten Abschnitts
2. `string $template` (optional) — Eigenes Template (Standard: `block_sections`)

---

### content_element() (ab 5.2)

Rendert ein Inhaltselement per Datenbankreferenz oder dynamisch.

```twig
{# Nach ID #}
{{ content_element(8472) }}

{# Konfiguration überschreiben #}
{{ content_element(5618, { perRow: 4 }) }}

{# Dynamisch erstellen #}
{{ content_element('text', { text: '<p>Hello World!</p>' }) }}

{# Via Fragment-Referenz #}
{{ content_element(fragment_reference) }}
```

**Parameter:**
- `int|string|FragmentReference $typeOrId` — Typ, Datenbank-ID oder Fragment-Referenz
- `array $data` (optional) — Daten/Konfigurationsüberschreibungen

---

### content_url() (ab 5.3)

Generiert die URL für ein Model-Objekt (wie Symfonys `path()`).

```twig
{% for item in items %}
    <a href="{{ content_url(item) }}">{{ item.title }}</a>
{% endfor %}

{# Mit Parametern #}
{{ content_url(pageModel, {foo: 'bar'}) }}

{# Relativer Pfad statt absoluter URL #}
{{ content_url(item, [], true) }}
```

**Parameter:**
- `Model $content` — Contao-Model
- `array $parameters` (optional) — URL-Parameter
- `bool $relative` (optional) — `true` für absoluten Pfad statt absoluter URL

---

### csp_hash() (ab 5.3)

Fügt CSP-Hashes für Inline-Styles und -Skripte hinzu.

```twig
{# Inline-JavaScript absichern #}
{% set script %}
    alert('foo');
{% endset %}
<script>{{ script }}</script>
{% do csp_hash('script-src', script) %}

{# Inline-Style absichern #}
{% set style %}
    body { background-color: magenta; }
{% endset %}
<style>{{ style }}</style>
{% do csp_hash('style-src', style) %}
```

**Parameter:**
1. `string $directive` — CSP-Direktive
2. `string $source` — Zu hashender Inhalt
3. `string $algorithm` (optional) — Hash-Algorithmus (Standard: `sha256`)

---

### csp_nonce() (ab 5.3)

Fügt CSP-Nonces für Inline-Styles und -Skripte hinzu.

```twig
<script{{ attrs().setIfExists('nonce', csp_nonce('script-src')) }}>
    alert('foo');
</script>

<style{{ attrs().setIfExists('nonce', csp_nonce('style-src')) }}>
    body { background-color: magenta; }
</style>
```

**Parameter:** `string $directive` — CSP-Direktive  
**Rückgabe:** `string|null` (Nonce-Wert)

---

### csp_source() (ab 5.3)

Fügt eine Quelle für eine CSP-Direktive hinzu. Nützlich für iframes und externe Medien.

```twig
{# Für iframes #}
{% set source = 'https://example.com/foobar' %}
{% do csp_source('frame-src', source) %}
<iframe src="{{ source }}">

{# Für Video-Elemente #}
{% set source = 'https://example.com/foobar.mp4' %}
{% do csp_source('media-src', source) %}
<video controls><source src="{{ source }}"></video>

{# Mehrere Direktiven #}
{% do csp_source(['frame-src', 'media-src'], source) %}
```

**Parameter:**
- `string|array $directive` — CSP-Direktive(n)
- `string $source` — Quell-URL

---

### figure()

Erstellt ein Figure-Objekt für Bildverarbeitung via Contao Image Studio.

```twig
{% use "@Contao/component/_figure.html.twig" %}

{% set image = figure('files/foo/bar.jpg', [1280, 720, 'crop']) %}

{% if image %}
    {% with {figure: image} %}{{ block('figure_component') }}{% endwith %}
{% endif %}
```

**Erweiterte Konfiguration:**
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

**Auf Bilddaten zugreifen:**
```twig
{% set resizedPath = figure(id, '_my_size').image.img.src %}
{% set originalPath = figure(id, '_my_size').image.filePath %}
```

**Parameter:**
- `mixed $from` — `FilesModel`, `FilesystemItem`, `ImageInterface`, UUID/ID/Pfad
- `mixed $size` — Bildgrößenkonfiguration, Referenz oder Size-Array
- `array $configuration` (optional) — `FigureBuilder`-Einstellungen

**Rückgabe:** `Figure|null`

---

### file_icon() (ab 5.7)

Rendert ein Icon basierend auf dem Dateityp im Backend.

```twig
{{ file_icon(download.file, 'Download', attrs().addClass('file-icon')) }}
```

**Parameter:**
1. `FilesystemItem $item` — Dateisystem-Element
2. `string $alt` (optional) — Alt-Text
3. `HtmlAttributes $attributes` (optional) — Zusätzliche HTML-Attribute

---

### frontend_module() (ab 5.2)

Rendert ein Frontend-Modul per Datenbankreferenz oder dynamisch.

```twig
{# Nach ID #}
{{ frontend_module(1701) }}

{# Konfiguration überschreiben #}
{{ frontend_module(1864, { hardLimit: 0 }) }}

{# Dynamisch #}
{{ frontend_module('newslist', {
    news_archives: [1, 2],
    news_template: 'news_latest',
    news_order: 'order_date_desc',
    numberOfItems: 10,
    imgSize: [0, 0, '_news_list'],
}) }}

{# Via Fragment-Referenz #}
{{ frontend_module(fragment_reference) }}
```

**Parameter:**
- `int|string|FragmentReference $typeOrId` — Typ, Datenbank-ID oder Fragment-Referenz
- `array $data` (optional) — Konfiguration/Überschreibungen

---

### include()

Contao überschreibt Twigs Standard-Include-Funktion um die Contao-Template-Hierarchie zu unterstützen.

---

### insert_tag()

Rendert ein Insert-Tag direkt.

```twig
<a href="{{ insert_tag('link_url::10') }}">{{ insert_tag('link_title::10') }}</a>
<p>{{ insert_tag('insert_article::123')|raw }}</p>
```

**Parameter:** `string $insertTag` — Insert-Tag ohne geschweifte Klammern  
**Rückgabe:** `string`

---

### picture_config()

Erstellt eine Bildkonfiguration zur Laufzeit (ohne `contao.image.sizes` in config).

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

**Parameter:** `array $config` — Konfiguration entspricht `contao.image.sizes` Bundle-Konfiguration  
**Rückgabe:** `PictureConfiguration`

---

### prefix_url()

Prefixiert relative URLs mit dem Basispfad (Ersatz für `<base href="…">`).

```twig
<a href="{{ prefix_url(userGeneratedUrl|insert_tag) }}">Link</a>
```

**Parameter:** `string $url` — Relative URL  
**Rückgabe:** `string` (pfad-absolute URL)

---

## 2. Twig-Filter

### csp_inline_styles (ab 5.3)

Extrahiert alle Inline-CSS-Style-Attribute eines HTML-Strings und fügt automatisch CSP-Hashes hinzu.

```twig
{{ some_html|csp_inline_styles|raw }}
```

Konfiguration erlaubter Stile: `contao.csp.allowed_inline_styles`.

---

### csp_unsafe_inline_style (ab 5.3.2)

Fügt CSP-Hash für einen Inline-Style hinzu und fügt automatisch `'unsafe-hashes'` zur Direktive hinzu.

**Warnung:** Nur vertrauenswürdige Stile übergeben!

```twig
<div style="{{ 'color: red'|csp_unsafe_inline_style }}">

<div{{ attrs().addStyle({ color: 'red' })|csp_unsafe_inline_style }}>
```

---

### deserialize (ab 5.3.8)

Deserialisiert einen String mit serialisierten Daten in ein Array. Intern: `Contao\StringUtil::deserialize()`.

```twig
{% set data = 'a:2:{i:0;s:3:"Foo";i:1;s:3:"Bar";}'|deserialize %}
{# data = ["Foo", "Bar"] #}

{{ (bar|deserialize).foo }}
```

---

### encode_email (ab 5.2)

Kodiert eine E-Mail-Adresse mit HTML-Entities. Intern: `Contao\StringUtil::encodeEmail()`.

```twig
{{ 'foobar@example.com'|encode_email }}
```

---

### escape

Contao überschreibt Twigs Standard-Escape-Filter um `ChunkedText` aus Insert-Tags zu unterstützen und verhindert Doppel-Kodierung.

```twig
{# Standard — kein Doppel-Encoding #}
{{ '&gt;'|e }}  {# Ausgabe: &gt; #}

{# Doppel-Encoding erzwingen #}
{{ '&gt;'|e('html', double_encode = true) }}
```

```twig
{# Selektives Escaping: Nur Text außerhalb von Insert-Tags #}
{{ text|insert_tag_raw|escape('html') }}
```

---

### format_bytes

Konvertiert Bytes in ein lesbares Format.

```twig
{{ 134217728|format_bytes }}         {# "128.0 MiB" #}
{{ 135000000|format_bytes }}         {# "128.7 MiB" #}
{{ 135000000|format_bytes(2) }}      {# "128.75 MiB" #}
{{ 135000000|format_bytes(3) }}      {# "128.746 MiB" #}
```

**Parameter:** `int $decimalPlaces` (optional, Standard: `1`)

---

### highlight

Syntax-Highlighting via highlight.php.

```twig
{% set highlighted = code|highlight('php') %}
{% set code_attributes = attrs()
    .addClass('hljs')
    .addClass(highlighted.language) %}
<pre><code{{ code_attributes }}>
    {{- highlighted.value|raw -}}
</code></pre>

{# Kurzform via __toString() #}
<pre><code>{{ code|highlight('php')|raw }}</code></pre>
```

**Parameter:** `string $language` (optional, Standard: `plaintext`)  
**Rückgabe:** `HighlightResult` mit `.language` und `.value`

---

### highlight_auto

Automatisches Syntax-Highlighting via highlight.php (Sprache wird auto-erkannt).

```twig
{% set highlighted = code|highlight_auto %}
<pre><code class="hljs {{ highlighted.language }}">
    {{- highlighted.value|raw -}}
</code></pre>

{# Sprachen einschränken #}
<pre><code>{{ code|highlight_auto(['C', 'C#', 'C++']) }}</code></pre>
```

**Rückgabe:** `HighlightResult` (wie `highlight`)

---

### insert_tag

Ersetzt Insert-Tags für Text-Ausgabe (nicht-HTML, z. B. in HTML-Attributen).

```twig
{{ '{{date::Y}}'|insert_tag }}           {# "1970" #}
{{ '{{fragment::{{date::Y}}}}'|insert_tag }}  {# "1970" (kein ESI-Tag) #}
```

---

### insert_tag_raw

Ersetzt Insert-Tags für HTML-Ausgabe.

```twig
{{ '{{date::Y}}'|insert_tag_raw }}           {# "1970" #}
{{ '{{fragment::{{date::Y}}}}'|insert_tag_raw }}  {# <esi:include ...></esi:include> #}

{# Escaping: HTML-Tags außerhalb = escaped, Insert-Tag-Output = nicht escaped #}
{{ '<span> foo {{br}} bar </span>'|insert_tag_raw }}
{# Ausgabe: &lt;span&gt; foo <br> bar &lt;/span&gt; #}
```

---

### sanitize_html (ab 5.1)

Bereinigt HTML-Code mit einem konfigurierten Symfony-Sanitizer.

```twig
{# Standard-Sanitizer — für externen HTML-Code #}
{{ '<div title=test style=color:red onclick=alert(1)><script>alert(2)</script>{{date::Y}}'|sanitize_html }}
{# Ausgabe: <div title="test">&#123;&#123;date::Y&#125;&#125;</div> #}

{# Contao-Sanitizer (ab 5.7) — für HTML aus dem Contao-Backend (TinyMCE) #}
{{ html_from_backend|sanitize_html('contao') }}
```

---

## 3. Twig-Globals

### contao (ab 5.3)

Das `contao` Twig-Global bietet Zugang zu nützlichen Funktionen und Eigenschaften.

```twig
{# Aktuelle Seite (PageModel) #}
{{ contao.page.title }}
{% set page = contao.page %}

{# Backend-Benutzer in Frontend-Session vorhanden? #}
{% if contao.has_backend_user %}…{% endif %}

{# Vorschau-Modus (versteckte Elemente anzeigen) aktiv? #}
{% if contao.is_preview_mode %}…{% endif %}

{# Request-Token für Formulare #}
{{ contao.request_token }}

{# Backend-Benutzer im Frontend (falls vorhanden) #}
{% set user = contao.backend_user.username|default %}
```

**Eigenschaften:**

| Eigenschaft | Typ | Beschreibung |
|-------------|-----|--------------|
| `contao.page` | `PageModel\|null` | Aktuelles PageModel |
| `contao.has_backend_user` | `bool` | Backend-Benutzer in Session vorhanden |
| `contao.is_preview_mode` | `bool` | Vorschau-Modus aktiv |
| `contao.request_token` | `string` | CSRF-Request-Token |
| `contao.backend_user` | `BackendUser\|null` | Backend-Benutzer (falls vorhanden) |

---

## 4. Twig-Tags

### {% add %}

Fügt Ausgabe zu verschiedenen Abschnitten des Dokuments hinzu.

**Unterstützte Positionen:**
- `head` — Ende des `<head>`-Bereichs
- `stylesheets` — Mit anderen Stylesheets gruppiert
- `body` — Ende des `<body>`-Bereichs

```twig
{# Skript zum head hinzufügen #}
{% add "my-analytics" to head %}
    <script>/* Analytics Code */</script>
{% endadd %}

{# Stylesheet hinzufügen #}
{% add "my-styles" to stylesheets %}
    <link rel="stylesheet" href="{{ asset('css/custom.css') }}">
{% endadd %}

{# Body-Skript mit benanntem Node (überschreibbar) #}
{% add "tracking-script" to body %}
    <script src="{{ asset('js/tracking.js') }}"></script>
{% endadd %}
```

---

### {% slot %} (ab 5.6)

Definiert Layout-Abschnitte für zusammengesetzten Content. Slots können in Seiten-Layouts Inhaltselemente oder Module aufnehmen.

```twig
{# Einfacher Slot #}
{% slot main %}{% endslot %}

{# Slot mit Wrapper (nur wenn nicht leer) #}
{% slot main %}
    <main>{{ slot() }}</main>
{% endslot %}

{# Slot mit Fallback-Inhalt #}
{% slot main %}
    […]
{% else %}
    Dieser Inhalt wird angezeigt wenn der Slot leer ist.
{% endslot %}
```

**Slot-Inhalt setzen (PHP):**
```php
/** @var \Contao\CoreBundle\Twig\LayoutTemplate $template */
$template->setSlot('main', 'Vertrauenswürdiger Inhalt für den <b>main</b>-Block.');
```

---

## 5. Contao Twig-Komponenten

Komponenten sind wiederverwendbare Template-Blöcke, die per `{% use %}` importiert und mit `block()` gerendert werden.

```twig
{# _figure.html.twig Komponente verwenden #}
{% use "@Contao/component/_figure.html.twig" %}

{% set image = figure('files/foo/bar.jpg', [800, 600, 'crop']) %}
{% if image %}
    {% with {figure: image} %}{{ block('figure_component') }}{% endwith %}
{% endif %}
```

**Komponente anpassen:**
```twig
{% use "@Contao/component/_picture.html.twig" %}
{% block image %}
    {% set img_attributes = attrs().addClass('my-image').mergeWith(img_attributes|default) %}
    <div>{{ parent() }}</div>
{% endblock %}
```

**Verfügbare Kernkomponenten** (unter `@Contao/component/`):
- `_figure.html.twig` — Abbildung mit Bild + Bildunterschrift
- `_picture.html.twig` — Responsives Bild
- `_image.html.twig` — Einfaches Bild

---

*Quellen:*
- https://docs.contao.org/5.x/dev/reference/twig/
- https://docs.contao.org/5.x/dev/reference/twig/functions/
- https://docs.contao.org/5.x/dev/reference/twig/filters/
- https://docs.contao.org/5.x/dev/reference/twig/globals/
- https://docs.contao.org/5.x/dev/reference/twig/tags/
- https://docs.contao.org/5.x/dev/reference/twig/tags/add/
- https://docs.contao.org/5.x/dev/reference/twig/tags/slot/
