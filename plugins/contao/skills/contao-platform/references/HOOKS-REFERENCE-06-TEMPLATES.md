# Contao Hooks – Templates

Hooks for back end and front end template parsing and widget output.

---

## Contents

- [`outputBackendTemplate`](#outputbackendtemplate)
- [`parseBackendTemplate`](#parsebackendtemplate)
- [`parseFrontendTemplate`](#parsefrontendtemplate)
- [`parseTemplate`](#parsetemplate)
- [`parseWidget`](#parsewidget)

## `outputBackendTemplate`

**Purpose:** Triggered when a back end template is sent to the screen. Allows modifying the rendered template content.

**Parameters:**

| # | Type | Name | Description |
|---|-----|------|-------------|
| 1 | `string` | `$buffer` | Rendered back end template content |
| 2 | `string` | `$template` | Template name without the extension (e.g. `be_main`) |

**Returns:** `string` – The original or modified `$buffer`.

**Timing:** After rendering, before the output is sent to the browser.

```php
use Contao\CoreBundle\DependencyInjection\Attribute\AsHook;

#[AsHook('outputBackendTemplate')]
class OutputBackendTemplateListener
{
    public function __invoke(string $buffer, string $template): string
    {
        if ('be_main' === $template) {
            $buffer = str_replace('</head>', '<style>.custom{color:red}</style></head>', $buffer);
        }
        return $buffer;
    }
}
```

---

## `parseBackendTemplate`

**Purpose:** Triggered when a back end template is parsed. Similar to `outputBackendTemplate`, but fires at parse time (earlier in the process).

**Parameters:**

| # | Type | Name | Description |
|---|-----|------|-------------|
| 1 | `string` | `$buffer` | Parsed back end template content |
| 2 | `string` | `$template` | Template name without the extension (e.g. `be_widget`) |

**Returns:** `string` – The original or modified `$buffer`.

**Timing:** While back end templates are parsed in the admin interface.

```php
#[AsHook('parseBackendTemplate')]
class ParseBackendTemplateListener
{
    public function __invoke(string $buffer, string $template): string
    {
        if ('be_main' === $template) {
            // Insert custom content
        }
        return $buffer;
    }
}
```

---

## `parseFrontendTemplate`

**Purpose:** Triggered when a front end template is parsed.

**Parameters:**

| # | Type | Name | Description |
|---|-----|------|-------------|
| 1 | `string` | `$buffer` | Parsed front end template content |
| 2 | `string` | `$templateName` | Template name without the extension (e.g. `nav_default`) |
| 3 | `\Contao\FrontendTemplate` | `$template` | The template instance |

**Returns:** `string` – The original or modified `$buffer`.

**Timing:** After a front end template has been parsed, before the output.

```php
#[AsHook('parseFrontendTemplate')]
class ParseFrontendTemplateListener
{
    public function __invoke(string $buffer, string $templateName, FrontendTemplate $template): string
    {
        if ('ce_text' === $templateName) {
            // Modify the content of a text element
        }
        return $buffer;
    }
}
```

---

## `parseTemplate`

**Purpose:** Triggered **before** a template is parsed. Receives the template object – ideal for adding your own template variables.

**Parameters:**

| # | Type | Name | Description |
|---|-----|------|-------------|
| 1 | `\Contao\Template` | `$template` | Front end or back end template instance |

**Returns:** `void`

**Timing:** Before the template is parsed. Template variables can be set here.

```php
#[AsHook('parseTemplate')]
class ParseTemplateListener
{
    public function __invoke(Template $template): void
    {
        if ('fe_page' === $template->getName() || str_starts_with($template->getName(), 'fe_page_')) {
            $template->customVar = 'myValue';
        }
    }
}
```

**Tip:** Closures let you inject helper functions as well:

```php
$template->isMemberOf = fn(int $groupId): bool =>
    $this->authorizationChecker->isGranted(
        ContaoCorePermissions::MEMBER_IN_GROUPS,
        $groupId
    );
```

---

## `parseWidget`

**Purpose:** Allows adjusting the output of a `\Contao\Widget` while it is parsed.

**Parameters:**

| # | Type | Name | Description |
|---|-----|------|-------------|
| 1 | `string` | `$buffer` | Output buffer of the widget |
| 2 | `\Contao\Widget` | `$widget` | The widget instance |

**Returns:** `string` – The modified output buffer.

**Timing:** While a widget is parsed, before the HTML is rendered.

```php
use Contao\Widget;

#[AsHook('parseWidget')]
class ParseWidgetListener
{
    public function __invoke(string $buffer, Widget $widget): string
    {
        if ('myFieldName' === $widget->name) {
            $buffer = '<div class="custom-wrapper">' . $buffer . '</div>';
        }
        return $buffer;
    }
}
```

---

_Source: https://docs.contao.org/5.x/dev/reference/hooks/ (as of 2025-06)_
