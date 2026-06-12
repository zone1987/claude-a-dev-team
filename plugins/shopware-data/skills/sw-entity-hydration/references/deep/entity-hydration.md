# Shopware DAL Entity Hydration — Deep Reference

Quellen: `src/Core/Framework/DataAbstractionLayer/Dbal/EntityHydrator.php`
         `src/Core/Framework/DataAbstractionLayer/Command/CreateHydratorCommand.php`

---

## Klassen-Hierarchie

```
EntityHydrator (Basis)
  └── ProductHydrator       (generiert via dal:create:hydrators)
  └── CategoryHydrator      (generiert)
  └── PropertyGroupHydrator (generiert)
  └── ...                   (alle Entities mit getHydratorClass())
```

Bei Partial Loading: immer Basis-`EntityHydrator`, nie Custom-Hydrator.

---

## Lebenszyklus einer Hydration

```
EntityReader::load()
  → EntityHydrator::hydrate($collection, $entityClass, $definition, $rows, $root, $context, $partial)
      → self::$hydrated = []          (Cache leeren)
      → self::$partial = $partial     (Partial-Paths setzen)
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

## assign() — Der überschreibbare Hook

```php
// Basis-Implementierung in EntityHydrator:
protected function assign(EntityDefinition $definition, Entity $entity, string $root, array $row, Context $context): Entity
{
    $entity = $this->hydrateFields($definition, $entity, $root, $row, $context, $definition->getFields());
    return $entity;
}

// Generierter Custom Hydrator (Performance-optimiert):
protected function assign(EntityDefinition $definition, Entity $entity, string $root, array $row, Context $context): Entity
{
    // 1. StorageAware-Felder direkt (kein decode-Overhead):
    if (isset($row[$root . '.id'])) {
        $entity->id = Uuid::fromBytesToHex($row[$root . '.id']);
    }
    if (isset($row[$root . '.product_number'])) {
        $entity->productNumber = $row[$root . '.product_number'];
    }
    // ...

    // 2. ManyToOne/OneToOne Assoziationen:
    $entity->manufacturer = $this->manyToOne($row, $root, $definition->getField('manufacturer'), $context);

    // 3. Translations:
    $this->translate($definition, $entity, $row, $root, $context, $definition->getTranslatedFields());

    // 4. Extension-Felder (Plugin-Extensions):
    $this->hydrateFields($definition, $entity, $root, $row, $context, $definition->getExtensionFields());

    // 5. ManyToMany via ID-Mapping:
    $this->manyToMany($row, $root, $entity, $definition->getField('categories'));

    return $entity;
}
```

---

## hydrateFields() — Feld-Dispatch

```php
foreach ($fields as $field) {
    // Partial-Filter: Feld nicht in $partial → überspringen
    if ($isPartial && !isset(self::$partialFullPaths[$key])) { continue; }

    // AssociationField + ArrayEntity → null initialisieren
    if ($field instanceof AssociationField && $entity instanceof ArrayEntity) {
        $entity->set($property, null);
    }

    if ($field instanceof ParentAssociationField) { continue; }           // lazy
    if ($field instanceof ManyToManyAssociationField) { manyToMany(); continue; }
    if ($field instanceof ManyToOneAssociationField || OneToOneAssociationField) { manyToOne(); continue; }
    if ($field instanceof AssociationField) { continue; }                 // OneToMany: lazy

    // Scalar-Feld:
    $value = $row[$root . '.' . $property];

    // TranslatedField → typed field aus Translation-Definition
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

## Partial Loading Details

```php
// Criteria mit Partial-Fields:
$criteria->addFields(['id', 'name', 'price', 'manufacturer.name']);

// Intern: EntityHydrator::mapPartialFieldsToHydrate()
// Baut self::$partialFullPaths auf:
// [
//   'product.id' => true,
//   'product.name' => true,
//   'product.price' => true,
//   'product.manufacturer' => true,
//   'product.manufacturer.name' => true,
// ]
```

Alle Felder die nicht in `$partialFullPaths` sind, werden übersprungen.  
Ergebnis: `PartialEntity` (kein typiertes Entity-Objekt).

---

## Translation-Chain Aufbau

```php
// EntityDefinitionQueryHelper::buildTranslationChain($root, $context, $inherited)
// → ['product.product', 'product.de-DE']  (main lang, fallback)
// Mit Inheritance:
// → ['product.product', 'product.parent.product', 'product.de-DE', 'product.parent.de-DE']

// translate() iteriert translatedFields:
foreach ($translatedFields as $field => $typed) {
    $fieldValue = self::value($row, $root, $field);      // resolved value
    $entity->addTranslated($field, decoded($fieldValue)); // alle Sprachen
    $entity->$field = decoded(value($row, $chain[0], $field)); // main language
}
```

---

## ManyToMany ID-Mapping

```sql
-- Query baut GROUP_CONCAT:
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
    // Die eigentlichen Entity-Objekte werden per separate Query geladen
}
```

---

## Custom Hydrator registrieren (services.xml)

```xml
<!-- Generiert von dal:create:hydrators in src/Core/Framework/DependencyInjection/hydrator.xml -->
<service id="Shopware\Core\Content\Product\ProductHydrator" public="true">
    <argument type="service" id="service_container"/>
</service>
```

**Wichtig:** Der Hydrator-Service muss `public="true"` sein, da er per `$container->get($hydratorClass)` geladen wird.

---

## Performance-Vergleich

| | Basis EntityHydrator | Custom Hydrator |
|---|---|---|
| Field-Dispatch | `hydrateFields()` Loop + `decode()` | Direkte PHP-Property-Assigns |
| UUID-Decoding | `$field->getSerializer()->decode()` | `Uuid::fromBytesToHex()` direkt |
| Typ-Cast | Via Serializer | PHP built-in cast `(int)`, `(bool)`, `(float)` |
| Eignung | Alle Entities, flexible | Performance-kritische Entities |

---

## Runtime-Felder

```php
// In Definition:
(new StringField('computed_field', 'computedField'))->addFlags(new Runtime()),
```

`hydrateFields()` prüft das `Runtime`-Flag **nicht** direkt — aber da kein DB-Alias für Runtime-Felder gebaut wird, ist `$row[$root . '.computedField']` nicht gesetzt → Feld wird übersprungen. Wert muss per `EntityLoadedEvent`-Subscriber befüllt werden.

---

## Caching

```php
private static array $hydrated = [];  // Session-Cache (per hydrate()-Call)
private static array $manyToOne = []; // ManyToOne-Property-Name Cache
private static array $translatedFields = []; // TranslatedField-Cache per EntityName
```

Der `self::$hydrated`-Cache wird zu Beginn jedes `hydrate()`-Calls geleert. Er verhindert doppelte Hydration derselben Entity-ID innerhalb einer Query (z.B. wenn ein Produkt in mehreren Rows auftaucht).

---

## dal:create:hydrators Command

```bash
# Whitelist auto-detect: product*, category*, property*
bin/console dal:create:hydrators

# Explizite Whitelist:
bin/console dal:create:hydrators product order order_line_item product_manufacturer

# Ausgabe:
# - src/Core/Content/Product/ProductHydrator.php
# - src/Core/Checkout/Order/OrderHydrator.php
# - (Aktualisiert Definition: fügt getHydratorClass() ein)
# - src/Core/Framework/DependencyInjection/hydrator.xml
```

**Einschränkungen:**
- Nur für `EntityDefinition` (nicht Translation/Mapping)
- Wenn `getHydratorClass()` bereits existiert → Definition nicht überschrieben
- Feature-Flag-abhängige Felder: Feature-Flags müssen aktiv sein beim Generieren
