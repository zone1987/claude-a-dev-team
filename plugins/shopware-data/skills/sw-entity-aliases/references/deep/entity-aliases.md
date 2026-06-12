# Shopware DAL Entity Aliases — Deep Reference

Quellen:
- `src/Core/Framework/DataAbstractionLayer/Field/Field.php`
- `src/Core/Framework/DataAbstractionLayer/Field/StorageAware.php`
- `src/Core/Framework/DataAbstractionLayer/CompiledFieldCollection.php`
- `src/Core/Framework/DataAbstractionLayer/Dbal/EntityDefinitionQueryHelper.php`
- `src/Core/Framework/DataAbstractionLayer/FieldCollection.php`

---

## Storage-Name vs. Property-Name

Jedes `StorageAware`-Feld hat zwei Namen:

| Begriff | Quelle | Verwendung |
|---------|--------|------------|
| **storageName** | `StorageAware::getStorageName()` | DB-Spaltenname in `CREATE TABLE`, SQL WHERE |
| **propertyName** | `Field::getPropertyName()` | PHP-Property, Criteria-Accessor, SQL-Alias |

```php
// Definition:
new FkField('tax_id', 'taxId', TaxDefinition::class)
//            ↑ storageName  ↑ propertyName

// StorageAware-Interface:
interface StorageAware {
    public function getStorageName(): string;
}

// Field-Basisklasse:
class Field {
    public function __construct(protected string $propertyName) {}
    public function getPropertyName(): string { return $this->propertyName; }
}

// Konkrete Klasse (z.B. IdField):
class IdField extends Field implements StorageAware {
    public function __construct(protected string $storageName, string $propertyName) {
        parent::__construct($propertyName);
    }
    public function getStorageName(): string { return $this->storageName; }
}
```

### Felder OHNE StorageAware

Diese Felder haben keinen storageName (kein eigener DB-Column):
- `TranslatedField` — verweist auf Translation-Definition
- `AssociationField` (alle) — JOIN, kein eigener Column
- `Runtime`-Felder mit Flag `Runtime`
- `ChildCountField`, `TreeLevelField`, `TreePathField` — berechnete Felder

---

## CompiledFieldCollection — Lookup-Maps

Nach `FieldCollection::compile()` wird eine `CompiledFieldCollection` erzeugt mit pre-built Maps:

```php
class CompiledFieldCollection {
    private array $mappedByStorageName = [];  // storage_name → Field
    private array $elements = [];             // propertyName → Field

    public function getByStorageName(string $storageName): ?Field {
        return $this->mappedByStorageName[$storageName] ?? null;
    }

    // Aufgebaut in compile():
    // foreach $fields:
    //   $this->mappedByStorageName[$field->getStorageName()] = $field;
}
```

Anwendung:
```php
// In EntityHydrator::getManyToOneProperty():
$reference = $field->getReferenceDefinition()->getFields()->getByStorageName(
    $field->getReferenceField()  // 'id' → propertyName 'id'
);
```

---

## SQL-Alias-Schema

### Scalar-Felder

```sql
-- Schema: `<table>`.`<storageName>` AS `<root>.<propertyName>`
SELECT `product`.`product_number` AS `product.productNumber`
SELECT `product`.`tax_id`         AS `product.taxId`
SELECT `product`.`id`             AS `product.id`
```

### Association-Aliase (JOINs)

```sql
-- ManyToOne: root = 'product.manufacturer'
LEFT JOIN `product_manufacturer` AS `product.manufacturer`
    ON `product`.`product_manufacturer_id` = `product.manufacturer`.`id`

SELECT `product.manufacturer`.`name` AS `product.manufacturer.name`
```

### Translation-Aliase

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

## EntityDefinitionQueryHelper::escape()

```php
public static function escape(string $string): string
{
    if (str_contains($string, '`')) {
        throw DataAbstractionLayerException::invalidIdentifier($string);
    }
    return '`' . $string . '`';
}
```

Alle Table- und Column-Namen werden escaped. Aliase (AS `product.name`) auch.  
**Wichtig:** Der Punkt in `product.name` ist Teil des Alias-Strings — MySQL erlaubt Backtick-escaped Strings mit Punkten.

---

## getFieldAccessor() — Accessor-Auflösung

```php
// EntityDefinitionQueryHelper::getFieldAccessor(
//   $fieldName,    // 'productNumber' oder 'manufacturer.name'
//   $definition,   // ProductDefinition
//   $root,         // 'product'
//   $context
// ): string

// Einfaches Feld:
getFieldAccessor('productNumber', $productDef, 'product', $context)
// → 'product.productNumber' (= SQL-Alias)

// Translated Feld:
getFieldAccessor('name', $productDef, 'product', $context)
// → COALESCE(`product.product`.`name`, `product.de-DE`.`name`)
//   (bei Inheritance: komplexeres COALESCE mit parent)

// Inherited Feld:
getFieldAccessor('taxId', $productDef, 'product', $context)
// → COALESCE(`product`.`tax_id`, `product.parent`.`tax_id`)
```

---

## buildTranslationChain()

```php
public static function buildTranslationChain(string $root, Context $context, bool $includeParent): array
{
    // Gibt Alias-Roots der Translation-JOINs zurück
    // Format: ['<root>.translation', '<root>.translation.fallback_1', ...]

    // Mit $includeParent = true (isInheritanceAware && considerInheritance):
    // ['<root>.translation', '<root>.parent.translation', '<root>.translation.fallback_1', '<root>.parent.translation.fallback_1']
}
```

Diese Chain wird in `hydrateFields()` genutzt um den richtigen Alias-Wert aus dem Row-Array zu lesen:

```php
$chain = EntityDefinitionQueryHelper::buildTranslationChain($root, $context, $inherited);
$key = array_shift($chain) . '.' . $property;
// → 'product.translation.name' → $row['product.translation.name']
```

---

## Field-Resolver und JOIN-Alias

Bei verschachtelten Criteria-Pfaden (`manufacturer.name`) resolved der DAL:

```
resolveAccessor('manufacturer.name', ProductDefinition, 'product', $query, $context)
  → $alias = 'product'
  → field = getField('manufacturer') → ManyToOneAssociationField
  → resolver.join(FieldResolverContext('product', 'product', field, ...))
      → JOIN `product_manufacturer` AS `product.manufacturer`
  → $alias = 'product.manufacturer'
  → field = getField('name') auf ProductManufacturerDefinition
  → return 'product.manufacturer.name'
```

---

## Criteria-Feld-Notation Regeln

| Notation | Bedeutung | Beispiel |
|----------|-----------|---------|
| `propertyName` | Direktes Feld | `productNumber` |
| `a.b` | Association-Feld | `manufacturer.name` |
| `a.b.c` | Tief verschachtelt | `manufacturer.translations.name` |
| `extensions.myExt.field` | Extension-Feld | `extensions.myPlugin.customProp` |

**Immer** camelCase Property-Namen, niemals snake_case Storage-Namen in Criteria.

---

## Bekannte Fallstricke

1. **`product_number` statt `productNumber`** in Criteria → `UnmappedFieldException`
2. **Association ohne `->addAssociation()`** und dann Feld-Filter darauf → JOIN fehlt
3. **Translated-Feld direkt filtern** → DAL baut automatisch COALESCE, kein manuelles JOIN nötig
4. **`getByStorageName()`** gibt `null` für TranslatedField (kein StorageAware)
5. **Version-Felder** haben storage `version_id` und property `versionId` — bei ManyToMany-Mappings auf versionierte Entities gibt es `ReferenceVersionField` mit explizitem storage-Name
