---
name: sw-associations-onetoone
description: >
  OneToOne-Associations in Shopware 6 DAL (genau ein zugeordnetes Objekt) inkl. OneToOneAssociationField und
  Fk-Platzierung. Trigger: "OneToOne", "1:1 Beziehung", "OneToOneAssociationField", "genau ein zugeordnet".
  Shopware 6.7.
---

# Shopware 6 — OneToOne-Association

Eine Entity ist genau einer anderen zugeordnet. Die FK kann auf einer der beiden Seiten liegen.

```php
// Seite mit FK
(new FkField('detail_id', 'detailId', FfDetailDefinition::class)),
(new OneToOneAssociationField('detail', 'detail_id', 'id', FfDetailDefinition::class, false)),
// Gegenseite (ohne eigene FK-Spalte)
(new OneToOneAssociationField('example', 'id', 'detail_id', FfExampleDefinition::class, false)),
```

Letzter Parameter `autoload` i.d.R. `false` lassen und gezielt laden. Für „gehört zu vielen" → `sw-associations-manytoone`.

→ Association-Typen & Details: [references/associations.md](references/associations.md)
