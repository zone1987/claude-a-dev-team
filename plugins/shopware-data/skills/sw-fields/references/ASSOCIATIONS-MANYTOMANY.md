# Shopware 6 — ManyToMany association

Requires a **mapping entity** (join table with two FkFields) that extends `MappingEntityDefinition`.

```php
// in both main definitions
(new ManyToManyAssociationField('tags', TagDefinition::class,
    FfExampleTagDefinition::class, 'example_id', 'tag_id')),

// mapping definition (MappingEntityDefinition)
(new FkField('example_id', 'exampleId', FfExampleDefinition::class))->addFlags(new PrimaryKey(), new Required()),
(new FkField('tag_id', 'tagId', TagDefinition::class))->addFlags(new PrimaryKey(), new Required()),
```

The mapping entity has a composite PK built from both FkFields and no id of its own. Write through a nested
payload (`['tags' => [['id' => $tagId]]]`).

→ Association types: [ASSOCIATIONS.md](ASSOCIATIONS.md) · Mapping example: [ASSOCIATIONS-MANYTOMANY-MAPPING-EXAMPLE.md](ASSOCIATIONS-MANYTOMANY-MAPPING-EXAMPLE.md)
