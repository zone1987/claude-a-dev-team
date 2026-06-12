# Contao 5 — Front-End-Module

## Übersicht

Front-End-Module generieren dynamischen Inhalt für komplexe Funktionalitäten, die
auf mehreren Seiten geteilt werden. Beispiele: News-Listen, Navigationselemente,
Mitgliederformulare.

Sie funktionieren als Fragment-Controller, die in den Hauptinhalt rendern, und
werden ähnlich wie Content Elements erstellt.

---

## Grundbestandteile

1. **Fragment-Controller** — Klasse, die `AbstractFrontendModuleController` erweitert
2. **Service-Tag** `contao.frontend_module`
3. **DCA-Konfiguration** in `tl_module` (Palette)
4. **Twig-Template** — Namenskonvention: `frontend_module/<type>.html.twig`
5. **Translations** für Backend-Labels

---

## Implementierungsbeispiel

### Controller

```php
// src/Controller/FrontendModule/MyNewsListController.php
namespace App\Controller\FrontendModule;

use Contao\CoreBundle\Controller\FrontendModule\AbstractFrontendModuleController;
use Contao\CoreBundle\DependencyInjection\Attribute\AsFrontendModule;
use Contao\CoreBundle\Twig\FragmentTemplate;
use Contao\ModuleModel;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;

#[AsFrontendModule(category: 'news')]
class MyNewsListController extends AbstractFrontendModuleController
{
    protected function getResponse(FragmentTemplate $template, ModuleModel $model, Request $request): Response
    {
        $template->set('items', $this->loadNews($model));
        return $template->getResponse();
    }

    private function loadNews(ModuleModel $model): array
    {
        // Datenbankabfrage o. Ä.
        return [];
    }
}
```

### DCA-Palette

```php
// contao/dca/tl_module.php
$GLOBALS['TL_DCA']['tl_module']['palettes']['my_news_list'] = '
    {title_legend},name,headline,type;
    {config_legend},numberOfItems;
    {template_legend},customTpl;
    {protected_legend:hide},protected;
    {expert_legend:hide},guests,cssID;
';
```

### Template

```twig
{# templates/frontend_module/my_news_list.html.twig #}
{% extends "@Contao/frontend_module/_base.html.twig" %}

{% block content %}
    <ul>
        {% for item in items %}
            <li>{{ item.headline }}</li>
        {% endfor %}
    </ul>
{% endblock %}
```

### Translations

```yaml
# translations/contao_default.en.yaml
FMD:
    my_news_list:
        - My News List
        - Displays a list of news items.
```

---

## Service-Tag-Optionen

| Option | Typ | Zweck |
|--------|-----|-------|
| `type` | string | Identifiziert Template und DCA-Palette (optional) |
| `category` | string | Gruppiert das Modul im Typ-Dropdown |
| `template` | string | Überschreibt generierten Template-Namen |
| `renderer` | string | Standard: `forward`; auch `inline` oder `esi` möglich |
| `method` | string | Gibt die aufzurufende Controller-Methode an |

---

## Registrierungsmethoden

**Via PHP-Attribut (empfohlen):**
```php
#[AsFrontendModule(category: 'news', type: 'my_news_list')]
```

**Via YAML-Service-Tag:**
```yaml
App\Controller\FrontendModule\MyNewsListController:
    tags:
        - name: contao.frontend_module
          type: my_news_list
          category: news
```

---

## PageModel-Zugriff

Wie bei Content Elements steht die aktuelle Seite über `$this->getPageModel()` bereit:

```php
protected function getResponse(FragmentTemplate $template, ModuleModel $model, Request $request): Response
{
    $page = $this->getPageModel();
    $template->set('currentAlias', $page->alias);
    return $template->getResponse();
}
```

---

## Unterschied: Front-End-Modul vs. Content Element

| Aspekt | Front-End-Modul | Content Element |
|--------|----------------|-----------------|
| Tabelle | `tl_module` | `tl_content` |
| Basis-Klasse | `AbstractFrontendModuleController` | `AbstractContentElementController` |
| Model-Typ | `ModuleModel` | `ContentModel` |
| Attribut | `#[AsFrontendModule]` | `#[AsContentElement]` |
| Template-Pfad | `frontend_module/<type>` | `content_element/<type>` |
| Platzierung | Seitenlayout/Artikel-Module | Artikel (Inhaltsbereich) |

---

*Quelle: https://docs.contao.org/5.x/dev/framework/front-end-modules/*  
*https://docs.contao.org/5.x/dev/getting-started/content-elements-modules/*
