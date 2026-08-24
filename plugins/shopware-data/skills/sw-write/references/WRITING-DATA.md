# Shopware 6 — writing data through the DAL

Every write goes through the repository generated per entity. **The service name is
`entity_name.repository`** — `product.repository`, `tax.repository`, `order.repository`.

## Contents

- [Injecting a repository](#injecting-a-repository)
- [create](#create)
- [Creating with a known id](#creating-with-a-known-id)
- [update, upsert and delete](#update-upsert-and-delete)
- [Assigning associated data](#assigning-associated-data)

## Injecting a repository

```php
// <plugin root>/src/Resources/config/services.php
$services->set(WritingData::class)
    ->args([
        service('product.repository'),
        service('tax.repository'),
    ]);
```

Switching entity means switching that reference — nothing else changes.

## create

```php
public function writeData(Context $context): void
{
    $this->productRepository->create([
        [
            'name' => 'Example product',
            'productNumber' => 'SW123',
            'stock' => 10,
            'taxId' => $this->getTaxId($context),
            'price' => [['currencyId' => Defaults::CURRENCY, 'gross' => 50, 'net' => 25, 'linked' => false]],
        ],
    ], $context);
}

private function getTaxId(Context $context): string
{
    $criteria = new Criteria();
    $criteria->addFilter(new EqualsFilter('taxRate', 19.00));

    return $this->taxRepository->searchIds($criteria, $context)->firstId();
}
```

**It is an array of arrays** — one write call can create several entities. The `Context` normally
travels down the stack from a controller or an event.

The imports needed:

```php
use Shopware\Core\Defaults;
use Shopware\Core\Framework\Context;
use Shopware\Core\Framework\DataAbstractionLayer\Search\Criteria;
use Shopware\Core\Framework\DataAbstractionLayer\Search\Filter\EqualsFilter;
```

`searchIds` rather than `search` is deliberate here: only the id is needed, so there is no reason to
hydrate the full tax entity. `firstId()` takes the first of them.

**On `price`:** it is a `JsonField`, so it is stored as JSON, and a product can hold several prices —
hence an array of arrays again. The structure is defined by `getConstraints` on
`PriceFieldSerializer`: a currency id, a gross and a net value, and `linked`. **`linked: true` means
a change to the gross price also changes the net price**, derived through the product's tax.

The full field list for a product lives in its definition.

## Creating with a known id

Shopware uses UUIDs, which has a practical consequence: **you can decide the id yourself** and keep
working with it, instead of reading the entity back to find out what it got.

```php
$productId = Uuid::randomHex();

$this->productRepository->create([
    [
        'id' => $productId,
        'name' => 'Example product',
        'productNumber' => 'SW127',
        'stock' => 10,
        'tax' => $this->getTaxId($context),
        'price' => [['currencyId' => Defaults::CURRENCY, 'gross' => 50, 'net' => 25, 'linked' => false]],
        'categories' => [
            ['id' => Uuid::randomHex(), 'name' => 'Example category'],
        ],
    ],
], $context);
```

The class is `Shopware\Core\Framework\Uuid\Uuid`.

## update, upsert and delete

**`update` always needs the id**, so it is usually preceded by a lookup:

```php
$criteria = new Criteria();
$criteria->addFilter(new EqualsFilter('name', 'Example product'));
$productId = $this->productRepository->searchIds($criteria, $context)->firstId();

$this->productRepository->update([
    ['id' => $productId, 'name' => 'New name'],
], $context);
```

Only the fields to change are passed.

**`upsert`** creates or updates as needed. **Always give it an id** — without one the data is always
created and never updated.

**`delete`** takes the ids only:

```php
$this->productRepository->delete([
    ['id' => $productId],
], $context);
```

All three take an array of arrays, so all three work in batch.

## Assigning associated data

**OneToOne and ManyToOne** — fill the id field of the association:

```php
'taxId' => $this->getTaxId($context),
```

**OneToMany and ManyToMany** — pass the associated entities as an array. Passing only an `id`
associates an existing record:

```php
$this->productRepository->update([
    [
        'id' => $productId,
        'categories' => [
            ['id' => $categoryId],
        ],
    ],
], $context);
```

The lookup for the id above uses `$this->categoryRepository`, and `Context::createDefaultContext()`
serves where no context arrives from the stack.

### A mapping entity cannot be updated

Every ManyToMany association has a mapping entity, and **updating it fails**:

```php
// product_category.repository — this does NOT work
$this->productCategoryRepository->update([
    ['productId' => 'myOldProductId', 'categoryId' => 'myNewCategoryId'],
], $context);
```

The reason is structural: an update needs a primary key plus the data to change, but on a mapping
entity **everything is a primary key**, and primary keys cannot be updated. The way out is replacing
the association — see `REPLACING-ASSOCIATED-DATA.md`.

### Creating an associated entity in the same call

Instead of assigning an existing record by id, fill the association field with the new entity's data.
Everything the associated entity requires has to be there — `name` and `taxRate` for a tax:

```php
$this->productRepository->create([
    [
        'name' => 'Example product',
        'productNumber' => 'SW123',
        'stock' => 10,
        'tax' => ['name' => 'test', 'taxRate' => 15],
        'price' => [['currencyId' => Defaults::CURRENCY, 'gross' => 50, 'net' => 25, 'linked' => false]],
    ],
], $context);
```

The tax is created together with the product and assigned automatically. **ToMany associations work
almost the same** — pass the fields alongside an id:

```php
'categories' => [
    ['id' => 'YourCategoryId', 'name' => 'Example category'],
],
```

## Related

For reading, call the Skill tool with `sw-query`. For adding an association to an entity of your own,
see `ASSOCIATIONS.md` in `sw-fields`.

## Source

[developer.shopware.com/docs/guides/plugins/plugins/framework/data-handling/writing-data.html](https://developer.shopware.com/docs/guides/plugins/plugins/framework/data-handling/writing-data.html),
Shopware 6.7, retrieved 2026-08-21.
