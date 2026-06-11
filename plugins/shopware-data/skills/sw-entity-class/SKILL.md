---
name: sw-entity-class
description: >
  Die Entity-Klasse einer Shopware-6 DAL-Definition: Properties, Getter/Setter, EntityIdTrait, translated-Felder,
  Association-Properties. Trigger: "Entity-Klasse", "Entity getter setter", "EntityIdTrait", "Entity property",
  "Entity class shopware", "->getName() entity". Shopware 6.7.
---

# Shopware 6 — Entity-Klasse

Die Entity ist das typisierte Datenobjekt zur Definition. Sie erweitert `Entity` und nutzt meist `EntityIdTrait`
(liefert `id`). Pro Feld der Definition ein `protected` Property + Getter/Setter; nullable für optionale Felder.

```php
class FfExampleEntity extends Entity
{
    use EntityIdTrait;
    protected string $name;
    protected ?string $description = null;
    public function getName(): string { return $this->name; }
    public function setName(string $name): void { $this->name = $name; }
}
```

`TranslatedField`-Werte landen im `translated`-Array bzw. werden auf die Properties gemappt (`sw-translations`).
Association-Properties typisieren auf die jeweilige Entity/Collection. Keine Geschäftslogik in der Entity.

→ Vollständiges Beispiel: [references/example.md](references/example.md)
