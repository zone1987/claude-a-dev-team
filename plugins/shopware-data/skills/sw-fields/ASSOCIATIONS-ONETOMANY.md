# Shopware 6 — OneToMany association

The parent entity references multiple children; the foreign key sits in the **child** table.

```php
// in the parent definition
(new OneToManyAssociationField('lines', FfLineDefinition::class, 'example_id'))
    ->addFlags(new CascadeDelete()),
// in the child definition
(new FkField('example_id', 'exampleId', FfExampleDefinition::class))->addFlags(new Required()),
(new ManyToOneAssociationField('example', 'example_id', FfExampleDefinition::class, 'id')),
```

`CascadeDelete` removes the children together with the parent. Avoid `autoload(true)` (performance, ADR
"deprecate autoload true") — load associations explicitly via Criteria (`sw-criteria`).

→ All 7 association types and details: [ASSOCIATIONS.md](ASSOCIATIONS.md)
