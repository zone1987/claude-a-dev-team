# Contao 5 — Getting Started

## Übersicht

Contao ist ein Open-Source-CMS, das als Symfony-Bundle implementiert ist und sich in
bestehende Symfony-Anwendungen integrieren oder als eigenständige Managed Edition
betrieben werden kann. Dieser Abschnitt deckt den Einstieg für neue Entwickler ab.

---

## Verzeichnisstruktur (Managed Edition)

Nach der Installation via `composer create-project contao/managed-edition` enthält
das Projekt folgende Kernverzeichnisse:

| Verzeichnis | Zweck |
|-------------|-------|
| `assets/` | Framework- und Drittanbieter-JS/CSS |
| `config/` | Anwendungskonfiguration |
| `files/` | Vom Contao-Dateimanager verwaltete Dateien |
| `public/` | Öffentliche Einstiegspunkte, Symlinks zu Ressourcen |
| `system/` | Legacy-Kompatibilitätsordner (Contao 3) |
| `templates/` | Eigene Contao- und Twig-Templates |
| `var/` | Transiente Dateien (Cache, Logs) |
| `vendor/` | Composer-Abhängigkeiten inklusive Contao |

### Verzeichnisse für die eigene Entwicklung

| Verzeichnis | Zweck |
|-------------|-------|
| `config/` | Anwendungskonfiguration |
| `contao/` | Contao-spezifische Konfiguration, DCAs, Translations |
| `src/` | Eigener PHP-Code (Controller, Event Listener, Services) |
| `templates/` | Eigene und überschriebene Templates |
| `translations/` | Symfony Translations (ab Version 5.3) |

---

## Konfigurationsdateien

### `config/`-Verzeichnis

| Datei | Zweck |
|-------|-------|
| `.env` | Standard-Umgebungsvariablen (wird committet) |
| `.env.local` | Umgebungs-spezifische Überschreibungen (in `.gitignore`) |
| `config.yaml` | Bundle- und Extension-Konfiguration |
| `config_dev.yaml` | Entwicklungsumgebungs-Einstellungen |
| `config_prod.yaml` | Produktionsumgebungs-Einstellungen |
| `parameters.yaml` | Datenbank- und SMTP-Zugangsdaten |
| `routes.yaml` | Anwendungs-spezifische Routen |
| `services.yaml` | Service-Definitionen |

### `contao/`-Verzeichnis

| Datei/Verzeichnis | Zweck |
|-------------------|-------|
| `contao/config/config.php` | Registriert Module, Content Elements, Models, Hooks, Crons |
| `contao/dca/` | Data Container Array Anpassungen |
| `contao/languages/` | Übersetzungsdateien nach Sprache |
| `contao/languages/de/` | Deutsche Übersetzungen |
| `contao/languages/en/` | Englische Übersetzungen (Fallback) |

---

## Autoloading und Services

### PSR-4 Autoloading

In `composer.json` ist standardmäßig konfiguriert:

```json
{
    "autoload": {
        "psr-4": {
            "App\\": "src/"
        }
    }
}
```

### Service-Konfiguration (`config/services.yaml`)

```yaml
services:
    _defaults:
        autowire: true
        autoconfigure: true

    App\:
        resource: ../src
```

Mit `autowire: true` und `autoconfigure: true` werden Hooks, Callbacks und Content
Elements automatisch erkannt und registriert – kein manueller Tag-Eintrag notwendig.

**Achtung:** Klassen, die Legacy-Contao-Framework-Klassen erweitern, benötigen manuelle
Service-Registrierung, da sie nicht über Autoconfigure entdeckt werden.

### Routen-Konfiguration (`config/routes.yaml`)

```yaml
app.controller:
    resource: ../src/Controller
    type: attribute
```

---

## DCA-Basics (Einstieg)

DCA-Anpassungen gehören in `contao/dca/<tabellenname>.php`. Beispiel: Feld `location`
zu News-Einträgen hinzufügen:

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

**Wichtig:** Nach Änderungen an Contao-Konfigurationen muss der Symfony Application
Cache für die Produktionsumgebung neu gebaut werden. In der Entwicklungsumgebung
werden Änderungen sofort wirksam.

---

## Hooks-Überblick (Einstieg)

Hooks erlauben das Einschleusen eigener Logik in bestimmte Ausführungspunkte des Frameworks.
Registrierung über das `#[AsHook]`-Attribut:

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

Dependency Injection funktioniert in Hooks über den Constructor:

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

## Translations im Einstieg

Übersetzungen werden in `contao/languages/<sprache>/` abgelegt. Beispiel für
Änderung eines bestehenden Labels:

```php
// contao/languages/en/default.php
$GLOBALS['TL_LANG']['MSC']['more'] = 'more';
```

Ab Contao 5.3 ist auch das Symfony-Translations-Format mit `contao_`-Präfix möglich:

```yaml
# translations/contao_default.en.yaml
MSC:
    more: more
```

---

## Content Elements & Module (Einstieg)

Für ein einfaches Content Element werden benötigt:
1. Controller-Klasse (PHP)
2. DCA-Palette
3. Twig-Template

Kurzbeispiel:

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

Das `contao/maker-bundle` kann Dateien automatisch über `make:contao:content-element`
bzw. `make:contao:frontend-module` generieren.

---

## Weiterführende Skills

- `contao-initial-setup` — Managed Edition vs. Symfony Application, Installation
- `contao-core-concepts` — Alle Kernkonzepte im Überblick
- `contao-extension-bundle` — Bundle erstellen und veröffentlichen
- `contao-content-elements` — Vollständige Content-Element-Dokumentation
- `contao-templates` — Twig-Template-System

---

*Quelle: https://docs.contao.org/5.x/dev/getting-started/*  
*https://docs.contao.org/5.x/dev/getting-started/starting-development/*  
*https://docs.contao.org/5.x/dev/getting-started/dca/*  
*https://docs.contao.org/5.x/dev/getting-started/hooks/*  
*https://docs.contao.org/5.x/dev/getting-started/content-elements-modules/*  
*https://docs.contao.org/5.x/dev/getting-started/translations/*
