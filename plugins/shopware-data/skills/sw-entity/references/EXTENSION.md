# Shopware 6 — entity extensions

An extension adds fields to an existing entity. **It is technical, not configurable by an admin**, and
unlike a custom field it can carry associations rather than just scalars.

## Contents

- [Extension or custom field](#extension-or-custom-field)
- [The extension class](#the-extension-class)
- [With a database table](#with-a-database-table)
- [The definition](#the-definition)
- [The migration and its foreign keys](#the-migration-and-its-foreign-keys)
- [Writing to the new field](#writing-to-the-new-field)
- [Without a database table](#without-a-database-table)
- [Bulk entity extensions](#bulk-entity-extensions)

## Extension or custom field

| | Custom field | Entity extension |
|---|---|---|
| Configured by | the admin, in the administration | code only |
| Types | mostly scalar — text, number and the like | anything, **including associations** |

Need an association between entities: extension. Scalars without an association work either way.

## The extension class

Extensions live under `<plugin root>/src/Extension/`, mirroring the core's own path — extending
`product` means `Extension/Content/Product/`. Extend
`Shopware\Core\Framework\DataAbstractionLayer\EntityExtension`, which requires
`getDefinitionClass`, and add fields by overriding `extendFields`.

```php
// <plugin root>/src/Extension/Content/Product/CustomExtension.php
public function extendFields(FieldCollection $collection): void
{
    $collection->add(
        // fields here
    );
}

public function getDefinitionClass(): string
{
    return ProductDefinition::class;
}
```

```php
// <plugin root>/src/Resources/config/services.php
use Symfony\Component\DependencyInjection\Loader\Configurator\ContainerConfigurator;

return static function (ContainerConfigurator $configurator): void {
    $services = $configurator->services();

    $services->set(CustomExtension::class)
        ->tag('shopware.entity.extension');
};
```

## With a database table

**You must not add a column to the `product` table.** The data goes into a table of its own, joined
by a OneToOne association:

```php
public function extendFields(FieldCollection $collection): void
{
    $collection->add(
        (new OneToOneAssociationField('exampleExtension', 'id', 'product_id', ExampleExtensionDefinition::class, true))
            ->addFlags(new CascadeDelete())
    );
}
```

`OneToOneAssociationField`'s parameters, in order:

| Parameter | Meaning |
|---|---|
| `propertyName` | the property on `ProductDefinition` holding the associated entity — camelCase, lower first |
| `storageName` | the column on this side, `id` here, referring to the product's `id` — always lowercase snake_case |
| `referenceField` | the column on the other side, `product_id`, defined in `ExampleExtensionDefinition` |
| `referenceClass` | the definition being associated |
| `autoload` | whether the association loads whenever the product loads — wanted here |

**`CascadeDelete` also governs cloning.** An association carrying it is included when a product is
cloned; `CascadeDelete(false)`, or dropping the flag, keeps the extension out of the clone.

## The definition

```php
// <plugin root>/src/Extension/Content/Product/ExampleExtensionDefinition.php
protected function defineFields(): FieldCollection
{
    return new FieldCollection([
        (new IdField('id', 'id'))->addFlags(new Required(), new PrimaryKey()),
        new FkField('product_id', 'productId', ProductDefinition::class),
        (new StringField('custom_string', 'customString')),
        // ReferenceVersionField only needed on versioned entities
        new ReferenceVersionField(ProductDefinition::class, 'product_version_id'),
        new OneToOneAssociationField('product', 'product_id', 'id', ProductDefinition::class, false),
    ]);
}
```

The table is `swag_example_extension`, the entity class `ExampleExtensionEntity` (from
`getEntityClass`). `product_id` is an `FkField` because that is what it is — a foreign key.

**The inverse association reverses the second and third parameters, and that order matters.** Its
`autoload` is `false`: the product is not loaded when the extension entity is read, while the
extension *is* loaded whenever the product is.

```php
$services->set(CustomExtension::class)
    ->tag('shopware.entity.extension');

$services->set(ExampleExtensionDefinition::class)
    ->tag('shopware.entity.definition', ['entity' => 'swag_example_extension']);
```

## The migration and its foreign keys

The table is created by a database migration. **The `AssociationFields` load the data, but foreign key
constraints are what keep it consistent** — they verify the key exists, and they delete the
`swag_example_extension` row when its product is deleted. Add them to the migration query.

## Writing to the new field

The association loads automatically; writing goes through the extended entity's repository:

```php
$this->productRepository->upsert([[
    'id' => $productId,
    'exampleExtension' => [
        'customString' => 'foo bar',
    ],
]], $context);
```

`exampleExtension` is the `propertyName` from the extension class, `customString` the property from
the definition.

## Without a database table

Where the data is derived rather than stored, add it on load. The entity's event class holds the
constants — `Shopware\Core\Content\Product\ProductEvents` for the product:

```php
// <plugin root>/src/Subscriber/ProductSubscriber.php
public static function getSubscribedEvents(): array
{
    return [ProductEvents::PRODUCT_LOADED_EVENT => 'onProductsLoaded'];
}

public function onProductsLoaded(EntityLoadedEvent $event): void
{
    /** @var ProductEntity $productEntity */
    foreach ($event->getEntities() as $productEntity) {
        $productEntity->addExtension('custom_string', new ArrayEntity(['foo' => 'bar']));
    }
}
```

**`addExtension`'s second argument has to be a struct**, not a string or any other scalar — hence
`ArrayEntity` here.

## Bulk entity extensions

**Available since 6.6.10.0.** Where many entities need extending, one `BulkEntityExtension` covers
them all. Each `yield` names the entity and the fields to add:

```php
public function collect(): \Generator
{
    yield ProductDefinition::ENTITY_NAME => [
        new FkField('main_category_id', 'mainCategoryId', CategoryDefinition::class),
    ];

    yield CategoryDefinition::ENTITY_NAME => [
        new FkField('product_id', 'productId', ProductDefinition::class),
        new ManyToOneAssociationField('product', 'product_id', ProductDefinition::class),
    ];
}
```

```php
$services->set(\Examples\MyBulkExtension::class)
    ->tag('shopware.bulk.entity.extension');
```

Note the different tag: `shopware.bulk.entity.extension`, not `shopware.entity.extension`.

## Source

[developer.shopware.com/docs/guides/plugins/plugins/framework/data-handling/add-complex-data-to-existing-entities.html](https://developer.shopware.com/docs/guides/plugins/plugins/framework/data-handling/add-complex-data-to-existing-entities.html),
Shopware 6.7, retrieved 2026-08-21.
