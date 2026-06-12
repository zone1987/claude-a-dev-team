# Contao 5.x Backend-Widget-Referenz

Backend-Widgets sind die Formular-Elemente für die Bearbeitungsmasken von Datensätzen im Contao-Backend, konfiguriert über `inputType` im DCA-Array.

---

## checkbox

Rendert eine oder mehrere Checkboxen.

**inputType:** `checkbox`

| Schlüssel | Typ | Beschreibung |
|-----------|-----|--------------|
| `inputType` | `string` | `checkbox` |
| `options` | `array` | Options-Array (kombiniert mit `eval.multiple`) |
| `options_callback` | `callable` | Callback der Optionen zurückgibt |
| `reference` | `array` | Übersetzungsreferenz für Optionen |
| `foreignKey` | `string` | Optionen aus anderer Tabelle laden |
| `eval.multiple` | `bool` | Mehrfachauswahl aktivieren |
| `eval.includeBlankOption` | `bool` | Leere Option einbeziehen |
| `eval.blankOptionLabel` | `string` | Label der leeren Option (Standard: `-`) |

**Options-Array-Formate:**
1. `['label1', 'label2']` — Index als Wert
2. `['value' => 'label']` — Wert => Label
3. `['foo' => ['a', 'b'], 'bar' => ['c', 'd']]` — Gruppierte Checkboxen

**SQL-Spaltendefinition:**
- Einzel-Checkbox (Toggle): `boolean` oder `'1'/'0'`
- Mehrfachauswahl: `blob` (serialisiertes Array)

**Beispiele:**

```php
// Toggle-Checkbox
'myCheckbox' => [
    'inputType' => 'checkbox',
    'sql' => ['type' => 'boolean', 'default' => false],
],

// Feste Optionen
'myCheckbox' => [
    'inputType' => 'checkbox',
    'options' => ['foo', 'bar', 'baz'],
    'eval' => ['multiple' => true],
    'sql' => ['type' => 'blob', 'notnull' => false],
],

// Dynamische Optionen
'myCheckbox' => [
    'inputType' => 'checkbox',
    'options_callback' => ['Vendor\Class', 'getOptions'],
    'eval' => ['multiple' => true],
    'sql' => ['type' => 'blob', 'notnull' => false],
],

// Optionen aus Tabelle
'myUsers' => [
    'inputType' => 'checkbox',
    'foreignKey' => 'tl_user.name',
    'sql' => ['type' => 'string', 'notnull' => false, 'default' => ''],
],
```

**Contao-Nutzung:** Überall — einfache Checkbox oft für Subpaletten-Selektor.

---

## checkboxWizard

Wie `checkbox` aber mit manueller Sortierung der ausgewählten Elemente.

**inputType:** `checkboxWizard`

Identische Optionen wie `checkbox` (siehe oben). Nützlich wenn die Reihenfolge der Auswahl relevant ist.

**Contao-Nutzung:** Seitenlayout-Einstellungen (CSS-Framework, JS-Templates), Bildformate in responsiven Bildgrößen.

---

## fileTree

Rendert einen Dateibaum-Picker für die Auswahl von Dateien oder Ordnern.

**inputType:** `fileTree`

| Schlüssel | Typ | Beschreibung |
|-----------|-----|--------------|
| `inputType` | `string` | `fileTree` |
| `eval.extensions` | `string` | Erlaubte Dateierweiterungen (kommagetrennt) |
| `eval.fieldType` | `string` | `checkbox` (Mehrfachauswahl) / `radio` (Einzelauswahl) |
| `eval.files` | `bool` | Dateien und Ordner anzeigen; `false` = nur Ordner |
| `eval.filesOnly` | `bool` | Radio-/Checkboxen bei Ordnern ausblenden |
| `eval.isGallery` | `bool` | Ausgewählte Dateien als Galerie anzeigen |
| `eval.isSortable` | `bool` | Sortierung ausgewählter Elemente aktivieren |
| `eval.multiple` | `bool` | Mehrfachauswahl aktivieren |
| `eval.path` | `string` | Eigenes Stammverzeichnis für Dateibaum |
| `eval.showFilePreview` | `bool` | Reguläre Dateien als Bilder anzeigen |

**Beispiele:**

```php
// Einzelbild-Auswahl
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

// Bildergalerie (Mehrfachauswahl)
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

// Ordner-Auswahl
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

**Contao-Nutzung:** Text-, Download-, Bild- und Galerie-Inhaltselemente.

---

## imageSize

Dropdown + zwei Textfelder für Bildgrößendefinition.

**inputType:** `imageSize`

Keine speziellen Optionen — alle `text`-Widget-Optionen gelten.

**Gespeicherter Wert:** Serialisiertes Image-Size-Array.

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

**Optionen überschreiben via Callback:**
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

**Contao-Nutzung:** Text-, Bild- und Galerie-Inhaltselemente.

---

## inputUnit

Textfeld mit kleinem Dropdown-Menü für die Einheit.

**inputType:** `inputUnit`

| Schlüssel | Typ | Beschreibung |
|-----------|-----|--------------|
| `inputType` | `string` | `inputUnit` |
| `options` | `array` | Optionen für das Dropdown |
| `reference` | `array` | Übersetzungsreferenz für Dropdown-Optionen |

**Gespeicherter Wert:** Serialisiertes assoziatives Array mit Schlüsseln `value` und `unit`.

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

**Contao-Nutzung:** Überschrift-Eingabe in Inhaltselementen und Modulen.

---

## listWizard

Expandierbarer Listenwizard mit Hinzufügen, Entfernen und Umsortieren.

**inputType:** `listWizard`

| Schlüssel | Typ | Beschreibung |
|-----------|-----|--------------|
| `inputType` | `string` | `listWizard` |
| `eval.allowHtml` | `bool` | HTML-Eingabe in Listfelder erlauben |
| `eval.maxlength` | `int` | Maximale Zeichenanzahl pro Listfeld |

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

**Contao-Nutzung:** Nur im Listen-Inhaltselement.

---

## moduleWizard

Weist Frontend-Module den Layout-Abschnitten zu (nur `tl_layout`).

**inputType:** `moduleWizard`

Keine speziellen Optionen.

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

**Contao-Nutzung:** Seitenlayout-Einstellungen in `tl_layout`.

---

## optionWizard

Expandierbare Liste von Optionen für Select-Felder (mit Kopieren, Löschen, Umsortieren, Standard-Option, Gruppen).

**inputType:** `optionWizard`

Keine speziellen Optionen.

```php
'foobar' => [
    'inputType' => 'optionWizard',
    'sql' => ['type' => 'blob', 'notnull' => false],
],
```

**Contao-Nutzung:** Formular-Generator für Select-Formularfelder.

---

## password

Passwort-Textfeld (`type="password"`) mit Anzeige-Schaltfläche.

**inputType:** `password`

Alle `text`-Widget-Optionen gelten.

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

Allgemeiner Picker für beliebige Data-Container-Elemente. Zeigt Backend-Ansicht im Popup.

**inputType:** `picker`

| Schlüssel | Typ | Beschreibung |
|-----------|-----|--------------|
| `inputType` | `string` | `picker` |
| `foreignKey` | `string` | Tabelle für Picker-Auswahl |
| `relation` | `array` | Tabellenreferenz via `'table' => 'tl_foobar'` |
| `eval.multiple` | `bool` | Mehrfachauswahl |
| `eval.isSortable` | `bool` | Drag-n-Drop-Sortierung bei Mehrfachauswahl |

**SQL:** Einzel → `integer`; Mehrfach → `blob` (serialisiertes Array)

```php
// News-Artikel (Einzelauswahl)
'myNewsReference' => [
    'inputType' => 'picker',
    'sql' => ['type' => 'integer', 'unsigned' => true, 'default' => 0],
    'relation' => ['type' => 'hasOne', 'load' => 'lazy', 'table' => 'tl_news'],
],

// Mehrere Inhaltselemente
'myContentElements' => [
    'inputType' => 'picker',
    'eval' => ['multiple' => true],
    'sql' => ['type' => 'blob', 'notnull' => false],
    'relation' => ['type' => 'hasMany', 'load' => 'lazy', 'table' => 'tl_content'],
],

// Eigener Data-Container (braucht eigenen PickerProvider)
'myProducts' => [
    'inputType' => 'picker',
    'eval' => ['multiple' => true],
    'sql' => ['type' => 'blob', 'notnull' => false],
    'relation' => ['type' => 'hasMany', 'load' => 'lazy', 'table' => 'tl_product'],
],
```

**Eigener PickerProvider:**
```php
namespace App\Picker;

use Contao\CoreBundle\Picker\AbstractTablePickerProvider;

class ProductsPickerProvider extends AbstractTablePickerProvider
{
    public function getName(): string { return 'productsPicker'; }
    protected function getDataContainer(): string { return \App\Driver\DC_Product::class; }
}
```

**Contao-Nutzung:** Inhaltselement-Include, Artikel-Teaser.

---

## radio

Radio-Button-Auswahl.

**inputType:** `radio`

| Schlüssel | Typ | Beschreibung |
|-----------|-----|--------------|
| `inputType` | `string` | `radio` |
| `options` | `array` | Options-Array |
| `options_callback` | `callable` | Callback der Optionen zurückgibt |
| `reference` | `array` | Übersetzungsreferenz |
| `foreignKey` | `string` | Optionen aus anderer Tabelle |
| `eval.includeBlankOption` | `bool` | Leere Option einbeziehen |
| `eval.blankOptionLabel` | `string` | Label der leeren Option |
| `eval.disabled` | `bool` | Feld deaktivieren |

```php
// Einfache Radio-Buttons
'example' => [
    'inputType' => 'radio',
    'options' => ['lorem' => 'Lorem', 'ipsum' => 'Ipsum', 'dolor' => 'Dolor'],
    'sql' => ['type' => 'string', 'length' => 8, 'default' => 'lorem'],
],

// Optionen aus Tabelle
'example' => [
    'inputType' => 'radio',
    'foreignKey' => 'tl_user.name',
    'sql' => ['type' => 'integer', 'unsigned' => true, 'default' => 0],
],
```

---

## select

Dropdown-Menü (einfach oder mehrfach), optional mit Choices.js/Chosen.

**inputType:** `select`

| Schlüssel | Typ | Beschreibung |
|-----------|-----|--------------|
| `inputType` | `string` | `select` |
| `options` | `array` | Options-Array |
| `options_callback` | `callable` | Callback der Optionen zurückgibt |
| `reference` | `array` | Übersetzungsreferenz |
| `foreignKey` | `string` | Optionen aus anderer Tabelle |
| `eval.multiple` | `bool` | Mehrfachauswahl |
| `eval.includeBlankOption` | `bool` | Leere Option einbeziehen |
| `eval.blankOptionLabel` | `string` | Label der leeren Option (Standard: `-`) |
| `eval.chosen` | `bool` | Choices.js/Chosen.js aktivieren (ab 5.5 ab 8 Optionen) |
| `eval.disabled` | `bool` | Feld deaktivieren |

**Options-Array-Formate:**
1. `['label1', 'label2']` — Index als Wert
2. `['value' => 'label']` — Wert => Label
3. `['gruppe' => ['a', 'b']]` — Gruppierter Select

**SQL:** Einzel → `string`; Mehrfach → `blob` (serialisiertes Array)

```php
// Einfacher Select
'isVisible' => [
    'inputType' => 'select',
    'options' => ['always', 'never', 'auto'],
    'sql' => ['type' => 'string', 'length' => 8, 'default' => 'auto'],
],

// Gruppierter Select
'mySelect' => [
    'inputType' => 'select',
    'options' => [
        'news'   => ['news_reader', 'news_list'],
        'events' => ['event_reader', 'event_list'],
    ],
    'sql' => ['type' => 'string', 'length' => 16, 'default' => ''],
],

// Dynamische Optionen mit Suchbox
'mySelect' => [
    'inputType' => 'select',
    'options_callback' => ['Vendor\Class', 'getOptions'],
    'eval' => ['chosen' => true],
    'sql' => ['type' => 'string', 'length' => 16, 'default' => ''],
],

// Optionen aus Tabelle
'myUsers' => [
    'inputType' => 'select',
    'foreignKey' => 'tl_user.name',
    'eval' => ['chosen' => true],
    'sql' => ['type' => 'integer', 'unsigned' => true, 'default' => 0],
],
```

---

## serpPreview

Zeigt Vorschau wie eine Suchmaschine Titel und Beschreibung darstellt.

**inputType:** `serpPreview`

| Schlüssel | Typ | Beschreibung |
|-----------|-----|--------------|
| `inputType` | `string` | `serpPreview` |
| `eval.titleFields` | `array` | Titelfelder — erster nicht-leerer Wert wird verwendet |
| `eval.descriptionFields` | `array` | Beschreibungsfelder — erster nicht-leerer Wert wird verwendet |
| `eval.title_tag_callback` | `callable` | Gibt Titelformat zurück (z. B. `'%s - Meine Website'`) |
| `eval.url_callback` | `callable` | Gibt URL für den Datensatz zurück |

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

**Contao-Nutzung:** Seiten-, News-, Kalender- und FAQ-Einstellungen.

---

## tableWizard

Tabellen-Wizard (noch nicht vollständig dokumentiert in den offiziellen Docs).

**inputType:** `tableWizard`

```php
'myTable' => [
    'inputType' => 'tableWizard',
    'sql' => ['type' => 'blob', 'notnull' => false],
],
```

**Contao-Nutzung:** Tabellen-Inhaltselement.

---

## text

Standard-Textfeld (`<input type="text">`).

**inputType:** `text`

Alle `eval`-Optionen gelten. Wichtigste:

| Schlüssel | Typ | Beschreibung |
|-----------|-----|--------------|
| `eval.maxlength` | `int` | Maximale Zeichenanzahl |
| `eval.minlength` | `int` | Minimale Zeichenanzahl |
| `eval.rgxp` | `string` | Validierungsregex |
| `eval.placeholder` | `string` | Platzhaltertext |
| `eval.mandatory` | `bool` | Pflichtfeld |
| `eval.readonly` | `bool` | Nur-Lesen |

```php
'myField' => [
    'inputType' => 'text',
    'eval' => ['maxlength' => 255, 'tl_class' => 'w50'],
    'sql' => ['type' => 'string', 'length' => 255, 'default' => ''],
],
```

---

## textarea

Mehrzeilige Texteingabe, optional mit TinyMCE oder Ace Editor.

**inputType:** `textarea`

| Schlüssel | Typ | Beschreibung |
|-----------|-----|--------------|
| `eval.rte` | `string` | Rich-Text-Editor: `tinyMCE`, `ace`, `ace\|html`, `ace\|json`, etc. |
| `eval.rows` | `int` | Anzahl Zeilen |
| `eval.cols` | `int` | Anzahl Spalten |

**SQL:** `text NULL` empfohlen.

```php
// Einfache Textarea
'myTextarea' => [
    'inputType' => 'textarea',
    'sql' => ['type' => 'text', 'notnull' => false],
],

// Mit TinyMCE
'myTextarea' => [
    'inputType' => 'textarea',
    'eval' => ['rte' => 'tinyMCE', 'helpwizard' => true],
    'sql' => ['type' => 'text', 'notnull' => false],
],

// Mit Ace Editor (JavaScript)
'myTextarea' => [
    'inputType' => 'textarea',
    'eval' => ['rte' => 'ace|js'],
    'sql' => ['type' => 'text', 'notnull' => false],
],
```

**Automatische Verarbeitung:** Bei `ace|html` oder Templates mit "tiny" werden `allowHtml` und `decodeEntities` aktiviert.

---

## timePeriod

Textfeld mit Dropdown-Menü für Zeiteinheiten.

**inputType:** `timePeriod`

| Schlüssel | Typ | Beschreibung |
|-----------|-----|--------------|
| `inputType` | `string` | `timePeriod` |
| `options` | `array` | Optionen für Dropdown (z. B. `['s', 'm', 'h']`) |
| `reference` | `array` | Übersetzungsreferenz |
| `eval.disabled` | `bool` | Feld deaktivieren |
| `eval.maxlength` | `int` | Maximale Zeichenanzahl |

**Gespeicherter Wert:** Serialisiertes Array (→ `blob` empfohlen).

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

**Übersetzungsdatei:**
```yaml
# translations/contao_tl_foobar.en.yaml
tl_foobar:
    s: Seconds
    m: Minutes
    h: Hours
```

---

## Nicht-dokumentierte Widgets

Folgende Widgets existieren im Contao-Core sind aber in der offiziellen Dokumentation noch nicht oder nur als Stub dokumentiert:

| inputType | Beschreibung |
|-----------|--------------|
| `chmod` | CHMOD-Tabelle für Datei-/Ordnerrechte |
| `keyValueWizard` | Key-Value-Wizard |
| `metaWizard` | Dateimanager-Metainformationen |
| `pageTree` | Seitenbaum-Picker (wie `fileTree` für Seiten) |
| `radioTable` | Tabelle mit Bildern und Radio-Buttons |
| `sectionWizard` | Seitenlayout-Abschnitte |
| `textStore` | Textfeld ohne Wert-Anzeige |
| `trbl` | Vier Textfelder + Einheiten-Dropdown (Top/Right/Bottom/Left) |

---

*Quellen:*
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
