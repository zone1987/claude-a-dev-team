# DAL Operations (Reading & Writing Data)

## Overview

Use `EntityRepository` services to read and write data through the DAL. Repository services follow the pattern `{entity_name}.repository`.

## Reading Data

### Basic Search

```php
use Shopware\Core\Framework\DataAbstractionLayer\EntityRepository;
use Shopware\Core\Framework\DataAbstractionLayer\Search\Criteria;
use Shopware\Core\Framework\Context;

class MyService
{
    public function __construct(
        private readonly EntityRepository $productRepository,
    ) {}

    public function findProducts(Context $context): void
    {
        $criteria = new Criteria();
        $criteria->setLimit(25);
        $criteria->setOffset(0);

        $result = $this->productRepository->search($criteria, $context);

        $products = $result->getEntities();  // EntityCollection
        $total = $result->getTotal();         // int
    }
}
```

### Search by ID

```php
$criteria = new Criteria([$productId]);
$product = $this->productRepository->search($criteria, $context)->first();
```

### Filters

```php
use Shopware\Core\Framework\DataAbstractionLayer\Search\Filter\EqualsFilter;
use Shopware\Core\Framework\DataAbstractionLayer\Search\Filter\EqualsAnyFilter;
use Shopware\Core\Framework\DataAbstractionLayer\Search\Filter\ContainsFilter;
use Shopware\Core\Framework\DataAbstractionLayer\Search\Filter\RangeFilter;
use Shopware\Core\Framework\DataAbstractionLayer\Search\Filter\MultiFilter;
use Shopware\Core\Framework\DataAbstractionLayer\Search\Filter\NotFilter;
use Shopware\Core\Framework\DataAbstractionLayer\Search\Filter\PrefixFilter;
use Shopware\Core\Framework\DataAbstractionLayer\Search\Filter\SuffixFilter;

$criteria = new Criteria();

// Equals
$criteria->addFilter(new EqualsFilter('active', true));

// Equals any (IN)
$criteria->addFilter(new EqualsAnyFilter('id', [$id1, $id2]));

// Contains (LIKE %value%)
$criteria->addFilter(new ContainsFilter('name', 'shirt'));

// Range
$criteria->addFilter(new RangeFilter('stock', [
    RangeFilter::GTE => 10,
    RangeFilter::LTE => 100,
]));

// Multi (AND/OR)
$criteria->addFilter(new MultiFilter(MultiFilter::CONNECTION_OR, [
    new EqualsFilter('active', true),
    new RangeFilter('stock', [RangeFilter::GT => 0]),
]));

// Not
$criteria->addFilter(new NotFilter(NotFilter::CONNECTION_AND, [
    new EqualsFilter('active', false),
]));
```

### Sorting

```php
use Shopware\Core\Framework\DataAbstractionLayer\Search\Sorting\FieldSorting;

$criteria->addSorting(new FieldSorting('name', FieldSorting::ASCENDING));
$criteria->addSorting(new FieldSorting('createdAt', FieldSorting::DESCENDING));
```

### Associations

```php
// Load related entities
$criteria->addAssociation('manufacturer');
$criteria->addAssociation('categories');
$criteria->addAssociation('media');

// Nested associations
$criteria->addAssociation('orderLineItems.product');

// Filter/sort associations
$criteria->getAssociation('categories')
    ->addFilter(new EqualsFilter('active', true))
    ->addSorting(new FieldSorting('name'));

// Limit associations
$criteria->getAssociation('categories')
    ->setLimit(5);
```

### Aggregations

```php
use Shopware\Core\Framework\DataAbstractionLayer\Search\Aggregation\Metric\CountAggregation;
use Shopware\Core\Framework\DataAbstractionLayer\Search\Aggregation\Metric\SumAggregation;
use Shopware\Core\Framework\DataAbstractionLayer\Search\Aggregation\Metric\AvgAggregation;
use Shopware\Core\Framework\DataAbstractionLayer\Search\Aggregation\Metric\MaxAggregation;
use Shopware\Core\Framework\DataAbstractionLayer\Search\Aggregation\Metric\MinAggregation;
use Shopware\Core\Framework\DataAbstractionLayer\Search\Aggregation\Bucket\TermsAggregation;

$criteria->addAggregation(new CountAggregation('count-products', 'id'));
$criteria->addAggregation(new SumAggregation('sum-stock', 'stock'));
$criteria->addAggregation(new AvgAggregation('avg-price', 'price'));

$result = $this->productRepository->search($criteria, $context);
$count = $result->getAggregations()->get('count-products');
```

### Search IDs Only

For better performance when you only need IDs:

```php
$criteria = new Criteria();
$criteria->addFilter(new EqualsFilter('active', true));

$ids = $this->productRepository->searchIds($criteria, $context);
$idList = $ids->getIds(); // array of string UUIDs
```

## Writing Data

### Create

```php
use Shopware\Core\Framework\Uuid\Uuid;

$this->productRepository->create([
    [
        'id' => Uuid::randomHex(),
        'name' => 'My Product',
        'productNumber' => 'SW-001',
        'stock' => 10,
        'taxId' => $taxId,
        'price' => [
            [
                'currencyId' => Defaults::CURRENCY,
                'gross' => 19.99,
                'net' => 16.80,
                'linked' => true,
            ],
        ],
    ],
], $context);
```

### Update

```php
$this->productRepository->update([
    [
        'id' => $productId,
        'stock' => 5,
        'active' => false,
    ],
], $context);
```

### Upsert (Create or Update)

```php
$this->productRepository->upsert([
    [
        'id' => $productId,  // Creates if not exists, updates if exists
        'name' => 'Updated Name',
        'stock' => 10,
    ],
], $context);
```

### Delete

```php
$this->productRepository->delete([
    ['id' => $productId],
], $context);
```

## SalesChannel Repository

For storefront/Store API context, use `SalesChannelRepository` which respects sales channel visibility:

```php
use Shopware\Core\System\SalesChannel\Entity\SalesChannelRepository;

class MyStorefrontService
{
    public function __construct(
        private readonly SalesChannelRepository $salesChannelProductRepository,
    ) {}

    public function loadProducts(SalesChannelContext $salesChannelContext): void
    {
        $criteria = new Criteria();
        $result = $this->salesChannelProductRepository->search($criteria, $salesChannelContext);
    }
}
```

Service registration uses `sales_channel.{entity}.repository`:
```xml
<argument type="service" id="sales_channel.product.repository"/>
```

## Best Practices

1. **Always set a title** on criteria for debugging: `$criteria->setTitle('my-service::load-products')`
2. **Use `searchIds()`** when you only need IDs — much faster than full entity hydration
3. **Limit associations** — only load what you need
4. **Use DAL over raw SQL** unless performance requires it (see ADR `2021-05-14-when-to-use-plain-sql-or-dal.md`)
5. **Batch writes** — pass multiple items in one `create()`/`update()` call
6. **Use `Uuid::randomHex()`** to generate IDs
