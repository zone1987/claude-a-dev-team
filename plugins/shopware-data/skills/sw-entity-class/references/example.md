# Example: Entity Classes

## ProductEntity

Uses `EntityIdTrait` for `id` and `EntityCustomFieldsTrait` for custom fields. All properties are `protected` with getter/setter methods.

```php
/**
 * @class ProductEntity
 * @package Shopware\Core\Content\Product
 */
#[Package('inventory')]
class ProductEntity extends Entity implements \Stringable
{
    use EntityCustomFieldsTrait;
    use EntityIdTrait;

    /**
     * @var string|null
     */
    protected ?string $parentId = null;

    /**
     * @var string|null
     */
    protected ?string $taxId = null;

    /**
     * @var string|null
     */
    protected ?string $manufacturerId = null;

    /**
     * @var bool|null
     */
    protected ?bool $active = null;

    /**
     * @var PriceCollection|null
     */
    protected ?PriceCollection $price = null;

    /**
     * @var string
     */
    protected string $productNumber;

    /**
     * @var int
     */
    protected int $stock;

    /**
     * @var bool
     */
    protected bool $available;

    /**
     * @var int|null
     */
    protected ?int $availableStock = null;

    /**
     * @var TaxEntity|null
     */
    protected ?TaxEntity $tax = null;

    /**
     * @var ProductManufacturerEntity|null
     */
    protected ?ProductManufacturerEntity $manufacturer = null;

    /**
     * @var ProductEntity|null
     */
    protected ?ProductEntity $parent = null;

    /**
     * @var ProductCollection|null
     */
    protected ?ProductCollection $children = null;

    /**
     * @var ProductMediaCollection|null
     */
    protected ?ProductMediaCollection $media = null;

    /**
     * @var CategoryCollection|null
     */
    protected ?CategoryCollection $categories = null;

    /**
     * @var ProductTranslationCollection|null
     */
    protected ?ProductTranslationCollection $translations = null;

    /**
     * @var float|null
     */
    protected ?float $weight = null;

    /**
     * @var float|null
     */
    protected ?float $width = null;

    /**
     * @var float|null
     */
    protected ?float $height = null;
}
```

## CategoryEntity

Tree entity with path, level, breadcrumb, and parent/children associations.

```php
/**
 * @class CategoryEntity
 * @package Shopware\Core\Content\Category
 */
#[Package('discovery')]
class CategoryEntity extends Entity
{
    use EntityCustomFieldsTrait;
    use EntityIdTrait;

    /**
     * @var string|null
     */
    protected ?string $parentId = null;

    /**
     * @var string|null
     */
    protected ?string $path = null;

    /**
     * @var int
     */
    protected int $level;

    /**
     * @var int
     */
    protected int $childCount;

    /**
     * @var bool
     */
    protected bool $active;

    /**
     * @var bool
     */
    protected bool $displayNestedProducts;

    /**
     * @var string
     */
    protected string $type;

    /**
     * @var CategoryEntity|null
     */
    protected ?CategoryEntity $parent = null;

    /**
     * @var CategoryCollection|null
     */
    protected ?CategoryCollection $children = null;

    /**
     * @var array<mixed>|null
     */
    protected ?array $breadcrumb = null;
}
```
