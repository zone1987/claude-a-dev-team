# Contao 5 — Back-End-Module

## Übersicht

Back-End-Module sind Navigationseinträge in der Contao-Verwaltungsoberfläche.
Das Framework gruppiert sie in Kategorien (z.B. "Content", "Layout") mit
einzelnen Modulen darunter.

---

## Registrierung

Module werden in `contao/config/config.php` über `$GLOBALS['BE_MOD']` registriert:

```php
// contao/config/config.php
$GLOBALS['BE_MOD']['content']['my_module'] = [
    'tables' => ['tl_my_module'],
];
```

### Kategorien

Standard-Kategorien in `BE_MOD`:
- `design` — Design/Layout-Einstellungen
- `modules` — Frontend-Module
- `content` — Inhaltsverwaltung
- `accounts` — Benutzer/Mitglieder
- `system` — Systemeinstellungen

---

## Konfigurationsoptionen

| Schlüssel | Beschreibung |
|-----------|-------------|
| `tables` | Datenbanktabellen, die das Modul verwaltet |
| `stylesheet` | Zusätzliche CSS-Dateien |
| `javascript` | Zusätzliche JavaScript-Dateien |
| `callback` | Custom-Output-Rendering-Klasse |
| `disablePermissionChecks` | Boolean: Berechtigungsprüfung deaktivieren |
| `hideInNavigation` | Boolean: Aus Hauptnavigation ausblenden |
| `<custom-key>` | Custom-Callback-Aktionen |

---

## tables (wichtigste Option)

Der `tables`-Schlüssel definiert, welche Datenbanktabellen das Modul verwaltet.
Mehrere Tabellen ermöglichen Parent-Child-Beziehungen:

```php
$GLOBALS['BE_MOD']['content']['parts'] = [
    'tables' => ['tl_vendor', 'tl_parts'],
];
```

Hierbei ist `tl_vendor` die Eltern-Tabelle, `tl_parts` die Kind-Tabelle.

---

## Assets laden

CSS und JavaScript im Backend global einbinden:

```php
$GLOBALS['BE_MOD']['content']['my_module'] = [
    'tables' => ['tl_my_module'],
    'javascript' => ['bundles/mymodule/scripts.js'],
    'stylesheet' => ['bundles/mymodule/styles.css'],
];
```

---

## Custom Callback

Eigenes Rendering über eine Callback-Klasse:

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

**Empfehlung:** Für komplexe Funktionalität eigene Backend-Routen verwenden
(siehe `contao-backend-routes`-Skill).

---

## Custom Action Keys

Eigene Aktionen per Query-Parameter (z.B. `&key=exportTheme`):

```php
$GLOBALS['BE_MOD']['content']['my_module'] = [
    'tables' => ['tl_my_module'],
    'exportCsv' => [\App\Contao\CsvExporter::class, 'export'],
];
```

URL-Aufruf: `contao?do=my_module&key=exportCsv`

---

## Translations

Sprachdateien in `contao/languages/<sprache>/modules.xlf`:

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

Als PHP-Array:
```php
// contao/languages/en/modules.php
$GLOBALS['TL_LANG']['MOD']['my_module'] = ['My Module', 'Manage entries of my module'];
```

---

## DCA für Backend-Module

Vollständiges Beispiel mit zwei verbundenen Tabellen (Vendor/Parts):

### tl_vendor (Eltern-Tabelle)

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

## Verwandte Skills

- `contao-backend-routes` — Eigene Backend-Controller und Menüeinträge
- `contao-dca-reference` — Vollständige DCA-Referenz (existierender Skill)

---

*Quelle: https://docs.contao.org/5.x/dev/framework/back-end-modules/*  
*https://docs.contao.org/5.x/dev/guides/dca/*
