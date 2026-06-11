# Example: Translation Definitions

## ProductTranslationDefinition

```php
/**
 * @class ProductTranslationDefinition
 * @package Shopware\Core\Content\Product\Aggregate\ProductTranslation
 */
#[Package('inventory')]
class ProductTranslationDefinition extends EntityTranslationDefinition
{
    /**
     * @var string
     */
    final public const ENTITY_NAME = 'product_translation';

    /**
     * @return string
     */
    public function getEntityName(): string { return self::ENTITY_NAME; }

    /**
     * @return string
     */
    public function getCollectionClass(): string { return ProductTranslationCollection::class; }

    /**
     * @return string
     */
    public function getEntityClass(): string { return ProductTranslationEntity::class; }

    /**
     * @return string
     */
    protected function getParentDefinitionClass(): string
    {
        return ProductDefinition::class;
    }

    /**
     * @return FieldCollection
     */
    protected function defineFields(): FieldCollection
    {
        return new FieldCollection([
            (new StringField('meta_description', 'metaDescription'))->addFlags(new ApiAware()),
            (new StringField('name', 'name'))->addFlags(new ApiAware(), new Required()),
            (new LongTextField('keywords', 'keywords'))->addFlags(new ApiAware()),
            (new LongTextField('description', 'description'))->addFlags(new ApiAware(), new AllowHtml()),
            (new StringField('meta_title', 'metaTitle'))->addFlags(new ApiAware()),
            (new StringField('pack_unit', 'packUnit'))->addFlags(new ApiAware()),
            new ListField('custom_search_keywords', 'customSearchKeywords'),
            (new JsonField('slot_config', 'slotConfig'))->addFlags(new ApiAware()),
            (new CustomFields())->addFlags(new ApiAware()),
        ]);
    }
}
```

## CategoryTranslationDefinition

```php
/**
 * @class CategoryTranslationDefinition
 * @package Shopware\Core\Content\Category\Aggregate\CategoryTranslation
 */
class CategoryTranslationDefinition extends EntityTranslationDefinition
{
    /**
     * @return string
     */
    protected function getParentDefinitionClass(): string
    {
        return CategoryDefinition::class;
    }

    /**
     * @return FieldCollection
     */
    protected function defineFields(): FieldCollection
    {
        return new FieldCollection([
            (new StringField('name', 'name'))->addFlags(new ApiAware(), new Required()),
            (new BreadcrumbField())->addFlags(new ApiAware(), new WriteProtected()),
            new JsonField('slot_config', 'slotConfig'),
            (new StringField('link_type', 'linkType'))->addFlags(new ApiAware()),
            (new IdField('internal_link', 'internalLink'))->addFlags(new ApiAware()),
            (new LongTextField('description', 'description'))->addFlags(new ApiAware(), new AllowHtml()),
            (new CustomFields())->addFlags(new ApiAware()),
        ]);
    }
}
```

**Auto-generated base fields** (by EntityTranslationDefinition):
- `FkField('{entity}_id')` with PrimaryKey, Required
- `FkField('language_id')` with PrimaryKey, Required
- `ManyToOneAssociationField` to parent entity
- `ManyToOneAssociationField` to language
- `ReferenceVersionField` if parent is version-aware
