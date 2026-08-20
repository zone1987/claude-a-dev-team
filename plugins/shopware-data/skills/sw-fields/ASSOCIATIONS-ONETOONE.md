# Shopware 6 — OneToOne association

One entity maps to exactly one other. The foreign key can sit on either side.

```php
// side holding the FK
(new FkField('detail_id', 'detailId', FfDetailDefinition::class)),
(new OneToOneAssociationField('detail', 'detail_id', 'id', FfDetailDefinition::class, false)),
// inverse side (no FK column of its own)
(new OneToOneAssociationField('example', 'id', 'detail_id', FfExampleDefinition::class, false)),
```

Leave the last parameter `autoload` at `false` as a rule and load explicitly. For "belongs to many" → `sw-associations-manytoone`.

→ Association types and details: [ASSOCIATIONS.md](ASSOCIATIONS.md)
