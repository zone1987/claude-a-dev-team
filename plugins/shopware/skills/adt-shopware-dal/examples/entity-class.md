# Example: Entity Classes

## ProductEntity

Uses `EntityIdTrait` for `id` and `EntityCustomFieldsTrait` for custom fields. All properties are `protected` with getter/setter methods.

```php
#[Package('inventory')]
class ProductEntity extends Entity implements \Stringable
{
    use EntityCustomFieldsTrait;
    use EntityIdTrait;

    protected ?string $parentId = null;
    protected ?string $taxId = null;
    protected ?string $manufacturerId = null;
    protected ?bool $active = null;          // nullable for inheritance
    protected ?PriceCollection $price = null;
    protected string $productNumber;
    protected int $stock;
    protected bool $available;
    protected ?int $availableStock = null;

    // Associations typed with collection/entity classes
    protected ?TaxEntity $tax = null;
    protected ?ProductManufacturerEntity $manufacturer = null;
    protected ?ProductEntity $parent = null;
    protected ?ProductCollection $children = null;
    protected ?ProductMediaCollection $media = null;
    protected ?CategoryCollection $categories = null;
    protected ?ProductTranslationCollection $translations = null;

    // Nullable properties for inherited fields (null = inherit from parent)
    protected ?float $weight = null;
    protected ?float $width = null;
    protected ?float $height = null;
}
```

## CategoryEntity

Tree entity with path, level, breadcrumb, and parent/children associations.

```php
#[Package('discovery')]
class CategoryEntity extends Entity
{
    use EntityCustomFieldsTrait;
    use EntityIdTrait;

    protected ?string $parentId = null;
    protected ?string $path = null;        // materialized path: |uuid1|uuid2|
    protected int $level;                  // tree depth (1-based)
    protected int $childCount;
    protected bool $active;
    protected bool $displayNestedProducts;
    protected string $type;                // 'page', 'link', 'folder'

    // Tree associations
    protected ?CategoryEntity $parent = null;
    protected ?CategoryCollection $children = null;

    // Breadcrumb from translation
    protected ?array $breadcrumb = null;
}
```
