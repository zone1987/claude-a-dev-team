# Shopware 6 — replacing and removing associated data

**A write never deletes.** That single fact is why replacing an association is not one call but two.

## Contents

- [Why replacing needs a delete first](#why-replacing-needs-a-delete-first)
- [Replacing a ToMany association](#replacing-a-tomany-association)
- [Replacing a ToOne association](#replacing-a-toone-association)
- [Removing a ToOne association](#removing-a-toone-association)
- [Removing a ManyToMany association](#removing-a-manytomany-association)
- [OneToMany: the hidden ManyToMany](#onetomany-the-hidden-manytomany)

## Why replacing needs a delete first

Assigning a different category to a product by passing only the new one **does not work**:

```php
// wrong — the product ends up with BOTH categories
$this->productRepository->update([
    [
        'id' => 'myProductId',
        'categories' => [
            ['id' => 'newCategoryId'],
        ],
    ],
], $context);
```

A write operation adds; it does not remove what is missing from the payload.

## Replacing a ToMany association

Delete the association through its **mapping repository**, then assign the new one. The mapping
entity's name comes from `getEntityName` in its definition — `product_category` here:

```php
// <plugin root>/src/Resources/config/services.php
$services->set(ReplacingData::class)
    ->args([
        service('product.repository'),
        service('product_category.repository'),
    ]);
```

```php
public function replaceData(Context $context): void
{
    $productId = 'myProductId';

    $this->productCategoryRepository->delete([
        ['productId' => $productId, 'categoryId' => 'oldCategoryId'],
    ], $context);

    $this->productRepository->update([
        [
            'id' => $productId,
            'categories' => [
                ['id' => 'newCategoryId'],
            ],
        ],
    ], $context);
}
```

This is the same for **ManyToMany and OneToMany** associations.

## Replacing a ToOne association

OneToOne and ManyToOne behave as expected — a single `update` with the new id, e.g. `'taxId' =>
$newTaxId`.

## Removing a ToOne association

Set the id field to `null`:

```php
public function removeAssocData(Context $context): void
{
    $this->productRepository->update([
        ['id' => 'myProductId', 'manufacturerId' => null],
    ], $context);
}
```

**Only possible where the association is not required** — a product's `taxId` cannot be removed,
because a product must always have a tax.

Where the product inherits from a parent, unsetting it here does **not** unset it on the parent.

## Removing a ManyToMany association

`delete` always needs the entity's primary keys. A mapping entity has **two** —
`ProductCategoryDefinition` owns `productId` and `categoryId`, and both are required to delete
precisely that association:

```php
$this->productCategoryRepository->delete([
    ['productId' => 'myProductId', 'categoryId' => 'myCategoryId'],
], $context);
```

## OneToMany: the hidden ManyToMany

A OneToMany association is usually just the other side of a ManyToOne, so removing it is the
`manufacturerId => null` case above, done through the `ProductDefinition` repository rather than the
`ProductManufacturerDefinition` one.

**But some OneToMany associations are ManyToMany associations in disguise**, used that way because
the mapping table needs extra data. `media` on the product is the example: a product can have several
media and a media can belong to several products, yet the field is a `OneToMany`.

Such an association is deleted like a ManyToMany — through the mapping repository — **but the mapping
definition has its own `id`**, and that is the key to use. Find it from the two ids you know:

```php
$criteria = new Criteria();
$criteria->addFilter(new EqualsFilter('productId', 'myProductId'));
$criteria->addFilter(new EqualsFilter('mediaId', 'myMediaId'));

$productMediaId = $this->productMediaRepository->searchIds($criteria, $context)->firstId();

$this->productMediaRepository->delete([
    ['id' => $productMediaId],
], $context);
```

`ProductMediaDefinition` has one primary key, `id`, so that is all the data array needs.

**This removes the association, not the media entity itself.**

So the question to answer before deleting a OneToMany association is which kind it is: a plain one,
or a mapping entity with its own id.

## Source

- [replacing-associated-data.html](https://developer.shopware.com/docs/guides/plugins/plugins/framework/data-handling/replacing-associated-data.html)
- [deleting-associated-data.html](https://developer.shopware.com/docs/guides/plugins/plugins/framework/data-handling/deleting-associated-data.html)

Shopware 6.7, retrieved 2026-08-21.
