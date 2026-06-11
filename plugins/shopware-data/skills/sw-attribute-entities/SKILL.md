---
name: sw-attribute-entities
description: >
  Attribut-basierte DAL-Entities in Shopware 6 (6.6+): Entity-Definition via PHP-Attribute (#[Entity], Field-Attribute)
  statt klassischer EntityDefinition. Trigger: "attribute entity", "PHP attribute entity", "#[Entity]",
  "AutoIncrement attribute", "attributbasierte Definition", "modern entity definition". Shopware 6.7.
---

# Shopware 6 — Attribut-basierte Entities

Seit 6.6 lassen sich Entities kompakt über PHP-Attribute beschreiben — eine einzige annotierte Klasse statt
Definition + Entity + Collection.

```php
#[Entity('ff_example')]
class FfExample extends Entity
{
    #[PrimaryKey] #[Field(type: FieldType::UUID)]
    public string $id;

    #[Field(type: FieldType::STRING)]
    public ?string $name = null;

    #[Translations]
    public array $translations = [];
}
```

Shopware leitet Definition/Collection automatisch ab. Gut für neue, überschaubare Entities. Komplexe Fälle
(spezielle Serializer, viele Associations) weiterhin klassisch (`sw-entity-definition`).

→ Attribut-Referenz & Mapping: [references/attributes.md](references/attributes.md)
