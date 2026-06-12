# Contao DCA – Framework-Infrastruktur (5.x)

## Überblick

Data Container Arrays (DCAs) beschreiben einen **Data Container** für beliebige Datensätze. Die Metadaten steuern Listenansicht, Backend-Formulare und Speicheroperationen.

### Verfügbare Treiber

| Treiber | Zweck |
|---------|-------|
| `DC_Table` | Datenbankdatensätze (häufigster Fall) |
| `DC_File` | Systemkonfiguration |
| `DC_Folder` | Dateilisten |

---

## DCA anlegen

```php
// contao/dca/tl_example.php
$GLOBALS['TL_DCA']['tl_example'] = [
    'config'   => [ /* … */ ],
    'list'     => [ /* … */ ],
    'fields'   => [ /* … */ ],
    'palettes' => [ /* … */ ],
];
```

Alle aktiven Module laden ihre DCAs sequenziell – spätere Module können frühere überschreiben.

---

## Callbacks registrieren

### 1. PHP-Attribute (empfohlen)

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

### 2. Service-Annotations

```php
/**
 * @Callback(table="tl_module", target="list.label.group", priority=100)
 */
```

### 3. YAML-Service-Tags

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

### Service-Tag-Optionen

| Option | Typ | Beschreibung |
|--------|-----|--------------|
| `name` | string | Muss `contao.callback` sein |
| `table` | string | Name des Data Containers |
| `target` | string | Callback-Typ |
| `method` | string | Optionaler Methodenname |
| `priority` | integer | Ausführungsreihenfolge (Standard: 0) |

### Invokable Services

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

Der bevorzugte Weg, Paletten programmatisch zu bearbeiten – statt Stringoperationen oder `str_replace()`.

### Felder hinzufügen

```php
use Contao\CoreBundle\DataContainer\PaletteManipulator;

PaletteManipulator::create()
    ->addField('custom_field', 'username')
    ->applyToPalette('admin', 'tl_user');
```

### Legenden hinzufügen

```php
PaletteManipulator::create()
    ->addLegend('custom_legend', 'date_legend', PaletteManipulator::POSITION_BEFORE)
    ->addField('custom_field', 'custom_legend', PaletteManipulator::POSITION_APPEND)
    ->applyToPalette('default', 'tl_news');
```

### Felder entfernen

```php
PaletteManipulator::create()
    ->removeField('custom_field', 'name_legend')
    ->applyToPalette('admin', 'tl_user');
```

### Subpaletten bearbeiten

```php
PaletteManipulator::create()
    ->addField('custom_field', 'singleSRC')
    ->removeField('floating')
    ->applyToSubpalette('addImage', 'tl_content');
```

### Positionskonstanten

| Konstante | Wirkung |
|-----------|---------|
| `POSITION_BEFORE` | Vor dem Eltern-Feld |
| `POSITION_AFTER` | Hinter dem Eltern-Feld (Standard) |
| `POSITION_PREPEND` | Vor der Eltern-Legende |
| `POSITION_APPEND` | Hinter der Eltern-Legende |

> Wichtig: Jede `PaletteManipulator`-Instanz behält ihre Änderungen. Neue Instanz anlegen um ungewollte Akkumulation zu vermeiden.

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

Eigene Treiber erweitern `\Contao\DataContainer` und implementieren `\listable` und/oder `\editable`. Referenz-Implementierungen: `DC_File`, `DC_Folder`, `DC_Table`.

---

*Quelle: https://docs.contao.org/5.x/dev/framework/dca/ (+ /palettemanipulator/)*
