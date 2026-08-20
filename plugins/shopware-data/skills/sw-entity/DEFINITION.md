# Shopware 6 — EntityDefinition

The `EntityDefinition` describes the schema (fields, associations, flags) of a DAL entity. Three building blocks always
belong together: **definition** (schema), **entity** (`sw-entity-class`), **collection** (`sw-entity-collection`).

```php
class FfExampleDefinition extends EntityDefinition
{
    public const ENTITY_NAME = 'ff_example';
    public function getEntityName(): string { return self::ENTITY_NAME; }
    public function getEntityClass(): string { return FfExampleEntity::class; }
    public function getCollectionClass(): string { return FfExampleCollection::class; }

    protected function defineFields(): FieldCollection
    {
        return new FieldCollection([
            (new IdField('id', 'id'))->addFlags(new PrimaryKey(), new Required()),
            (new StringField('name', 'name'))->addFlags(new Required()),
        ]);
    }
}
```

Register it in `services.xml` with the tag `shopware.entity.definition`. Table name = `ENTITY_NAME` (snake_case),
the PK is always an `IdField` with a binary UUIDv7. Create the schema through a migration (`sw-database-migration`).

→ Core classes and architecture: [DEFINITION-CORE-CLASSES.md](DEFINITION-CORE-CLASSES.md)
→ Full example: [DEFINITION-EXAMPLE.md](DEFINITION-EXAMPLE.md) · PropertyGroup example: [DEFINITION-PROPERTY-GROUP-EXAMPLE.md](DEFINITION-PROPERTY-GROUP-EXAMPLE.md)
→ Fields: `sw-field-types` · Flags: `sw-field-flags` · Associations: `sw-associations-*` · Attribute variant: `sw-attribute-entities`
