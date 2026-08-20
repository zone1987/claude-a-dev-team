# Contao Hooks – Comments

Hooks for the comment system (adding, permissions, listing).

---

## Contents

- [`addComment`](#addcomment)
- [`isAllowedToEditComment`](#isallowedtoeditcomment)
- [`listComments`](#listcomments)

## `addComment`

**Purpose:** Triggered when a comment is added.

**Parameters:**

| # | Type | Name | Description |
|---|-----|------|-------------|
| 1 | `int` | `$commentId` | Database ID of the new comment (`tl_comments`) |
| 2 | `array` | `$commentData` | Comment fields (without the ID) |
| 3 | `\Contao\Comments` | `$comments` | The Comments class that triggered the hook |

**Returns:** `void`

**Timing:** Immediately after a comment has been saved to the database.

```php
use Contao\CoreBundle\DependencyInjection\Attribute\AsHook;
use Contao\Comments;

#[AsHook('addComment')]
class AddCommentListener
{
    public function __invoke(int $commentId, array $commentData, Comments $comments): void
    {
        // e.g. send a moderation notification
    }
}
```

---

## `isAllowedToEditComment`

**Purpose:** Determines whether a back end user may edit a comment from an unknown source.

**Parameters:**

| # | Type | Name | Description |
|---|-----|------|-------------|
| 1 | `int` | `$parentId` | ID of the parent record |
| 2 | `string` | `$parentTable` | Name of the parent table |

**Returns:** `bool` – `true` = access granted, `false` = access denied or the hook is not responsible.

**Timing:** When the back end checks whether a user may edit a comment.

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

**Purpose:** Triggered when comments from an unknown source are listed in the back end. Allows rendering comments from your own tables.

**Parameters:**

| # | Type | Name | Description |
|---|-----|------|-------------|
| 1 | `array` | `$comment` | The current comment record |

**Returns:** `string` – HTML representation of the comment, or an empty string if the hook is not responsible.

**Timing:** When the comment list is rendered in the back end.

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

_Source: https://docs.contao.org/5.x/dev/reference/hooks/ (as of 2025-06)_
