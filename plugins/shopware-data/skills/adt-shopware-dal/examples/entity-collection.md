# Example: Entity Collections

## Minimal Collection (ProductCollection)

```php
/**
 * @class ProductCollection
 * @package Shopware\Core\Content\Product
 * @extends EntityCollection<ProductEntity>
 */
#[Package('inventory')]
class ProductCollection extends EntityCollection
{
    /**
     * @return string
     */
    public function getApiAlias(): string
    {
        return 'product_collection';
    }

    /**
     * @return string
     */
    protected function getExpectedClass(): string
    {
        return ProductEntity::class;
    }
}
```

## Collection with Helpers (CategoryCollection)

```php
/**
 * @class CategoryCollection
 * @package Shopware\Core\Content\Category
 * @extends EntityCollection<CategoryEntity>
 */
#[Package('discovery')]
class CategoryCollection extends EntityCollection
{
    /**
     * @return array<string>
     */
    public function getParentIds(): array
    {
        return $this->fmap(fn (CategoryEntity $category) => $category->getParentId());
    }

    /**
     * @param string $id
     * @return self
     */
    public function filterByParentId(string $id): self
    {
        return $this->filter(fn (CategoryEntity $category) => $category->getParentId() === $id);
    }

    /**
     * @return self
     */
    public function sortByPosition(): self
    {
        $this->elements = AfterSort::sort($this->elements, 'afterCategoryId');
        return $this;
    }

    /**
     * @return self
     */
    public function sortByName(): self
    {
        $this->sort(fn (CategoryEntity $a, CategoryEntity $b) =>
            strnatcasecmp((string) $a->getTranslated()['name'], (string) $b->getTranslated()['name']));
        return $this;
    }

    /**
     * @return string
     */
    public function getApiAlias(): string { return 'category_collection'; }

    /**
     * @return string
     */
    protected function getExpectedClass(): string { return CategoryEntity::class; }
}
```

## Collection with Filtering (MediaCollection)

```php
/**
 * @class MediaCollection
 * @package Shopware\Core\Content\Media
 * @extends EntityCollection<MediaEntity>
 */
#[Package('discovery')]
class MediaCollection extends EntityCollection
{
    /**
     * @return array<array-key, string>
     */
    public function getUserIds(): array
    {
        return $this->fmap(fn (MediaEntity $media) => $media->getUserId());
    }

    /**
     * @param string $id
     * @return self
     */
    public function filterByUserId(string $id): self
    {
        return $this->filter(fn (MediaEntity $media) => $media->getUserId() === $id);
    }

    /**
     * @return string
     */
    public function getApiAlias(): string { return 'media_collection'; }

    /**
     * @return string
     */
    protected function getExpectedClass(): string { return MediaEntity::class; }
}
```
