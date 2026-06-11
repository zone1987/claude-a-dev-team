# Example: PropertyGroup + PropertyGroupOption

Demonstrates: parent/child definitions, getParentDefinitionClass, ReverseInherited, RestrictDelete, enum-like constants, getDefaults.

## PropertyGroupDefinition

```php
/**
 * @class PropertyGroupDefinition
 * @package Shopware\Core\Content\Property
 */
class PropertyGroupDefinition extends EntityDefinition
{
    /**
     * @var string
     */
    final public const DISPLAY_TYPE_TEXT = 'text';

    /**
     * @var string
     */
    final public const DISPLAY_TYPE_IMAGE = 'image';

    /**
     * @var string
     */
    final public const DISPLAY_TYPE_MEDIA = 'media';

    /**
     * @var string
     */
    final public const DISPLAY_TYPE_COLOR = 'color';

    /**
     * @var string
     */
    final public const SORTING_TYPE_ALPHANUMERIC = 'alphanumeric';

    /**
     * @var string
     */
    final public const SORTING_TYPE_POSITION = 'position';

    /**
     * @return array{displayType: string, sortingType: string, filterable: bool, visibleOnProductDetailPage: bool}
     */
    public function getDefaults(): array
    {
        return [
            'displayType' => self::DISPLAY_TYPE_TEXT,
            'sortingType' => self::SORTING_TYPE_ALPHANUMERIC,
            'filterable' => true,
            'visibleOnProductDetailPage' => true,
        ];
    }

    /**
     * @return FieldCollection
     */
    protected function defineFields(): FieldCollection
    {
        return new FieldCollection([
            (new IdField('id', 'id'))->addFlags(new ApiAware(), new PrimaryKey(), new Required()),
            (new TranslatedField('name'))
                ->addFlags(new ApiAware(), new SearchRanking(SearchRanking::HIGH_SEARCH_RANKING)),
            (new StringField('display_type', 'displayType'))->addFlags(new ApiAware(), new Required()),
            (new StringField('sorting_type', 'sortingType'))->addFlags(new ApiAware(), new Required()),
            (new BoolField('filterable', 'filterable'))->addFlags(new ApiAware()),
            (new OneToManyAssociationField('options', PropertyGroupOptionDefinition::class, 'property_group_id'))
                ->addFlags(new ApiAware(), new CascadeDelete(),
                    new SearchRanking(SearchRanking::ASSOCIATION_SEARCH_RANKING)),
            (new TranslationsAssociationField(PropertyGroupTranslationDefinition::class, 'property_group_id'))
                ->addFlags(new Required(), new CascadeDelete()),
        ]);
    }
}
```

## PropertyGroupOptionDefinition (Child)

```php
/**
 * @class PropertyGroupOptionDefinition
 * @package Shopware\Core\Content\Property\Aggregate\PropertyGroupOption
 */
class PropertyGroupOptionDefinition extends EntityDefinition
{
    /**
     * @return string|null
     */
    protected function getParentDefinitionClass(): ?string
    {
        return PropertyGroupDefinition::class;
    }

    /**
     * @return FieldCollection
     */
    protected function defineFields(): FieldCollection
    {
        return new FieldCollection([
            (new IdField('id', 'id'))->addFlags(new ApiAware(), new PrimaryKey(), new Required()),
            (new FkField('property_group_id', 'groupId', PropertyGroupDefinition::class))
                ->addFlags(new ApiAware(), new Required()),
            (new TranslatedField('name'))
                ->addFlags(new ApiAware(), new SearchRanking(SearchRanking::HIGH_SEARCH_RANKING)),
            (new StringField('color_hex_code', 'colorHexCode'))->addFlags(new ApiAware()),
            (new FkField('media_id', 'mediaId', MediaDefinition::class))->addFlags(new ApiAware()),

            // Runtime field (computed, not stored)
            (new BoolField('combinable', 'combinable'))->addFlags(new ApiAware(), new Runtime()),

            (new ManyToOneAssociationField('group', 'property_group_id', PropertyGroupDefinition::class))
                ->addFlags(new ApiAware()),

            // RestrictDelete: cannot delete option if used in product configurator
            (new OneToManyAssociationField('productConfiguratorSettings',
                ProductConfiguratorSettingDefinition::class, 'property_group_option_id'))
                ->addFlags(new RestrictDelete()),

            // ReverseInherited: tells DAL that product.properties is the inherited side
            (new ManyToManyAssociationField('productProperties', ProductDefinition::class,
                ProductPropertyDefinition::class, 'property_group_option_id', 'product_id'))
                ->addFlags(new CascadeDelete(), new ReverseInherited('properties')),
        ]);
    }
}
```
