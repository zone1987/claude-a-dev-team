# Contao 5.x DCA — Palettes & Callbacks

## 4. palettes

Eine Palette ist eine Gruppe von Formfeldern zum Bearbeiten eines Datensatzes. Paletten müssen nicht alle Tabellenspalten enthalten.

### 4.1 Haupt-Paletten

```php
$GLOBALS['TL_DCA']['tl_example'] = [
    'palettes' => [
        'default' => '{title_legend},title,alias,addImage',
    ],
];
```

Mindestens eine `default`-Palette sollte definiert sein.

### 4.2 __selector__ und Subpaletten

Subpaletten werden in `subpalettes` definiert und erscheinen dynamisch per Ajax, wenn ein Hauptpalettenfeld aktiv ist.

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

**Empfehlung:** `submitOnChange` in eval setzen, damit die Subpalette sofort erscheint/verschwindet.

### 4.3 Subpaletten mit Select-Feldern

Verschiedene Subpaletten je nach Select-Feldwert über das Format `feldName_feldWert`:

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

### 4.4 Mehrere Haupt-Paletten

Ein Selektor wechselt zwischen mehreren Hauptpaletten — der Schlüssel entspricht dem Selektor-Wert:

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

### 4.5 Legendengruppen

Kommas trennen Felder, Semikolons erzeugen neue Fieldsets. Jede Gruppe hat eine _legend_:

```
{title_legend},headline,alias,author;{date_legend},date,time;{teaser_legend:collapsed},subheadline,teaser
```

- Legendenbezeichnungen aus `$GLOBALS['TL_LANG']['tl_news']['title_legend']`
- `:collapsed` = Gruppe standardmäßig eingeklappt

### 4.6 Palette Manipulator

```php
use Contao\CoreBundle\DataContainer\PaletteManipulator;

PaletteManipulator::create()
    ->addLegend('custom_legend', 'title_legend', PaletteManipulator::POSITION_AFTER)
    ->addField('myField', 'custom_legend', PaletteManipulator::POSITION_APPEND)
    ->applyToPalette('default', 'tl_example')
;
```

### 4.7 CSS-Klassen für Feldanordnung (tl_class)

| Klasse | Beschreibung |
|--------|--------------|
| `w25` | 25% Breite, links (ab 5.1) |
| `w33` | 33,33% Breite, links (ab 5.1) |
| `w50` | 50% Breite, links |
| `w66` | 66,67% Breite, links (ab 5.1) |
| `w75` | 75% Breite, links (ab 5.1) |
| `clr` | Floats löschen |
| `wizard` | Verkürzt für Wizard-Schaltflächen |
| `long` | Volle verfügbare Breite |
| `cbx` | Mindesthöhe 46px |
| `m12` | 17px Ober-/Unterabstand |

---

## 5. callbacks

Callbacks sind Einstiegspunkte für eigenen Code im DCA. Sie folgen einem Event-Dispatcher-Muster und sind immer an eine bestimmte DCA-Tabelle gebunden.

### 5.1 Globale Callbacks (config.*)

#### config.onload

Wird ausgeführt wenn das DataContainer-Objekt initialisiert wird. Nützlich für Berechtigungsprüfungen oder Laufzeit-DCA-Änderungen.

```php
use Contao\CoreBundle\DependencyInjection\Attribute\AsCallback;
use Contao\DataContainer;

#[AsCallback(table: 'tl_example', target: 'config.onload')]
class OnLoadListener
{
    public function __invoke(?DataContainer $dc): void
    {
        // Berechtigungen prüfen oder DCA anpassen
    }
}
```

**Parameter:** `DataContainer|null`  
**Rückgabe:** `void`

#### config.oncreate

Wird ausgeführt wenn ein neuer Datensatz erstellt wird.

**Parameter:** `string $table`, `int $insertId`, `array $fields`, `DataContainer $dc`  
**Rückgabe:** `void`

#### config.onbeforesubmit

Wird vor dem Speichern des Backend-Formulars ausgeführt. Ermöglicht Wertänderungen und Multi-Feld-Validierung.

**Parameter:** `array $values`, `DataContainer $dc`  
**Rückgabe:** `array` (Datensatzwerte)

#### config.onsubmit

Wird nach dem Speichern des Backend-Formulars ausgeführt.

**Parameter (Backend):** `DataContainer $dc`  
**Parameter (Frontend "Persönliche Daten"):** `FrontendUser $user`, `ModulePersonalData $module`  
**Rückgabe:** `void`

#### config.ondelete

Wird vor dem Löschen eines Datensatzes ausgeführt.

**Parameter (DC_Folder):** `string $filePath`, `DataContainer $dc`  
**Parameter (andere):** `DataContainer $dc`, `int $undoId`  
**Rückgabe:** `void`

#### config.oncut

Wird nach dem Verschieben eines Datensatzes ausgeführt.

**Parameter:** `DataContainer $dc`  
**Rückgabe:** `void`

#### config.oncopy

Wird nach dem Duplizieren eines Datensatzes ausgeführt.

**Parameter:** `int $insertId`, `DataContainer $dc`  
**Rückgabe:** `void`

#### config.oncreate_version

Wird nach dem Hinzufügen einer alten Datensatzversion zu `tl_version` ausgeführt.

**Parameter:** `string $table`, `int $parentId`, `int $version`, `array $data`  
**Rückgabe:** `void`

#### config.onrestore_version

Wird nach dem Wiederherstellen einer Datensatzversion ausgeführt.

**Parameter:** `string $table`, `int $parentId`, `int $version`, `array $data`  
**Rückgabe:** `void`

#### config.onundo

Wird nach dem Wiederherstellen eines gelöschten Datensatzes ausgeführt.

**Parameter:** `string $table`, `array $data`, `DataContainer $dc`  
**Rückgabe:** `void`

#### config.oninvalidate_cache_tags

Wird ausgeführt wenn ein Datensatz über das Backend geändert wird. Erlaubt das Hinzufügen zusätzlicher Cache-Tags zur Invalidierung.

**Parameter:** `DataContainer $dc`, `array $tags`  
**Rückgabe:** `array` (Cache-Tags zum Invalidieren)

#### config.onshow

Passt das Info-Modal-Fenster eines Datensatzes an.

**Parameter:** `array $existingData`, `array $recordData`, `DataContainer $dc`  
**Rückgabe:** `array` (Tabellenzeilen und -spalten für Modal)

#### config.onpalette (ab 5.3)

Passt die Palette dynamisch basierend auf Objektwerten an.

**Parameter:** `string $palette`, `DataContainer $dc`  
**Rückgabe:** `string` (angepasste Palette)

---

### 5.2 Listing Callbacks (list.*)

**Hinweis:** Alle Listing-Callbacks sind singular — nur ein Callback pro Ereignis erlaubt.

#### list.sorting.paste_button

Generiert individuelle Einfüge-Schaltflächen. Nur in Baum- oder erweitertem Baummodus (Modi 5 und 6).

**Parameter:** `DataContainer $dc`, `array $row`, `string $table`, `bool $cr`, `array $clipboard`, `array|null $children`, `string|null $previous`, `string|null $next`  
**Rückgabe:** `string` (HTML für zusätzliche Schaltflächen)

#### list.sorting.child_record

Definiert wie Kindeinträge in der "Elternansicht" gerendert werden.

**Parameter:** `array $row`  
**Rückgabe:** `string` (HTML)

#### list.sorting.header

Erlaubt individuelle Labels im "Elternansicht"-Header.

**Parameter:** `array $currentLabels`, `DataContainer $dc`  
**Rückgabe:** `array` (Header-Labels)

#### list.sorting.panel_callback.subpanel

Fügt HTML für eigene Panels ein. `subpanel` durch eigenen Panel-Namen ersetzen.

**Parameter:** `DataContainer $dc`  
**Rückgabe:** `string` (HTML)

#### list.label.group

Erlaubt individuelle Gruppenköpfe in Listenansichten.

**Parameter:** `string $group`, `string $mode`, `string $field`, `array $row`, `DataContainer $dc`  
**Rückgabe:** `string`

#### list.label.label

Erlaubt individuelle Labels in Listenansichten.

**Parameter (Baumansicht):** `array $row`, `string $label`, `DataContainer $dc`, `string $imageAttr`, `bool $returnImage`, `bool $protected`  
**Parameter (Listenansicht):** `array $row`, `string $label`, `DataContainer $dc`, `array $columns`  
**Parameter (Elternansicht):** `array $row`, `string $label`, `DataContainer $dc`  
**Rückgabe:** `string` (Baum-/Elternansicht) oder `array` (Listenansicht mit showColumns)

---

### 5.3 Operations Callbacks (list.operations.*)

**Hinweis:** Alle Operations-Callbacks sind singular.

#### list.global_operations.\<OPERATION\>.button

Generiert eigene Schaltflächen für globale Operationen.

**Parameter:** `string|null $href`, `string $label`, `string $title`, `string $class`, `string $attributes`, `string $table`, `array $rootIds`  
**Rückgabe:** `string` (HTML)

#### list.operations.\<OPERATION\>.button

Konfiguriert oder ersetzt Schaltflächen für spezifische Operationen.

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

**Parameter:** `DataContainerOperation $operation`  
**Rückgabe:** `void`

---

### 5.4 Field Callbacks (fields.\<FIELD\>.*)

#### fields.\<FIELD\>.attributes (ab 5.1)

Passt Feld-Attribute dynamisch vor der Widget-Generierung an.

**Parameter:** `array $attributes`, `DataContainer|null $dc`  
**Rückgabe:** `array` (angepasste Attribute)

#### fields.\<FIELD\>.options

Singular-Callback. Lädt Daten in Dropdown-Menüs oder Checkbox-Listen.

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

**Parameter:** `DataContainer|null $dc`  
**Rückgabe:** `array`

#### fields.\<FIELD\>.input_field

Singular-Callback. Erstellt individuelle Formfelder. Feld wird nicht automatisch gespeichert.

**Parameter:** `DataContainer $dc`, `string $extendedLabel`  
**Rückgabe:** `string` (HTML)

#### fields.\<FIELD\>.load

Wird ausgeführt wenn ein Formularfeld initialisiert wird. Lädt Standardwerte.

**Parameter (Backend):** `mixed $value`, `DataContainer $dc`  
**Parameter (Frontend):** `mixed $value`, `FrontendUser $user`, `ModulePersonalData $module`  
**Rückgabe:** `mixed` (neuer Wert)

#### fields.\<FIELD\>.save

Wird beim Absenden eines Feldes ausgeführt. Individuelle Validierung — Exception mit Fehlermeldung verhindert das Speichern.

```php
#[AsCallback(table: 'tl_example', target: 'fields.myfield.save')]
class MyFieldSaveListener
{
    public function __invoke(mixed $value, DataContainer $dc): mixed
    {
        if (!$this->isValid($value)) {
            throw new \Exception('Ungültiger Wert!');
        }
        return $value;
    }
}
```

**Parameter (Backend):** `mixed $value`, `DataContainer $dc`  
**Parameter (Frontend Persönliche Daten):** `mixed $value`, `FrontendUser $user`, `ModulePersonalData $module`  
**Parameter (Frontend Registrierung):** `mixed $value`  
**Rückgabe:** `mixed` (neuer Wert)

#### fields.\<FIELD\>.wizard

Fügt HTML nach dem Eingabefeld hinzu (typischerweise Wizard-Schaltfläche).

**Parameter:** `DataContainer $dc`  
**Rückgabe:** `string` (HTML)

#### fields.\<FIELD\>.xlabel

Fügt HTML nach dem Feld-Label hinzu (typischerweise Import-Wizard-Schaltfläche).

**Parameter:** `DataContainer $dc`  
**Rückgabe:** `string` (HTML)

#### fields.\<FIELD\>.eval.url (serpPreview)

Fügt URL zum serpPreview-Feld hinzu.

**Parameter:** `Model $model`  
**Rückgabe:** `string` (URL)

#### fields.\<FIELD\>.eval.title_tag (serpPreview)

Modifiziert den Title-Tag des serpPreview-Feldes.

**Parameter:** `Model $model`  
**Rückgabe:** `string` (Title-Tag)

---

### 5.5 Edit Callbacks

#### edit.buttons

Modifiziert Aktionsschaltflächen am unteren Ende des Bearbeitungsformulars.

**Parameter:** `array $buttons`, `DataContainer $dc`  
**Rückgabe:** `array` (Schaltflächen-Markup)

---

### 5.6 Select Callbacks

#### select.buttons

Modifiziert Aktionsschaltflächen nach dem Auswählen von Zeilen.

**Parameter:** `array $buttons`, `DataContainer $dc`  
**Rückgabe:** `array` (Schaltflächen-Markup)

---

### 5.7 Callbacks registrieren (Übersicht)

**Via Attribut (empfohlen):**
```php
use Contao\CoreBundle\DependencyInjection\Attribute\AsCallback;

#[AsCallback(table: 'tl_example', target: 'config.onload', priority: 10)]
class MyListener
{
    public function __invoke(?DataContainer $dc): void { … }
}
```

**Via DCA (Legacy):**
```php
$GLOBALS['TL_DCA']['tl_example']['config']['onload_callback'][] = [
    MyClass::class, 'onLoad'
];
```

---

*Quellen:*
- https://docs.contao.org/5.x/dev/reference/dca/palettes/
- https://docs.contao.org/5.x/dev/reference/dca/callbacks/
