# Example: Entity Collections

## Minimal Collection (ProductCollection)

```php
/**
 * @extends EntityCollection<ProductEntity>
 */
#[Package('inventory')]
class ProductCollection extends EntityCollection
{
    public function getApiAlias(): string
    {
        return 'product_collection';
    }

    protected function getExpectedClass(): string
    {
        return ProductEntity::class;
    }
}
```

## Collection with Helpers (CategoryCollection)

```php
/**
 * @extends EntityCollection<CategoryEntity>
 */
#[Package('discovery')]
class CategoryCollection extends EntityCollection
{
    public function getParentIds(): array
    {
        return $this->fmap(fn (CategoryEntity $category) => $category->getParentId());
    }

    public function filterByParentId(string $id): self
    {
        return $this->filter(fn (CategoryEntity $category) => $category->getParentId() === $id);
    }

    public function sortByPosition(): self
    {
        $this->elements = AfterSort::sort($this->elements, 'afterCategoryId');
        return $this;
    }

    public function sortByName(): self
    {
        $this->sort(fn (CategoryEntity $a, CategoryEntity $b) =>
            strnatcasecmp((string) $a->getTranslated()['name'], (string) $b->getTranslated()['name']));
        return $this;
    }

    public function getApiAlias(): string { return 'category_collection'; }
    protected function getExpectedClass(): string { return CategoryEntity::class; }
}
```

## Collection with Filtering (MediaCollection)

```php
/**
 * @extends EntityCollection<MediaEntity>
 */
#[Package('discovery')]
class MediaCollection extends EntityCollection
{
    public function getUserIds(): array
    {
        return $this->fmap(fn (MediaEntity $media) => $media->getUserId());
    }

    public function filterByUserId(string $id): self
    {
        return $this->filter(fn (MediaEntity $media) => $media->getUserId() === $id);
    }

    public function getApiAlias(): string { return 'media_collection'; }
    protected function getExpectedClass(): string { return MediaEntity::class; }
}
```
