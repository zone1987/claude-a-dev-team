# Contao Hooks – Kalender / News

Hooks für Kalender-Events und News-Listen.

---

## `findCalendarBoundaries`

**Zweck:** Erlaubt Anpassung der Datumsgrenzen, die das Kalender-Modul für die Anzeige von Monaten und Paginierungs-Links verwendet. Besonders nützlich in Kombination mit `getAllEvents`.

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `int&` | `$dateFrom` | Unix-Timestamp der unteren Grenze (Referenz) |
| 2 | `int&` | `$dateTo` | Unix-Timestamp der oberen Grenze (Referenz) |
| 3 | `int&` | `$repeatUntil` | Maximaler `repeatEnd`-Wert aus `tl_calendar_events` (Referenz) |
| 4 | `\Contao\Module` | `$module` | Die Frontend-Modul-Instanz |

**Rückgabe:** `void` (Parameter werden per Referenz modifiziert)

**Zeitpunkt:** Im Grenzwert-Erkennungsprozess des Kalender-Moduls, vor Generierung der Paginierungs-Links.

```php
use Contao\CoreBundle\DependencyInjection\Attribute\AsHook;
use Contao\Module;

#[AsHook('findCalendarBoundaries')]
class FindCalendarBoundariesListener
{
    public function __invoke(int &$dateFrom, int &$dateTo, int &$repeatUntil, Module $module): void
    {
        // Grenzen erweitern, z.B. für dynamisch hinzugefügte Events
        $extendedDate = strtotime('+1 year', $dateTo);
        if ($extendedDate > $dateTo) {
            $dateTo = $extendedDate;
        }
    }
}
```

---

## `getAllEvents`

**Zweck:** Erlaubt Modifikation der Event-Ergebnismengen von Kalender- und Event-Modulen.

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `array` | `$events` | Assoziatives Array aller Events, gruppiert nach Datum |
| 2 | `array` | `$calendars` | IDs der im Frontend-Modul aktivierten Kalender |
| 3 | `int` | `$timeStart` | Kalender-Perioden-Startdatum als Timestamp |
| 4 | `int` | `$timeEnd` | Kalender-Perioden-Enddatum als Timestamp |
| 5 | `\Contao\Module` | `$module` | Die Frontend-Modul-Instanz |

**Rückgabe:** `array` – Alle Events, gruppiert nach Timestamp.

**Zeitpunkt:** Wenn Kalender- und Event-Module ihre Event-Daten abrufen.

```php
#[AsHook('getAllEvents')]
class GetAllEventsListener
{
    public function __invoke(array $events, array $calendars, int $timeStart, int $timeEnd, Module $module): array
    {
        // Eigene Events dynamisch hinzufügen
        $customEvent = [
            'title'    => 'Mein Custom Event',
            'tstamp'   => strtotime('next monday'),
            'href'     => '',
            'class'    => '',
            'startTime'=> strtotime('next monday'),
            'endTime'  => strtotime('next monday') + 3600,
        ];
        $events[strtotime('next monday')][strtotime('next monday')][] = $customEvent;
        return $events;
    }
}
```

---

## `newsListCountItems`

**Zweck:** Wird benötigt, wenn die News-Liste mit eigenem Sortieren/Filtern über `newsListFetchItems` angepasst wird, damit die Paginierung korrekt funktioniert.

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `array` | `$newsArchives` | IDs der im News-Listen-Modul angezeigten Archive |
| 2 | `bool` | `$featuredOnly` | Ob nur hervorgehobene News-Einträge angezeigt werden |
| 3 | `\Contao\Module` | `$module` | Die Frontend-Modul-Instanz |

**Rückgabe:** `int|false` – Anzahl der News-Einträge (Ganzzahl, auch `0`), oder `false` wenn dieser Hook nicht zuständig ist. Bei non-false-Rückgabe werden nachfolgende Hooks dieses Typs nicht ausgeführt.

**Zeitpunkt:** Bei der Paginierungs-Berechnung der News-Liste.

```php
#[AsHook('newsListCountItems')]
class NewsListCountItemsListener
{
    public function __invoke(array $newsArchives, bool $featuredOnly, Module $module): int|false
    {
        if ($this->isResponsible($module)) {
            return $this->countMyCustomItems($newsArchives, $featuredOnly);
        }
        return false;
    }
}
```

---

## `newsListFetchItems`

**Zweck:** Erlaubt die Rückgabe einer eigenen Sammlung von `\Contao\NewsModel`-Instanzen für das News-Listen-Modul. Ermöglicht benutzerdefiniertes Filtern oder Sortieren.

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `array` | `$newsArchives` | IDs der angezeigten Archive |
| 2 | `bool\|null` | `$featuredOnly` | Ob nur hervorgehobene News angezeigt werden |
| 3 | `int` | `$limit` | Limit aus dem News-Listen-Modul |
| 4 | `int` | `$offset` | Offset aus dem News-Listen-Modul |
| 5 | `\Contao\Module` | `$module` | Die Frontend-Modul-Instanz |

**Rückgabe:** `\Contao\Model\Collection|false|null` – Model-Collection (oder `null` wenn keine Einträge), oder `false` wenn Hook nicht zuständig. Bei non-false-Rückgabe werden nachfolgende Hooks nicht ausgeführt.

**Zeitpunkt:** Beim Abrufen der News-Einträge im News-Listen-Modul.

```php
#[AsHook('newsListFetchItems')]
class NewsListFetchItemsListener
{
    public function __invoke(array $newsArchives, bool|null $featuredOnly, int $limit, int $offset, Module $module)
    {
        if ($this->isResponsible($module)) {
            return \Contao\NewsModel::findBy(
                ['pid IN (' . implode(',', $newsArchives) . ')', 'myCustomField = ?'],
                ['myValue'],
                ['limit' => $limit, 'offset' => $offset, 'order' => 'date DESC']
            );
        }
        return false;
    }
}
```

---

## `parseArticles`

**Zweck:** Wird beim Parsen von News-Artikeln ausgelöst. Übergibt das Frontend-Template, den aktuellen Artikel und die News-Modul-Instanz.

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `\Contao\FrontendTemplate` | `$template` | Template-Instanz für den News-Artikel (z.B. `news_full`) |
| 2 | `array` | `$newsEntry` | Aktueller News-Datenbankeintrag |
| 3 | `\Contao\Module` | `$module` | Die Modul-Instanz (z.B. `ModuleNewsList`) |

**Rückgabe:** `void`

**Zeitpunkt:** Beim Parsen von News-Artikeln im Frontend.

```php
use Contao\FrontendTemplate;
use Contao\Module;
use Contao\UserModel;

#[AsHook('parseArticles')]
class ParseArticlesListener
{
    public function __invoke(FrontendTemplate $template, array $newsEntry, Module $module): void
    {
        // Autor-Name anstelle von ID anzeigen
        $author = UserModel::findById($newsEntry['author']);
        if (null !== $author) {
            $template->authorName = $author->name;
        }
    }
}
```

---

_Quelle: https://docs.contao.org/5.x/dev/reference/hooks/ (Stand 2025-06)_
