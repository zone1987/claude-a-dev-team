# Shopware 6 — EntityCollection

Die Collection hält mehrere Entities typisiert. Sie erweitert `EntityCollection` und gibt in `getExpectedClass()`
die Entity-Klasse zurück. Eigene Convenience-Helfer (filter/map/group) sind üblich.

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

Suchergebnisse (`$result->getEntities()`) liefern diese Collection. PHPDoc-Generic `@extends EntityCollection<...>`
für PHPStan/IDE setzen.

→ Vollständiges Beispiel: [COLLECTION-EXAMPLE.md](COLLECTION-EXAMPLE.md)
