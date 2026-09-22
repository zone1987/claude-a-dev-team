# sw-entity-hydration

The `EntityHydrator` translates flat DB rows (DBAL array) into typed `Entity` objects.

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

## Shopware DAL Entity Hydration — Deep Reference

Sources: `src/Core/Framework/DataAbstractionLayer/Dbal/EntityHydrator.php`
         `src/Core/Framework/DataAbstractionLayer/Command/CreateHydratorCommand.php`

---

### Contents

- [Class hierarchy](#class-hierarchy)
- [Lifecycle of a hydration](#lifecycle-of-a-hydration)
- [assign() — the overridable hook](#assign--the-overridable-hook)
- [hydrateFields() — field dispatch](#hydratefields--field-dispatch)
- [Partial Loading Details](#partial-loading-details)
- [Building the translation chain](#building-the-translation-chain)
- [ManyToMany ID mapping](#manytomany-id-mapping)
- [Registering a custom hydrator](#registering-a-custom-hydrator)
- [Performance comparison](#performance-comparison)
- [Runtime fields](#runtime-fields)
- [Caching](#caching)
- [dal:create:hydrators command](#dalcreatehydrators-command)

### Class hierarchy

```
EntityHydrator (base)
  └── ProductHydrator       (generated via dal:create:hydrators)
  └── CategoryHydrator      (generated)
  └── PropertyGroupHydrator (generated)
  └── ...                   (all entities with getHydratorClass())
```

With partial loading: always the base `EntityHydrator`, never a custom hydrator.

---

### Lifecycle of a hydration

```
EntityReader::load()
  → EntityHydrator::hydrate($collection, $entityClass, $definition, $rows, $root, $context, $partial)
      → self::$hydrated = []          (clear cache)
      → self::$partial = $partial     (set partial paths)
      → foreach $rows: hydrateEntity()
          → $hydratorClass = $definition->getHydratorClass()
          → if partial: $hydratorClass = EntityHydrator::class, $entityClass = PartialEntity::class
          → $hydrator = $container->get($hydratorClass)
          → buildUniqueIdentifier() → cache key
          → if cached: return self::$hydrated[$cacheKey]
          → $entity = new $entityClass()
          → addExtension(FOREIGN_KEYS, ArrayStruct)
          → addExtension(INTERNAL_MAPPING_STORAGE, ArrayStruct)
          → setUniqueIdentifier($identifier)
          → internalSetEntityData($entityName, $fieldVisibility)
          → $hydrator->assign($definition, $entity, $root, $row, $context)
          → self::$hydrated[$cacheKey] = $entity
```

---

### assign() — the overridable hook

```php
// Base implementation in EntityHydrator:
protected function assign(EntityDefinition $definition, Entity $entity, string $root, array $row, Context $context): Entity
{
    $entity = $this->hydrateFields($definition, $entity, $root, $row, $context, $definition->getFields());
    return $entity;
}

// Generated custom hydrator (performance-optimized):
protected function assign(EntityDefinition $definition, Entity $entity, string $root, array $row, Context $context): Entity
{
    // 1. StorageAware fields directly (no decode overhead):
    if (isset($row[$root . '.id'])) {
        $entity->id = Uuid::fromBytesToHex($row[$root . '.id']);
    }
    if (isset($row[$root . '.product_number'])) {
        $entity->productNumber = $row[$root . '.product_number'];
    }
    // ...

    // 2. ManyToOne/OneToOne associations:
    $entity->manufacturer = $this->manyToOne($row, $root, $definition->getField('manufacturer'), $context);

    // 3. Translations:
    $this->translate($definition, $entity, $row, $root, $context, $definition->getTranslatedFields());

    // 4. Extension fields (plugin extensions):
    $this->hydrateFields($definition, $entity, $root, $row, $context, $definition->getExtensionFields());

    // 5. ManyToMany via ID mapping:
    $this->manyToMany($row, $root, $entity, $definition->getField('categories'));

    return $entity;
}
```

---

### hydrateFields() — field dispatch

```php
foreach ($fields as $field) {
    // Partial filter: field not in $partial → skip
    if ($isPartial && !isset(self::$partialFullPaths[$key])) { continue; }

    // AssociationField + ArrayEntity → initialize to null
    if ($field instanceof AssociationField && $entity instanceof ArrayEntity) {
        $entity->set($property, null);
    }

    if ($field instanceof ParentAssociationField) { continue; }           // lazy
    if ($field instanceof ManyToManyAssociationField) { manyToMany(); continue; }
    if ($field instanceof ManyToOneAssociationField || OneToOneAssociationField) { manyToOne(); continue; }
    if ($field instanceof AssociationField) { continue; }                 // OneToMany: lazy

    // Scalar field:
    $value = $row[$root . '.' . $property];

    // TranslatedField → typed field from the translation definition
    if ($field instanceof TranslatedField) {
        $typed = EntityDefinitionQueryHelper::getTranslatedField($definition, $field);
    }

    if ($typed instanceof CustomFields) { customFields(); continue; }

    if ($field instanceof TranslatedField) {
        // Resolved value + Translation chain
        $entity->addTranslated($property, $decoded);
        $entity->assign([$property => $chainDecoded]);
        continue;
    }

    // Standard scalar:
    $decoded = $definition->decode($property, $value);
    $entity->assign([$property => $decoded]);
}
```

---

### Partial Loading Details

```php
// Criteria with partial fields:
$criteria->addFields(['id', 'name', 'price', 'manufacturer.name']);

// Internal: EntityHydrator::mapPartialFieldsToHydrate()
// Builds up self::$partialFullPaths:
// [
//   'product.id' => true,
//   'product.name' => true,
//   'product.price' => true,
//   'product.manufacturer' => true,
//   'product.manufacturer.name' => true,
// ]
```

All fields that are not in `$partialFullPaths` are skipped.  
Result: `PartialEntity` (not a typed entity object).

---

### Building the translation chain

```php
// EntityDefinitionQueryHelper::buildTranslationChain($root, $context, $inherited)
// → ['product.product', 'product.de-DE']  (main lang, fallback)
// With inheritance:
// → ['product.product', 'product.parent.product', 'product.de-DE', 'product.parent.de-DE']

// translate() iterates translatedFields:
foreach ($translatedFields as $field => $typed) {
    $fieldValue = self::value($row, $root, $field);      // resolved value
    $entity->addTranslated($field, decoded($fieldValue)); // all languages
    $entity->$field = decoded(value($row, $chain[0], $field)); // main language
}
```

---

### ManyToMany ID mapping

```sql
-- The query builds GROUP_CONCAT:
GROUP_CONCAT(HEX(product_category.category_id) SEPARATOR '||') AS `product.categories.id_mapping`
```

```php
protected function manyToMany(array $row, string $root, Entity $entity, ?Field $field): void
{
    $accessor = $root . '.' . $field->getPropertyName() . '.id_mapping';
    $ids = explode('||', (string) $row[$accessor]);
    $ids = array_map('strtolower', array_filter($ids));
    
    $mapping = $entity->getExtension(EntityReader::INTERNAL_MAPPING_STORAGE);
    $mapping->set($field->getPropertyName(), $ids);
    // The actual entity objects are loaded via a separate query
}
```

---

### Registering a custom hydrator

In the core, `dal:create:hydrators` generates
`src/Core/Framework/DependencyInjection/hydrator.xml` (existing core code). In a plugin the hydrator is
registered in `src/Resources/config/services/hydrators.php` — PHP, not XML (`XmlFileLoader` is
`@deprecated tag:v6.8.0`), explicitly and without autowiring
(→ `shopware-core` → `sw-services` → `DEPENDENCY-INJECTION.md`):

```php
$services->set(MyEntityHydrator::class)
    ->args([service('service_container')])
    ->public();
```

**Important:** the hydrator service must be `public="true"`, since it is loaded via `$container->get($hydratorClass)`.

---

### Performance comparison

| | Base EntityHydrator | Custom hydrator |
|---|---|---|
| Field dispatch | `hydrateFields()` loop + `decode()` | direct PHP property assignments |
| UUID decoding | `$field->getSerializer()->decode()` | `Uuid::fromBytesToHex()` directly |
| Type cast | via serializer | PHP built-in cast `(int)`, `(bool)`, `(float)` |
| Suitability | all entities, flexible | performance-critical entities |

---

### Runtime fields

```php
// In the definition:
(new StringField('computed_field', 'computedField'))->addFlags(new Runtime()),
```

`hydrateFields()` does **not** check the `Runtime` flag directly — but since no DB alias is built for runtime fields, `$row[$root . '.computedField']` is not set → the field is skipped. The value must be filled in by an `EntityLoadedEvent` subscriber.

---

### Caching

```php
private static array $hydrated = [];  // session cache (per hydrate() call)
private static array $manyToOne = []; // ManyToOne property name cache
private static array $translatedFields = []; // TranslatedField cache per entity name
```

The `self::$hydrated` cache is cleared at the start of every `hydrate()` call. It prevents duplicate hydration of the same entity ID within one query (e.g. when a product appears in several rows).

---

### dal:create:hydrators command

```bash
## Whitelist auto-detect: product*, category*, property*
bin/console dal:create:hydrators

## Explicit whitelist:
bin/console dal:create:hydrators product order order_line_item product_manufacturer

## Output:
## - src/Core/Content/Product/ProductHydrator.php
## - src/Core/Checkout/Order/OrderHydrator.php
## - (updates the definition: inserts getHydratorClass())
## - src/Core/Framework/DependencyInjection/hydrator.xml
```

**Limitations:**
- only for `EntityDefinition` (not translation/mapping)
- if `getHydratorClass()` already exists → the definition is not overwritten
- feature-flag-dependent fields: the feature flags must be active while generating
