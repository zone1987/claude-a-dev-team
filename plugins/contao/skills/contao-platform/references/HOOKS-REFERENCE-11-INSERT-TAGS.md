# Contao Hooks – Insert tags

Hooks for custom insert tags and insert tag flags.

> **Note:** Both hooks in this group are deprecated in Contao 5.x and will be removed in Contao 6. Use `Contao\CoreBundle\InsertTag\InsertTagParser` with your own `InsertTagSubscriber` classes instead.

---

## `replaceInsertTags`

**Purpose:** Triggered when an unknown insert tag is found. Allows implementing your own insert tags.

**Parameters:**

| # | Type | Name | Description |
|---|-----|------|-------------|
| 1 | `string` | `$insertTag` | The unknown insert tag |
| 2 | `bool` | `$useCache` | Whether caching is used |
| 3 | `string` | `$cachedValue` | The cached replacement value (if present) |
| 4 | `array` | `$flags` | Flags appended to the tag |
| 5 | `array` | `$tags` | Split page content for tag replacement |
| 6 | `array` | `$cache` | Cached replacements found so far |
| 7 | `int` | `$_rit` | Counter for the iteration over the tag parts |
| 8 | `int` | `$_cnt` | Number of elements in `$tags` |

**Returns:** `string` – Replacement text if the tag is handled, `false` to continue.

**Timing:** When the system encounters an unknown insert tag.

**Deprecated:** Will be removed in Contao 6. → Use `InsertTagSubscriber` instead.

```php
use Contao\CoreBundle\DependencyInjection\Attribute\AsHook;

#[AsHook('replaceInsertTags')]
class ReplaceInsertTagsListener
{
    public function __invoke(string $tag): string|false
    {
        if (str_starts_with($tag, 'my_tag::')) {
            $param = substr($tag, strlen('my_tag::'));
            return $this->resolveMyTag($param);
        }
        return false;
    }
}
```

**Modern alternative (Contao 5+):**

```php
use Contao\CoreBundle\DependencyInjection\Attribute\AsInsertTag;

#[AsInsertTag('my_tag')]
class MyTagListener
{
    public function __invoke(\Contao\CoreBundle\InsertTag\InsertTagToken $token): string
    {
        return $this->resolveMyTag($token->getParameters()->get(0));
    }
}
```

---

## `insertTagFlags`

**Purpose:** Triggered when unknown flags are passed to insert tags. Allows your own processing logic for unknown flags.

**Parameters:**

| # | Type | Name | Description |
|---|-----|------|-------------|
| 1 | `string` | `$flag` | Name of the insert tag flag |
| 2 | `string` | `$tag` | Name of the insert tag |
| 3 | `string` | `$cachedValue` | The cached replacement value |
| 4 | `array` | `$flags` | Array of the flags in use |
| 5 | `bool` | `$useCache` | Whether caching is applied |
| 6 | `array` | `$tags` | Split page content |
| 7 | `array` | `$cache` | Cached replacements found so far |
| 8 | `int` | `$_rit` | Counter for the tag part iteration |
| 9 | `int` | `$_cnt` | Number of elements in `$tags` |

**Returns:** `string|false` – Replacement text if the flag is handled, `false` to continue.

**Timing:** While unknown flags in insert tags are processed (e.g. `{{date::D d. F Y|myFlag}}`).

**Deprecated:** Will be removed in Contao 6.

```php
#[AsHook('insertTagFlags')]
class InsertTagFlagsListener
{
    public function __invoke(
        string $flag,
        string $tag,
        string $cachedValue,
        array $flags,
        bool $useCache,
        array $tags,
        array $cache,
        int $_rit,
        int $_cnt
    ): string|false {
        if ('monthNamesAustria' === $flag) {
            return str_replace(
                ['Januar', 'Februar', 'März'],
                ['Jänner', 'Feber', 'März'],
                $cachedValue
            );
        }
        return false;
    }
}
```

---

_Source: https://docs.contao.org/5.x/dev/reference/hooks/ (as of 2025-06)_
