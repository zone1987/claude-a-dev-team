# Contao Hooks – Insert-Tags

Hooks für eigene Insert-Tags und Insert-Tag-Flags.

> **Hinweis:** Beide Hooks in dieser Gruppe sind in Contao 5.x deprecated und werden in Contao 6 entfernt. Als Alternative sollte der `Contao\CoreBundle\InsertTag\InsertTagParser` mit eigenen `InsertTagSubscriber`-Klassen verwendet werden.

---

## `replaceInsertTags`

**Zweck:** Wird ausgelöst, wenn ein unbekanntes Insert-Tag gefunden wird. Ermöglicht die Implementierung eigener Insert-Tags.

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `string` | `$insertTag` | Das unbekannte Insert-Tag |
| 2 | `bool` | `$useCache` | Ob Caching verwendet werden soll |
| 3 | `string` | `$cachedValue` | Der gecachte Ersetzungswert (falls vorhanden) |
| 4 | `array` | `$flags` | An das Tag angehängte Flags |
| 5 | `array` | `$tags` | Aufgeteilter Seiteninhalt für Tag-Ersetzung |
| 6 | `array` | `$cache` | Bisher gefundene gecachte Ersetzungen |
| 7 | `int` | `$_rit` | Zähler für die Iteration über Tag-Teile |
| 8 | `int` | `$_cnt` | Anzahl der Elemente in `$tags` |

**Rückgabe:** `string` – Ersetzungstext wenn Tag behandelt wird, `false` um weiterzumachen.

**Zeitpunkt:** Wenn das System auf ein unbekanntes Insert-Tag stößt.

**Deprecated:** Wird in Contao 6 entfernt. → Stattdessen `InsertTagSubscriber` verwenden.

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

**Moderne Alternative (Contao 5+):**

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

**Zweck:** Wird ausgelöst, wenn unbekannte Flags an Insert-Tags übergeben werden. Ermöglicht eigene Verarbeitungslogik für unbekannte Flags.

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `string` | `$flag` | Name des Insert-Tag-Flags |
| 2 | `string` | `$tag` | Name des Insert-Tags |
| 3 | `string` | `$cachedValue` | Der gecachte Ersetzungswert |
| 4 | `array` | `$flags` | Array der verwendeten Flags |
| 5 | `bool` | `$useCache` | Ob Caching angewendet werden soll |
| 6 | `array` | `$tags` | Aufgeteilter Seiteninhalt |
| 7 | `array` | `$cache` | Bisher gefundene gecachte Ersetzungen |
| 8 | `int` | `$_rit` | Zähler für Tag-Teil-Iteration |
| 9 | `int` | `$_cnt` | Anzahl der Elemente in `$tags` |

**Rückgabe:** `string|false` – Ersetzungstext wenn Flag behandelt wird, `false` um weiterzumachen.

**Zeitpunkt:** Bei der Verarbeitung unbekannter Flags in Insert-Tags (z.B. `{{date::D d. F Y|myFlag}}`).

**Deprecated:** Wird in Contao 6 entfernt.

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

_Quelle: https://docs.contao.org/5.x/dev/reference/hooks/ (Stand 2025-06)_
