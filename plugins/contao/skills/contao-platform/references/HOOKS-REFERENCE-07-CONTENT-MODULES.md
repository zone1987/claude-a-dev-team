# Contao Hooks – Content elements / Front end modules

Hooks for rendering articles, content elements, front end modules and forms.

---

## Contents

- [`compileArticle`](#compilearticle)
- [`getArticle`](#getarticle)
- [`getArticles`](#getarticles)
- [`getContentElement`](#getcontentelement)
- [`getFrontendModule`](#getfrontendmodule)
- [`getForm`](#getform)
- [`isVisibleElement`](#isvisibleelement)

## `compileArticle`

**Purpose:** Triggered after the article module has been compiled. Allows adding extra data to the template.

**Parameters:**

| # | Type | Name | Description |
|---|-----|------|-------------|
| 1 | `\Contao\FrontendTemplate` | `$template` | Front end template of the article module |
| 2 | `array` | `$data` | Module configuration as an associative array |
| 3 | `\Contao\Module` | `$module` | The current module instance |

**Returns:** `void`

**Timing:** After the article module compilation has finished.

```php
#[AsHook('compileArticle')]
class CompileArticleListener
{
    public function __invoke(FrontendTemplate $template, array $data, Module $module): void
    {
        $template->customContent = '<p>This content is available in mod_article.html5 through $this->customContent</p>';
    }
}
```

---

## `getArticle`

**Purpose:** Allows overriding the article configuration **before** rendering.

**Parameters:**

| # | Type | Name | Description |
|---|-----|------|-------------|
| 1 | `\Contao\ArticleModel` | `$article` | DB result from `tl_article` |

**Returns:** `void`

**Timing:** Before an article is rendered.

```php
use Contao\ArticleModel;

#[AsHook('getArticle')]
class GetArticleListener
{
    public function __invoke(ArticleModel $article): void
    {
        // Modify the article properties
        $article->cssID = serialize(['', 'my-class']);
    }
}
```

---

## `getArticles`

**Purpose:** Allows replacing the articles of a column with your own content.

**Parameters:**

| # | Type | Name | Description |
|---|-----|------|-------------|
| 1 | `int` | `$pageId` | Parent page ID of the articles |
| 2 | `string` | `$column` | The column the articles are rendered for |

**Returns:** `string|null` – String with your own content (prevents further hook execution), or `null` for the default behaviour.

**Timing:** While the articles of a page column are rendered.

```php
#[AsHook('getArticles')]
class GetArticlesListener
{
    public function __invoke(int $pageId, string $column): string|null
    {
        if (42 === $pageId && 'main' === $column) {
            return '<div class="custom">Custom content</div>';
        }
        return null;
    }
}
```

---

## `getContentElement`

**Purpose:** Triggered when a content element is rendered. Allows modifying the rendered output.

**Parameters:**

| # | Type | Name | Description |
|---|-----|------|-------------|
| 1 | `\Contao\ContentModel` | `$contentModel` | DB result from `tl_content` |
| 2 | `string` | `$buffer` | Generated output of the content element |
| 3 | `object` | `$element` | Instance of the content element class |

**Returns:** `string` – The original or modified output buffer.

**Timing:** While each content element of a page is rendered.

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

**Purpose:** Allows manipulating the generated output of front end modules. Also runs for forms in page layouts.

**Parameters:**

| # | Type | Name | Description |
|---|-----|------|-------------|
| 1 | `\Contao\ModuleModel` | `$model` | DB result of the front end module |
| 2 | `string` | `$buffer` | Generated output of the module |
| 3 | `object` | `$module` | Instance of the front end module class |

**Returns:** `string` – The modified or original `$buffer`.

**Timing:** During front end module generation.

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

**Purpose:** Allows manipulating the form generation. Called only when a form is rendered via `\Contao\Controller::getForm()` (for example through the `{{insert_form::*}}` insert tag). **Not** when a form is rendered directly through form content elements.

**Parameters:**

| # | Type | Name | Description |
|---|-----|------|-------------|
| 1 | `\Contao\FormModel` | `$formModel` | DB result from `tl_form` |
| 2 | `string` | `$buffer` | Generated form output |
| 3 | `\Contao\Form` | `$form` | The form instance |

**Returns:** `string` – The modified or original `$buffer`.

**Timing:** While a form is rendered through `{{insert_form::*}}`.

```php
use Contao\Form;
use Contao\FormModel;

#[AsHook('getForm')]
class GetFormListener
{
    public function __invoke(FormModel $formModel, string $buffer, Form $form): string
    {
        if (5 === (int) $form->id) {
            // Modify the form output
        }
        return $buffer;
    }
}
```

---

## `isVisibleElement`

**Purpose:** Determines whether an element (article, front end module or content element) should be visible in the front end. Unlike other hooks, it prevents the markup generation entirely.

**Parameters:**

| # | Type | Name | Description |
|---|-----|------|-------------|
| 1 | `\Contao\Model` | `$element` | DB result from `tl_article`, `tl_content` or `tl_module` |
| 2 | `bool` | `$isVisible` | Current visibility state |

**Returns:** `bool` – `true` = visible, `false` = hidden.

**Timing:** During the front end visibility check of articles, content elements and modules.

```php
use Contao\ContentModel;
use Contao\Model;

#[AsHook('isVisibleElement')]
class IsVisibleElementListener
{
    public function __invoke(Model $element, bool $isVisible): bool
    {
        if ($element instanceof ContentModel) {
            // Apply your own visibility logic
            if ($this->shouldHideElement($element)) {
                return false;
            }
        }
        return $isVisible;
    }
}
```

---

_Source: https://docs.contao.org/5.x/dev/reference/hooks/ (as of 2025-06)_
