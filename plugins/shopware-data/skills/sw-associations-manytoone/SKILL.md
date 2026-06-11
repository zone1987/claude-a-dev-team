---
name: sw-associations-manytoone
description: >
  ManyToOne-Associations in Shopware 6 DAL (viele Kinder zeigen auf ein Eltern-Objekt) inkl. FkField +
  ManyToOneAssociationField, sowie Tree-/Parent-Child-Strukturen. Trigger: "ManyToOne", "n:1 Beziehung",
  "gehört zu", "FkField", "ManyToOneAssociationField", "parent reference", "Baumstruktur entity". Shopware 6.7.
---

# Shopware 6 — ManyToOne-Association

Die Entity hält einen Fremdschlüssel auf das Ziel und die zugehörige Association.

```php
(new FkField('category_id', 'categoryId', CategoryDefinition::class))->addFlags(new Required()),
(new ManyToOneAssociationField('category', 'category_id', CategoryDefinition::class, 'id')),
```

Self-referencing (parent/child) bildet **Tree**-Strukturen (z.B. Kategorien): `parent_id` + `ParentAssociationField`/
`ChildrenAssociationField` + `TreeLevelField`/`TreePathField`. Lösch-Verhalten über Flags (`RestrictDelete`/`SetNullOnDelete`).

→ Association-Typen: [references/associations.md](references/associations.md) · Tree-Beispiel: [references/tree-example.md](references/tree-example.md)
