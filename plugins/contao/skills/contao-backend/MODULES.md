# Contao 5 — Backend modules

## Contents

- [Overview](#overview)
- [Registration](#registration)
- [Configuration options](#configuration-options)
- [tables (most important option)](#tables-most-important-option)
- [Loading assets](#loading-assets)
- [Custom Callback](#custom-callback)
- [Custom Action Keys](#custom-action-keys)
- [Translations](#translations)
- [DCA for backend modules](#dca-for-backend-modules)
- [Related skills](#related-skills)

## Overview

Backend modules are navigation entries in the Contao administration interface.
The framework groups them into categories (e.g. "Content", "Layout") with
individual modules underneath.

---

## Registration

Modules are registered in `contao/config/config.php` via `$GLOBALS['BE_MOD']`:

```php
// contao/config/config.php
$GLOBALS['BE_MOD']['content']['my_module'] = [
    'tables' => ['tl_my_module'],
];
```

### Categories

Standard categories in `BE_MOD`:
- `design` — design/layout settings
- `modules` — frontend modules
- `content` — content management
- `accounts` — users/members
- `system` — system settings

---

## Configuration options

| Key | Description |
|-----------|-------------|
| `tables` | Database tables managed by the module |
| `stylesheet` | Additional CSS files |
| `javascript` | Additional JavaScript files |
| `callback` | Custom output rendering class |
| `disablePermissionChecks` | Boolean: disable permission checks |
| `hideInNavigation` | Boolean: hide from the main navigation |
| `<custom-key>` | Custom callback actions |

---

## tables (most important option)

The `tables` key defines which database tables the module manages.
Multiple tables enable parent-child relationships:

```php
$GLOBALS['BE_MOD']['content']['parts'] = [
    'tables' => ['tl_vendor', 'tl_parts'],
];
```

Here `tl_vendor` is the parent table and `tl_parts` the child table.

---

## Loading assets

Including CSS and JavaScript globally in the backend:

```php
$GLOBALS['BE_MOD']['content']['my_module'] = [
    'tables' => ['tl_my_module'],
    'javascript' => ['bundles/mymodule/scripts.js'],
    'stylesheet' => ['bundles/mymodule/styles.css'],
];
```

---

## Custom Callback

Custom rendering via a callback class:

```php
$GLOBALS['BE_MOD']['content']['my_module'] = [
    'callback' => \App\Contao\BackendModule::class,
];
```

```php
// src/Contao/BackendModule.php
namespace App\Contao;

class BackendModule
{
    public function generate(): string
    {
        return '<div class="tl_listing_container">Custom content</div>';
    }
}
```

**Recommendation:** for complex functionality, use custom backend routes
(see the `contao-backend-routes` skill).

---

## Custom Action Keys

Custom actions via query parameter (e.g. `&key=exportTheme`):

```php
$GLOBALS['BE_MOD']['content']['my_module'] = [
    'tables' => ['tl_my_module'],
    'exportCsv' => [\App\Contao\CsvExporter::class, 'export'],
];
```

URL call: `contao?do=my_module&key=exportCsv`

---

## Translations

Language files in `contao/languages/<language>/modules.xlf`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<xliff version="1.1">
  <file datatype="php" original="src/Resources/contao/languages/en/modules.php" source-language="en">
    <body>
      <trans-unit id="MOD.my_module.0">
        <source>My Module</source>
      </trans-unit>
      <trans-unit id="MOD.my_module.1">
        <source>Manage entries of my module</source>
      </trans-unit>
    </body>
  </file>
</xliff>
```

As a PHP array:
```php
// contao/languages/en/modules.php
$GLOBALS['TL_LANG']['MOD']['my_module'] = ['My Module', 'Manage entries of my module'];
```

---

## DCA for backend modules

Complete example with two related tables (vendor/parts):

### tl_vendor (parent table)

```php
// contao/dca/tl_vendor.php
$GLOBALS['TL_DCA']['tl_vendor'] = [
    'config' => [
        'dataContainer' => \Contao\DC_Table::class,
        'ctable' => ['tl_parts'],
        'enableVersioning' => true,
        'sql' => [
            'keys' => ['id' => 'primary'],
        ],
    ],
    'list' => [
        'sorting' => [
            'mode' => \Contao\DataContainer::MODE_SORTED,
            'flag' => \Contao\DataContainer::SORT_INITIAL_LETTER_ASC,
            'fields' => ['name'],
            'panelLayout' => 'search,limit',
        ],
        'label' => [
            'fields' => ['name'],
            'format' => '%s',
        ],
        'operations' => [
            'edit' => ['href' => 'act=edit', 'icon' => 'edit.svg'],
            'delete' => ['href' => 'act=delete', 'icon' => 'delete.svg'],
            'parts' => ['href' => 'table=tl_parts', 'icon' => 'edit.svg'],
        ],
    ],
    'palettes' => [
        'default' => '{vendor_legend},name;{address_legend},street,postal,city,country',
    ],
    'fields' => [
        'id' => ['sql' => ['type' => 'integer', 'unsigned' => true, 'autoincrement' => true]],
        'tstamp' => ['sql' => ['type' => 'integer', 'unsigned' => true, 'default' => 0]],
        'name' => [
            'label' => ['Name', 'Vendor name'],
            'inputType' => 'text',
            'search' => true,
            'flag' => \Contao\DataContainer::SORT_INITIAL_LETTER_ASC,
            'eval' => ['mandatory' => true, 'maxlength' => 255, 'tl_class' => 'w50'],
            'sql' => ['type' => 'string', 'length' => 255, 'default' => ''],
        ],
        // ...
    ],
];
```

---

## Related skills

- `contao-backend-routes` — custom backend controllers and menu entries
- `contao-dca-reference` — complete DCA reference (existing skill)

---

*Source: https://docs.contao.org/5.x/dev/framework/back-end-modules/*  
*https://docs.contao.org/5.x/dev/guides/dca/*
