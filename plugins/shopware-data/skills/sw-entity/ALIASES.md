# sw-entity-aliases

The DAL separates the **storage name** (DB column) from the **property name** (PHP object).

Details: [ALIASES-DETAIL.md](ALIASES-DETAIL.md)

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
