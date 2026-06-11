---
name: sw-entity-definition
description: >
  Eine Shopware-6 DAL-EntityDefinition bauen: defineFields(), getEntityName(), getEntityClass(),
  getCollectionClass(), Registrierung via shopware.entity.definition. Der Einstieg für jede eigene Tabelle/Entity.
  Trigger: "EntityDefinition", "neue Entity", "eigene Tabelle/Entität", "defineFields", "Entity registrieren",
  "DAL entity", "create entity definition". Shopware 6.7. Scaffolder: /sw-entity.
---

# Shopware 6 — EntityDefinition

Die `EntityDefinition` beschreibt Schema (Felder, Associations, Flags) einer DAL-Entity. Drei Bausteine gehören
immer zusammen: **Definition** (Schema), **Entity** (`sw-entity-class`), **Collection** (`sw-entity-collection`).

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

Registrierung in `services.xml` mit Tag `shopware.entity.definition`. Tabellenname = `ENTITY_NAME` (snake_case),
PK ist immer ein `IdField` mit BinaryUUIDv7. Schema per Migration anlegen (`sw-database-migration`).

→ Core-Klassen & Architektur: [references/core-classes.md](references/core-classes.md)
→ Vollständiges Beispiel: [references/example.md](references/example.md) · PropertyGroup-Beispiel: [references/property-group-example.md](references/property-group-example.md)
→ Felder: `sw-field-types` · Flags: `sw-field-flags` · Associations: `sw-associations-*` · Attribut-Variante: `sw-attribute-entities`
