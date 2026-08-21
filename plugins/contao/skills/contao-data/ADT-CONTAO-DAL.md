# Contao Models, Collections & Enumerations (5.x)

## Contents

- [Overview](#overview)
- [Retrieving records](#retrieving-records)
- [Modifying records](#modifying-records)
- [Options parameter](#options-parameter)
- [Eager Loading / Relations](#eager-loading--relations)
- [Collections](#collections)
- [Custom Models (3 steps)](#custom-models-3-steps)
- [Enumerations (Contao 5.3 and later)](#enumerations-contao-53-and-later)
- [Return values at a glance](#return-values-at-a-glance)

## Overview

Models are objects for creating new records as well as for reading and modifying existing records from the database – comparable to Doctrine entities. Every database table corresponds to a model class (`tl_article` → `ArticleModel`, `tl_news` → `NewsModel`).

---

## Retrieving records

Static methods for database queries:

| Method | Description |
|---------|-------------|
| `findById($id)` | Record by ID |
| `findByIdOrAlias($value)` | ID or alias field |
| `findOneBy($field, $value)` | Single record |
| `findBy($field, $value, $options)` | Collection of records |
| `findAll()` | All records |
| `countBy($field, $value)` | Number of matches |

### Late Static Binding (`__callStatic`)

```php
$page = PageModel::findById(5);
$page = PageModel::findOneByAdminEmail('admin@example.com');
$pages = PageModel::findByLanguage('de');
$count = PageModel::countByLanguage('de');
```

Returns `null` if there is no match.

---

## Modifying records

```php
$page = PageModel::findById(5);
$id   = $page->id;
$page->alias = 'index';
$page->save();
```

---

## Options parameter

| Option | Purpose | SQL equivalent | Example |
|--------|-------|----------------|---------|
| `limit` | Limit the number | `LIMIT` | `3` |
| `offset` | Skip the beginning | `OFFSET` | `10` |
| `order` | Sorting | `ORDER BY` | `'id DESC'` |
| `return` | Output type | — | `'Model'`, `'Collection'`, `'Array'` |
| `eager` | Eager loading | `LEFT JOIN` | `true` |
| `having` | Join filter | `HAVING` | `"author__username = 'k.jones'"` |

```php
$options = ['limit' => 5, 'offset' => 10, 'order' => 'title ASC'];
$pages   = PageModel::findBy('pid', 1, $options);
$pages   = PageModel::findByPid(1, $options);
```

---

## Eager Loading / Relations

`'eager' => true` loads related `hasOne`/`belongsTo` records via JOIN. Columns of the foreign table receive the prefix `<foreignKey>__`.

```php
$articles = ArticleModel::findBy('tl_article.published = ?', true, [
    'return' => 'Array',
    'eager'  => true,
    'having' => "author__username = 'k.jones'",
]);

$author = $articles[0]->getRelated('author');
```

---

## Collections

A `Collection` always contains at least one model. No match → `null` (not an empty collection).

### findAll / findMultipleByIds

```php
$pages = PageModel::findAll();
$pages = PageModel::findMultipleByIds([1, 2, 3]);
```

### Complex conditions

```php
$pages = PageModel::findBy(
    ['language = ?', 'pid = ?'],
    ['de', 1]
);

// IN clause (IDs always as intval!)
$items = FoobarModel::findBy(
    ['type = ?', 'id IN (' . implode(',', array_map('\intval', $ids)) . ')'],
    ['store']
);
```

### Iteration

```php
foreach (PageModel::findAll() as $page) {
    // $page is a model instance
}
```

### Extracting columns

```php
$titles = $pages->fetchEach('title');   // One column of all rows
$rows   = $pages->fetchAll();           // All columns of all rows
```

---

## Custom Models (3 steps)

### 1. Create the DCA

```php
// contao/dca/tl_example.php
$GLOBALS['TL_DCA']['tl_example'] = [ /* … */ ];
```

### 2. Create the model class

Naming convention: remove `tl_`, snake_case → PascalCase, append "Model".

```php
// src/Model/ExampleModel.php
namespace App\Model;

use Contao\Model;

/**
 * @property string $hash  IDE support
 */
class ExampleModel extends Model
{
    protected static $strTable = 'tl_example';

    public function setHash(): void
    {
        $this->hash = md5($this->id);
    }
}
```

### 3. Register the model

```php
// contao/config/config.php
use App\Model\ExampleModel;

$GLOBALS['TL_MODELS']['tl_example'] = ExampleModel::class;
```

---

## Enumerations (Contao 5.3 and later)

### DCA configuration

```php
// contao/dca/tl_member.php
$GLOBALS['TL_DCA']['tl_member']['fields']['salutation'] = [
    'inputType' => 'select',
    'enum'      => App\Data\Salutation::class,
];
```

### Resolution

```php
$member = MemberModel::findById(42);

$member->salutation;                // Returns a string, e.g. 'ms'
$member->getEnum('salutation');     // Returns an App\Data\Salutation instance or null
```

### Type-safe getter with fallback

```php
use App\Data\Salutation;
use Contao\MemberModel;

class SalutableMember extends MemberModel
{
    public function getSalutation(): Salutation
    {
        return $this->getEnum('salutation') ?? Salutation::mx;
    }
}
```

---

## Return values at a glance

| Method | Returns |
|---------|----------|
| `findOneBy()` | `Model|null` |
| `findBy()` | `Collection|null` |
| `findByPk()`, `findById()`, `findByIdOrAlias()` | always `Model|null` |

---

*Source: https://docs.contao.org/5.x/dev/framework/models/ (+ /collections/, /customization/, /enumerations/)*
