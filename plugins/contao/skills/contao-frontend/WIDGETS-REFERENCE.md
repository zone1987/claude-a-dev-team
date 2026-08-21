# Contao 5.x Backend Widget Reference

Backend widgets are the form elements for the record editing masks in the Contao back end, configured via `inputType` in the DCA array.

---

## Contents

- [checkbox](#checkbox)
- [checkboxWizard](#checkboxwizard)
- [fileTree](#filetree)
- [imageSize](#imagesize)
- [inputUnit](#inputunit)
- [listWizard](#listwizard)
- [moduleWizard](#modulewizard)
- [optionWizard](#optionwizard)
- [password](#password)
- [picker](#picker)
- [radio](#radio)
- [select](#select)
- [serpPreview](#serppreview)
- [tableWizard](#tablewizard)
- [text](#text)
- [textarea](#textarea)
- [timePeriod](#timeperiod)
- [Undocumented widgets](#undocumented-widgets)

## checkbox

Renders one or more checkboxes.

**inputType:** `checkbox`

| Key | Type | Description |
|-----------|-----|--------------|
| `inputType` | `string` | `checkbox` |
| `options` | `array` | Options array (combined with `eval.multiple`) |
| `options_callback` | `callable` | Callback that returns the options |
| `reference` | `array` | Translation reference for options |
| `foreignKey` | `string` | Load options from another table |
| `eval.multiple` | `bool` | Enable multiple selection |
| `eval.includeBlankOption` | `bool` | Include a blank option |
| `eval.blankOptionLabel` | `string` | Label of the blank option (default: `-`) |

**Options array formats:**
1. `['label1', 'label2']` — index as value
2. `['value' => 'label']` — value => label
3. `['foo' => ['a', 'b'], 'bar' => ['c', 'd']]` — grouped checkboxes

**SQL column definition:**
- Single checkbox (toggle): `boolean` or `'1'/'0'`
- Multiple selection: `blob` (serialized array)

**Examples:**

```php
// Toggle checkbox
'myCheckbox' => [
    'inputType' => 'checkbox',
    'sql' => ['type' => 'boolean', 'default' => false],
],

// Fixed options
'myCheckbox' => [
    'inputType' => 'checkbox',
    'options' => ['foo', 'bar', 'baz'],
    'eval' => ['multiple' => true],
    'sql' => ['type' => 'blob', 'notnull' => false],
],

// Dynamic options
'myCheckbox' => [
    'inputType' => 'checkbox',
    'options_callback' => ['Vendor\Class', 'getOptions'],
    'eval' => ['multiple' => true],
    'sql' => ['type' => 'blob', 'notnull' => false],
],

// Options from a table
'myUsers' => [
    'inputType' => 'checkbox',
    'foreignKey' => 'tl_user.name',
    'sql' => ['type' => 'string', 'notnull' => false, 'default' => ''],
],
```

**Contao usage:** Everywhere — a simple checkbox is often used as a subpalette selector.

---

## checkboxWizard

Like `checkbox`, but with manual sorting of the selected elements.

**inputType:** `checkboxWizard`

Identical options to `checkbox` (see above). Useful when the order of the selection matters.

**Contao usage:** Page layout settings (CSS framework, JS templates), image formats in responsive image sizes.

---

## fileTree

Renders a file tree picker for selecting files or folders.

**inputType:** `fileTree`

| Key | Type | Description |
|-----------|-----|--------------|
| `inputType` | `string` | `fileTree` |
| `eval.extensions` | `string` | Allowed file extensions (comma-separated) |
| `eval.fieldType` | `string` | `checkbox` (multiple selection) / `radio` (single selection) |
| `eval.files` | `bool` | Show files and folders; `false` = folders only |
| `eval.filesOnly` | `bool` | Hide radio buttons/checkboxes for folders |
| `eval.isGallery` | `bool` | Show the selected files as a gallery |
| `eval.isSortable` | `bool` | Enable sorting of the selected elements |
| `eval.multiple` | `bool` | Enable multiple selection |
| `eval.path` | `string` | Custom root directory for the file tree |
| `eval.showFilePreview` | `bool` | Show regular files as images |

**Examples:**

```php
// Single image selection
'singleSRC' => [
    'exclude' => true,
    'inputType' => 'fileTree',
    'eval' => [
        'filesOnly'  => true,
        'fieldType'  => 'radio',
        'extensions' => '%contao.image.valid_extensions%',
    ],
    'sql' => ['type' => 'binary', 'length' => 16, 'fixed' => true, 'notnull' => false],
],

// Image gallery (multiple selection)
'multiSRC' => [
    'exclude' => true,
    'inputType' => 'fileTree',
    'eval' => [
        'fieldType'  => 'checkbox',
        'files'      => true,
        'isGallery'  => true,
        'multiple'   => true,
        'extensions' => '%contao.image.valid_extensions%',
    ],
    'sql' => ['type' => 'blob', 'notnull' => false],
],

// Folder selection
'folders' => [
    'inputType' => 'fileTree',
    'eval' => [
        'files'     => false,
        'fieldType' => 'checkbox',
        'multiple'  => true,
    ],
    'sql' => ['type' => 'blob', 'notnull' => false],
],
```

**Contao usage:** Text, download, image and gallery content elements.

---

## imageSize

Dropdown plus two text fields for the image size definition.

**inputType:** `imageSize`

No special options — all `text` widget options apply.

**Stored value:** Serialized image size array.

```php
'size' => [
    'exclude' => true,
    'inputType' => 'imageSize',
    'reference' => &$GLOBALS['TL_LANG']['MSC'],
    'eval' => [
        'rgxp'               => 'natural',
        'includeBlankOption' => true,
        'nospace'            => true,
        'tl_class'           => 'w50',
    ],
    'options_callback' => ['contao.listener.image_size_options', '__invoke'],
    'sql' => ['type' => 'string', 'length' => 128, 'default' => ''],
],
```

**Overriding the options via callback:**
```php
use Contao\CoreBundle\DependencyInjection\Attribute\AsCallback;
use Contao\CoreBundle\Image\ImageSizes;

#[AsCallback(table: 'tl_content', target: 'fields.size.options')]
class ImageSizeOptionsListener
{
    public function __construct(private readonly ImageSizes $imageSizes) {}

    public function __invoke(): array
    {
        return $this->imageSizes->getAllOptions();
    }
}
```

**Contao usage:** Text, image and gallery content elements.

---

## inputUnit

Text field with a small dropdown menu for the unit.

**inputType:** `inputUnit`

| Key | Type | Description |
|-----------|-----|--------------|
| `inputType` | `string` | `inputUnit` |
| `options` | `array` | Options for the dropdown |
| `reference` | `array` | Translation reference for the dropdown options |

**Stored value:** Serialized associative array with the keys `value` and `unit`.

```php
'headline' => [
    'exclude' => true,
    'inputType' => 'inputUnit',
    'options' => ['h1', 'h2', 'h3', 'h4', 'h5', 'h6'],
    'eval' => [
        'maxlength'     => 200,
        'basicEntities' => true,
        'tl_class'      => 'w50',
    ],
    'sql' => [
        'type'    => 'string',
        'length'  => 255,
        'default' => 'a:2:{s:5:"value";s:0:"";s:4:"unit";s:2:"h2";}',
    ],
],
```

**Contao usage:** Headline input in content elements and modules.

---

## listWizard

Expandable list wizard with add, remove and reorder.

**inputType:** `listWizard`

| Key | Type | Description |
|-----------|-----|--------------|
| `inputType` | `string` | `listWizard` |
| `eval.allowHtml` | `bool` | Allow HTML input in the list fields |
| `eval.maxlength` | `int` | Maximum number of characters per list field |

```php
use Doctrine\DBAL\Platforms\MySQLPlatform;

'jobTitles' => [
    'inputType' => 'listWizard',
    'eval' => ['maxlength' => 32],
    'sql' => [
        'type'    => 'blob',
        'length'  => MySQLPlatform::LENGTH_LIMIT_BLOB,
        'notnull' => false,
    ],
],
```

**Contao usage:** Only in the list content element.

---

## moduleWizard

Assigns front end modules to the layout sections (`tl_layout` only).

**inputType:** `moduleWizard`

No special options.

```php
use Doctrine\DBAL\Platforms\MySQLPlatform;

'modules' => [
    'default'   => [['mod' => 0, 'col' => 'main', 'enable' => 1]],
    'inputType' => 'moduleWizard',
    'sql' => [
        'type'    => 'blob',
        'length'  => MySQLPlatform::LENGTH_LIMIT_BLOB,
        'notnull' => false,
    ],
],
```

**Contao usage:** Page layout settings in `tl_layout`.

---

## optionWizard

Expandable list of options for select fields (with copy, delete, reorder, default option, groups).

**inputType:** `optionWizard`

No special options.

```php
'foobar' => [
    'inputType' => 'optionWizard',
    'sql' => ['type' => 'blob', 'notnull' => false],
],
```

**Contao usage:** Form generator for select form fields.

---

## password

Password text field (`type="password"`) with a reveal button.

**inputType:** `password`

All `text` widget options apply.

```php
'myPassword' => [
    'inputType' => 'password',
    'eval' => [
        'mandatory' => true,
        'minlength' => Config::get('minPasswordLength'),
        'tl_class'  => 'w50',
    ],
    'sql' => ['type' => 'string', 'length' => 255, 'default' => ''],
],
```

---

## picker

Generic picker for arbitrary data container elements. Shows a back end view in a popup.

**inputType:** `picker`

| Key | Type | Description |
|-----------|-----|--------------|
| `inputType` | `string` | `picker` |
| `foreignKey` | `string` | Table for the picker selection |
| `relation` | `array` | Table reference via `'table' => 'tl_foobar'` |
| `eval.multiple` | `bool` | Multiple selection |
| `eval.isSortable` | `bool` | Drag-and-drop sorting for multiple selection |

**SQL:** single → `integer`; multiple → `blob` (serialized array)

```php
// News article (single selection)
'myNewsReference' => [
    'inputType' => 'picker',
    'sql' => ['type' => 'integer', 'unsigned' => true, 'default' => 0],
    'relation' => ['type' => 'hasOne', 'load' => 'lazy', 'table' => 'tl_news'],
],

// Multiple content elements
'myContentElements' => [
    'inputType' => 'picker',
    'eval' => ['multiple' => true],
    'sql' => ['type' => 'blob', 'notnull' => false],
    'relation' => ['type' => 'hasMany', 'load' => 'lazy', 'table' => 'tl_content'],
],

// Custom data container (requires a custom PickerProvider)
'myProducts' => [
    'inputType' => 'picker',
    'eval' => ['multiple' => true],
    'sql' => ['type' => 'blob', 'notnull' => false],
    'relation' => ['type' => 'hasMany', 'load' => 'lazy', 'table' => 'tl_product'],
],
```

**Custom PickerProvider:**
```php
namespace App\Picker;

use Contao\CoreBundle\Picker\AbstractTablePickerProvider;

class ProductsPickerProvider extends AbstractTablePickerProvider
{
    public function getName(): string { return 'productsPicker'; }
    protected function getDataContainer(): string { return \App\Driver\DC_Product::class; }
}
```

**Contao usage:** Content element include, article teaser.

---

## radio

Radio button selection.

**inputType:** `radio`

| Key | Type | Description |
|-----------|-----|--------------|
| `inputType` | `string` | `radio` |
| `options` | `array` | Options array |
| `options_callback` | `callable` | Callback that returns the options |
| `reference` | `array` | Translation reference |
| `foreignKey` | `string` | Options from another table |
| `eval.includeBlankOption` | `bool` | Include a blank option |
| `eval.blankOptionLabel` | `string` | Label of the blank option |
| `eval.disabled` | `bool` | Disable the field |

```php
// Simple radio buttons
'example' => [
    'inputType' => 'radio',
    'options' => ['lorem' => 'Lorem', 'ipsum' => 'Ipsum', 'dolor' => 'Dolor'],
    'sql' => ['type' => 'string', 'length' => 8, 'default' => 'lorem'],
],

// Options from a table
'example' => [
    'inputType' => 'radio',
    'foreignKey' => 'tl_user.name',
    'sql' => ['type' => 'integer', 'unsigned' => true, 'default' => 0],
],
```

---

## select

Dropdown menu (single or multiple), optionally with Choices.js/Chosen.

**inputType:** `select`

| Key | Type | Description |
|-----------|-----|--------------|
| `inputType` | `string` | `select` |
| `options` | `array` | Options array |
| `options_callback` | `callable` | Callback that returns the options |
| `reference` | `array` | Translation reference |
| `foreignKey` | `string` | Options from another table |
| `eval.multiple` | `bool` | Multiple selection |
| `eval.includeBlankOption` | `bool` | Include a blank option |
| `eval.blankOptionLabel` | `string` | Label of the blank option (default: `-`) |
| `eval.chosen` | `bool` | Enable Choices.js/Chosen.js (as of 5.5 from 8 options on) |
| `eval.disabled` | `bool` | Disable the field |

**Options array formats:**
1. `['label1', 'label2']` — index as value
2. `['value' => 'label']` — value => label
3. `['gruppe' => ['a', 'b']]` — grouped select

**SQL:** single → `string`; multiple → `blob` (serialized array)

```php
// Simple select
'isVisible' => [
    'inputType' => 'select',
    'options' => ['always', 'never', 'auto'],
    'sql' => ['type' => 'string', 'length' => 8, 'default' => 'auto'],
],

// Grouped select
'mySelect' => [
    'inputType' => 'select',
    'options' => [
        'news'   => ['news_reader', 'news_list'],
        'events' => ['event_reader', 'event_list'],
    ],
    'sql' => ['type' => 'string', 'length' => 16, 'default' => ''],
],

// Dynamic options with a search box
'mySelect' => [
    'inputType' => 'select',
    'options_callback' => ['Vendor\Class', 'getOptions'],
    'eval' => ['chosen' => true],
    'sql' => ['type' => 'string', 'length' => 16, 'default' => ''],
],

// Options from a table
'myUsers' => [
    'inputType' => 'select',
    'foreignKey' => 'tl_user.name',
    'eval' => ['chosen' => true],
    'sql' => ['type' => 'integer', 'unsigned' => true, 'default' => 0],
],
```

---

## serpPreview

Shows a preview of how a search engine renders the title and description.

**inputType:** `serpPreview`

| Key | Type | Description |
|-----------|-----|--------------|
| `inputType` | `string` | `serpPreview` |
| `eval.titleFields` | `array` | Title fields — the first non-empty value is used |
| `eval.descriptionFields` | `array` | Description fields — the first non-empty value is used |
| `eval.title_tag_callback` | `callable` | Returns the title format (e.g. `'%s - My Website'`) |
| `eval.url_callback` | `callable` | Returns the URL for the record |

```php
'serpPreview' => [
    'inputType' => 'serpPreview',
    'eval' => [
        'title_tag_callback'  => static fn (): string => '%s - Example Website',
        'titleFields'         => ['pageTitle', 'headline'],
        'descriptionFields'   => ['description', 'teaser'],
    ],
    'sql' => null,
],
```

**Contao usage:** Page, news, calendar and FAQ settings.

---

## tableWizard

Table wizard (not yet fully documented in the official docs).

**inputType:** `tableWizard`

```php
'myTable' => [
    'inputType' => 'tableWizard',
    'sql' => ['type' => 'blob', 'notnull' => false],
],
```

**Contao usage:** Table content element.

---

## text

Standard text field (`<input type="text">`).

**inputType:** `text`

All `eval` options apply. The most important ones:

| Key | Type | Description |
|-----------|-----|--------------|
| `eval.maxlength` | `int` | Maximum number of characters |
| `eval.minlength` | `int` | Minimum number of characters |
| `eval.rgxp` | `string` | Validation regex |
| `eval.placeholder` | `string` | Placeholder text |
| `eval.mandatory` | `bool` | Mandatory field |
| `eval.readonly` | `bool` | Read-only |

```php
'myField' => [
    'inputType' => 'text',
    'eval' => ['maxlength' => 255, 'tl_class' => 'w50'],
    'sql' => ['type' => 'string', 'length' => 255, 'default' => ''],
],
```

---

## textarea

Multi-line text input, optionally with TinyMCE or the Ace editor.

**inputType:** `textarea`

| Key | Type | Description |
|-----------|-----|--------------|
| `eval.rte` | `string` | Rich text editor: `tinyMCE`, `ace`, `ace\|html`, `ace\|json`, etc. |
| `eval.rows` | `int` | Number of rows |
| `eval.cols` | `int` | Number of columns |

**SQL:** `text NULL` recommended.

```php
// Simple textarea
'myTextarea' => [
    'inputType' => 'textarea',
    'sql' => ['type' => 'text', 'notnull' => false],
],

// With TinyMCE
'myTextarea' => [
    'inputType' => 'textarea',
    'eval' => ['rte' => 'tinyMCE', 'helpwizard' => true],
    'sql' => ['type' => 'text', 'notnull' => false],
],

// With the Ace editor (JavaScript)
'myTextarea' => [
    'inputType' => 'textarea',
    'eval' => ['rte' => 'ace|js'],
    'sql' => ['type' => 'text', 'notnull' => false],
],
```

**Automatic processing:** With `ace|html` or templates containing "tiny", `allowHtml` and `decodeEntities` are enabled.

---

## timePeriod

Text field with a dropdown menu for time units.

**inputType:** `timePeriod`

| Key | Type | Description |
|-----------|-----|--------------|
| `inputType` | `string` | `timePeriod` |
| `options` | `array` | Options for the dropdown (e.g. `['s', 'm', 'h']`) |
| `reference` | `array` | Translation reference |
| `eval.disabled` | `bool` | Disable the field |
| `eval.maxlength` | `int` | Maximum number of characters |

**Stored value:** Serialized array (→ `blob` recommended).

```php
use Doctrine\DBAL\Platforms\MySQLPlatform;

'time' => [
    'inputType' => 'timePeriod',
    'options'   => ['s', 'm', 'h'],
    'reference' => &$GLOBALS['TL_LANG']['tl_foobar']['timePeriod'],
    'sql' => [
        'type'    => 'blob',
        'length'  => MySQLPlatform::LENGTH_LIMIT_BLOB,
        'notnull' => false,
    ],
],
```

**Translation file:**
```yaml
# translations/contao_tl_foobar.en.yaml
tl_foobar:
    s: Seconds
    m: Minutes
    h: Hours
```

---

## Undocumented widgets

The following widgets exist in the Contao core but are not yet documented in the official documentation, or only as a stub:

| inputType | Description |
|-----------|--------------|
| `chmod` | CHMOD table for file/folder permissions |
| `keyValueWizard` | Key-value wizard |
| `metaWizard` | File manager meta information |
| `pageTree` | Page tree picker (like `fileTree` for pages) |
| `radioTable` | Table with images and radio buttons |
| `sectionWizard` | Page layout sections |
| `textStore` | Text field without value display |
| `trbl` | Four text fields plus unit dropdown (top/right/bottom/left) |

---

*Sources:*
- https://docs.contao.org/5.x/dev/reference/widgets/
- https://docs.contao.org/5.x/dev/reference/widgets/checkbox/
- https://docs.contao.org/5.x/dev/reference/widgets/checkboxwizard/
- https://docs.contao.org/5.x/dev/reference/widgets/filetree/
- https://docs.contao.org/5.x/dev/reference/widgets/imagesize/
- https://docs.contao.org/5.x/dev/reference/widgets/inputunit/
- https://docs.contao.org/5.x/dev/reference/widgets/listwizard/
- https://docs.contao.org/5.x/dev/reference/widgets/modulewizard/
- https://docs.contao.org/5.x/dev/reference/widgets/optionwizard/
- https://docs.contao.org/5.x/dev/reference/widgets/password/
- https://docs.contao.org/5.x/dev/reference/widgets/picker/
- https://docs.contao.org/5.x/dev/reference/widgets/radio/
- https://docs.contao.org/5.x/dev/reference/widgets/select/
- https://docs.contao.org/5.x/dev/reference/widgets/serppreview/
- https://docs.contao.org/5.x/dev/reference/widgets/tablewizard/
- https://docs.contao.org/5.x/dev/reference/widgets/text/
- https://docs.contao.org/5.x/dev/reference/widgets/textarea/
- https://docs.contao.org/5.x/dev/reference/widgets/time-period/
