# Contao 5.x DCA — Palettes & Callbacks

## 4. palettes

A palette is a group of form fields for editing a record. Palettes do not have to contain all table columns.

### 4.1 Main palettes

```php
$GLOBALS['TL_DCA']['tl_example'] = [
    'palettes' => [
        'default' => '{title_legend},title,alias,addImage',
    ],
];
```

At least one `default` palette should be defined.

### 4.2 __selector__ and subpalettes

Subpalettes are defined in `subpalettes` and appear dynamically via Ajax when a main palette field is active.

```php
$GLOBALS['TL_DCA']['tl_example'] = [
    'palettes' => [
        '__selector__' => ['addImage'],
        'default'      => '{title_legend},title,alias,addImage',
    ],
    'subpalettes' => [
        'addImage' => 'singleSRC,size',
    ],
];
```

**Recommendation:** set `submitOnChange` in eval so the subpalette appears/disappears immediately.

### 4.3 Subpalettes with select fields

Different subpalettes depending on the select field value, via the format `fieldName_fieldValue`:

```php
$GLOBALS['TL_DCA']['tl_example'] = [
    'palettes' => [
        '__selector__' => ['selectField'],
        'default'      => '{title_legend},title,alias,selectField',
    ],
    'subpalettes' => [
        'selectField_value1' => 'field1,field2',
        'selectField_value2' => 'field3,field4',
    ],
];
```

### 4.4 Multiple main palettes

A selector switches between multiple main palettes — the key corresponds to the selector value:

```php
$GLOBALS['TL_DCA']['tl_example'] = [
    'palettes' => [
        '__selector__' => ['type'],
        'default'      => '{title_legend},type',
        'text'         => '{title_legend},type,textField',
        'image'        => '{title_legend},type,imageField',
    ],
];
```

### 4.5 Legend groups

Commas separate fields, semicolons create new fieldsets. Every group has a _legend_:

```
{title_legend},headline,alias,author;{date_legend},date,time;{teaser_legend:collapsed},subheadline,teaser
```

- Legend captions come from `$GLOBALS['TL_LANG']['tl_news']['title_legend']`
- `:collapsed` = group collapsed by default

### 4.6 Palette Manipulator

```php
use Contao\CoreBundle\DataContainer\PaletteManipulator;

PaletteManipulator::create()
    ->addLegend('custom_legend', 'title_legend', PaletteManipulator::POSITION_AFTER)
    ->addField('myField', 'custom_legend', PaletteManipulator::POSITION_APPEND)
    ->applyToPalette('default', 'tl_example')
;
```

### 4.7 CSS classes for field arrangement (tl_class)

| Class | Description |
|--------|--------------|
| `w25` | 25% width, left (as of 5.1) |
| `w33` | 33.33% width, left (as of 5.1) |
| `w50` | 50% width, left |
| `w66` | 66.67% width, left (as of 5.1) |
| `w75` | 75% width, left (as of 5.1) |
| `clr` | Clear floats |
| `wizard` | Shortened for wizard buttons |
| `long` | Full available width |
| `cbx` | Minimum height 46px |
| `m12` | 17px top/bottom spacing |

---

## 5. callbacks

Callbacks are entry points for custom code in the DCA. They follow an event dispatcher pattern and are always bound to a specific DCA table.

### 5.1 Global callbacks (config.*)

#### config.onload

Executed when the DataContainer object is initialised. Useful for permission checks or runtime DCA modifications.

```php
use Contao\CoreBundle\DependencyInjection\Attribute\AsCallback;
use Contao\DataContainer;

#[AsCallback(table: 'tl_example', target: 'config.onload')]
class OnLoadListener
{
    public function __invoke(?DataContainer $dc): void
    {
        // Check permissions or adjust the DCA
    }
}
```

**Parameters:** `DataContainer|null`  
**Returns:** `void`

#### config.oncreate

Executed when a new record is created.

**Parameters:** `string $table`, `int $insertId`, `array $fields`, `DataContainer $dc`  
**Returns:** `void`

#### config.onbeforesubmit

Executed before the backend form is saved. Allows value changes and multi-field validation.

**Parameters:** `array $values`, `DataContainer $dc`  
**Returns:** `array` (record values)

#### config.onsubmit

Executed after the backend form has been saved.

**Parameters (backend):** `DataContainer $dc`  
**Parameters (front end "personal data"):** `FrontendUser $user`, `ModulePersonalData $module`  
**Returns:** `void`

#### config.ondelete

Executed before a record is deleted.

**Parameters (DC_Folder):** `string $filePath`, `DataContainer $dc`  
**Parameters (others):** `DataContainer $dc`, `int $undoId`  
**Returns:** `void`

#### config.oncut

Executed after a record has been moved.

**Parameters:** `DataContainer $dc`  
**Returns:** `void`

#### config.oncopy

Executed after a record has been duplicated.

**Parameters:** `int $insertId`, `DataContainer $dc`  
**Returns:** `void`

#### config.oncreate_version

Executed after an old record version has been added to `tl_version`.

**Parameters:** `string $table`, `int $parentId`, `int $version`, `array $data`  
**Returns:** `void`

#### config.onrestore_version

Executed after a record version has been restored.

**Parameters:** `string $table`, `int $parentId`, `int $version`, `array $data`  
**Returns:** `void`

#### config.onundo

Executed after a deleted record has been restored.

**Parameters:** `string $table`, `array $data`, `DataContainer $dc`  
**Returns:** `void`

#### config.oninvalidate_cache_tags

Executed when a record is changed via the backend. Allows additional cache tags to be added for invalidation.

**Parameters:** `DataContainer $dc`, `array $tags`  
**Returns:** `array` (cache tags to invalidate)

#### config.onshow

Adjusts the info modal window of a record.

**Parameters:** `array $existingData`, `array $recordData`, `DataContainer $dc`  
**Returns:** `array` (table rows and columns for the modal)

#### config.onpalette (as of 5.3)

Adjusts the palette dynamically based on object values.

**Parameters:** `string $palette`, `DataContainer $dc`  
**Returns:** `string` (adjusted palette)

---

### 5.2 Listing callbacks (list.*)

**Note:** all listing callbacks are singular — only one callback per event is allowed.

#### list.sorting.paste_button

Generates custom paste buttons. Only in tree or extended tree mode (modes 5 and 6).

**Parameters:** `DataContainer $dc`, `array $row`, `string $table`, `bool $cr`, `array $clipboard`, `array|null $children`, `string|null $previous`, `string|null $next`  
**Returns:** `string` (HTML for additional buttons)

#### list.sorting.child_record

Defines how child entries are rendered in the "parent view".

**Parameters:** `array $row`  
**Returns:** `string` (HTML)

#### list.sorting.header

Allows custom labels in the "parent view" header.

**Parameters:** `array $currentLabels`, `DataContainer $dc`  
**Returns:** `array` (header labels)

#### list.sorting.panel_callback.subpanel

Inserts HTML for custom panels. Replace `subpanel` with your own panel name.

**Parameters:** `DataContainer $dc`  
**Returns:** `string` (HTML)

#### list.label.group

Allows custom group headers in list views.

**Parameters:** `string $group`, `string $mode`, `string $field`, `array $row`, `DataContainer $dc`  
**Returns:** `string`

#### list.label.label

Allows custom labels in list views.

**Parameters (tree view):** `array $row`, `string $label`, `DataContainer $dc`, `string $imageAttr`, `bool $returnImage`, `bool $protected`  
**Parameters (list view):** `array $row`, `string $label`, `DataContainer $dc`, `array $columns`  
**Parameters (parent view):** `array $row`, `string $label`, `DataContainer $dc`  
**Returns:** `string` (tree/parent view) or `array` (list view with showColumns)

---

### 5.3 Operations callbacks (list.operations.*)

**Note:** all operations callbacks are singular.

#### list.global_operations.\<OPERATION\>.button

Generates custom buttons for global operations.

**Parameters:** `string|null $href`, `string $label`, `string $title`, `string $class`, `string $attributes`, `string $table`, `array $rootIds`  
**Returns:** `string` (HTML)

#### list.operations.\<OPERATION\>.button

Configures or replaces buttons for specific operations.

```php
use Contao\CoreBundle\DependencyInjection\Attribute\AsCallback;
use Contao\CoreBundle\DataContainer\DataContainerOperation;

#[AsCallback(table: 'tl_example', target: 'list.operations.edit.button')]
class EditButtonListener
{
    public function __invoke(DataContainerOperation $operation): void
    {
        if (!$this->isAllowed($operation->getRecord())) {
            $operation->disable();
        }
    }
}
```

**Parameters:** `DataContainerOperation $operation`  
**Returns:** `void`

---

### 5.4 Field callbacks (fields.\<FIELD\>.*)

#### fields.\<FIELD\>.attributes (as of 5.1)

Adjusts field attributes dynamically before the widget is generated.

**Parameters:** `array $attributes`, `DataContainer|null $dc`  
**Returns:** `array` (adjusted attributes)

#### fields.\<FIELD\>.options

Singular callback. Loads data into dropdown menus or checkbox lists.

```php
#[AsCallback(table: 'tl_example', target: 'fields.myfield.options')]
class MyFieldOptionsListener
{
    public function __invoke(?DataContainer $dc): array
    {
        return ['option1' => 'Label 1', 'option2' => 'Label 2'];
    }
}
```

**Parameters:** `DataContainer|null $dc`  
**Returns:** `array`

#### fields.\<FIELD\>.input_field

Singular callback. Creates custom form fields. The field is not saved automatically.

**Parameters:** `DataContainer $dc`, `string $extendedLabel`  
**Returns:** `string` (HTML)

#### fields.\<FIELD\>.load

Executed when a form field is initialised. Loads default values.

**Parameters (backend):** `mixed $value`, `DataContainer $dc`  
**Parameters (front end):** `mixed $value`, `FrontendUser $user`, `ModulePersonalData $module`  
**Returns:** `mixed` (new value)

#### fields.\<FIELD\>.save

Executed when a field is submitted. Custom validation — throwing an exception with an error message prevents saving.

```php
#[AsCallback(table: 'tl_example', target: 'fields.myfield.save')]
class MyFieldSaveListener
{
    public function __invoke(mixed $value, DataContainer $dc): mixed
    {
        if (!$this->isValid($value)) {
            throw new \Exception('Invalid value!');
        }
        return $value;
    }
}
```

**Parameters (backend):** `mixed $value`, `DataContainer $dc`  
**Parameters (front end personal data):** `mixed $value`, `FrontendUser $user`, `ModulePersonalData $module`  
**Parameters (front end registration):** `mixed $value`  
**Returns:** `mixed` (new value)

#### fields.\<FIELD\>.wizard

Adds HTML after the input field (typically a wizard button).

**Parameters:** `DataContainer $dc`  
**Returns:** `string` (HTML)

#### fields.\<FIELD\>.xlabel

Adds HTML after the field label (typically an import wizard button).

**Parameters:** `DataContainer $dc`  
**Returns:** `string` (HTML)

#### fields.\<FIELD\>.eval.url (serpPreview)

Adds a URL to the serpPreview field.

**Parameters:** `Model $model`  
**Returns:** `string` (URL)

#### fields.\<FIELD\>.eval.title_tag (serpPreview)

Modifies the title tag of the serpPreview field.

**Parameters:** `Model $model`  
**Returns:** `string` (title tag)

---

### 5.5 Edit callbacks

#### edit.buttons

Modifies the action buttons at the bottom of the edit form.

**Parameters:** `array $buttons`, `DataContainer $dc`  
**Returns:** `array` (button markup)

---

### 5.6 Select callbacks

#### select.buttons

Modifies the action buttons after rows have been selected.

**Parameters:** `array $buttons`, `DataContainer $dc`  
**Returns:** `array` (button markup)

---

### 5.7 Registering callbacks (overview)

**Via attribute (recommended):**
```php
use Contao\CoreBundle\DependencyInjection\Attribute\AsCallback;

#[AsCallback(table: 'tl_example', target: 'config.onload', priority: 10)]
class MyListener
{
    public function __invoke(?DataContainer $dc): void { … }
}
```

**Via DCA (legacy):**
```php
$GLOBALS['TL_DCA']['tl_example']['config']['onload_callback'][] = [
    MyClass::class, 'onLoad'
];
```

---

*Sources:*
- https://docs.contao.org/5.x/dev/reference/dca/palettes/
- https://docs.contao.org/5.x/dev/reference/dca/callbacks/
