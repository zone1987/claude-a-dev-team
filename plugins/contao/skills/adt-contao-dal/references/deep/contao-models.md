# Contao Models, Collections & Enumerations (5.x)

## Überblick

Models sind Objekte zum Erstellen neuer Datensätze sowie zum Lesen und Modifizieren bestehender Datensätze aus der Datenbank – vergleichbar mit Doctrine Entities. Jede Datenbanktabelle entspricht einer Model-Klasse (`tl_article` → `ArticleModel`, `tl_news` → `NewsModel`).

---

## Datensätze abrufen

Statische Methoden für Datenbankabfragen:

| Methode | Beschreibung |
|---------|-------------|
| `findById($id)` | Datensatz per ID |
| `findByIdOrAlias($value)` | ID oder Alias-Feld |
| `findOneBy($field, $value)` | Einzelner Datensatz |
| `findBy($field, $value, $options)` | Collection von Datensätzen |
| `findAll()` | Alle Datensätze |
| `countBy($field, $value)` | Anzahl Treffer |

### Late Static Binding (`__callStatic`)

```php
$page = PageModel::findById(5);
$page = PageModel::findOneByAdminEmail('admin@example.com');
$pages = PageModel::findByLanguage('de');
$count = PageModel::countByLanguage('de');
```

Gibt `null` zurück wenn kein Treffer.

---

## Datensätze modifizieren

```php
$page = PageModel::findById(5);
$id   = $page->id;
$page->alias = 'index';
$page->save();
```

---

## Options-Parameter

| Option | Zweck | SQL-Äquivalent | Beispiel |
|--------|-------|----------------|---------|
| `limit` | Anzahl begrenzen | `LIMIT` | `3` |
| `offset` | Anfang überspringen | `OFFSET` | `10` |
| `order` | Sortierung | `ORDER BY` | `'id DESC'` |
| `return` | Ausgabetyp | — | `'Model'`, `'Collection'`, `'Array'` |
| `eager` | Eager Loading | `LEFT JOIN` | `true` |
| `having` | Join-Filter | `HAVING` | `"author__username = 'k.jones'"` |

```php
$options = ['limit' => 5, 'offset' => 10, 'order' => 'title ASC'];
$pages   = PageModel::findBy('pid', 1, $options);
$pages   = PageModel::findByPid(1, $options);
```

---

## Eager Loading / Relationen

`'eager' => true` lädt verwandte `hasOne`/`belongsTo`-Datensätze per JOIN. Spalten der Fremdtabelle erhalten das Präfix `<foreignKey>__`.

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

Eine `Collection` enthält immer mindestens ein Model. Kein Treffer → `null` (keine leere Collection).

### findAll / findMultipleByIds

```php
$pages = PageModel::findAll();
$pages = PageModel::findMultipleByIds([1, 2, 3]);
```

### Komplexe Bedingungen

```php
$pages = PageModel::findBy(
    ['language = ?', 'pid = ?'],
    ['de', 1]
);

// IN-Klausel (IDs immer als intval!)
$items = FoobarModel::findBy(
    ['type = ?', 'id IN (' . implode(',', array_map('\intval', $ids)) . ')'],
    ['store']
);
```

### Iteration

```php
foreach (PageModel::findAll() as $page) {
    // $page ist eine Model-Instanz
}
```

### Spalten extrahieren

```php
$titles = $pages->fetchEach('title');   // Eine Spalte aller Zeilen
$rows   = $pages->fetchAll();           // Alle Spalten aller Zeilen
```

---

## Custom Models (3 Schritte)

### 1. DCA anlegen

```php
// contao/dca/tl_example.php
$GLOBALS['TL_DCA']['tl_example'] = [ /* … */ ];
```

### 2. Model-Klasse erstellen

Namenskonvention: `tl_` entfernen, snake_case → PascalCase, „Model" anhängen.

```php
// src/Model/ExampleModel.php
namespace App\Model;

use Contao\Model;

/**
 * @property string $hash  IDE-Unterstützung
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

### 3. Model registrieren

```php
// contao/config/config.php
use App\Model\ExampleModel;

$GLOBALS['TL_MODELS']['tl_example'] = ExampleModel::class;
```

---

## Enumerations (ab Contao 5.3)

### DCA-Konfiguration

```php
// contao/dca/tl_member.php
$GLOBALS['TL_DCA']['tl_member']['fields']['salutation'] = [
    'inputType' => 'select',
    'enum'      => App\Data\Salutation::class,
];
```

### Auflösung

```php
$member = MemberModel::findById(42);

$member->salutation;                // Gibt String zurück, z.B. 'ms'
$member->getEnum('salutation');     // Gibt App\Data\Salutation-Instanz oder null zurück
```

### Type-Safe Getter mit Fallback

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

## Rückgabewerte im Überblick

| Methode | Rückgabe |
|---------|----------|
| `findOneBy()` | `Model|null` |
| `findBy()` | `Collection|null` |
| `findByPk()`, `findById()`, `findByIdOrAlias()` | immer `Model|null` |

---

*Quelle: https://docs.contao.org/5.x/dev/framework/models/ (+ /collections/, /customization/, /enumerations/)*
