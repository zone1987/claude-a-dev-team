# Shopware 6 — ManyToOne association

The entity holds a foreign key to the target plus the matching association.

```php
(new FkField('category_id', 'categoryId', CategoryDefinition::class))->addFlags(new Required()),
(new ManyToOneAssociationField('category', 'category_id', CategoryDefinition::class, 'id')),
```

Self-referencing (parent/child) forms **tree** structures (categories, for example): `parent_id` + `ParentAssociationField`/
`ChildrenAssociationField` + `TreeLevelField`/`TreePathField`. Control delete behaviour through flags (`RestrictDelete`/`SetNullOnDelete`).

→ Association types: [ASSOCIATIONS.md](ASSOCIATIONS.md) · Tree example: [ASSOCIATIONS-MANYTOONE-TREE-EXAMPLE.md](ASSOCIATIONS-MANYTOONE-TREE-EXAMPLE.md)
