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

→ Attribut-Referenz & Mapping: [ATTRIBUTE-ENTITIES-ATTRIBUTES.md](ATTRIBUTE-ENTITIES-ATTRIBUTES.md)
