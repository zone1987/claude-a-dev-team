# Example: Translation Definitions

## ProductTranslationDefinition

```php
#[Package('inventory')]
class ProductTranslationDefinition extends EntityTranslationDefinition
{
    final public const ENTITY_NAME = 'product_translation';

    public function getEntityName(): string { return self::ENTITY_NAME; }
    public function getCollectionClass(): string { return ProductTranslationCollection::class; }
    public function getEntityClass(): string { return ProductTranslationEntity::class; }

    // MUST override this
    protected function getParentDefinitionClass(): string
    {
        return ProductDefinition::class;
    }

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
class CategoryTranslationDefinition extends EntityTranslationDefinition
{
    protected function getParentDefinitionClass(): string
    {
        return CategoryDefinition::class;
    }

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
