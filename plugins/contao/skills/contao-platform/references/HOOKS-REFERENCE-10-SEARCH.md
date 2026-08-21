# Contao Hooks – Search

Hooks for the front end search and the search index.

---

## `customizeSearch`

**Purpose:** Allows adjusting the pages that are searched when the search module is used in the front end. `$pageIds` is passed by reference.

**Parameters:**

| # | Type | Name | Description |
|---|-----|------|-------------|
| 1 | `array&` | `$pageIds` | The current page IDs that are searched (by reference) |
| 2 | `string` | `$keywords` | The search keywords |
| 3 | `string` | `$queryType` | Query type: `and` or `or` |
| 4 | `bool` | `$fuzzy` | Whether a fuzzy search is used |
| 5 | `\Contao\Module` | `$module` | The front end module instance |

**Returns:** `void` (modification through the reference)

**Timing:** When a user starts a search through the front end search module, before it is executed.

```php
use Contao\CoreBundle\DependencyInjection\Attribute\AsHook;
use Contao\Module;

#[AsHook('customizeSearch')]
class CustomizeSearchListener
{
    public function __invoke(
        array &$pageIds,
        string $keywords,
        string $queryType,
        bool $fuzzy,
        Module $module
    ): void {
        // Exclude certain pages from the search
        $excludedIds = [42, 43, 44];
        $pageIds = array_diff($pageIds, $excludedIds);
    }
}
```

---

## `indexPage`

**Purpose:** Triggered when page content is added to the search index. Allows modifying the indexing data.

**Parameters:**

| # | Type | Name | Description |
|---|-----|------|-------------|
| 1 | `string` | `$content` | Page content |
| 2 | `array` | `$pageData` | Information about the page |
| 3 | `array&` | `$indexData` | Data collected for indexing (by reference, stored in `tl_search`) |

**Returns:** `void`

**Timing:** During the indexing process, when page content is added to the search index.

```php
#[AsHook('indexPage')]
class IndexPageListener
{
    public function __invoke(string $content, array $pageData, array &$indexData): void
    {
        // Add your own metadata to the index
        $indexData['custom_field'] = $this->extractCustomData($content);
    }
}
```

---

_Source: https://docs.contao.org/5.x/dev/reference/hooks/ (as of 2025-06)_
