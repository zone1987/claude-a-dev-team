---
name: sw-associations-onetomany
description: >
  OneToMany-Associations in Shopware 6 DAL (Eltern hat viele Kinder), inkl. OneToManyAssociationField,
  ReferenceField, CascadeDelete, autoload. Trigger: "OneToMany", "1:n Beziehung", "hat viele", "child entities",
  "OneToManyAssociationField", "Kinder-Entities". Shopware 6.7.
---

# Shopware 6 — OneToMany-Association

Eltern-Entity referenziert mehrere Kinder; die FK liegt in der **Kind**-Tabelle.

```php
// in der Eltern-Definition
(new OneToManyAssociationField('lines', FfLineDefinition::class, 'example_id'))
    ->addFlags(new CascadeDelete()),
// in der Kind-Definition
(new FkField('example_id', 'exampleId', FfExampleDefinition::class))->addFlags(new Required()),
(new ManyToOneAssociationField('example', 'example_id', FfExampleDefinition::class, 'id')),
```

`CascadeDelete` löscht Kinder mit dem Elternteil. `autoload(true)` vermeiden (Performance, ADR
„deprecate autoload true") — Associations gezielt per Criteria laden (`sw-criteria`).

→ Alle 7 Association-Typen & Details: [references/associations.md](references/associations.md)
