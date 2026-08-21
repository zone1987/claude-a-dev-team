# Contao Hooks – Page / Layout / Front end output

Hooks for page assembly, layout selection, breadcrumb and output modification.

---

## Contents

- [`generatePage`](#generatepage)
- [`generateBreadcrumb`](#generatebreadcrumb)
- [`getPageLayout`](#getpagelayout)
- [`getPageStatusIcon`](#getpagestatusicon)
- [`loadPageDetails`](#loadpagedetails)
- [`modifyFrontendPage`](#modifyfrontendpage)
- [`outputFrontendTemplate`](#outputfrontendtemplate)
- [`replaceDynamicScriptTags`](#replacedynamicscripttags)

## `generatePage`

**Purpose:** Triggered **before** the main layout (`fe_page`) is compiled.

**Parameters:**

| # | Type | Name | Description |
|---|-----|------|-------------|
| 1 | `\Contao\PageModel` | `$pageModel` | The current page object |
| 2 | `\Contao\LayoutModel` | `$layout` | The page layout in use |
| 3 | `\Contao\PageRegular` | `$pageRegular` | The current page type |

**Returns:** `void`

**Timing:** Before the main layout template is compiled.

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
        // e.g. add JS/CSS to the page dynamically
    }
}
```

---

## `generateBreadcrumb`

**Purpose:** Allows manipulating the breadcrumb navigation of the breadcrumb front end module.

**Parameters:**

| # | Type | Name | Description |
|---|-----|------|-------------|
| 1 | `array` | `$items` | Breadcrumb items (each with `isRoot`, `isActive`, `href`, `title`, `link`, `data`, `class`) |
| 2 | `\Contao\Module` | `$module` | The front end module instance |

**Returns:** `array` – The (possibly modified) array of breadcrumb items.

**Timing:** While the breadcrumb navigation is generated.

```php
#[AsHook('generateBreadcrumb')]
class GenerateBreadcrumbListener
{
    public function __invoke(array $items, Module $module): array
    {
        // Modify, add or remove breadcrumb items
        return $items;
    }
}
```

---

## `getPageLayout`

**Purpose:** Triggered while a regular page is generated. Allows modifying the page or layout object.

**Parameters:**

| # | Type | Name | Description |
|---|-----|------|-------------|
| 1 | `\Contao\PageModel` | `$page` | The page model instance |
| 2 | `\Contao\LayoutModel` | `$layout` | The layout of the page |
| 3 | `\Contao\PageRegular` | `$pageRegular` | The page type instance |

**Returns:** `void`

**Timing:** During regular page generation.

```php
#[AsHook('getPageLayout')]
class GetPageLayoutListener
{
    public function __invoke(PageModel $page, LayoutModel $layout, PageRegular $pageRegular): void
    {
        // Modify the layout object, e.g. include different style sheets
    }
}
```

---

## `getPageStatusIcon`

**Purpose:** Triggered when the matching page status icon is determined. Allows your own icons for custom page types.

**Parameters:**

| # | Type | Name | Description |
|---|-----|------|-------------|
| 1 | `object` | `$page` | DB result from `tl_page` (`PageModel`, `Database\Result` or `stdClass`) |
| 2 | `string` | `$image` | Icon file name determined by default |

**Returns:** `string` – Your own icon path or the unchanged `$image` value.

**Timing:** While the status icon is determined in the back end.

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

**Purpose:** Runs when page details are loaded via `\Contao\PageModel::loadDetails()`. Allows adding your own data to the page instance (e.g. inheriting settings from root pages).

**Parameters:**

| # | Type | Name | Description |
|---|-----|------|-------------|
| 1 | `array` | `$parentModels` | All parent page models |
| 2 | `\Contao\PageModel` | `$page` | The current page |

**Returns:** `void`

**Timing:** When the page details are loaded through `PageModel::loadDetails()`.

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

**Purpose:** Triggered when a front end template is sent to the screen. Allows changes to the rendered HTML. Fires **after** insert tags have been replaced.

**Parameters:**

| # | Type | Name | Description |
|---|-----|------|-------------|
| 1 | `string` | `$buffer` | Rendered template content |
| 2 | `string` | `$templateName` | Template name without the extension (e.g. `fe_page`) |

**Returns:** `string` – The original or modified `$buffer`.

**Timing:** After insert tags have been replaced, before the final output.

> For modifications **before** insert tag replacement, use `outputFrontendTemplate`.

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

**Purpose:** Triggered when a front end template is output. Fires **before** insert tags are replaced.

**Parameters:**

| # | Type | Name | Description |
|---|-----|------|-------------|
| 1 | `string` | `$buffer` | Rendered template content |
| 2 | `string` | `$template` | Template name without the extension (e.g. `fe_page`) |

**Returns:** `string` – The original or modified `$buffer`.

**Timing:** Before insert tags are replaced.

```php
#[AsHook('outputFrontendTemplate')]
class OutputFrontendTemplateListener
{
    public function __invoke(string $buffer, string $template): string
    {
        if ('fe_page' === $template) {
            // Insert tags are not replaced yet – be careful!
        }
        return $buffer;
    }
}
```

---

## `replaceDynamicScriptTags`

**Purpose:** Runs before Contao replaces dynamic script tags (`[[TL_JQUERY]]`, `[[TL_MOOTOOLS]]`, `[[TL_BODY]]`, `[[TL_CSS]]`, `[[TL_HEAD]]`). Allows your own replacement or upstream logic.

**Parameters:**

| # | Type | Name | Description |
|---|-----|------|-------------|
| 1 | `string` | `$buffer` | Page output buffer with the script tags still unreplaced |

**Returns:** `string` – The modified buffer.

**Timing:** Before Contao replaces the script tags.

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

_Source: https://docs.contao.org/5.x/dev/reference/hooks/ (as of 2025-06)_
