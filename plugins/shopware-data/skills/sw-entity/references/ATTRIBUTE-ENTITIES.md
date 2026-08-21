# Shopware 6 — Attribute-based entities

Since 6.6 you can describe entities compactly through PHP attributes — a single annotated class instead of
definition + entity + collection.

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

Shopware derives definition and collection automatically. Good for new, manageable entities. Keep complex cases
(special serializers, many associations) classic (`sw-entity-definition`).

→ Attribute reference and mapping: [ATTRIBUTE-ENTITIES-ATTRIBUTES.md](ATTRIBUTE-ENTITIES-ATTRIBUTES.md)
