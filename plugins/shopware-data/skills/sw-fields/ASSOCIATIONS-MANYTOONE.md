# Shopware 6 — ManyToOne-Association

Die Entity hält einen Fremdschlüssel auf das Ziel und die zugehörige Association.

```php
(new FkField('category_id', 'categoryId', CategoryDefinition::class))->addFlags(new Required()),
(new ManyToOneAssociationField('category', 'category_id', CategoryDefinition::class, 'id')),
```

Self-referencing (parent/child) bildet **Tree**-Strukturen (z.B. Kategorien): `parent_id` + `ParentAssociationField`/
`ChildrenAssociationField` + `TreeLevelField`/`TreePathField`. Lösch-Verhalten über Flags (`RestrictDelete`/`SetNullOnDelete`).

→ Association-Typen: [ASSOCIATIONS.md](ASSOCIATIONS.md) · Tree-Beispiel: [ASSOCIATIONS-MANYTOONE-TREE-EXAMPLE.md](ASSOCIATIONS-MANYTOONE-TREE-EXAMPLE.md)
