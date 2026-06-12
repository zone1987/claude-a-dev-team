# Contao Hooks – Seite / Layout / Frontend-Ausgabe

Hooks für Seitenaufbau, Layout-Auswahl, Breadcrumb, Ausgabemodifikation.

---

## `generatePage`

**Zweck:** Wird **vor** dem Kompilieren des Haupt-Layouts (`fe_page`) ausgelöst.

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `\Contao\PageModel` | `$pageModel` | Das aktuelle Seitenobjekt |
| 2 | `\Contao\LayoutModel` | `$layout` | Das verwendete Seiten-Layout |
| 3 | `\Contao\PageRegular` | `$pageRegular` | Der aktuelle Seitentyp |

**Rückgabe:** `void`

**Zeitpunkt:** Vor dem Kompilieren des Haupt-Layout-Templates.

```php
use Contao\CoreBundle\DependencyInjection\Attribute\AsHook;
use Contao\LayoutModel;
use Contao\PageModel;
use Contao\PageRegular;

#[AsHook('generatePage')]
class GeneratePageListener
{
    public function __invoke(PageModel $pageModel, LayoutModel $layout, PageRegular $pageRegular): void
    {
        // z.B. JS/CSS dynamisch zur Seite hinzufügen
    }
}
```

---

## `generateBreadcrumb`

**Zweck:** Ermöglicht Manipulation der Breadcrumb-Navigation des Breadcrumb-Frontend-Moduls.

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `array` | `$items` | Breadcrumb-Items (je mit `isRoot`, `isActive`, `href`, `title`, `link`, `data`, `class`) |
| 2 | `\Contao\Module` | `$module` | Die Frontend-Modul-Instanz |

**Rückgabe:** `array` – Das (ggf. modifizierte) Array der Breadcrumb-Items.

**Zeitpunkt:** Beim Generieren der Breadcrumb-Navigation.

```php
#[AsHook('generateBreadcrumb')]
class GenerateBreadcrumbListener
{
    public function __invoke(array $items, Module $module): array
    {
        // Breadcrumb-Items modifizieren, hinzufügen oder entfernen
        return $items;
    }
}
```

---

## `getPageLayout`

**Zweck:** Wird beim Generieren einer regulären Seite ausgelöst. Ermöglicht Modifikation des Seiten- oder Layout-Objekts.

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `\Contao\PageModel` | `$page` | Die Seiten-Modell-Instanz |
| 2 | `\Contao\LayoutModel` | `$layout` | Das Layout der Seite |
| 3 | `\Contao\PageRegular` | `$pageRegular` | Die Seitentyp-Instanz |

**Rückgabe:** `void`

**Zeitpunkt:** Während der regulären Seitengenerierung.

```php
#[AsHook('getPageLayout')]
class GetPageLayoutListener
{
    public function __invoke(PageModel $page, LayoutModel $layout, PageRegular $pageRegular): void
    {
        // Layout-Objekt modifizieren, z.B. andere Stylesheets einbinden
    }
}
```

---

## `getPageStatusIcon`

**Zweck:** Wird ausgelöst, wenn das passende Seiten-Status-Icon berechnet wird. Ermöglicht eigene Icons für benutzerdefinierte Seitentypen.

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `object` | `$page` | DB-Ergebnis aus `tl_page` (`PageModel`, `Database\Result` oder `stdClass`) |
| 2 | `string` | `$image` | Standardmäßig berechneter Icon-Dateiname |

**Rückgabe:** `string` – Eigener Icon-Pfad oder unveränderter `$image`-Wert.

**Zeitpunkt:** Bei der Berechnung des Status-Icons im Backend.

```php
#[AsHook('getPageStatusIcon')]
class GetPageStatusIconListener
{
    public function __invoke($page, string $image): string
    {
        if ('my_page_type' === $page->type) {
            return 'bundles/myapp/page_icon.svg';
        }
        return $image;
    }
}
```

---

## `loadPageDetails`

**Zweck:** Wird ausgeführt, wenn Seiten-Details via `\Contao\PageModel::loadDetails()` geladen werden. Ermöglicht Hinzufügen eigener Daten zur Seiten-Instanz (z.B. Vererbung von Root-Seiten-Einstellungen).

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `array` | `$parentModels` | Alle übergeordneten Seiten-Modelle |
| 2 | `\Contao\PageModel` | `$page` | Die aktuelle Seite |

**Rückgabe:** `void`

**Zeitpunkt:** Beim Laden der Seiten-Details über `PageModel::loadDetails()`.

```php
#[AsHook('loadPageDetails')]
class LoadPageDetailsListener
{
    public function __invoke(array $parentModels, PageModel $page): void
    {
        if (!empty($parentModels)) {
            $rootPage = end($parentModels);
            $page->myCustomVar = $rootPage->rootMyCustomVar;
        }
    }
}
```

---

## `modifyFrontendPage`

**Zweck:** Wird ausgelöst, wenn ein Frontend-Template auf dem Bildschirm ausgegeben wird. Ermöglicht Änderungen am gerenderten HTML. Feuert **nach** Insert-Tag-Ersetzung.

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `string` | `$buffer` | Gerenderter Template-Inhalt |
| 2 | `string` | `$templateName` | Template-Name ohne Extension (z.B. `fe_page`) |

**Rückgabe:** `string` – Originaler oder modifizierter `$buffer`.

**Zeitpunkt:** Nach Insert-Tag-Ersetzung, vor endgültiger Ausgabe.

> Für Modifikationen **vor** Insert-Tag-Ersetzung: `outputFrontendTemplate` verwenden.

```php
#[AsHook('modifyFrontendPage')]
class ModifyFrontendPageListener
{
    public function __invoke(string $buffer, string $templateName): string
    {
        if ('fe_page' === $templateName) {
            $buffer = str_replace('</body>', '<script>/* custom */</script></body>', $buffer);
        }
        return $buffer;
    }
}
```

---

## `outputFrontendTemplate`

**Zweck:** Wird ausgelöst, wenn ein Frontend-Template ausgegeben wird. Feuert **vor** Insert-Tag-Ersetzung.

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `string` | `$buffer` | Gerenderter Template-Inhalt |
| 2 | `string` | `$template` | Template-Name ohne Extension (z.B. `fe_page`) |

**Rückgabe:** `string` – Originaler oder modifizierter `$buffer`.

**Zeitpunkt:** Vor Insert-Tag-Ersetzung.

```php
#[AsHook('outputFrontendTemplate')]
class OutputFrontendTemplateListener
{
    public function __invoke(string $buffer, string $template): string
    {
        if ('fe_page' === $template) {
            // Insert-Tags noch nicht ersetzt – Vorsicht!
        }
        return $buffer;
    }
}
```

---

## `replaceDynamicScriptTags`

**Zweck:** Wird ausgeführt, bevor Contao dynamische Script-Tags (`[[TL_JQUERY]]`, `[[TL_MOOTOOLS]]`, `[[TL_BODY]]`, `[[TL_CSS]]`, `[[TL_HEAD]]`) ersetzt. Ermöglicht eigene Ersetzung oder vorgelagerte Logik.

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `string` | `$buffer` | Seiten-Ausgabe-Puffer mit noch nicht ersetzten Script-Tags |

**Rückgabe:** `string` – Modifizierter Puffer.

**Zeitpunkt:** Vor der Ersetzung von Script-Tags durch Contao.

```php
#[AsHook('replaceDynamicScriptTags')]
class ReplaceDynamicScriptTagsListener
{
    public function __invoke(string $buffer): string
    {
        return str_replace('[[TL_CSS]]', '[[TL_CSS]]<link rel="stylesheet" href="assets/custom.css">', $buffer);
    }
}
```

---

_Quelle: https://docs.contao.org/5.x/dev/reference/hooks/ (Stand 2025-06)_
