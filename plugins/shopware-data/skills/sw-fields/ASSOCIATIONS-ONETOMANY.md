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

→ Alle 7 Association-Typen & Details: [ASSOCIATIONS.md](ASSOCIATIONS.md)
