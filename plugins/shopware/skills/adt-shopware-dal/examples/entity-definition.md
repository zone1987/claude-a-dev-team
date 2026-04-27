# Example: ProductDefinition (Complex Entity)

Demonstrates: inheritance, versioning, all association types, translated fields, ManyToManyIdFields, feature flags, defaults, multiple FK types.

```php
#[Package('inventory')]
class ProductDefinition extends EntityDefinition
{
    final public const ENTITY_NAME = 'product';

    public function getEntityName(): string { return self::ENTITY_NAME; }
    public function isInheritanceAware(): bool { return true; }
    public function getCollectionClass(): string { return ProductCollection::class; }
    public function getEntityClass(): string { return ProductEntity::class; }
    public function getHydratorClass(): string { return ProductHydrator::class; }
    public function since(): ?string { return '6.0.0.0'; }

    public function getDefaults(): array
    {
        return [
            'isCloseout' => false,
            'minPurchase' => 1,
            'purchaseSteps' => 1,
            'shippingFree' => false,
            'restockTime' => null,
            'active' => true,
            'markAsTopseller' => false,
            'type' => self::TYPE_PHYSICAL,
        ];
    }

    protected function defineFields(): FieldCollection
    {
        return new FieldCollection([
            // Primary key + version
            (new IdField('id', 'id'))->addFlags(new ApiAware(), new PrimaryKey(), new Required()),
            (new VersionField())->addFlags(new ApiAware()),

            // Parent-child inheritance
            (new ParentFkField(self::class))->addFlags(new ApiAware()),
            (new ReferenceVersionField(self::class, 'parent_version_id'))->addFlags(new ApiAware(), new Required()),

            // Foreign keys with Inherited flag
            (new FkField('product_manufacturer_id', 'manufacturerId', ProductManufacturerDefinition::class))
                ->addFlags(new ApiAware(), new Inherited()),
            (new FkField('tax_id', 'taxId', TaxDefinition::class))
                ->addFlags(new ApiAware(), new Inherited(), new Required()),
            // NoConstraint for circular reference (product -> product_media -> product)
            (new FkField('product_media_id', 'coverId', ProductMediaDefinition::class))
                ->addFlags(new ApiAware(), new Inherited(), new NoConstraint()),

            // Price field with ApiCriteriaAware (hidden from API but usable in criteria)
            (new PriceField('price', 'price'))->addFlags(new Inherited(), new Required(), new ApiCriteriaAware()),

            // Scalar fields
            (new BoolField('active', 'active'))->addFlags(new ApiAware(), new Inherited()),
            (new IntField('stock', 'stock'))->addFlags(new ApiAware(), new Required()),
            (new FloatField('weight', 'weight'))->addFlags(new ApiAware(), new Inherited()),

            // WriteProtected computed fields
            (new BoolField('available', 'available'))->addFlags(new ApiAware(), new WriteProtected()),
            (new FloatField('rating_average', 'ratingAverage'))
                ->addFlags(new ApiAware(), new WriteProtected(), new Inherited()),

            // Runtime field with dependencies
            (new ListField('variation', 'variation', StringField::class))
                ->addFlags(new Runtime(['options.name', 'options.group.name'])),

            // ManyToManyIdField (denormalized, write-protected, auto-indexed)
            (new ManyToManyIdField('property_ids', 'propertyIds', 'properties'))
                ->addFlags(new ApiAware(), new Inherited()),

            // Translated fields with SearchRanking
            (new TranslatedField('name', true))
                ->addFlags(new ApiAware(), new Inherited(), new SearchRanking(SearchRanking::HIGH_SEARCH_RANKING)),
            (new TranslatedField('description'))->addFlags(new ApiAware(), new Inherited()),
            (new TranslatedField('customFields'))->addFlags(new ApiAware(), new Inherited()),

            // Associations
            (new ParentAssociationField(self::class, 'id'))->addFlags(new ApiAware()),
            (new ChildrenAssociationField(self::class))->addFlags(new ApiAware()),
            (new ManyToOneAssociationField('manufacturer', 'product_manufacturer_id', ProductManufacturerDefinition::class))
                ->addFlags(new ApiAware(), new Inherited()),
            (new OneToManyAssociationField('prices', ProductPriceDefinition::class, 'product_id'))
                ->addFlags(new CascadeDelete(), new Inherited()),
            (new ManyToManyAssociationField('categories', CategoryDefinition::class,
                ProductCategoryDefinition::class, 'product_id', 'category_id'))
                ->addFlags(new ApiAware(), new CascadeDelete(), new Inherited()),
            (new TranslationsAssociationField(ProductTranslationDefinition::class, 'product_id'))
                ->addFlags(new ApiAware(), new Inherited(), new Required()),
        ]);
    }
}
```
