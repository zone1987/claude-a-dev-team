# Example: ManyToMany Mapping Definition

## ProductCategoryDefinition

```php
#[Package('inventory')]
class ProductCategoryDefinition extends MappingEntityDefinition
{
    final public const ENTITY_NAME = 'product_category';

    public function getEntityName(): string { return self::ENTITY_NAME; }
    public function isVersionAware(): bool { return true; }

    protected function defineFields(): FieldCollection
    {
        return new FieldCollection([
            // Composite primary key: both FKs + version references
            (new FkField('product_id', 'productId', ProductDefinition::class))
                ->addFlags(new PrimaryKey(), new Required()),
            (new ReferenceVersionField(ProductDefinition::class))
                ->addFlags(new PrimaryKey(), new Required()),

            (new FkField('category_id', 'categoryId', CategoryDefinition::class))
                ->addFlags(new PrimaryKey(), new Required()),
            (new ReferenceVersionField(CategoryDefinition::class))
                ->addFlags(new PrimaryKey(), new Required()),

            // ManyToOne back-references (not autoloaded)
            new ManyToOneAssociationField('product', 'product_id', ProductDefinition::class, 'id', false),
            new ManyToOneAssociationField('category', 'category_id', CategoryDefinition::class, 'id', false),
        ]);
    }
}
```

**Key points:**
- Extends `MappingEntityDefinition` (no entity class, no collection, no createdAt/updatedAt)
- Composite PK includes version references for both entities
- Version-aware when either referenced entity is version-aware
- ManyToOne back-references allow loading the full entity from either side
