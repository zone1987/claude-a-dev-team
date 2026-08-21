# Contao DCA – framework infrastructure (5.x)

## Contents

- [Overview](#overview)
- [Creating a DCA](#creating-a-dca)
- [Registering callbacks](#registering-callbacks)
- [PaletteManipulator](#palettemanipulator)
- [Custom Drivers](#custom-drivers)

## Overview

Data Container Arrays (DCAs) describe a **data container** for arbitrary records. The metadata controls the list view, the back end forms and the save operations.

### Available drivers

| Driver | Purpose |
|---------|-------|
| `DC_Table` | Database records (most common case) |
| `DC_File` | System configuration |
| `DC_Folder` | File lists |

---

## Creating a DCA

```php
// contao/dca/tl_example.php
$GLOBALS['TL_DCA']['tl_example'] = [
    'config'   => [ /* … */ ],
    'list'     => [ /* … */ ],
    'fields'   => [ /* … */ ],
    'palettes' => [ /* … */ ],
];
```

All active modules load their DCAs sequentially – later modules can override earlier ones.

---

## Registering callbacks

### 1. PHP attributes (recommended)

```php
use Contao\CoreBundle\DependencyInjection\Attribute\AsCallback;

#[AsCallback(table: 'tl_module', target: 'list.label.group', priority: 100)]
public function onGroupCallback(
    string $group, string $mode, string $field,
    array $record, DataContainer $dc
): string {
    return $group;
}
```

### 2. Service annotations

```php
/**
 * @Callback(table="tl_module", target="list.label.group", priority=100)
 */
```

### 3. YAML service tags

```yaml
services:
    App\EventListener\DataContainer\ModuleCallbackListener:
        tags:
            -
                name: contao.callback
                table: tl_module
                target: list.label.group
                method: onGroupCallback
                priority: 100
```

### Service tag options

| Option | Type | Description |
|--------|-----|--------------|
| `name` | string | Must be `contao.callback` |
| `table` | string | Name of the data container |
| `target` | string | Callback type |
| `method` | string | Optional method name |
| `priority` | integer | Execution order (default: 0) |

### Invokable services

```php
#[AsCallback(table: 'tl_module', target: 'list.label.group')]
class ModuleCallbackListener
{
    public function __invoke(
        string $group, string $mode, string $field,
        array $record, DataContainer $dc
    ): string {
        return $group;
    }
}
```

---

## PaletteManipulator

The preferred way to edit palettes programmatically – instead of string operations or `str_replace()`.

### Adding fields

```php
use Contao\CoreBundle\DataContainer\PaletteManipulator;

PaletteManipulator::create()
    ->addField('custom_field', 'username')
    ->applyToPalette('admin', 'tl_user');
```

### Adding legends

```php
PaletteManipulator::create()
    ->addLegend('custom_legend', 'date_legend', PaletteManipulator::POSITION_BEFORE)
    ->addField('custom_field', 'custom_legend', PaletteManipulator::POSITION_APPEND)
    ->applyToPalette('default', 'tl_news');
```

### Removing fields

```php
PaletteManipulator::create()
    ->removeField('custom_field', 'name_legend')
    ->applyToPalette('admin', 'tl_user');
```

### Editing subpalettes

```php
PaletteManipulator::create()
    ->addField('custom_field', 'singleSRC')
    ->removeField('floating')
    ->applyToSubpalette('addImage', 'tl_content');
```

### Position constants

| Constant | Effect |
|-----------|---------|
| `POSITION_BEFORE` | Before the parent field |
| `POSITION_AFTER` | After the parent field (default) |
| `POSITION_PREPEND` | Before the parent legend |
| `POSITION_APPEND` | After the parent legend |

> Important: every `PaletteManipulator` instance keeps its changes. Create a new instance to avoid unwanted accumulation.

---

## Custom Drivers

```php
use Vendor\Driver\FoobarDriver;

$GLOBALS['TL_DCA']['tl_example'] = [
    'config' => [
        'dataContainer' => FoobarDriver::class,
    ],
];
```

Custom drivers extend `\Contao\DataContainer` and implement `\listable` and/or `\editable`. Reference implementations: `DC_File`, `DC_Folder`, `DC_Table`.

---

*Source: https://docs.contao.org/5.x/dev/framework/dca/ (+ /palettemanipulator/)*
