# Shopware 6 — Entity class

The entity is the typed data object matching the definition. It extends `Entity` and usually uses `EntityIdTrait`
(which supplies `id`). One `protected` property plus getter/setter per definition field; nullable for optional fields.

```php
class FfExampleEntity extends Entity
{
    use EntityIdTrait;
    protected string $name;
    protected ?string $description = null;
    public function getName(): string { return $this->name; }
    public function setName(string $name): void { $this->name = $name; }
}
```

`TranslatedField` values end up in the `translated` array or get mapped onto the properties (`sw-translations`).
Type association properties to the respective entity/collection. No business logic in the entity.

→ Full example: [CLASS-EXAMPLE.md](CLASS-EXAMPLE.md)
