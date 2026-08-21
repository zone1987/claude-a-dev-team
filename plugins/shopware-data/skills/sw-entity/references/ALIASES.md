# sw-entity-aliases

The DAL separates the **storage name** (DB column) from the **property name** (PHP object).


## Contents

- [Basic principle](#basic-principle)
- [SQL aliases in queries](#sql-aliases-in-queries)
- [Association alias](#association-alias)
- [getByStorageName](#getbystoragename)
- [buildTranslationChain](#buildtranslationchain)
- [Criteria accessor vs. storage name](#criteria-accessor-vs-storage-name)
- [Entity name as alias root](#entity-name-as-alias-root)

## Basic principle

```php
// IdField('id', 'id')          → storage=id,              property=id
// FkField('tax_id', 'taxId',…) → storage=tax_id,          property=taxId
// StringField('product_number', 'productNumber') → storage=product_number, property=productNumber
```

- `StorageAware::getStorageName()` → DB column name
- `Field::getPropertyName()` → PHP property name

## SQL aliases in queries

The DAL builds all SQL aliases following the `<root>.<propertyName>` scheme:

```sql
-- root = 'product'
SELECT `product`.`id` AS `product.id`,
       `product`.`product_number` AS `product.productNumber`,
       `product`.`tax_id` AS `product.taxId`
FROM `product`
```

The escape helper: `EntityDefinitionQueryHelper::escape($string)` → `` `$string` ``

## Association alias

```
product.manufacturer           → JOIN alias for ManyToOne
product.manufacturer.name      → Criteria accessor across the association
product.translations           → translation alias root
product.translation            → resolved translation alias (main language)
product.translation.de-DE      → fallback language alias
```

In Criteria: dot notation follows the PHP property name (not the storageName):

```php
$criteria->addAssociation('manufacturer');        // property: 'manufacturer'
$criteria->addFilter(new EqualsFilter('manufacturer.name', 'ACME'));
// → SQL: LEFT JOIN product_manufacturer ON ... WHERE `product.manufacturer`.`name` = :param
```

## getByStorageName

```php
// Find a field by DB column name (e.g. 'tax_id' → TaxId FkField):
$field = $definition->getFields()->getByStorageName('tax_id');
// → FkField with propertyName='taxId'

// Compiled FieldCollection required:
$compiled = $definition->getFields();  // CompiledFieldCollection
$field = $compiled->getByStorageName('product_number');
```

## buildTranslationChain

```php
// EntityDefinitionQueryHelper::buildTranslationChain($root, $context, $inherited)

// Without inheritance:
// ['product.translation', 'product.translation.fallback_1', ...]
// (count depends on the language chain in the context)

// With inheritance:
// ['product.translation', 'product.parent.translation', 'product.translation.fallback_1', 'product.parent.translation.fallback_1']
```

Internal SQL alias per language in the query:
```sql
`product.translation` AS `product.name`  -- resolved value
`product.translation`.`name` AS `product.product.name`  -- main lang
```

## Criteria accessor vs. storage name

```php
// Always property names (camelCase) in Criteria, NEVER storage_names:
$criteria->addFilter(new EqualsFilter('productNumber', 'SW-100'));  // ✓
$criteria->addFilter(new EqualsFilter('product_number', 'SW-100')); // ✗ → exception

// Deeply nested via dot notation:
$criteria->addFilter(new EqualsFilter('categories.name', 'Electronics'));
$criteria->addFilter(new EqualsFilter('manufacturer.translations.name', 'Acme'));
```

## Entity name as alias root

The entity name (table name) is always the starting alias in a query:
```
product                → root alias for ProductDefinition
order_line_item        → root alias for OrderLineItemDefinition
product.manufacturer   → JOIN alias for ManyToOne to ProductManufacturerDefinition
```

## Shopware DAL Entity Aliases — Deep Reference

Sources:
- `src/Core/Framework/DataAbstractionLayer/Field/Field.php`
- `src/Core/Framework/DataAbstractionLayer/Field/StorageAware.php`
- `src/Core/Framework/DataAbstractionLayer/CompiledFieldCollection.php`
- `src/Core/Framework/DataAbstractionLayer/Dbal/EntityDefinitionQueryHelper.php`
- `src/Core/Framework/DataAbstractionLayer/FieldCollection.php`

---

### Contents

- [Storage name vs. property name](#storage-name-vs-property-name)
- [CompiledFieldCollection — lookup maps](#compiledfieldcollection--lookup-maps)
- [SQL alias scheme](#sql-alias-scheme)
- [EntityDefinitionQueryHelper::escape()](#entitydefinitionqueryhelperescape)
- [getFieldAccessor() — Accessor Resolution](#getfieldaccessor--accessor-resolution)
- [buildTranslationChain()](#buildtranslationchain)
- [Field Resolver and JOIN Alias](#field-resolver-and-join-alias)
- [Criteria Field Notation Rules](#criteria-field-notation-rules)
- [Known Pitfalls](#known-pitfalls)

### Storage name vs. property name

Every `StorageAware` field has two names:

| Term | Source | Usage |
|---------|--------|------------|
| **storageName** | `StorageAware::getStorageName()` | DB column name in `CREATE TABLE`, SQL WHERE |
| **propertyName** | `Field::getPropertyName()` | PHP property, Criteria accessor, SQL alias |

```php
// Definition:
new FkField('tax_id', 'taxId', TaxDefinition::class)
//            ↑ storageName  ↑ propertyName

// StorageAware interface:
interface StorageAware {
    public function getStorageName(): string;
}

// Field base class:
class Field {
    public function __construct(protected string $propertyName) {}
    public function getPropertyName(): string { return $this->propertyName; }
}

// Concrete class (e.g. IdField):
class IdField extends Field implements StorageAware {
    public function __construct(protected string $storageName, string $propertyName) {
        parent::__construct($propertyName);
    }
    public function getStorageName(): string { return $this->storageName; }
}
```

#### Fields WITHOUT StorageAware

These fields have no storageName (no own DB column):
- `TranslatedField` — points to the translation definition
- `AssociationField` (all) — JOIN, no own column
- `Runtime` fields with the `Runtime` flag
- `ChildCountField`, `TreeLevelField`, `TreePathField` — computed fields

---

### CompiledFieldCollection — lookup maps

After `FieldCollection::compile()` a `CompiledFieldCollection` is created with pre-built maps:

```php
class CompiledFieldCollection {
    private array $mappedByStorageName = [];  // storage_name → Field
    private array $elements = [];             // propertyName → Field

    public function getByStorageName(string $storageName): ?Field {
        return $this->mappedByStorageName[$storageName] ?? null;
    }

    // Built up in compile():
    // foreach $fields:
    //   $this->mappedByStorageName[$field->getStorageName()] = $field;
}
```

Usage:
```php
// In EntityHydrator::getManyToOneProperty():
$reference = $field->getReferenceDefinition()->getFields()->getByStorageName(
    $field->getReferenceField()  // 'id' → propertyName 'id'
);
```

---

### SQL alias scheme

#### Scalar Fields

```sql
-- Schema: `<table>`.`<storageName>` AS `<root>.<propertyName>`
SELECT `product`.`product_number` AS `product.productNumber`
SELECT `product`.`tax_id`         AS `product.taxId`
SELECT `product`.`id`             AS `product.id`
```

#### Association Aliases (JOINs)

```sql
-- ManyToOne: root = 'product.manufacturer'
LEFT JOIN `product_manufacturer` AS `product.manufacturer`
    ON `product`.`product_manufacturer_id` = `product.manufacturer`.`id`

SELECT `product.manufacturer`.`name` AS `product.manufacturer.name`
```

#### Translation Aliases

```sql
-- root = 'product', main language = 'de-DE'
LEFT JOIN `product_translation` AS `product.product`
    ON `product`.`id` = `product.product`.`product_id`
    AND `product.product`.`language_id` = :languageId

-- Fallback:
LEFT JOIN `product_translation` AS `product.de-DE`
    ON `product`.`id` = `product.de-DE`.`product_id`
    AND `product.de-DE`.`language_id` = :fallbackLanguageId

-- SELECT:
COALESCE(`product.product`.`name`, `product.de-DE`.`name`)
    AS `product.name`                         -- resolved value
`product.product`.`name`
    AS `product.product.name`                 -- main language raw
```

---

### EntityDefinitionQueryHelper::escape()

```php
public static function escape(string $string): string
{
    if (str_contains($string, '`')) {
        throw DataAbstractionLayerException::invalidIdentifier($string);
    }
    return '`' . $string . '`';
}
```

All table and column names are escaped. Aliases (AS `product.name`) as well.  
**Important:** The dot in `product.name` is part of the alias string — MySQL allows backtick-escaped strings containing dots.

---

### getFieldAccessor() — Accessor Resolution

```php
// EntityDefinitionQueryHelper::getFieldAccessor(
//   $fieldName,    // 'productNumber' or 'manufacturer.name'
//   $definition,   // ProductDefinition
//   $root,         // 'product'
//   $context
// ): string

// Simple field:
getFieldAccessor('productNumber', $productDef, 'product', $context)
// → 'product.productNumber' (= SQL alias)

// Translated field:
getFieldAccessor('name', $productDef, 'product', $context)
// → COALESCE(`product.product`.`name`, `product.de-DE`.`name`)
//   (with inheritance: more complex COALESCE including parent)

// Inherited field:
getFieldAccessor('taxId', $productDef, 'product', $context)
// → COALESCE(`product`.`tax_id`, `product.parent`.`tax_id`)
```

---

### buildTranslationChain()

```php
public static function buildTranslationChain(string $root, Context $context, bool $includeParent): array
{
    // Returns the alias roots of the translation JOINs
    // Format: ['<root>.translation', '<root>.translation.fallback_1', ...]

    // With $includeParent = true (isInheritanceAware && considerInheritance):
    // ['<root>.translation', '<root>.parent.translation', '<root>.translation.fallback_1', '<root>.parent.translation.fallback_1']
}
```

This chain is used in `hydrateFields()` to read the correct alias value from the row array:

```php
$chain = EntityDefinitionQueryHelper::buildTranslationChain($root, $context, $inherited);
$key = array_shift($chain) . '.' . $property;
// → 'product.translation.name' → $row['product.translation.name']
```

---

### Field Resolver and JOIN Alias

For nested Criteria paths (`manufacturer.name`) the DAL resolves as follows:

```
resolveAccessor('manufacturer.name', ProductDefinition, 'product', $query, $context)
  → $alias = 'product'
  → field = getField('manufacturer') → ManyToOneAssociationField
  → resolver.join(FieldResolverContext('product', 'product', field, ...))
      → JOIN `product_manufacturer` AS `product.manufacturer`
  → $alias = 'product.manufacturer'
  → field = getField('name') on ProductManufacturerDefinition
  → return 'product.manufacturer.name'
```

---

### Criteria Field Notation Rules

| Notation | Meaning | Example |
|----------|-----------|---------|
| `propertyName` | Direct field | `productNumber` |
| `a.b` | Association field | `manufacturer.name` |
| `a.b.c` | Deeply nested | `manufacturer.translations.name` |
| `extensions.myExt.field` | Extension field | `extensions.myPlugin.customProp` |

**Always** camelCase property names, never snake_case storage names in Criteria.

---

### Known Pitfalls

1. **`product_number` instead of `productNumber`** in Criteria → `UnmappedFieldException`
2. **Association without `->addAssociation()`** and then a field filter on it → JOIN is missing
3. **Filtering a translated field directly** → the DAL builds COALESCE automatically, no manual JOIN needed
4. **`getByStorageName()`** returns `null` for TranslatedField (not StorageAware)
5. **Version fields** have storage `version_id` and property `versionId` — for ManyToMany mappings onto versioned entities there is `ReferenceVersionField` with an explicit storage name
