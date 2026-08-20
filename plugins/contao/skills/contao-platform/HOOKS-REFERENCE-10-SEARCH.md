# Contao Hooks – Suche

Hooks für die Frontend-Suche und den Suchindex.

---

## `customizeSearch`

**Zweck:** Erlaubt Anpassung der Seiten, die beim Einsatz des Suchmoduls im Frontend durchsucht werden. Die `$pageIds` werden per Referenz übergeben.

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `array&` | `$pageIds` | Die aktuellen Seiten-IDs, die durchsucht werden (Referenz) |
| 2 | `string` | `$keywords` | Die Suchbegriffe |
| 3 | `string` | `$queryType` | Abfrage-Typ: `and` oder `or` |
| 4 | `bool` | `$fuzzy` | Ob unscharfe Suche verwendet werden soll |
| 5 | `\Contao\Module` | `$module` | Die Frontend-Modul-Instanz |

**Rückgabe:** `void` (Modifikation über Referenz)

**Zeitpunkt:** Wenn ein Benutzer eine Suche über das Frontend-Suchmodul startet, vor der Ausführung.

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
        // Bestimmte Seiten von der Suche ausschließen
        $excludedIds = [42, 43, 44];
        $pageIds = array_diff($pageIds, $excludedIds);
    }
}
```

---

## `indexPage`

**Zweck:** Wird ausgelöst, wenn der Seiteninhalt dem Suchindex hinzugefügt wird. Ermöglicht Modifikation der Indexierungsdaten.

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `string` | `$content` | Seiteninhalt |
| 2 | `array` | `$pageData` | Informationen über die Seite |
| 3 | `array&` | `$indexData` | Für die Indexierung gesammelte Daten (Referenz, wird in `tl_search` gespeichert) |

**Rückgabe:** `void`

**Zeitpunkt:** Beim Indexierungsprozess, wenn Seiteninhalt dem Suchindex hinzugefügt wird.

```php
#[AsHook('indexPage')]
class IndexPageListener
{
    public function __invoke(string $content, array $pageData, array &$indexData): void
    {
        // Eigene Metadaten zum Index hinzufügen
        $indexData['custom_field'] = $this->extractCustomData($content);
    }
}
```

---

_Quelle: https://docs.contao.org/5.x/dev/reference/hooks/ (Stand 2025-06)_
