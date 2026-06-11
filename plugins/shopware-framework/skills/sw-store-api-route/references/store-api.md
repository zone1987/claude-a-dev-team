# Store API Routes

## Overview

Store API routes provide data to the storefront and headless clients. They follow the decorator pattern with an abstract route class and a concrete implementation.

## Abstract Route

```php
<?php declare(strict_types=1);

namespace FfContentPlus\Core\Content\Item\SalesChannel;

use Shopware\Core\Framework\Log\Package;
use Shopware\Core\System\SalesChannel\SalesChannelContext;
use Symfony\Component\HttpFoundation\Request;

/**
 * @class AbstractItemRoute
 * @package FfContentPlus\Core\Content\Item\SalesChannel
 */
#[Package('custom-plugins')]
abstract class AbstractItemRoute
{
    /**
     * @return AbstractItemRoute
     */
    abstract public function getDecorated(): AbstractItemRoute;

    /**
     * @param Request $request
     * @param SalesChannelContext $context
     * @return ItemRouteResponse
     */
    abstract public function load(Request $request, SalesChannelContext $context): ItemRouteResponse;
}
```

## Route Response

```php
<?php declare(strict_types=1);

namespace FfContentPlus\Core\Content\Item\SalesChannel;

use FfContentPlus\Core\Content\Item\ItemCollection;
use Shopware\Core\Framework\Log\Package;
use Shopware\Core\System\SalesChannel\StoreApiResponse;

/**
 * @class ItemRouteResponse
 * @package FfContentPlus\Core\Content\Item\SalesChannel
 */
#[Package('custom-plugins')]
class ItemRouteResponse extends StoreApiResponse
{
    /**
     * @param ItemCollection $items
     */
    public function __construct(
        private readonly ItemCollection $items,
    ) {
        parent::__construct($items);
    }

    /**
     * @return ItemCollection
     */
    public function getItems(): ItemCollection
    {
        return $this->items;
    }
}
```

## Concrete Route Implementation

```php
<?php declare(strict_types=1);

namespace FfContentPlus\Core\Content\Item\SalesChannel;

use FfContentPlus\Core\Content\Item\ItemCollection;
use Shopware\Core\Framework\DataAbstractionLayer\EntityRepository;
use Shopware\Core\Framework\DataAbstractionLayer\Search\Criteria;
use Shopware\Core\Framework\DataAbstractionLayer\Search\Filter\EqualsFilter;
use Shopware\Core\Framework\Log\Package;
use Shopware\Core\Framework\Plugin\Exception\DecorationPatternException;
use Shopware\Core\Framework\Routing\StoreApiRouteScope;
use Shopware\Core\PlatformRequest;
use Shopware\Core\System\SalesChannel\SalesChannelContext;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\Routing\Attribute\Route;

/**
 * @class ItemRoute
 * @package FfContentPlus\Core\Content\Item\SalesChannel
 */
#[Route(defaults: [PlatformRequest::ATTRIBUTE_ROUTE_SCOPE => [StoreApiRouteScope::ID]])]
#[Package('custom-plugins')]
class ItemRoute extends AbstractItemRoute
{
    /**
     * @param EntityRepository $itemRepository
     */
    public function __construct(
        private readonly EntityRepository $itemRepository,
    ) {}

    /**
     * @return AbstractItemRoute
     */
    public function getDecorated(): AbstractItemRoute
    {
        throw new DecorationPatternException(self::class);
    }

    /**
     * @param Request $request
     * @param SalesChannelContext $context
     * @return ItemRouteResponse
     */
    #[Route(
        path: '/store-api/ff/content-plus/items',
        name: 'store-api.ff.content-plus.items',
        methods: ['GET', 'POST'],
    )]
    public function load(Request $request, SalesChannelContext $context): ItemRouteResponse
    {
        $criteria = new Criteria();
        $criteria->addFilter(new EqualsFilter('active', true));
        $criteria->addAssociation('media');
        $criteria->setTitle('ff-content-plus::item-route');

        /** @var ItemCollection $items */
        $items = $this->itemRepository
            ->search($criteria, $context->getContext())
            ->getEntities();

        return new ItemRouteResponse($items);
    }
}
```

## Service Registration

```xml
<service id="FfContentPlus\Core\Content\Item\SalesChannel\ItemRoute">
    <argument type="service" id="ff_content_plus_item.repository"/>
</service>

<!-- Register abstract route for decoration -->
<service id="FfContentPlus\Core\Content\Item\SalesChannel\AbstractItemRoute"
         class="FfContentPlus\Core\Content\Item\SalesChannel\ItemRoute">
    <argument type="service" id="ff_content_plus_item.repository"/>
</service>
```

## Route Registration (routes.xml)

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<routes xmlns="http://symfony.com/schema/routing"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://symfony.com/schema/routing https://symfony.com/schema/routing/routing-1.0.xsd">

    <import resource="../../Core/Content/Item/SalesChannel/" type="attribute"/>
</routes>
```

## Route URL Convention

Plugin Store API routes: `/store-api/{vendor}/{plugin-kebab}/{resource}`

Examples:
- `/store-api/ff/content-plus/items`
- `/store-api/adt/product-export/status`

## Decorating Existing Routes

```xml
<service id="FfContentPlus\Core\Decorator\DecoratedProductDetailRoute"
         decorates="Shopware\Core\Content\Product\SalesChannel\Detail\ProductDetailRoute">
    <argument type="service" id="FfContentPlus\Core\Decorator\DecoratedProductDetailRoute.inner"/>
</service>
```

```php
class DecoratedProductDetailRoute extends AbstractProductDetailRoute
{
    public function __construct(
        private readonly AbstractProductDetailRoute $decorated,
        private readonly MyService $myService,
    ) {}

    public function getDecorated(): AbstractProductDetailRoute
    {
        return $this->decorated;
    }

    public function load(string $productId, Request $request, SalesChannelContext $context, Criteria $criteria): ProductDetailRouteResponse
    {
        $response = $this->decorated->load($productId, $request, $context, $criteria);
        // Add custom data to response
        return $response;
    }
}
```

## ApiAware Flag

Entities must have `ApiAware` flags on fields that should be accessible via Store API. Without this flag, fields are only available in Admin API.
