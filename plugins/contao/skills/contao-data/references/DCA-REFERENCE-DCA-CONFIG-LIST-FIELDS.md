# Contao 5.x DCA — Config, List, Fields

## Contents

- [Overview](#overview)
- [1. config](#1-config)
- [2. list](#2-list)
- [3. fields](#3-fields)

## Overview

The **Data Container Array (DCA)** is the central configuration format for database-backed backend forms and list views in Contao. It is divided into five main areas: `config`, `list`, `fields`, `palettes` and `callbacks`.

---

## 1. config

Configures the table itself (data container type, versioning, relations, callbacks).

### Minimal example

```php
use Contao\DC_Table;

// contao/dca/tl_example.php
$GLOBALS['TL_DCA']['tl_example']['config'] = [
    'dataContainer' => DC_Table::class,
    'enableVersioning' => true,
    'sql' => [
        'keys' => [
            'id' => 'primary',
        ],
    ],
];
```

### config key reference

| Key | Type | Description |
|-----------|-----|--------------|
| `label` | `string` | Label for page or file trees (reference to `$GLOBALS['TL_LANG']`) |
| `ptable` | `string` | Parent table (table.pid = ptable.id) |
| `dynamicPtable` | `bool` | Set the parent table dynamically (as in `tl_content`) |
| `ctable` | `array` | Child tables (table.id = ctable.pid) |
| `dataContainer` | `string` | `\Contao\DC_Table`, `\Contao\DC_File` or `\Contao\DC_Folder` |
| `markAsCopy` | `string` | Name of the field that receives "(copy)" when copying |
| `uploadPath` | `string` | Path to the root folder of the file manager |
| `validFileTypes` | `string` | Comma-separated list of allowed file extensions |
| `editableFileTypes` | `string` | File extensions editable in the source code editor |
| `databaseAssisted` | `bool` | File manager synchronises with a database table |
| `closed` | `bool` | No new records |
| `notEditable` | `bool` | Table not editable |
| `notDeletable` | `bool` | Records not deletable |
| `notSortable` | `bool` | Records not sortable |
| `notCopyable` | `bool` | Records not copyable |
| `notCreatable` | `bool` | No new records (duplicating still possible) |
| `switchToEdit` | `bool` | "Save and edit" button on creation (sorting mode 4 only) |
| `enableVersioning` | `bool` | Store old versions |
| `hideVersionMenu` | `bool` | Hide the version dropdown |
| `doNotCopyRecords` | `bool` | Do not copy child table records when duplicating |
| `doNotDeleteRecords` | `bool` | Do not delete child table records when deleting |
| `backlink` | `string` | Optional query parameters for the back link (e.g. `do=news`) |
| `backendSearchIgnore` | `bool` | As of 5.7: exclude data from the backend search (DC_Table only) |
| `oncreate_callback` | `array` | Called when a record is created |
| `onload_callback` | `array` | Called when the DataContainer is initialised |
| `onbeforesubmit_callback` | `array` | Called before the form is submitted |
| `onsubmit_callback` | `array` | Called after a record is updated |
| `ondelete_callback` | `array` | Called when deleting |
| `oncut_callback` | `array` | Called when moving |
| `oncopy_callback` | `array` | Called when duplicating |
| `onundo_callback` | `array` | Called when restoring |
| `oncreate_version_callback` | `array` | Called when a version is created |
| `onrestore_version_callback` | `array` | Called when a version is restored |
| `onpalette_callback` | `array` | As of 5.3: called while the palette is being built |
| `sql` | `array` | Table configuration (keys, indexes) |

### config.sql reference

```php
$GLOBALS['TL_DCA']['tl_example']['config']['sql'] = [
    'engine'  => 'InnoDB',   // optional, storage engine
    'charset' => 'utf8mb4',  // optional, character set
    'keys' => [
        'id'          => 'primary',
        'foobar'      => 'index',
        'alias'       => 'unique',
        'lorem,ipsum' => 'index', // combined index
    ],
];
```

---

## 2. list

Defines how records are presented in the backend.

### 2.1 list.sorting

```php
$GLOBALS['TL_DCA']['tl_example']['list']['sorting'] = [
    'mode'         => 2,
    'flag'         => 1,
    'panelLayout'  => 'filter;search,limit',
    'fields'       => ['title'],
];
```

#### Sorting modes (`mode`)

| Value | Constant | Description |
|------|-----------|--------------|
| `0` | — | No sorting |
| `1` | `MODE_SORTED` | Sorting by a fixed field |
| `2` | `MODE_SORTABLE` | Sorting by a selectable field |
| `3` | `MODE_UNSORTED` | Sorting by parent table |
| `4` | `MODE_PARENT` | Child entries of a parent record (e.g. content elements) |
| `5` | `MODE_TREE` | Tree view (e.g. page structure) |
| `6` | `MODE_TREE_EXTENDED` | Child entries within the tree (e.g. articles) |

#### Sorting flags (`flag`)

| Value | Constant | Description |
|------|-----------|--------------|
| `1` | `SORT_INITIAL_LETTER_ASC` | Initial letter ascending |
| `2` | `SORT_INITIAL_LETTER_DESC` | Initial letter descending |
| `3` | `SORT_INITIAL_TWO_LETTERS_ASC` | First two letters ascending |
| `4` | `SORT_INITIAL_TWO_LETTERS_DESC` | First two letters descending |
| `5` | `SORT_DAY_ASC` | Day ascending |
| `6` | `SORT_DAY_DESC` | Day descending |
| `7` | `SORT_MONTH_ASC` | Month ascending |
| `8` | `SORT_MONTH_DESC` | Month descending |
| `9` | `SORT_YEAR_ASC` | Year ascending |
| `10` | `SORT_YEAR_DESC` | Year descending |
| `11` | `SORT_ASC` | Ascending |
| `12` | `SORT_DESC` | Descending |

#### All sorting keys

| Key | Type | Description |
|-----------|-----|--------------|
| `mode` | `int` | Sorting mode (see above) |
| `flag` | `int` | Sorting direction/type |
| `panelLayout` | `string` | Panel options: `search`, `sort`, `filter`, `limit`; comma = space, semicolon = line break |
| `fields` | `array` | Default sorting fields |
| `headerFields` | `array` | Fields in the header element (mode 4 only) |
| `icon` | `string` | Tree icon path (modes 5–6) |
| `root` | `array` | Root record IDs (page mounts) |
| `rootPaste` | `bool` | Paste buttons at root level (default: `false`) |
| `filter` | `array` | Custom query filters |
| `disableGrouping` | `bool` | Disable group headers in list/parent view |
| `defaultSearchField` | `string` | Default search field; fallback for breadcrumb labels (as of 5.3) |
| `paste_button_callback` | Callback | Custom paste buttons |
| `child_record_callback` | Callback | Render child entries (mode 4 only) |
| `header_callback` | Callback | Modify header fields (mode 4 only) |
| `panel_callback` | Callback | Include custom panel HTML |
| `child_record_class` | `string` | CSS class for parent view elements |
| `renderAsGrid` | `bool` | Show records as grid tiles |

### 2.2 list.label

```php
$GLOBALS['TL_DCA']['tl_example']['list']['label'] = [
    'fields'      => ['title', 'user_id:tl_user.name'],
    'showColumns' => false,
    'format'      => '%s (%s)',
];
```

| Key | Type | Description |
|-----------|-----|--------------|
| `fields` | `array` | Fields to display (format `field` or `field:table.column` for joins) |
| `showColumns` | `bool` | Generate a table header with column names |
| `showFirstOrderBy` | `bool` | Always show the first sorting field (default: `true`) |
| `format` | `string` | HTML format string (e.g. `'%s (%s)'`) |
| `maxCharacters` | `int` | Maximum label characters |
| `group_callback` | Callback | Custom group headers |
| `label_callback` | Callback | Custom labels |

### 2.3 list.global_operations

```php
$GLOBALS['TL_DCA']['tl_example']['list']['global_operations'] = [
    'all' => [
        'label'      => &$GLOBALS['TL_LANG']['MSC']['all'],
        'href'       => 'act=selectAll',
        'class'      => 'header_edit_all',
        'attributes' => 'onclick="Backend.getScrollOffset()" accesskey="e"',
    ],
];

// As of Contao 5.3: shorthand notation
$GLOBALS['TL_DCA']['tl_example']['list']['global_operations'] = [
    'all',
    'toggleNodes',
    'my_op' => ['href' => 'do=my_operation'],
];
```

| Key | Type | Description |
|-----------|-----|--------------|
| `label` | `string` | Button caption |
| `href` | `string` | URL fragment (e.g. `act=editAll`) |
| `icon` | `string` | Icon path/file name |
| `class` | `string` | CSS class |
| `attributes` | `string` | Additional HTML attributes |
| `button_callback` | Callback | Custom button generation |
| `route` | `string` | Symfony route name |
| `prefetch` | `bool` | Disable Turbo prefetch (as of 5.5) |
| `showOnSelect` | `bool` | Visibility during "edit all" |

### 2.4 list.operations

```php
// Default operations:
$GLOBALS['TL_DCA']['tl_example']['list']['operations'] = [
    'edit',
    'children',
    'copy',
    'cut',
    'delete',
    'toggle',
    'show',
];

// As of 5.5: ! forces display in the overview instead of the context menu
$GLOBALS['TL_DCA']['tl_example']['list']['operations'] = [
    '!edit',
    '!children',
    'copy',
    'cut',
    'delete',
    'toggle',
    'show',
];
```

| Key | Type | Description |
|-----------|-----|--------------|
| `label` | `string` | Button caption |
| `href` | `string` | URL fragment |
| `icon` | `string` | Icon path |
| `attributes` | `string` | Additional HTML attributes |
| `button_callback` | Callback | Custom button generation |
| `showInHeader` | `bool` | Show in the header element (mode 4 only) |
| `route` | `string` | Symfony route redirect |
| `primary` | `bool` | Show in the overview instead of the context menu (as of 5.5) |
| `prefetch` | `bool` | Disable Turbo prefetch (as of 5.5) |

#### Toggle operation

```php
$GLOBALS['TL_DCA']['tl_foobar']['list']['operations']['toggle'] = [
    'href' => 'act=toggle&amp;field=published',
    'icon' => 'visible.svg',
];

$GLOBALS['TL_DCA']['tl_foobar']['fields']['published'] = [
    'toggle'    => true,
    'inputType' => 'checkbox',
    'sql'       => ['type' => 'boolean', 'default' => false],
];

// Reversed toggle:
$GLOBALS['TL_DCA']['tl_foobar']['fields']['invisible'] = [
    'reverseToggle' => true,
    'inputType'     => 'checkbox',
    'sql'           => ['type' => 'boolean', 'default' => false],
];
```

---

## 3. fields

Defines table columns and form widgets.

### 3.1 Minimal example

```php
$GLOBALS['TL_DCA']['tl_example']['fields']['myfield'] = [
    'label'     => &$GLOBALS['TL_LANG']['tl_example']['myfield'],
    'exclude'   => true,
    'inputType' => 'text',
    'eval'      => ['tl_class' => 'w50', 'maxlength' => 255],
    'sql'       => "varchar(255) NOT NULL default ''",
];
```

### 3.2 All field keys

| Key | Type | Description |
|-----------|-----|--------------|
| `label` | `array` | Field label with description (reference to `$GLOBALS['TL_LANG']`) |
| `default` | mixed | Default value for new records |
| `exclude` | `bool` | As of 5.3 defaults to `true`; excluded for non-admins |
| `toggle` | `bool` | Field triggers a toggle action |
| `reverseToggle` | `bool` | Reverse the toggle action |
| `search` | `bool` | Include in the search menu and backend search |
| `backendSearch` | `bool` | Overrides `search` for the backend search only (as of 5.7) |
| `sorting` | `bool` | Include in the sorting menu |
| `filter` | `bool` | Include in the filter menu |
| `flag` | `int` | Sorting mode (1–12) |
| `length` | `int` | Number of characters for sorting groups (flags 3–4) |
| `inputType` | `string` | Widget type |
| `options` | `array` | Options for select/radio fields |
| `options_callback` | `array` | Callback returning the options |
| `enum` | `BackedEnum` | Fill options/reference from an enum (as of 5.3) |
| `foreignKey` | `string` | Load options from a database table |
| `reference` | `array` | Translation reference for options |
| `explanation` | `string` | Array key for the help wizard text |
| `input_field_callback` | `array` | Custom input field (not saved automatically) |
| `eval` | `array` | Field-specific configuration |
| `wizard` | `array` | Callback functions for the wizard |
| `sql` | `string\|array` | Database field definition |
| `relation` | `array` | Relations to other tables |
| `targetColumn` | `string` | JSON storage column for virtual fields (as of 5.7, default: `jsonData`) |
| `load_callback` | `array` | Called when the field is loaded |
| `save_callback` | `array` | Called when the field is saved |
| `xlabel` | `array` | HTML after the field label |
| `attributes_callback` | `array` | Adjust field attributes dynamically |

### 3.3 inputType — all available types

| inputType | Widget |
|-----------|--------|
| `checkbox` | Checkbox (single or multiple) |
| `checkboxWizard` | Checkbox wizard with sorting |
| `chmod` | CHMOD table |
| `fileTree` | File tree picker |
| `imageSize` | Two text fields + unit dropdown |
| `inputUnit` | Text field + unit dropdown |
| `keyValueWizard` | Key » value wizard |
| `listWizard` | List wizard |
| `metaWizard` | File manager meta information |
| `moduleWizard` | Module wizard |
| `optionWizard` | Option wizard |
| `pageTree` | Page tree picker |
| `password` | Password field |
| `picker` | Generic picker |
| `radio` | Radio buttons |
| `radioTable` | Table with images and radio buttons |
| `sectionWizard` | Page layout sections |
| `select` | Dropdown menu |
| `serpPreview` | Search engine result preview |
| `tableWizard` | Table wizard |
| `text` | Text field |
| `textStore` | Text field (do not display the value) |
| `textarea` | Textarea |
| `timePeriod` | Text field + dropdown |
| `trbl` | Four text fields + unit dropdown |

### 3.4 eval — all options

| Key | Type | Description |
|-----------|-----|--------------|
| `allowHtml` | `bool` | Accept HTML input according to the backend settings |
| `alwaysSave` | `bool` | Always save, even if unchanged |
| `autogrow` | `bool` | Enable textarea autogrow (default `true`, as of 5.7) |
| `basicEntities` | `bool` | Convert basic entities when editing/saving |
| `blankOptionLabel` | `string` | Label for the blank option (default `-`) |
| `chosen` | `bool` | Enhance selects with Chosen/Choices.js (as of 5.5) |
| `collapseUncheckedGroups` | `bool` | Collapse option groups without checked elements |
| `colorpicker` | `bool` | Add a colour picker |
| `cols` | `int` | Number of columns for textarea/radioTable/tableWizard |
| `csv` | `string` | Separator for list fields instead of serialising |
| `customRgxp` | `string` | Custom regular expression |
| `errorMsg` | `string` | Error message for `customRgxp` |
| `customTpl` | `string` | Custom template file name |
| `datepicker` | `bool` | Add the MooTools DatePicker |
| `dcaPicker` | `bool\|array` | Show the generic picker |
| `decodeEntities` | `bool` | Decode HTML entities |
| `disabled` | `bool` | Disable the field |
| `doNotCopy` | `bool` | Skip when duplicating |
| `doNotSaveEmpty` | `bool` | Do not save empty values |
| `doNotShow` | `bool` | Hide in "edit all"/details |
| `doNotTrim` | `bool` | Skip whitespace trimming |
| `encrypt` | `bool` | Store encrypted |
| `extensions` | `string` | Allowed file extensions (comma-separated) |
| `fallback` | `bool` | Assign only once per table |
| `feEditable` | `bool` | Editable in the front end (tl_member only) |
| `feGroup` | `string` | Registration form section |
| `fieldType` | `string` | `checkbox`/`radio` for file/page trees |
| `files` | `bool` | Show files and folders in the file tree |
| `filesOnly` | `bool` | Hide checkboxes/radio buttons on folders |
| `findInSet` | `bool` | Sort by option values instead of labels |
| `helpwizard` | `bool` | Show the help wizard icon |
| `hideInput` | `bool` | Hide the field value display |
| `includeBlankOption` | `bool` | Add a blank option to the dropdown |
| `isAssociative` | `bool` | Mark the options array as associative |
| `isBoolean` | `bool` | Mark the field as boolean |
| `isGallery` | `bool` | Show fileTree elements as a gallery |
| `isHexColor` | `bool` | Hex colour notation with automatic clean-up |
| `isSortable` | `bool` | Enable sorting for the selected elements |
| `mandatory` | `bool` | Mandatory field |
| `maxlength` | `int` | Maximum number of characters |
| `maxval` | `int` | Maximum numeric value |
| `metaFields` | `array` | Available fields for the metaWizard |
| `minlength` | `int` | Minimum number of characters |
| `minval` | `int` | Minimum numeric value |
| `multiple` | `bool` | Multiple selection |
| `nospace` | `bool` | Disallow spaces |
| `orderField` | `string` | Column for the sort order of the selected elements |
| `path` | `string` | Custom root directory for the file tree |
| `placeholder` | `string` | Placeholder text |
| `preserveTags` | `bool` | Keep all HTML tags |
| `readonly` | `bool` | Read-only field |
| `rgxp` | `string` | Regular expression (see below) |
| `rows` | `int` | Number of rows for textarea/tableWizard |
| `rte` | `string` | Rich text editor (`ace`, `tinyMCE`) |
| `size` | `int` | Size of a multiple select / number of input fields |
| `showFilePreview` | `bool` | Show regular files as images |
| `spaceToUnderscore` | `bool` | Replace spaces with underscores |
| `style` | `string` | Inline CSS |
| `submitOnChange` | `bool` | Submit the form when the value changes |
| `tl_class` | `string` | CSS classes |
| `trailingSlash` | `bool` | Add/remove a trailing slash |
| `unique` | `bool` | Unique value |
| `uploadFolder` | `string` | Target folder for the upload widget |
| `useRawRequestData` | `bool` | Use the raw Symfony request data (bypasses filtering!) |
| `versionize` | `bool` | Include in versioning (default `true`) |

#### tl_class CSS classes

| Class | Description |
|--------|--------------|
| `w25` | 25% width, left aligned (as of 5.1) |
| `w33` | 33.33% width, left aligned (as of 5.1) |
| `w50` | 50% width, left aligned |
| `w66` | 66.67% width, left aligned (as of 5.1) |
| `w75` | 75% width, left aligned (as of 5.1) |
| `clr` | Clear floats (`clear:both`) |
| `wizard` | Shortened for wizard buttons |
| `long` | Entire available width |
| `cbx` | Minimum height 46px (single checkboxes) |
| `m12` | 17px top/bottom spacing |
| `cbx m12` | Combined: 80px minimum height |

#### rgxp — regular expressions

| Value | Description |
|------|--------------|
| `digit` | Numeric characters, period, minus, decimal comma |
| `natural` | Non-negative natural numbers |
| `alpha` | Alphabetic, period, minus, space |
| `alnum` | Alphanumeric, period, minus, underscore, space |
| `extnd` | Disallows `#<>()\\=` |
| `date` | Valid date |
| `time` | Valid time |
| `datim` | Valid date and time |
| `friendly` | E-mail in "friendly name" format |
| `email` | Valid e-mail address |
| `emails` | Valid e-mail list |
| `url` | Valid URL |
| `alias` | Valid alias |
| `folderalias` | Valid folder URL alias |
| `phone` | Phone number |
| `prcnt` | Numbers 0–100 |
| `locale` | Valid locale (e.g. `de_CH`) |
| `language` | Valid language code (e.g. `de-CH`) |
| `fieldname` | Valid field name |
| `httpurl` | Absolute URL (http/https) |
| `custom` | Custom regex via `customRgxp` |

### 3.5 sql — column definition

**As a string:**
```php
'sql' => "varchar(255) NOT NULL default ''"
```

**As a Doctrine schema array:**

| Doctrine schema | SQL equivalent |
|-----------------|----------------|
| `['type' => 'string', 'length' => 32, 'default' => '']` | `VARCHAR(32) NOT NULL DEFAULT ''` |
| `['type' => 'string', 'length' => 1, 'fixed' => true, 'default' => '']` | `CHAR(1) NOT NULL DEFAULT ''` |
| `['type' => 'integer', 'notnull' => false, 'unsigned' => true]` | `INT UNSIGNED NULL` |
| `['type' => 'binary', 'length' => 16, 'fixed' => true, 'notnull' => false]` | `BINARY(16) NULL` |
| `['type' => 'boolean', 'default' => false]` | `TINYINT(1) NOT NULL DEFAULT 0` |
| `['type' => 'blob', 'notnull' => false]` | `BLOB NULL` |
| `['type' => 'text', 'notnull' => false]` | `TEXT NULL` |

### 3.6 relation

```php
'relation' => [
    'type'  => 'hasOne',   // hasOne | hasMany | belongsTo | belongsToMany
    'load'  => 'lazy',     // lazy | eager
    'table' => 'tl_files', // optional, extracted from foreignKey
    'field' => 'uuid',     // optional, default: id
],
```

| `type` | Description |
|--------|--------------|
| `hasOne` | Child record |
| `hasMany` | Serialised child records |
| `belongsTo` | Parent record |
| `belongsToMany` | Serialised parent records |

### 3.7 Enumerations (as of Contao 5.3)

```php
// PHP enum with TranslatableLabelInterface
enum Salutation: string implements \Contao\CoreBundle\Translation\TranslatableLabelInterface
{
    case ms = 'ms';
    case mr = 'mr';
    case mx = 'mx';

    public function label(): \Symfony\Component\Translation\TranslatableMessage
    {
        return new \Symfony\Component\Translation\TranslatableMessage(
            'salutation.label.' . $this->value,
            [],
            'messages',
        );
    }
}

// DCA usage
$GLOBALS['TL_DCA']['tl_member']['fields']['salutation'] = [
    'inputType' => 'select',
    'enum'      => Salutation::class,
];
```

### 3.8 Virtual fields (as of Contao 5.7)

Fields without an SQL definition are treated as virtual fields automatically and stored in a JSON column (`jsonData`).

```php
// Virtual field
$GLOBALS['TL_DCA']['tl_content']['fields']['example1'] = [
    'inputType' => 'text',
    // no 'sql' definition → virtual, stored in jsonData
];

// Custom target column
$GLOBALS['TL_DCA']['tl_content']['fields']['example1'] = [
    'inputType'    => 'text',
    'targetColumn' => 'foobar', // JSON data in a custom column
];
```

**Limitations:** filtering/searching virtual fields is only supported within `DC_Table`.

---

*Sources:*
- https://docs.contao.org/5.x/dev/reference/dca/config/
- https://docs.contao.org/5.x/dev/reference/dca/list/
- https://docs.contao.org/5.x/dev/reference/dca/fields/
