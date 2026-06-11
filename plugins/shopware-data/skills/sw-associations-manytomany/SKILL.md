---
name: sw-associations-manytomany
description: >
  ManyToMany-Associations in Shopware 6 DAL über eine Mapping-Entity (MappingEntityDefinition) inkl.
  ManyToManyAssociationField. Trigger: "ManyToMany", "n:m Beziehung", "Mapping-Entity", "MappingEntityDefinition",
  "ManyToManyAssociationField", "Zwischentabelle", "Verknüpfungstabelle". Shopware 6.7.
---

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

→ Association-Typen: [references/associations.md](references/associations.md) · Mapping-Beispiel: [references/mapping-example.md](references/mapping-example.md)
