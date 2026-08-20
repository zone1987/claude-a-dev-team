# Contao Hooks – Calendar / News

Hooks for calendar events and news lists.

---

## Contents

- [`findCalendarBoundaries`](#findcalendarboundaries)
- [`getAllEvents`](#getallevents)
- [`newsListCountItems`](#newslistcountitems)
- [`newsListFetchItems`](#newslistfetchitems)
- [`parseArticles`](#parsearticles)

## `findCalendarBoundaries`

**Purpose:** Allows adjusting the date boundaries the calendar module uses to display months and pagination links. Particularly useful in combination with `getAllEvents`.

**Parameters:**

| # | Type | Name | Description |
|---|-----|------|-------------|
| 1 | `int&` | `$dateFrom` | Unix timestamp of the lower boundary (by reference) |
| 2 | `int&` | `$dateTo` | Unix timestamp of the upper boundary (by reference) |
| 3 | `int&` | `$repeatUntil` | Highest `repeatEnd` value from `tl_calendar_events` (by reference) |
| 4 | `\Contao\Module` | `$module` | The front end module instance |

**Returns:** `void` (the parameters are modified by reference)

**Timing:** During the boundary detection of the calendar module, before the pagination links are generated.

```php
use Contao\CoreBundle\DependencyInjection\Attribute\AsHook;
use Contao\Module;

#[AsHook('findCalendarBoundaries')]
class FindCalendarBoundariesListener
{
    public function __invoke(int &$dateFrom, int &$dateTo, int &$repeatUntil, Module $module): void
    {
        // Extend the boundaries, e.g. for dynamically added events
        $extendedDate = strtotime('+1 year', $dateTo);
        if ($extendedDate > $dateTo) {
            $dateTo = $extendedDate;
        }
    }
}
```

---

## `getAllEvents`

**Purpose:** Allows modifying the event result sets of calendar and event modules.

**Parameters:**

| # | Type | Name | Description |
|---|-----|------|-------------|
| 1 | `array` | `$events` | Associative array of all events, grouped by date |
| 2 | `array` | `$calendars` | IDs of the calendars enabled in the front end module |
| 3 | `int` | `$timeStart` | Start date of the calendar period as a timestamp |
| 4 | `int` | `$timeEnd` | End date of the calendar period as a timestamp |
| 5 | `\Contao\Module` | `$module` | The front end module instance |

**Returns:** `array` – All events, grouped by timestamp.

**Timing:** When calendar and event modules fetch their event data.

```php
#[AsHook('getAllEvents')]
class GetAllEventsListener
{
    public function __invoke(array $events, array $calendars, int $timeStart, int $timeEnd, Module $module): array
    {
        // Add your own events dynamically
        $customEvent = [
            'title'    => 'My custom event',
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

**Purpose:** Required when the news list is customised with your own sorting or filtering through `newsListFetchItems`, so that the pagination works correctly.

**Parameters:**

| # | Type | Name | Description |
|---|-----|------|-------------|
| 1 | `array` | `$newsArchives` | IDs of the archives shown in the news list module |
| 2 | `bool` | `$featuredOnly` | Whether only featured news items are shown |
| 3 | `\Contao\Module` | `$module` | The front end module instance |

**Returns:** `int|false` – Number of news items (an integer, `0` included), or `false` if this hook is not responsible. On a non-false return, subsequent hooks of this type are not executed.

**Timing:** During the pagination calculation of the news list.

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

**Purpose:** Allows returning your own collection of `\Contao\NewsModel` instances for the news list module. Enables custom filtering or sorting.

**Parameters:**

| # | Type | Name | Description |
|---|-----|------|-------------|
| 1 | `array` | `$newsArchives` | IDs of the archives shown |
| 2 | `bool\|null` | `$featuredOnly` | Whether only featured news items are shown |
| 3 | `int` | `$limit` | Limit from the news list module |
| 4 | `int` | `$offset` | Offset from the news list module |
| 5 | `\Contao\Module` | `$module` | The front end module instance |

**Returns:** `\Contao\Model\Collection|false|null` – Model collection (or `null` if there are no items), or `false` if the hook is not responsible. On a non-false return, subsequent hooks are not executed.

**Timing:** When the news items are fetched in the news list module.

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

**Purpose:** Triggered while news articles are parsed. Receives the front end template, the current article and the news module instance.

**Parameters:**

| # | Type | Name | Description |
|---|-----|------|-------------|
| 1 | `\Contao\FrontendTemplate` | `$template` | Template instance for the news article (e.g. `news_full`) |
| 2 | `array` | `$newsEntry` | Current news database record |
| 3 | `\Contao\Module` | `$module` | The module instance (e.g. `ModuleNewsList`) |

**Returns:** `void`

**Timing:** While news articles are parsed in the front end.

```php
use Contao\FrontendTemplate;
use Contao\Module;
use Contao\UserModel;

#[AsHook('parseArticles')]
class ParseArticlesListener
{
    public function __invoke(FrontendTemplate $template, array $newsEntry, Module $module): void
    {
        // Show the author name instead of the ID
        $author = UserModel::findById($newsEntry['author']);
        if (null !== $author) {
            $template->authorName = $author->name;
        }
    }
}
```

---

_Source: https://docs.contao.org/5.x/dev/reference/hooks/ (as of 2025-06)_
