# Contao Hooks – DCA / Backend

Hooks für Data Container Array (DCA), Backend-Navigation, AJAX-Aktionen und Systemwartung.

---

## `executePostActions`

**Zweck:** Wird bei AJAX-Requests ausgelöst, die ein DCA-Objekt benötigen (Post-Actions).

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `string` | `$action` | Name der ausgeführten Aktion |
| 2 | `\Contao\DataContainer` | `$dc` | Das DataContainer-Objekt der aktuellen DCA-Instanz |

**Rückgabe:** `void`

**Zeitpunkt:** Bei AJAX-Requests mit DCA-Objekt, nach der primären Aktionsverarbeitung.

```php
use Contao\CoreBundle\DependencyInjection\Attribute\AsHook;
use Contao\DataContainer;

#[AsHook('executePostActions')]
class ExecutePostActionsListener
{
    public function __invoke(string $action, DataContainer $dc): void
    {
        if ('myCustomAction' === $action) {
            // Eigene AJAX-Aktion verarbeiten
            echo json_encode(['status' => 'ok']);
            exit;
        }
    }
}
```

---

## `executePreActions`

**Zweck:** Wird bei AJAX-Requests ausgelöst, die **kein** DCA-Objekt benötigen (Pre-Actions).

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `string` | `$action` | Name der ausgeführten Aktion |

**Rückgabe:** `void`

**Zeitpunkt:** Bei AJAX-Requests ohne DCA-Objekt.

```php
#[AsHook('executePreActions')]
class ExecutePreActionsListener
{
    public function __invoke(string $action): void
    {
        if ('myPreAction' === $action) {
            // Verarbeiten und Response ausgeben
            echo 'result';
            exit;
        }
    }
}
```

---

## `getAttributesFromDca`

**Zweck:** Wird ausgelöst, wenn Widget-Attribute aus einem Data Container Array extrahiert werden.

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `array` | `$attributes` | Array der Widget-Attribute |
| 2 | `mixed` | `$context` | `\Contao\DataContainer`, `\Contao\Module` oder `null` |

**Rückgabe:** `array` – Das (ggf. modifizierte) Attribut-Array.

**Zeitpunkt:** Bei der Widget-Attribut-Extraktion aus DCA-Konfiguration.

```php
#[AsHook('getAttributesFromDca')]
class GetAttributesFromDcaListener
{
    public function __invoke(array $attributes, $context = null): array
    {
        // Widget-Attribute anpassen
        if (isset($attributes['inputType']) && 'text' === $attributes['inputType']) {
            $attributes['class'] = ($attributes['class'] ?? '') . ' my-text-field';
        }
        return $attributes;
    }
}
```

---

## `getUserNavigation`

**Zweck:** Erlaubt Manipulation der Backend-Benutzer-Navigation.

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `array` | `$modules` | Kompilierte Liste der Backend-Module |
| 2 | `bool` | `$showAll` | Ob alle Module angezeigt werden (auch bei zugeklappten Gruppen) |

**Rückgabe:** `array` – Das (ggf. modifizierte) Modul-Array.

**Zeitpunkt:** Während der Kompilierung der Backend-Benutzer-Navigation.

```php
#[AsHook('getUserNavigation')]
class GetUserNavigationListener
{
    public function __invoke(array $modules, bool $showAll): array
    {
        $modules['system']['modules']['my_link'] = [
            'label' => 'Externe Seite',
            'title' => 'Externe Seite besuchen',
            'class' => 'navigation',
            'href'  => 'https://example.com',
        ];
        return $modules;
    }
}
```

---

## `getSystemMessages`

**Zweck:** Erlaubt das Hinzufügen eigener Meldungen auf dem Backend-Startbildschirm.

**Parameter:** keine

**Rückgabe:** `string` – HTML mit Meldungen, oder leerer String.

**Zeitpunkt:** Beim Rendern des Backend-Startbildschirms.

```php
#[AsHook('getSystemMessages')]
class GetSystemMessagesListener
{
    public function __invoke(): string
    {
        if ($this->hasWarnings()) {
            return '<p class="tl_error">Achtung: Es gibt offene Aufgaben!</p>';
        }
        return '';
    }
}
```

---

## `loadDataContainer`

**Zweck:** Wird ausgelöst, wenn eine DCA-Datei geladen wird. Ideal für dynamische DCA-Anpassungen.

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `string` | `$table` | Name des geladenen Data Containers (z.B. `tl_content`) |

**Rückgabe:** `void`

**Zeitpunkt:** Wenn eine DCA-Datei in das System geladen wird.

```php
#[AsHook('loadDataContainer')]
class LoadDataContainerListener
{
    public function __invoke(string $table): void
    {
        if ('tl_content' === $table) {
            // DCA dynamisch erweitern
            $GLOBALS['TL_DCA']['tl_content']['fields']['myField'] = [
                'inputType' => 'text',
                'eval'      => ['tl_class' => 'w50'],
                'sql'       => "varchar(255) NOT NULL default ''",
            ];
        }
    }
}
```

---

## `reviseTable`

**Zweck:** Wird ausgelöst, wenn Contao verwaiste Datensätze aus einer Tabelle entfernt.

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `string` | `$table` | Aktuelle Tabellenname |
| 2 | `array\|null` | `$newRecords` | IDs neuer Datensätze |
| 3 | `string\|null` | `$parentTable` | Optionaler Eltern-Tabellenname |
| 4 | `array\|null` | `$childTables` | Optionale Namen von Kind-Tabellen |

**Rückgabe:** `bool|null` – `true` um die aktuelle Seite neu zu laden, sonst `false`/`null`.

**Zeitpunkt:** Beim Bereinigungsprozess verwaister Datensätze im Backend.

```php
#[AsHook('reviseTable')]
class ReviseTableListener
{
    public function __invoke(string $table, array|null $newRecords, string|null $parentTable, array|null $childTables): bool|null
    {
        if ('tl_my_table' === $table) {
            // Eigene Bereinigungslogik ausführen
            return true; // Seite neu laden
        }
        return null;
    }
}
```

---

_Quelle: https://docs.contao.org/5.x/dev/reference/hooks/ (Stand 2025-06)_
