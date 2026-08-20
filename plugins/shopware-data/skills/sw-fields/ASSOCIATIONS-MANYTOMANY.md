# Shopware 6 — ManyToMany-Association

Benötigt eine **Mapping-Entity** (Zwischentabelle mit zwei FkFields), die `MappingEntityDefinition` erweitert.

```php
// in beiden Haupt-Definitionen
(new ManyToManyAssociationField('tags', TagDefinition::class,
    FfExampleTagDefinition::class, 'example_id', 'tag_id')),

// Mapping-Definition (MappingEntityDefinition)
(new FkField('example_id', 'exampleId', FfExampleDefinition::class))->addFlags(new PrimaryKey(), new Required()),
(new FkField('tag_id', 'tagId', TagDefinition::class))->addFlags(new PrimaryKey(), new Required()),
```

Die Mapping-Entity hat einen kombinierten PK aus beiden FkFields, keine eigene Id. Schreiben über verschachteltes
Payload (`['tags' => [['id' => $tagId]]]`).

→ Association-Typen: [ASSOCIATIONS.md](ASSOCIATIONS.md) · Mapping-Beispiel: [ASSOCIATIONS-MANYTOMANY-MAPPING-EXAMPLE.md](ASSOCIATIONS-MANYTOMANY-MAPPING-EXAMPLE.md)
