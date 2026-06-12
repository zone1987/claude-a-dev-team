# Contao 5.x DCA — Config, List, Fields

## Überblick

Das **Data Container Array (DCA)** ist das zentrale Konfigurationsformat für Datenbankgestützte Backend-Formulare und Listenansichten in Contao. Es gliedert sich in fünf Hauptbereiche: `config`, `list`, `fields`, `palettes` und `callbacks`.

---

## 1. config

Konfiguriert die Tabelle selbst (Data-Container-Typ, Versionierung, Relationen, Callbacks).

### Minimales Beispiel

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

### config-Schlüssel Referenz

| Schlüssel | Typ | Beschreibung |
|-----------|-----|--------------|
| `label` | `string` | Label für Seiten- oder Dateibäume (Verweis auf `$GLOBALS['TL_LANG']`) |
| `ptable` | `string` | Elterntabelle (table.pid = ptable.id) |
| `dynamicPtable` | `bool` | Elterntabelle dynamisch setzen (wie in `tl_content`) |
| `ctable` | `array` | Kindtabellen (table.id = ctable.pid) |
| `dataContainer` | `string` | `\Contao\DC_Table`, `\Contao\DC_File` oder `\Contao\DC_Folder` |
| `markAsCopy` | `string` | Feldname, das beim Kopieren "(copy)" erhält |
| `uploadPath` | `string` | Pfad zum Stammordner des Dateimanagers |
| `validFileTypes` | `string` | Kommagetrennte erlaubte Dateierweiterungen |
| `editableFileTypes` | `string` | Im Quellcode-Editor bearbeitbare Dateierweiterungen |
| `databaseAssisted` | `bool` | Dateimanager synchronisiert mit Datenbanktabelle |
| `closed` | `bool` | Keine neuen Datensätze |
| `notEditable` | `bool` | Tabelle nicht bearbeitbar |
| `notDeletable` | `bool` | Datensätze nicht löschbar |
| `notSortable` | `bool` | Datensätze nicht sortierbar |
| `notCopyable` | `bool` | Datensätze nicht kopierbar |
| `notCreatable` | `bool` | Keine Neuerstellung (Duplizieren möglich) |
| `switchToEdit` | `bool` | "Speichern und bearbeiten"-Schaltfläche beim Erstellen (nur Sortiermodus 4) |
| `enableVersioning` | `bool` | Alte Versionen sichern |
| `hideVersionMenu` | `bool` | Versionsdropdown ausblenden |
| `doNotCopyRecords` | `bool` | Kindtabellen-Datensätze beim Duplizieren nicht kopieren |
| `doNotDeleteRecords` | `bool` | Kindtabellen-Datensätze beim Löschen nicht löschen |
| `backlink` | `string` | Optionale Query-Parameter für Zurück-Link (z. B. `do=news`) |
| `backendSearchIgnore` | `bool` | Ab 5.7: Daten von Backend-Suche ausschließen (nur DC_Table) |
| `oncreate_callback` | `array` | Aufruf bei Datensatzerstellung |
| `onload_callback` | `array` | Aufruf bei DataContainer-Initialisierung |
| `onbeforesubmit_callback` | `array` | Aufruf vor Formular-Submit |
| `onsubmit_callback` | `array` | Aufruf nach Datensatz-Update |
| `ondelete_callback` | `array` | Aufruf beim Löschen |
| `oncut_callback` | `array` | Aufruf beim Verschieben |
| `oncopy_callback` | `array` | Aufruf beim Duplizieren |
| `onundo_callback` | `array` | Aufruf beim Wiederherstellen |
| `oncreate_version_callback` | `array` | Aufruf beim Erstellen einer Version |
| `onrestore_version_callback` | `array` | Aufruf beim Wiederherstellen einer Version |
| `onpalette_callback` | `array` | Ab 5.3: Aufruf beim Aufbau der Palette |
| `sql` | `array` | Tabellenkonfiguration (Keys, Indizes) |

### config.sql Referenz

```php
$GLOBALS['TL_DCA']['tl_example']['config']['sql'] = [
    'engine'  => 'InnoDB',   // optional, Storage Engine
    'charset' => 'utf8mb4',  // optional, Zeichensatz
    'keys' => [
        'id'          => 'primary',
        'foobar'      => 'index',
        'alias'       => 'unique',
        'lorem,ipsum' => 'index', // kombinierter Index
    ],
];
```

---

## 2. list

Definiert, wie Datensätze im Backend dargestellt werden.

### 2.1 list.sorting

```php
$GLOBALS['TL_DCA']['tl_example']['list']['sorting'] = [
    'mode'         => 2,
    'flag'         => 1,
    'panelLayout'  => 'filter;search,limit',
    'fields'       => ['title'],
];
```

#### Sortierungsmodi (`mode`)

| Wert | Konstante | Beschreibung |
|------|-----------|--------------|
| `0` | — | Keine Sortierung |
| `1` | `MODE_SORTED` | Sortierung nach festem Feld |
| `2` | `MODE_SORTABLE` | Sortierung nach wählbarem Feld |
| `3` | `MODE_UNSORTED` | Sortierung nach Elterntabelle |
| `4` | `MODE_PARENT` | Kindeinträge eines Eltern-Datensatzes (z. B. Content-Elemente) |
| `5` | `MODE_TREE` | Baumansicht (z. B. Seitenstruktur) |
| `6` | `MODE_TREE_EXTENDED` | Kindeinträge innerhalb des Baums (z. B. Artikel) |

#### Sortierungsflaggen (`flag`)

| Wert | Konstante | Beschreibung |
|------|-----------|--------------|
| `1` | `SORT_INITIAL_LETTER_ASC` | Anfangsbuchstaben aufsteigend |
| `2` | `SORT_INITIAL_LETTER_DESC` | Anfangsbuchstaben absteigend |
| `3` | `SORT_INITIAL_TWO_LETTERS_ASC` | Erste zwei Buchstaben aufsteigend |
| `4` | `SORT_INITIAL_TWO_LETTERS_DESC` | Erste zwei Buchstaben absteigend |
| `5` | `SORT_DAY_ASC` | Tag aufsteigend |
| `6` | `SORT_DAY_DESC` | Tag absteigend |
| `7` | `SORT_MONTH_ASC` | Monat aufsteigend |
| `8` | `SORT_MONTH_DESC` | Monat absteigend |
| `9` | `SORT_YEAR_ASC` | Jahr aufsteigend |
| `10` | `SORT_YEAR_DESC` | Jahr absteigend |
| `11` | `SORT_ASC` | Aufsteigend |
| `12` | `SORT_DESC` | Absteigend |

#### Alle sorting-Schlüssel

| Schlüssel | Typ | Beschreibung |
|-----------|-----|--------------|
| `mode` | `int` | Sortiermodus (siehe oben) |
| `flag` | `int` | Sortierrichtung/-typ |
| `panelLayout` | `string` | Panel-Optionen: `search`, `sort`, `filter`, `limit`; Komma = Leerzeichen, Semikolon = Zeilenumbruch |
| `fields` | `array` | Standard-Sortierfelder |
| `headerFields` | `array` | Felder im Header-Element (nur Modus 4) |
| `icon` | `string` | Baum-Icon-Pfad (Modi 5–6) |
| `root` | `array` | Wurzel-Datensatz-IDs (Pagemounts) |
| `rootPaste` | `bool` | Einfüge-Schaltflächen auf Wurzelebene (Standard: `false`) |
| `filter` | `array` | Benutzerdefinierte Query-Filter |
| `disableGrouping` | `bool` | Gruppenköpfe in Listen-/Elternansicht deaktivieren |
| `defaultSearchField` | `string` | Standard-Suchfeld; Fallback für Breadcrumb-Labels (ab 5.3) |
| `paste_button_callback` | Callback | Eigene Einfüge-Schaltflächen |
| `child_record_callback` | Callback | Kindeinträge rendern (nur Modus 4) |
| `header_callback` | Callback | Header-Felder bearbeiten (nur Modus 4) |
| `panel_callback` | Callback | Eigenes Panel-HTML einbinden |
| `child_record_class` | `string` | CSS-Klasse für Elternansicht-Elemente |
| `renderAsGrid` | `bool` | Datensätze als Rasterkacheln anzeigen |

### 2.2 list.label

```php
$GLOBALS['TL_DCA']['tl_example']['list']['label'] = [
    'fields'      => ['title', 'user_id:tl_user.name'],
    'showColumns' => false,
    'format'      => '%s (%s)',
];
```

| Schlüssel | Typ | Beschreibung |
|-----------|-----|--------------|
| `fields` | `array` | Anzuzeigende Felder (Format `field` oder `field:table.column` für Joins) |
| `showColumns` | `bool` | Tabellenkopf mit Spaltennamen generieren |
| `showFirstOrderBy` | `bool` | Erstes Sortierfeld immer anzeigen (Standard: `true`) |
| `format` | `string` | HTML-Format-String (z. B. `'%s (%s)'`) |
| `maxCharacters` | `int` | Maximale Label-Zeichen |
| `group_callback` | Callback | Eigene Gruppenköpfe |
| `label_callback` | Callback | Eigene Labels |

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

// Ab Contao 5.3: Kurzschreibweise
$GLOBALS['TL_DCA']['tl_example']['list']['global_operations'] = [
    'all',
    'toggleNodes',
    'my_op' => ['href' => 'do=my_operation'],
];
```

| Schlüssel | Typ | Beschreibung |
|-----------|-----|--------------|
| `label` | `string` | Schaltflächenbezeichnung |
| `href` | `string` | URL-Fragment (z. B. `act=editAll`) |
| `icon` | `string` | Icon-Pfad/-Dateiname |
| `class` | `string` | CSS-Klasse |
| `attributes` | `string` | Zusätzliche HTML-Attribute |
| `button_callback` | Callback | Eigene Schaltflächengenerierung |
| `route` | `string` | Symfony-Route-Name |
| `prefetch` | `bool` | Turbo-Prefetch deaktivieren (ab 5.5) |
| `showOnSelect` | `bool` | Sichtbarkeit beim "Alle bearbeiten" |

### 2.4 list.operations

```php
// Standard-Operationen:
$GLOBALS['TL_DCA']['tl_example']['list']['operations'] = [
    'edit',
    'children',
    'copy',
    'cut',
    'delete',
    'toggle',
    'show',
];

// Ab 5.5: ! erzwingt Anzeige in der Übersicht statt Kontextmenü
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

| Schlüssel | Typ | Beschreibung |
|-----------|-----|--------------|
| `label` | `string` | Schaltflächenbezeichnung |
| `href` | `string` | URL-Fragment |
| `icon` | `string` | Icon-Pfad |
| `attributes` | `string` | Zusätzliche HTML-Attribute |
| `button_callback` | Callback | Eigene Schaltflächengenerierung |
| `showInHeader` | `bool` | Im Header-Element anzeigen (nur Modus 4) |
| `route` | `string` | Symfony-Route-Weiterleitung |
| `primary` | `bool` | In Übersicht statt Kontextmenü anzeigen (ab 5.5) |
| `prefetch` | `bool` | Turbo-Prefetch deaktivieren (ab 5.5) |

#### Toggle-Operation

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

// Umgekehrter Toggle:
$GLOBALS['TL_DCA']['tl_foobar']['fields']['invisible'] = [
    'reverseToggle' => true,
    'inputType'     => 'checkbox',
    'sql'           => ['type' => 'boolean', 'default' => false],
];
```

---

## 3. fields

Definiert Tabellenspalten und Form-Widgets.

### 3.1 Minimales Beispiel

```php
$GLOBALS['TL_DCA']['tl_example']['fields']['myfield'] = [
    'label'     => &$GLOBALS['TL_LANG']['tl_example']['myfield'],
    'exclude'   => true,
    'inputType' => 'text',
    'eval'      => ['tl_class' => 'w50', 'maxlength' => 255],
    'sql'       => "varchar(255) NOT NULL default ''",
];
```

### 3.2 Alle Feld-Schlüssel

| Schlüssel | Typ | Beschreibung |
|-----------|-----|--------------|
| `label` | `array` | Feld-Label mit Beschreibung (Verweis auf `$GLOBALS['TL_LANG']`) |
| `default` | mixed | Standardwert bei neuen Datensätzen |
| `exclude` | `bool` | Ab 5.3 Standard `true`; für Nicht-Admins ausgeschlossen |
| `toggle` | `bool` | Feld löst Toggle-Aktion aus |
| `reverseToggle` | `bool` | Toggle-Aktion umkehren |
| `search` | `bool` | Im Suchmenü und Backend-Suche einbeziehen |
| `backendSearch` | `bool` | Überschreibt `search` nur für Backend-Suche (ab 5.7) |
| `sorting` | `bool` | Im Sortiermenü einbeziehen |
| `filter` | `bool` | Im Filtermenü einbeziehen |
| `flag` | `int` | Sortiermodus (1–12) |
| `length` | `int` | Zeichenanzahl für Sortiergruppen (Flags 3–4) |
| `inputType` | `string` | Widget-Typ |
| `options` | `array` | Optionen für Auswahl-/Radiofelder |
| `options_callback` | `array` | Callback der Optionen zurückgibt |
| `enum` | `BackedEnum` | Optionen/Referenz aus Enum befüllen (ab 5.3) |
| `foreignKey` | `string` | Optionen aus Datenbanktabelle laden |
| `reference` | `array` | Übersetzungsreferenz für Optionen |
| `explanation` | `string` | Array-Key für Hilfe-Wizard-Text |
| `input_field_callback` | `array` | Eigenes Input-Feld (wird nicht automatisch gespeichert) |
| `eval` | `array` | Feld-spezifische Konfiguration |
| `wizard` | `array` | Callback-Funktionen für Wizard |
| `sql` | `string\|array` | Datenbankfeldddefinition |
| `relation` | `array` | Relationen zu anderen Tabellen |
| `targetColumn` | `string` | JSON-Speicherspalte für virtuelle Felder (ab 5.7, Standard: `jsonData`) |
| `load_callback` | `array` | Aufgerufen beim Laden des Feldes |
| `save_callback` | `array` | Aufgerufen beim Speichern des Feldes |
| `xlabel` | `array` | HTML nach Feld-Label |
| `attributes_callback` | `array` | Feld-Attribute dynamisch anpassen |

### 3.3 inputType — Alle verfügbaren Typen

| inputType | Widget |
|-----------|--------|
| `checkbox` | Checkbox (einzeln oder mehrfach) |
| `checkboxWizard` | Checkbox-Wizard mit Sortierung |
| `chmod` | CHMOD-Tabelle |
| `fileTree` | Dateibaum-Picker |
| `imageSize` | Zwei Textfelder + Einheiten-Dropdown |
| `inputUnit` | Textfeld + Einheiten-Dropdown |
| `keyValueWizard` | Key » Value Wizard |
| `listWizard` | Listenwizard |
| `metaWizard` | Dateimanager-Metainformationen |
| `moduleWizard` | Modulwizard |
| `optionWizard` | Option-Wizard |
| `pageTree` | Seitenbaum-Picker |
| `password` | Passwortfeld |
| `picker` | Allgemeiner Picker |
| `radio` | Radio-Buttons |
| `radioTable` | Tabelle mit Bildern und Radio-Buttons |
| `sectionWizard` | Seitenlayout-Abschnitte |
| `select` | Dropdown-Menü |
| `serpPreview` | Suchmaschinen-Ergebnis-Vorschau |
| `tableWizard` | Tabellen-Wizard |
| `text` | Textfeld |
| `textStore` | Textfeld (Wert nicht anzeigen) |
| `textarea` | Textarea |
| `timePeriod` | Textfeld + Dropdown |
| `trbl` | Vier Textfelder + Einheiten-Dropdown |

### 3.4 eval — Alle Optionen

| Schlüssel | Typ | Beschreibung |
|-----------|-----|--------------|
| `allowHtml` | `bool` | HTML-Eingabe gemäß Backend-Einstellungen akzeptieren |
| `alwaysSave` | `bool` | Immer speichern, auch wenn unverändert |
| `autogrow` | `bool` | Textarea-Autogrow aktivieren (Standard `true`, ab 5.7) |
| `basicEntities` | `bool` | Einfache Entities beim Bearbeiten/Speichern konvertieren |
| `blankOptionLabel` | `string` | Label für leere Option (Standard `-`) |
| `chosen` | `bool` | Selects mit Chosen/Choices.js (ab 5.5) verbessern |
| `collapseUncheckedGroups` | `bool` | Optionsgruppen ohne aktivierte Elemente einklappen |
| `colorpicker` | `bool` | Farbauswahl hinzufügen |
| `cols` | `int` | Spaltenanzahl für Textarea/radioTable/tableWizard |
| `csv` | `string` | Trennzeichen für Listenfelder statt serialisiert |
| `customRgxp` | `string` | Eigener regulärer Ausdruck |
| `errorMsg` | `string` | Fehlermeldung für `customRgxp` |
| `customTpl` | `string` | Eigener Template-Dateiname |
| `datepicker` | `bool` | MooTools-DatePicker hinzufügen |
| `dcaPicker` | `bool\|array` | Allgemeinen Picker anzeigen |
| `decodeEntities` | `bool` | HTML-Entities dekodieren |
| `disabled` | `bool` | Feld deaktivieren |
| `doNotCopy` | `bool` | Beim Duplizieren überspringen |
| `doNotSaveEmpty` | `bool` | Leer nicht speichern |
| `doNotShow` | `bool` | In "Alle bearbeiten"/Details ausblenden |
| `doNotTrim` | `bool` | Whitespace-Trimming überspringen |
| `encrypt` | `bool` | Verschlüsselt speichern |
| `extensions` | `string` | Erlaubte Dateiendungen (kommagetrennt) |
| `fallback` | `bool` | Nur einmal pro Tabelle zuweisen |
| `feEditable` | `bool` | Im Frontend bearbeitbar (nur tl_member) |
| `feGroup` | `string` | Registrierungsformular-Abschnitt |
| `fieldType` | `string` | `checkbox`/`radio` für Datei-/Seitenbäume |
| `files` | `bool` | Dateien und Ordner im Dateibaum anzeigen |
| `filesOnly` | `bool` | Checkboxen/Radiobuttons bei Ordnern ausblenden |
| `findInSet` | `bool` | Nach Optionswerten statt Labels sortieren |
| `helpwizard` | `bool` | Hilfe-Wizard-Icon anzeigen |
| `hideInput` | `bool` | Feldwert-Anzeige verstecken |
| `includeBlankOption` | `bool` | Leere Option zu Dropdown hinzufügen |
| `isAssociative` | `bool` | Assoziatives Options-Array kennzeichnen |
| `isBoolean` | `bool` | Boolean-Feld kennzeichnen |
| `isGallery` | `bool` | fileTree-Elemente als Galerie anzeigen |
| `isHexColor` | `bool` | Hex-Farb-Notation mit auto. Bereinigung |
| `isSortable` | `bool` | Sortierung für ausgewählte Elemente aktivieren |
| `mandatory` | `bool` | Pflichtfeld |
| `maxlength` | `int` | Maximale Zeichenanzahl |
| `maxval` | `int` | Maximaler Zahlenwert |
| `metaFields` | `array` | Verfügbare Felder für metaWizard |
| `minlength` | `int` | Minimale Zeichenanzahl |
| `minval` | `int` | Minimaler Zahlenwert |
| `multiple` | `bool` | Mehrfachauswahl |
| `nospace` | `bool` | Leerzeichen verbieten |
| `orderField` | `string` | Spalte für Sortierreihenfolge ausgewählter Elemente |
| `path` | `string` | Eigenes Stammverzeichnis für Dateibaum |
| `placeholder` | `string` | Platzhaltertext |
| `preserveTags` | `bool` | Alle HTML-Tags behalten |
| `readonly` | `bool` | Nur-Lesen-Feld |
| `rgxp` | `string` | Regulärer Ausdruck (siehe unten) |
| `rows` | `int` | Zeilenanzahl für Textarea/tableWizard |
| `rte` | `string` | Rich-Text-Editor (`ace`, `tinyMCE`) |
| `size` | `int` | Größe bei Mehrfach-Select / Anzahl Input-Felder |
| `showFilePreview` | `bool` | Reguläre Dateien als Bilder anzeigen |
| `spaceToUnderscore` | `bool` | Leerzeichen durch Unterstriche ersetzen |
| `style` | `string` | Inline-CSS |
| `submitOnChange` | `bool` | Formular bei Wertänderung absenden |
| `tl_class` | `string` | CSS-Klassen |
| `trailingSlash` | `bool` | Abschließenden Schrägstrich hinzufügen/entfernen |
| `unique` | `bool` | Einzigartiger Wert |
| `uploadFolder` | `string` | Zielordner für Upload-Widget |
| `useRawRequestData` | `bool` | Rohe Symfony-Request-Daten verwenden (Filterung umgehen!) |
| `versionize` | `bool` | In Versionierung einbeziehen (Standard `true`) |

#### tl_class CSS-Klassen

| Klasse | Beschreibung |
|--------|--------------|
| `w25` | 25% Breite, links ausgerichtet (ab 5.1) |
| `w33` | 33,33% Breite, links ausgerichtet (ab 5.1) |
| `w50` | 50% Breite, links ausgerichtet |
| `w66` | 66,67% Breite, links ausgerichtet (ab 5.1) |
| `w75` | 75% Breite, links ausgerichtet (ab 5.1) |
| `clr` | Floats löschen (`clear:both`) |
| `wizard` | Verkürzt für Wizard-Schaltflächen |
| `long` | Gesamte verfügbare Breite |
| `cbx` | Mindesthöhe 46px (einzelne Checkboxen) |
| `m12` | 17px Ober-/Unterabstand |
| `cbx m12` | Kombiniert: 80px Mindesthöhe |

#### rgxp — Reguläre Ausdrücke

| Wert | Beschreibung |
|------|--------------|
| `digit` | Numerische Zeichen, Punkt, Minus, Dezimalkomma |
| `natural` | Nicht-negative natürliche Zahlen |
| `alpha` | Alphabetisch, Punkt, Minus, Leerzeichen |
| `alnum` | Alphanumerisch, Punkt, Minus, Unterstrich, Leerzeichen |
| `extnd` | Verbietet `#<>()\\=` |
| `date` | Gültiges Datum |
| `time` | Gültige Uhrzeit |
| `datim` | Gültiges Datum und Uhrzeit |
| `friendly` | E-Mail im "Friendly Name"-Format |
| `email` | Gültige E-Mail-Adresse |
| `emails` | Gültige E-Mail-Liste |
| `url` | Gültige URL |
| `alias` | Gültiger Alias |
| `folderalias` | Gültiger Ordner-URL-Alias |
| `phone` | Telefonnummer |
| `prcnt` | Zahlen 0–100 |
| `locale` | Gültiges Locale (z. B. `de_CH`) |
| `language` | Gültiger Sprachcode (z. B. `de-CH`) |
| `fieldname` | Gültiger Feldname |
| `httpurl` | Absolute URL (http/https) |
| `custom` | Eigener Regex über `customRgxp` |

### 3.5 sql — Spaltendefinition

**Als String:**
```php
'sql' => "varchar(255) NOT NULL default ''"
```

**Als Doctrine Schema Array:**

| Doctrine Schema | SQL-Äquivalent |
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
    'table' => 'tl_files', // optional, wird aus foreignKey extrahiert
    'field' => 'uuid',     // optional, Standard: id
],
```

| `type` | Beschreibung |
|--------|--------------|
| `hasOne` | Kind-Datensatz |
| `hasMany` | Serialisierte Kind-Datensätze |
| `belongsTo` | Eltern-Datensatz |
| `belongsToMany` | Serialisierte Eltern-Datensätze |

### 3.7 Enumerations (ab Contao 5.3)

```php
// PHP Enum mit TranslatableLabelInterface
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

// DCA-Nutzung
$GLOBALS['TL_DCA']['tl_member']['fields']['salutation'] = [
    'inputType' => 'select',
    'enum'      => Salutation::class,
];
```

### 3.8 Virtuelle Felder (ab Contao 5.7)

Felder ohne SQL-Definition werden automatisch als virtuelle Felder behandelt und in einer JSON-Spalte (`jsonData`) gespeichert.

```php
// Virtuelles Feld
$GLOBALS['TL_DCA']['tl_content']['fields']['example1'] = [
    'inputType' => 'text',
    // keine 'sql'-Definition → virtuell, gespeichert in jsonData
];

// Eigene Zielspalte
$GLOBALS['TL_DCA']['tl_content']['fields']['example1'] = [
    'inputType'    => 'text',
    'targetColumn' => 'foobar', // JSON-Daten in eigene Spalte
];
```

**Einschränkungen:** Filtern/Suchen virtueller Felder nur innerhalb `DC_Table` unterstützt.

---

*Quellen:*
- https://docs.contao.org/5.x/dev/reference/dca/config/
- https://docs.contao.org/5.x/dev/reference/dca/list/
- https://docs.contao.org/5.x/dev/reference/dca/fields/
