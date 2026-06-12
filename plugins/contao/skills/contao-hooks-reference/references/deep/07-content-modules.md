# Contao Hooks – Content-Elemente / Frontend-Module

Hooks für das Rendern von Artikeln, Inhaltselementen, Frontend-Modulen und Formularen.

---

## `compileArticle`

**Zweck:** Wird ausgelöst, nachdem das Artikel-Modul kompiliert wurde. Ermöglicht Hinzufügen zusätzlicher Daten zum Template.

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `\Contao\FrontendTemplate` | `$template` | Frontend-Template des Artikel-Moduls |
| 2 | `array` | `$data` | Modul-Konfiguration als assoziatives Array |
| 3 | `\Contao\Module` | `$module` | Die aktuelle Modul-Instanz |

**Rückgabe:** `void`

**Zeitpunkt:** Nach Abschluss der Artikel-Modul-Kompilierung.

```php
#[AsHook('compileArticle')]
class CompileArticleListener
{
    public function __invoke(FrontendTemplate $template, array $data, Module $module): void
    {
        $template->customContent = '<p>Dieser Inhalt ist in mod_article.html5 über $this->customContent verfügbar</p>';
    }
}
```

---

## `getArticle`

**Zweck:** Erlaubt die Überschreibung der Artikel-Konfiguration **vor** dem Rendern.

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `\Contao\ArticleModel` | `$article` | DB-Ergebnis aus `tl_article` |

**Rückgabe:** `void`

**Zeitpunkt:** Vor dem Rendern eines Artikels.

```php
use Contao\ArticleModel;

#[AsHook('getArticle')]
class GetArticleListener
{
    public function __invoke(ArticleModel $article): void
    {
        // Artikel-Eigenschaften modifizieren
        $article->cssID = serialize(['', 'meine-klasse']);
    }
}
```

---

## `getArticles`

**Zweck:** Erlaubt das Ersetzen der Artikel einer Spalte durch eigene Inhalte.

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `int` | `$pageId` | Eltern-Seiten-ID der Artikel |
| 2 | `string` | `$column` | Die Spalte, für die Artikel gerendert werden |

**Rückgabe:** `string|null` – String mit eigenem Inhalt (verhindert weitere Hook-Ausführung), oder `null` für Standardverhalten.

**Zeitpunkt:** Beim Rendern von Artikeln einer Seiten-Spalte.

```php
#[AsHook('getArticles')]
class GetArticlesListener
{
    public function __invoke(int $pageId, string $column): string|null
    {
        if (42 === $pageId && 'main' === $column) {
            return '<div class="custom">Eigener Inhalt</div>';
        }
        return null;
    }
}
```

---

## `getContentElement`

**Zweck:** Wird ausgelöst, wenn ein Content-Element gerendert wird. Erlaubt Modifikation der gerenderten Ausgabe.

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `\Contao\ContentModel` | `$contentModel` | DB-Ergebnis aus `tl_content` |
| 2 | `string` | `$buffer` | Generierte Ausgabe des Content-Elements |
| 3 | `object` | `$element` | Instanz der Content-Element-Klasse |

**Rückgabe:** `string` – Originaler oder modifizierter Ausgabe-Puffer.

**Zeitpunkt:** Beim Rendern jedes Content-Elements einer Seite.

```php
use Contao\ContentModel;

#[AsHook('getContentElement')]
class GetContentElementListener
{
    public function __invoke(ContentModel $contentModel, string $buffer, $element): string
    {
        if ('text' === $contentModel->type) {
            $buffer = '<div class="wrapper">' . $buffer . '</div>';
        }
        return $buffer;
    }
}
```

---

## `getFrontendModule`

**Zweck:** Erlaubt Manipulation der generierten Ausgabe von Frontend-Modulen. Wird auch für Formulare in Seiten-Layouts ausgeführt.

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `\Contao\ModuleModel` | `$model` | DB-Ergebnis des Frontend-Moduls |
| 2 | `string` | `$buffer` | Generierte Ausgabe des Moduls |
| 3 | `object` | `$module` | Instanz der Frontend-Modul-Klasse |

**Rückgabe:** `string` – Modifizierter oder originaler `$buffer`.

**Zeitpunkt:** Während der Frontend-Modul-Generierung.

```php
use Contao\ModuleModel;

#[AsHook('getFrontendModule')]
class GetFrontendModuleListener
{
    public function __invoke(ModuleModel $model, string $buffer, object $module): string
    {
        if (2 === (int) $model->id) {
            return '<div class="module-wrapper">' . $buffer . '</div>';
        }
        return $buffer;
    }
}
```

---

## `getForm`

**Zweck:** Erlaubt Manipulation der Formular-Generierung. Wird nur aufgerufen, wenn ein Formular via `\Contao\Controller::getForm()` gerendert wird (z.B. über `{{insert_form::*}}`-Insert-Tag). **Nicht** bei direkter Formular-Darstellung über Form-Content-Elemente.

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `\Contao\FormModel` | `$formModel` | DB-Ergebnis aus `tl_form` |
| 2 | `string` | `$buffer` | Generierte Formular-Ausgabe |
| 3 | `\Contao\Form` | `$form` | Die Formular-Instanz |

**Rückgabe:** `string` – Modifizierter oder originaler `$buffer`.

**Zeitpunkt:** Beim Rendern eines Formulars über `{{insert_form::*}}`.

```php
use Contao\Form;
use Contao\FormModel;

#[AsHook('getForm')]
class GetFormListener
{
    public function __invoke(FormModel $formModel, string $buffer, Form $form): string
    {
        if (5 === (int) $form->id) {
            // Formular-Ausgabe modifizieren
        }
        return $buffer;
    }
}
```

---

## `isVisibleElement`

**Zweck:** Bestimmt, ob ein Element (Artikel, Frontend-Modul oder Content-Element) im Frontend sichtbar sein soll. Verhindert im Gegensatz zu anderen Hooks die komplette Markup-Generierung.

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `\Contao\Model` | `$element` | DB-Ergebnis aus `tl_article`, `tl_content` oder `tl_module` |
| 2 | `bool` | `$isVisible` | Aktueller Sichtbarkeitsstatus |

**Rückgabe:** `bool` – `true` = sichtbar, `false` = ausgeblendet.

**Zeitpunkt:** Bei der Frontend-Sichtbarkeitsprüfung von Artikeln, Content-Elementen und Modulen.

```php
use Contao\ContentModel;
use Contao\Model;

#[AsHook('isVisibleElement')]
class IsVisibleElementListener
{
    public function __invoke(Model $element, bool $isVisible): bool
    {
        if ($element instanceof ContentModel) {
            // Eigene Sichtbarkeitslogik anwenden
            if ($this->shouldHideElement($element)) {
                return false;
            }
        }
        return $isVisible;
    }
}
```

---

_Quelle: https://docs.contao.org/5.x/dev/reference/hooks/ (Stand 2025-06)_
