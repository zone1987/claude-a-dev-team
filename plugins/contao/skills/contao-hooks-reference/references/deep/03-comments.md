# Contao Hooks – Kommentare

Hooks für das Kommentar-System (Hinzufügen, Berechtigungen, Auflistung).

---

## `addComment`

**Zweck:** Wird ausgelöst, wenn ein Kommentar hinzugefügt wird.

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `int` | `$commentId` | Datenbank-ID des neuen Kommentars (`tl_comments`) |
| 2 | `array` | `$commentData` | Kommentar-Felder (ohne ID) |
| 3 | `\Contao\Comments` | `$comments` | Die Comments-Klasse, die den Hook ausgelöst hat |

**Rückgabe:** `void`

**Zeitpunkt:** Direkt nachdem ein Kommentar in der Datenbank gespeichert wurde.

```php
use Contao\CoreBundle\DependencyInjection\Attribute\AsHook;
use Contao\Comments;

#[AsHook('addComment')]
class AddCommentListener
{
    public function __invoke(int $commentId, array $commentData, Comments $comments): void
    {
        // z.B. Moderations-Benachrichtigung senden
    }
}
```

---

## `isAllowedToEditComment`

**Zweck:** Bestimmt, ob ein Backend-Benutzer einen Kommentar aus einer unbekannten Quelle bearbeiten darf.

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `int` | `$parentId` | ID des übergeordneten Datensatzes |
| 2 | `string` | `$parentTable` | Name der übergeordneten Tabelle |

**Rückgabe:** `bool` – `true` = Zugriff erlaubt, `false` = Zugriff verweigert oder Hook nicht zuständig.

**Zeitpunkt:** Wenn im Backend geprüft wird, ob ein Benutzer einen Kommentar bearbeiten darf.

```php
#[AsHook('isAllowedToEditComment')]
class IsAllowedToEditCommentListener
{
    public function __invoke(int $parentId, string $parentTable): bool
    {
        if ('tl_my_custom_table' === $parentTable) {
            return \Contao\BackendUser::getInstance()->hasAccess('custom', 'modules');
        }
        return false;
    }
}
```

---

## `listComments`

**Zweck:** Wird ausgelöst, wenn Kommentare aus einer unbekannten Quelle im Backend aufgelistet werden. Ermöglicht die Darstellung von Kommentaren aus eigenen Tabellen.

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `array` | `$comment` | Der aktuelle Kommentar-Datensatz |

**Rückgabe:** `string` – HTML-Darstellung des Kommentars, oder leerer String wenn Hook nicht zuständig.

**Zeitpunkt:** Beim Rendern der Kommentar-Liste im Backend.

```php
#[AsHook('listComments')]
class ListCommentsListener
{
    public function __invoke(array $comment): string
    {
        if ('tl_mytable' === $comment['source']) {
            return '<a href="contao/main.php?do=mytable">' . $comment['title'] . '</a>';
        }
        return '';
    }
}
```

---

_Quelle: https://docs.contao.org/5.x/dev/reference/hooks/ (Stand 2025-06)_
