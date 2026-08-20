# Contao Hooks – DCA / Back end

Hooks for the Data Container Array (DCA), back end navigation, AJAX actions and system maintenance.

---

## Contents

- [`executePostActions`](#executepostactions)
- [`executePreActions`](#executepreactions)
- [`getAttributesFromDca`](#getattributesfromdca)
- [`getUserNavigation`](#getusernavigation)
- [`getSystemMessages`](#getsystemmessages)
- [`loadDataContainer`](#loaddatacontainer)
- [`reviseTable`](#revisetable)

## `executePostActions`

**Purpose:** Triggered on AJAX requests that require a DCA object (post actions).

**Parameters:**

| # | Type | Name | Description |
|---|-----|------|-------------|
| 1 | `string` | `$action` | Name of the executed action |
| 2 | `\Contao\DataContainer` | `$dc` | The DataContainer object of the current DCA instance |

**Returns:** `void`

**Timing:** On AJAX requests with a DCA object, after the primary action has been processed.

```php
use Contao\CoreBundle\DependencyInjection\Attribute\AsHook;
use Contao\DataContainer;

#[AsHook('executePostActions')]
class ExecutePostActionsListener
{
    public function __invoke(string $action, DataContainer $dc): void
    {
        if ('myCustomAction' === $action) {
            // Process your own AJAX action
            echo json_encode(['status' => 'ok']);
            exit;
        }
    }
}
```

---

## `executePreActions`

**Purpose:** Triggered on AJAX requests that do **not** require a DCA object (pre actions).

**Parameters:**

| # | Type | Name | Description |
|---|-----|------|-------------|
| 1 | `string` | `$action` | Name of the executed action |

**Returns:** `void`

**Timing:** On AJAX requests without a DCA object.

```php
#[AsHook('executePreActions')]
class ExecutePreActionsListener
{
    public function __invoke(string $action): void
    {
        if ('myPreAction' === $action) {
            // Process and output the response
            echo 'result';
            exit;
        }
    }
}
```

---

## `getAttributesFromDca`

**Purpose:** Triggered when widget attributes are extracted from a Data Container Array.

**Parameters:**

| # | Type | Name | Description |
|---|-----|------|-------------|
| 1 | `array` | `$attributes` | Array of the widget attributes |
| 2 | `mixed` | `$context` | `\Contao\DataContainer`, `\Contao\Module` or `null` |

**Returns:** `array` – The (possibly modified) attribute array.

**Timing:** While widget attributes are extracted from the DCA configuration.

```php
#[AsHook('getAttributesFromDca')]
class GetAttributesFromDcaListener
{
    public function __invoke(array $attributes, $context = null): array
    {
        // Adjust the widget attributes
        if (isset($attributes['inputType']) && 'text' === $attributes['inputType']) {
            $attributes['class'] = ($attributes['class'] ?? '') . ' my-text-field';
        }
        return $attributes;
    }
}
```

---

## `getUserNavigation`

**Purpose:** Allows manipulating the back end user navigation.

**Parameters:**

| # | Type | Name | Description |
|---|-----|------|-------------|
| 1 | `array` | `$modules` | Compiled list of the back end modules |
| 2 | `bool` | `$showAll` | Whether all modules are shown (even for collapsed groups) |

**Returns:** `array` – The (possibly modified) module array.

**Timing:** While the back end user navigation is compiled.

```php
#[AsHook('getUserNavigation')]
class GetUserNavigationListener
{
    public function __invoke(array $modules, bool $showAll): array
    {
        $modules['system']['modules']['my_link'] = [
            'label' => 'External page',
            'title' => 'Visit the external page',
            'class' => 'navigation',
            'href'  => 'https://example.com',
        ];
        return $modules;
    }
}
```

---

## `getSystemMessages`

**Purpose:** Allows adding your own messages to the back end start screen.

**Parameters:** none

**Returns:** `string` – HTML with the messages, or an empty string.

**Timing:** While the back end start screen is rendered.

```php
#[AsHook('getSystemMessages')]
class GetSystemMessagesListener
{
    public function __invoke(): string
    {
        if ($this->hasWarnings()) {
            return '<p class="tl_error">Caution: there are open tasks!</p>';
        }
        return '';
    }
}
```

---

## `loadDataContainer`

**Purpose:** Triggered when a DCA file is loaded. Ideal for dynamic DCA adjustments.

**Parameters:**

| # | Type | Name | Description |
|---|-----|------|-------------|
| 1 | `string` | `$table` | Name of the loaded data container (e.g. `tl_content`) |

**Returns:** `void`

**Timing:** When a DCA file is loaded into the system.

```php
#[AsHook('loadDataContainer')]
class LoadDataContainerListener
{
    public function __invoke(string $table): void
    {
        if ('tl_content' === $table) {
            // Extend the DCA dynamically
            $GLOBALS['TL_DCA']['tl_content']['fields']['myField'] = [
                'inputType' => 'text',
                'eval'      => ['tl_class' => 'w50'],
                'sql'       => "varchar(255) NOT NULL default ''",
            ];
        }
    }
}
```

---

## `reviseTable`

**Purpose:** Triggered when Contao removes orphaned records from a table.

**Parameters:**

| # | Type | Name | Description |
|---|-----|------|-------------|
| 1 | `string` | `$table` | Current table name |
| 2 | `array\|null` | `$newRecords` | IDs of new records |
| 3 | `string\|null` | `$parentTable` | Optional parent table name |
| 4 | `array\|null` | `$childTables` | Optional names of child tables |

**Returns:** `bool|null` – `true` to reload the current page, otherwise `false`/`null`.

**Timing:** During the clean-up process for orphaned records in the back end.

```php
#[AsHook('reviseTable')]
class ReviseTableListener
{
    public function __invoke(string $table, array|null $newRecords, string|null $parentTable, array|null $childTables): bool|null
    {
        if ('tl_my_table' === $table) {
            // Run your own clean-up logic
            return true; // reload the page
        }
        return null;
    }
}
```

---

_Source: https://docs.contao.org/5.x/dev/reference/hooks/ (as of 2025-06)_
