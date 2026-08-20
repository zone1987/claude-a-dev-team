# sw-entity-hydration

Der `EntityHydrator` übersetzt flache DB-Zeilen (DBAL-Array) in typisierte `Entity`-Objekte.

Details: [HYDRATION-DETAIL.md](HYDRATION-DETAIL.md)

## Contents

- [Kernaprinzip](#kernaprinzip)
- [Partial Loading (PartialEntity)](#partial-loading-partialentity)
- [Custom Hydrator erzeugen](#custom-hydrator-erzeugen)
- [Translation-Hydration](#translation-hydration)
- [Runtime-Felder](#runtime-felder)
- [Wichtige Methoden](#wichtige-methoden)

## Kernaprinzip

```
DB-Row (flat array)  →  EntityHydrator::hydrate()  →  EntityCollection
                              ↓
                    hydrateEntity() per Row
                              ↓
                    Hydrator::assign() (überschreibbar)
                              ↓
                    Entity-Objekt (typed properties)
```

Jede `EntityDefinition` kann eine eigene Hydrator-Klasse referenzieren:

```php
// In der Definition:
public function getHydratorClass(): string
{
    return ProductHydrator::class;
}
```

Der spezifische Hydrator extends `EntityHydrator` und überschreibt `assign()`.

## Partial Loading (PartialEntity)

```php
$criteria = new Criteria();
$criteria->addFields(['id', 'name', 'price']);
// → EntityHydrator nutzt PartialEntity statt ProductEntity
// → Nur die angeforderten Felder werden hydratisiert
```

Bei Partial Loading:
- `self::$partial !== []` → Collection wird durch leere `EntityCollection` ersetzt
- `PartialEntity` statt spez. Entity-Klasse
- Basis-`EntityHydrator` statt spez. Hydrator

## Custom Hydrator erzeugen

```bash
# Generiert Hydrator-Klassen für product, category, property-Entities:
bin/console dal:create:hydrators

# Für spezifische Entities (Whitelist):
bin/console dal:create:hydrators product_manufacturer order_line_item
```

Der generierte Hydrator enthält direkte Property-Assigns (kein `decode()`) für bekannte Typen:

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
        // ... alle StorageAware-Felder direkt
        
        $entity->manufacturer = $this->manyToOne($row, $root, $definition->getField('manufacturer'), $context);
        
        $this->translate($definition, $entity, $row, $root, $context, $definition->getTranslatedFields());
        $this->hydrateFields($definition, $entity, $root, $row, $context, $definition->getExtensionFields());
        
        return $entity;
    }
}
```

## Translation-Hydration

```
DB-Row enthält Translations-Chain-Aliase:
  product.name          → resolved fallback value
  product.product.name  → main language
  product.de-DE.name    → fallback language

EntityHydrator::translate():
  1. buildTranslationChain() → ['product.product', 'product.de-DE']
  2. Per TranslatedField: entity->addTranslated($property, $decoded)
  3. entity->$property = chainFieldValue (main language)
```

## Runtime-Felder

Felder mit `Runtime`-Flag werden vom Hydrator **übersprungen** — sie werden nicht aus der DB gelesen. Wert muss per Subscriber/Decorator gesetzt werden.

## Wichtige Methoden

| Methode | Zweck |
|---------|-------|
| `hydrate()` | Entry-Point, iteriert Rows |
| `hydrateEntity()` | Einzelne Row → Entity, cached per ID |
| `assign()` | Überschreibbarer Hook für eigenen Hydrator |
| `hydrateFields()` | Iteriert alle Felder, dispatcht nach Typ |
| `translate()` | Translation-Chain auflösen |
| `manyToOne()` | Assoziierte Entity hydratisieren |
| `manyToMany()` | ID-Mapping aus `||`-separiertem String |
| `customFields()` | JSON merge bei Inherited CustomFields |
| `buildUniqueIdentifier()` | PK-Werte aus Row extrahieren |
| `createClass()` | `new $class()` (static, für Hydrator-Extension) |
