# sw-entity-aliases

Das DAL trennt **Storage-Name** (DB-Spalte) von **Property-Name** (PHP-Objekt).

Details: [ALIASES-DETAIL.md](ALIASES-DETAIL.md)

## Contents

- [Grundprinzip](#grundprinzip)
- [SQL-Aliase in Queries](#sql-aliase-in-queries)
- [Association-Alias](#association-alias)
- [getByStorageName](#getbystoragename)
- [buildTranslationChain](#buildtranslationchain)
- [Criteria-Accessor vs. Storage-Name](#criteria-accessor-vs-storage-name)
- [Entity-Name als Alias-Root](#entity-name-als-alias-root)

## Grundprinzip

```php
// IdField('id', 'id')          → storage=id,              property=id
// FkField('tax_id', 'taxId',…) → storage=tax_id,          property=taxId
// StringField('product_number', 'productNumber') → storage=product_number, property=productNumber
```

- `StorageAware::getStorageName()` → DB-Spaltenname
- `Field::getPropertyName()` → PHP-Propertyname

## SQL-Aliase in Queries

Der DAL baut alle SQL-Aliase nach dem Schema `<root>.<propertyName>`:

```sql
-- root = 'product'
SELECT `product`.`id` AS `product.id`,
       `product`.`product_number` AS `product.productNumber`,
       `product`.`tax_id` AS `product.taxId`
FROM `product`
```

Der Escape-Helper: `EntityDefinitionQueryHelper::escape($string)` → `` `$string` ``

## Association-Alias

```
product.manufacturer           → JOIN-Alias für ManyToOne
product.manufacturer.name      → Criteria-Accessor über Association hinweg
product.translations           → Translation-Alias-Root
product.translation            → Resolved-Translation-Alias (main language)
product.translation.de-DE      → Fallback-Language-Alias
```

In Criteria: Dot-Notation folgt der PHP-Property-Name (nicht storageName):

```php
$criteria->addAssociation('manufacturer');        // property: 'manufacturer'
$criteria->addFilter(new EqualsFilter('manufacturer.name', 'ACME'));
// → SQL: LEFT JOIN product_manufacturer ON ... WHERE `product.manufacturer`.`name` = :param
```

## getByStorageName

```php
// Feld per DB-Spaltenname finden (z.B. 'tax_id' → TaxId-FkField):
$field = $definition->getFields()->getByStorageName('tax_id');
// → FkField mit propertyName='taxId'

// Kompilingtes FieldCollection nötig:
$compiled = $definition->getFields();  // CompiledFieldCollection
$field = $compiled->getByStorageName('product_number');
```

## buildTranslationChain

```php
// EntityDefinitionQueryHelper::buildTranslationChain($root, $context, $inherited)

// Ohne Inheritance:
// ['product.translation', 'product.translation.fallback_1', ...]
// (Anzahl abhängig von Language-Chain im Context)

// Mit Inheritance:
// ['product.translation', 'product.parent.translation', 'product.translation.fallback_1', 'product.parent.translation.fallback_1']
```

Interner SQL-Alias je Sprache im Query:
```sql
`product.translation` AS `product.name`  -- resolved value
`product.translation`.`name` AS `product.product.name`  -- main lang
```

## Criteria-Accessor vs. Storage-Name

```php
// Immer Property-Namen (camelCase) in Criteria, NIE storage_names:
$criteria->addFilter(new EqualsFilter('productNumber', 'SW-100'));  // ✓
$criteria->addFilter(new EqualsFilter('product_number', 'SW-100')); // ✗ → Exception

// Tief verschachtelt via Dot-Notation:
$criteria->addFilter(new EqualsFilter('categories.name', 'Electronics'));
$criteria->addFilter(new EqualsFilter('manufacturer.translations.name', 'Acme'));
```

## Entity-Name als Alias-Root

Der Entity-Name (Tabellenname) ist immer der Start-Alias in einer Query:
```
product                → root alias für ProductDefinition
order_line_item        → root alias für OrderLineItemDefinition
product.manufacturer   → JOIN-Alias für ManyToOne auf ProductManufacturerDefinition
```
