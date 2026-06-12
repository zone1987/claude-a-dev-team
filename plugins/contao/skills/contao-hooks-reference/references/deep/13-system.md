# Contao Hooks – System / Sonstiges

Hooks für System-Initialisierung, Validierung, SQL, Datum, Sprache, Cookies und Logging.

---

## `addCustomRegexp`

**Zweck:** Wird ausgelöst, wenn eine unbekannte Validierungsoption (`rgxp`) gefunden wird. Ermöglicht eigene Validierungsregeln für Formularfelder und DCA-Felder.

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `string` | `$regexp` | Der unbekannte Regulärausdruck-Bezeichner |
| 2 | `mixed` | `$input` | Der zu validierende Eingabewert |
| 3 | `\Contao\Widget` | `$widget` | Das Formular-Widget |

**Rückgabe:** `bool` – `true` = Verarbeitung stoppen (nicht an weitere Hooks übergeben), `false` = weiterverarbeiten.

**Zeitpunkt:** Bei der Formularfeld-Validierung, wenn ein unbekannter `rgxp`-Wert in DCA-Feldern oder Formular-Generator-Textfeldern gefunden wird.

```php
use Contao\CoreBundle\DependencyInjection\Attribute\AsHook;
use Contao\Widget;

#[AsHook('addCustomRegexp')]
class AddCustomRegexpListener
{
    public function __invoke(string $regexp, $input, Widget $widget): bool
    {
        if ('plz' !== $regexp) {
            return false; // Nicht zuständig
        }
        // Deutsche Postleitzahl validieren (5 Ziffern)
        if (!preg_match('/^\d{5}$/', $input)) {
            $widget->addError('Bitte geben Sie eine gültige Postleitzahl ein.');
        }
        return true; // Eigene Verarbeitung abgeschlossen
    }
}
```

Verwendung im DCA:
```php
'fields' => [
    'plz' => [
        'inputType' => 'text',
        'eval' => ['rgxp' => 'plz'],
    ]
]
```

---

## `colorizeLogEntries`

**Zweck:** Wird ausgelöst, wenn ein Log-Eintrag im Backend angezeigt wird. Ermöglicht Anpassung der Darstellung (Label/CSS).

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `array` | `$row` | Der Log-Eintrag-Datensatz |
| 2 | `string` | `$label` | Von Contao generiertes Label |

**Rückgabe:** `string` – Modifiziertes Label.

**Zeitpunkt:** Beim Anzeigen von Log-Einträgen im Backend.

```php
#[AsHook('colorizeLogEntries')]
class ColorizeLogEntriesListener
{
    public function __invoke(array $row, string $label): string
    {
        if ('ERROR' === $row['action']) {
            $label = preg_replace(
                '@^(.*</span> )(.*)$@U',
                '$1<span class="tl_red">$2</span>',
                $label
            );
        }
        return $label;
    }
}
```

---

## `initializeSystem`

**Zweck:** Wird direkt nach dem Abschluss der System-Initialisierung und **vor** dem Start der Request-Verarbeitung ausgelöst. Kein Contao-Request-Scope gesetzt, keine Sprachweiterleitung ausgeführt.

**Parameter:** keine

**Rückgabe:** `void`

**Zeitpunkt:** Nach System-Initialisierung, vor Request-Verarbeitung.

```php
#[AsHook('initializeSystem')]
class InitializeSystemListener
{
    public function __invoke(): void
    {
        // Sehr frühe Initialisierungslogik
        // Kein Contao-Request-Scope verfügbar!
    }
}
```

---

## `loadLanguageFile`

**Zweck:** Wird ausgelöst, wenn eine Sprachdatei über `\Contao\System::loadLanguageFile()` geladen wird.

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `string` | `$name` | Sprachdatei-Name ohne Extension (z.B. `tl_content`) |
| 2 | `string` | `$currentLanguage` | Die geladene Sprache (z.B. `de`) |
| 3 | `string` | `$cacheKey` | Interner Cache-Schlüssel der geladenen Datei |

**Rückgabe:** `void`

**Zeitpunkt:** Wenn das System eine Sprachdatei lädt.

```php
#[AsHook('loadLanguageFile')]
class LoadLanguageFileListener
{
    public function __invoke(string $name, string $currentLanguage, string $cacheKey): void
    {
        if ('tl_content' === $name && 'de' === $currentLanguage) {
            // Eigene Übersetzungen hinzufügen
            $GLOBALS['TL_LANG']['tl_content']['myField'] = ['Mein Feld', 'Beschreibung'];
        }
    }
}
```

---

## `parseDate`

**Zweck:** Wird immer ausgelöst, wenn `\Contao\Date::parse()` verwendet wird. Ermöglicht benutzerdefinierte Datumsformatierung basierend auf Locale und Format.

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `string` | `$formattedDate` | Bereits formatiertes Datum |
| 2 | `string` | `$format` | Angefordertes Datumsformat |
| 3 | `int\|null` | `$timestamp` | Der gegebene Timestamp |

**Rückgabe:** `string` – Das (ggf. modifizierte) formatierte Datum.

**Zeitpunkt:** Wenn `\Contao\Date::parse()` aufgerufen wird.

```php
#[AsHook('parseDate')]
class ParseDateListener
{
    public function __invoke(string $formattedDate, string $format, int|null $timestamp): string
    {
        // Österreichische Monatsnamen einsetzen
        return str_replace(
            ['Januar', 'Februar'],
            ['Jänner', 'Feber'],
            $formattedDate
        );
    }
}
```

---

## `setCookie`

**Zweck:** Wird ausgelöst, wenn ein Cookie an den Browser gesendet wird. Erlaubt Modifikation der Cookie-Eigenschaften.

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `\stdClass` | `$cookie` | Objekt mit Cookie-Eigenschaften (`strName`, `varValue`, `intExpires`, `strPath`, `strDomain`, `blnSecure`, `blnHttpOnly`) |

**Rückgabe:** `\stdClass` – Das (ggf. modifizierte) Cookie-Objekt.

**Zeitpunkt:** Wenn die Applikation ein Cookie an den Browser sendet.

> **Deprecated:** Wird in Contao 6 entfernt. Stattdessen einen `kernel.response`-Listener implementieren.

```php
#[AsHook('setCookie')]
class SetCookieListener
{
    public function __invoke(\stdClass $cookie): \stdClass
    {
        // Cookie-Pfad auf Root setzen
        $cookie->strPath = '/';
        return $cookie;
    }
}
```

---

## `sqlCompileCommands`

**Zweck:** Wird beim Kompilieren der Datenbank-Update-Befehle ausgelöst. Ermöglicht Modifikation der SQL-Statements vor deren Ausführung.

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `array` | `$sql` | Array der Änderungen, die auf die Datenbank angewendet werden sollen |

**Rückgabe:** `array` – Das modifizierte Array von Datenbankänderungen.

**Zeitpunkt:** Beim Kompilierungsprozess der Datenbank-Update-Befehle.

```php
#[AsHook('sqlCompileCommands')]
class SqlCompileCommandsListener
{
    public function __invoke(array $sql): array
    {
        // SQL-Statements modifizieren oder hinzufügen
        return $sql;
    }
}
```

---

## `sqlGetFromDB`

**Zweck:** Wird beim Parsen der aktuellen Datenbank-Definition ausgelöst. Ermöglicht Ergänzung der generierten SQL-Statements.

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `array` | `$sql` | Kompilierte SQL-Definitionen |

**Rückgabe:** `array` – Das modifizierte `$sql`-Array.

**Zeitpunkt:** Beim Parsen der Datenbank-Definition.

```php
#[AsHook('sqlGetFromDB')]
class SqlGetFromDBListener
{
    public function __invoke(array $sql): array
    {
        // Eigene SQL-Definitionen hinzufügen
        return $sql;
    }
}
```

---

## `sqlGetFromDca`

**Zweck:** Wird beim Auswerten von SQL-Definitionen in DCA-Dateien ausgelöst.

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `array` | `$sql` | Die geparste SQL-Definition aus DCA-Dateien |

**Rückgabe:** `array` – Das modifizierte SQL-Definitions-Array.

**Zeitpunkt:** Bei der Auswertung von SQL-Definitionen aus DCA-Dateien.

```php
#[AsHook('sqlGetFromDca')]
class SqlGetFromDcaListener
{
    public function __invoke(array $sql): array
    {
        // SQL-Definitionen aus DCA modifizieren
        return $sql;
    }
}
```

---

_Quelle: https://docs.contao.org/5.x/dev/reference/hooks/ (Stand 2025-06)_
