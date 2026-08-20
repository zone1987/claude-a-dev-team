# sw-entity-hydration

The `EntityHydrator` translates flat DB rows (DBAL array) into typed `Entity` objects.

Details: [HYDRATION-DETAIL.md](HYDRATION-DETAIL.md)

## Contents

- [Core principle](#core-principle)
- [Partial loading (PartialEntity)](#partial-loading-partialentity)
- [Creating a custom hydrator](#creating-a-custom-hydrator)
- [Translation hydration](#translation-hydration)
- [Runtime fields](#runtime-fields)
- [Important methods](#important-methods)

## Core principle

```
DB-Row (flat array)  →  EntityHydrator::hydrate()  →  EntityCollection
                              ↓
                    hydrateEntity() per row
                              ↓
                    Hydrator::assign() (overridable)
                              ↓
                    Entity object (typed properties)
```

Every `EntityDefinition` can reference its own hydrator class:

```php
// In the definition:
public function getHydratorClass(): string
{
    return ProductHydrator::class;
}
```

The specific hydrator extends `EntityHydrator` and overrides `assign()`.

## Partial loading (PartialEntity)

```php
$criteria = new Criteria();
$criteria->addFields(['id', 'name', 'price']);
// → EntityHydrator uses PartialEntity instead of ProductEntity
// → only the requested fields are hydrated
```

With partial loading:
- `self::$partial !== []` → collection is replaced by an empty `EntityCollection`
- `PartialEntity` instead of the specific entity class
- base `EntityHydrator` instead of the specific hydrator

## Creating a custom hydrator

```bash
# Generates hydrator classes for the product, category, property entities:
bin/console dal:create:hydrators

# For specific entities (whitelist):
bin/console dal:create:hydrators product_manufacturer order_line_item
```

The generated hydrator contains direct property assignments (no `decode()`) for known types:

```php
class ProductHydrator extends EntityHydrator
{
    protected function assign(EntityDefinition $definition, Entity $entity, string $root, array $row, Context $context): Entity
    {
        if (isset($row[$root . '.id'])) {
            $entity->id = Uuid::fromBytesToHex($row[$root . '.id']);
        }
        if (isset($row[$root . '.active'])) {
            $entity->active = (bool) $row[$root . '.active'];
        }
        // ... all StorageAware fields directly
        
        $entity->manufacturer = $this->manyToOne($row, $root, $definition->getField('manufacturer'), $context);
        
        $this->translate($definition, $entity, $row, $root, $context, $definition->getTranslatedFields());
        $this->hydrateFields($definition, $entity, $root, $row, $context, $definition->getExtensionFields());
        
        return $entity;
    }
}
```

## Translation hydration

```
DB row contains translation chain aliases:
  product.name          → resolved fallback value
  product.product.name  → main language
  product.de-DE.name    → fallback language

EntityHydrator::translate():
  1. buildTranslationChain() → ['product.product', 'product.de-DE']
  2. Per TranslatedField: entity->addTranslated($property, $decoded)
  3. entity->$property = chainFieldValue (main language)
```

## Runtime fields

Fields with the `Runtime` flag are **skipped** by the hydrator — they are not read from the DB. The value must be set via a subscriber/decorator.

## Important methods

| Method | Purpose |
|---------|-------|
| `hydrate()` | entry point, iterates rows |
| `hydrateEntity()` | single row → entity, cached per ID |
| `assign()` | overridable hook for your own hydrator |
| `hydrateFields()` | iterates all fields, dispatches by type |
| `translate()` | resolve the translation chain |
| `manyToOne()` | hydrate the associated entity |
| `manyToMany()` | ID mapping from a `||`-separated string |
| `customFields()` | JSON merge for inherited custom fields |
| `buildUniqueIdentifier()` | extract PK values from the row |
| `createClass()` | `new $class()` (static, for hydrator extension) |
