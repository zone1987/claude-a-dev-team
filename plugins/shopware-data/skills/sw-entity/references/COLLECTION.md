# Shopware 6 — EntityCollection

The collection holds multiple entities in a typed way. It extends `EntityCollection` and returns the entity class
from `getExpectedClass()`. Convenience helpers of your own (filter/map/group) are common.

```php
/** @extends EntityCollection<FfExampleEntity> */
class FfExampleCollection extends EntityCollection
{
    protected function getExpectedClass(): string { return FfExampleEntity::class; }

    public function filterByActive(): self
    {
        return $this->filter(fn (FfExampleEntity $e) => $e->isActive());
    }
}
```

Search results (`$result->getEntities()`) return this collection. Add the PHPDoc generic `@extends EntityCollection<...>`
for PHPStan and your IDE.

→ Full example: [COLLECTION-EXAMPLE.md](COLLECTION-EXAMPLE.md)
