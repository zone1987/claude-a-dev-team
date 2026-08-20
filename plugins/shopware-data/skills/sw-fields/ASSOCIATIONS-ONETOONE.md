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

→ Association-Typen & Details: [ASSOCIATIONS.md](ASSOCIATIONS.md)
