# Shopware 6 — Entity extension

Adds fields and associations to a core entity (or a third-party entity) WITHOUT changing its definition.

```php
class ProductExtension extends EntityExtension
{
    public function getDefinitionClass(): string { return ProductDefinition::class; }

    public function extendFields(FieldCollection $collection): void
    {
        $collection->add(
            (new OneToManyAssociationField('ffNotes', FfNoteDefinition::class, 'product_id'))
                ->addFlags(new ApiAware(), new CascadeDelete())
        );
    }
}
```

Register it with the `shopware.entity.extension` tag. Columns of your own require a migration. Additional
simple fields are often easier through **custom fields** (`sw-custom-fields`) — use an extension for real associations and logic.

→ Scaffold: [examples/EntityExtension.php](examples/EntityExtension.php)
