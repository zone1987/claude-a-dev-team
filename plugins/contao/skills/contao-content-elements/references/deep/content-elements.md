# Contao 5 — Content Elements

## Übersicht

Content Elements sind die fundamentalen Inhaltsbausteine in Contao. Sie sind als
Fragment-Controller implementiert, empfangen Daten über ein Content Model und
geben eine Response zurück, die in den Hauptinhalt gerendert wird.

---

## Grundbestandteile

Jedes Content Element besteht aus:

1. **Fragment-Controller** — Klasse, die `AbstractContentElementController` erweitert
2. **Service-Tag** `contao.content_element` mit:
   - **type**: Identifiziert das Template und die DCA-Palette (wird aus Klassenname abgeleitet)
   - **category**: Gruppiert Elemente in Dropdowns (Default: `miscellaneous`)
   - **template**: Optionaler Custom-Template-Pfad
3. **DCA-Palette** in `tl_content`
4. **Twig-Template** (`content_element/<type>.html.twig`)
5. **Translations** für Backend-Labels

---

## Minimale Implementierung

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

### DCA-Palette

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

## Service-Tag-Optionen

| Option | Typ | Beschreibung |
|--------|-----|-------------|
| `name` | string | Muss `contao.content_element` sein |
| `type` | string | Eigener Typ-Bezeichner (Pflicht bei Überschreibung) |
| `category` | string | Gruppiert das Element im Selektor |
| `template` | string | Überschreibt Standard-Template-Pfad |
| `renderer` | string | `inline`, `esi` oder `forward` (Standard) |
| `method` | string | Aufzurufende Controller-Methode |
| `nestedFragments` | bool/array | Aktiviert verschachtelte Kind-Elemente |

---

## Registrierungsmethoden

**Via PHP-Attribut (empfohlen):**
```php
#[AsContentElement(category: 'texts', template: 'content_element/my_element')]
```

**Via Annotation:**
```php
/** @ContentElement("my_element", category="texts") */
```

**Via YAML-Service-Tag:**
```yaml
# config/services.yaml
App\Controller\ContentElement\ExampleElementController:
    tags:
        - name: contao.content_element
          type: example_element
          category: texts
```

---

## PageModel-Zugriff

Innerhalb des Controllers steht die aktuelle Seite über `$this->getPageModel()`
zur Verfügung:

```php
protected function getResponse(FragmentTemplate $template, ContentModel $model, Request $request): Response
{
    $page = $this->getPageModel();
    // $page ist ein \Contao\PageModel-Objekt
    $template->set('pageTitle', $page->pageTitle);
    return $template->getResponse();
}
```

---

## Nested Fragments (ab Contao 5.3)

Nested Fragments erlauben es einem Parent-Element, Kind-Content-Elements zu enthalten.

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

## Wrapper-Elemente (Legacy)

Legacy-Wrapper-Elemente (start/stop/single/separator) werden in `$GLOBALS['TL_WRAPPERS']`
registriert:

```php
// contao/config/config.php
$GLOBALS['TL_WRAPPERS']['start'][] = 'my_start_element';
$GLOBALS['TL_WRAPPERS']['stop'][] = 'my_stop_element';
$GLOBALS['TL_WRAPPERS']['single'][] = 'my_single_element';
```

**Wichtig:** Backend-Ausgabe sollte sich von der Frontend-Ausgabe unterscheiden, um
Darstellungsprobleme zu vermeiden.

---

## Content Elements für eigene Tabellen

Content Elements lassen sich auch als Kind-Datensätze eigener Tabellen nutzen:

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

Backend-Modul:
```php
$GLOBALS['BE_MOD']['content']['example'] = [
    'tables' => ['tl_example', 'tl_content'],
];
```

Rendering im Frontend:
```php
use Contao\ContentModel;
use Contao\Controller;

$models = ContentModel::findPublishedByPidAndTable($recordId, 'tl_example');
foreach ($models as $model) {
    echo Controller::getContentElement($model);
}
```

**Performance-Tipp:** Anonyme Funktionen für Lazy-Evaluation nutzen — Content wird nur
bei tatsächlichem Zugriff aus der Datenbank geladen.

---

## Maker Bundle

Das `contao/maker-bundle` kann Dateien automatisch generieren:

```bash
bin/console make:contao:content-element
```

---

*Quelle: https://docs.contao.org/5.x/dev/framework/content-elements/*  
*https://docs.contao.org/5.x/dev/getting-started/content-elements-modules/*  
*https://docs.contao.org/5.x/dev/guides/using-content-elements/*
