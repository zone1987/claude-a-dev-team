# Events & Subscribers

## Overview

Shopware uses Symfony's event system. Plugins subscribe to events via `EventSubscriberInterface` to react to system events (entity writes, page loads, cart changes, etc.).

## Event Subscriber

```php
<?php declare(strict_types=1);

namespace FfContentPlus\Subscriber;

use Shopware\Core\Content\Product\ProductEvents;
use Shopware\Core\Framework\DataAbstractionLayer\Event\EntityWrittenEvent;
use Shopware\Core\Framework\Log\Package;
use Symfony\Component\EventDispatcher\EventSubscriberInterface;

/**
 * @class ProductWrittenSubscriber
 * @package FfContentPlus\Subscriber
 */
#[Package('custom-plugins')]
class ProductWrittenSubscriber implements EventSubscriberInterface
{
    /**
     * @return array<string, string|array{0: string, 1: int}>
     */
    public static function getSubscribedEvents(): array
    {
        return [
            ProductEvents::PRODUCT_WRITTEN_EVENT => 'onProductWritten',
            // With priority (higher = earlier)
            ProductEvents::PRODUCT_LOADED_EVENT => ['onProductLoaded', 500],
        ];
    }

    /**
     * @param EntityWrittenEvent $event
     * @return void
     */
    public function onProductWritten(EntityWrittenEvent $event): void
    {
        $ids = $event->getIds();
        $context = $event->getContext();
        // Process written product IDs
    }
}
```

## Service Registration

With `autoconfigure="true"`, subscribers are auto-tagged:

```xml
<service id="FfContentPlus\Subscriber\ProductWrittenSubscriber"/>
```

Without autoconfigure:

```xml
<service id="FfContentPlus\Subscriber\ProductWrittenSubscriber">
    <tag name="kernel.event_subscriber"/>
</service>
```

## Common Events

### Entity Events

```php
use Shopware\Core\Content\Product\ProductEvents;
use Shopware\Core\Content\Category\CategoryEvents;
use Shopware\Core\Checkout\Order\OrderEvents;
use Shopware\Core\Checkout\Customer\CustomerEvents;

// Pattern: {entity}.written, {entity}.loaded, {entity}.deleted
ProductEvents::PRODUCT_WRITTEN_EVENT      // 'product.written'
ProductEvents::PRODUCT_LOADED_EVENT       // 'product.loaded'
ProductEvents::PRODUCT_DELETED_EVENT      // 'product.deleted'
OrderEvents::ORDER_WRITTEN_EVENT          // 'order.written'
CustomerEvents::CUSTOMER_WRITTEN_EVENT    // 'customer.written'
```

### Checkout Events

```php
use Shopware\Core\Checkout\Cart\Event\CartChangedEvent;
use Shopware\Core\Checkout\Cart\Event\CartCreatedEvent;
use Shopware\Core\Checkout\Cart\Event\CartDeletedEvent;
use Shopware\Core\Checkout\Cart\Event\CartSavedEvent;
use Shopware\Core\Checkout\Cart\Event\CheckoutOrderPlacedEvent;
use Shopware\Core\Checkout\Customer\Event\CustomerLoginEvent;
use Shopware\Core\Checkout\Customer\Event\CustomerRegisterEvent;
```

### Storefront Events

```php
use Shopware\Storefront\Page\Product\ProductPageLoadedEvent;
use Shopware\Storefront\Page\Navigation\NavigationPageLoadedEvent;
use Shopware\Storefront\Page\Checkout\Confirm\CheckoutConfirmPageLoadedEvent;
```

## Flow Events (Business Events)

Flow events trigger Flow Builder actions. Implement `FlowEventAware`:

```php
use Shopware\Core\Framework\Event\FlowEventAware;
use Shopware\Core\Framework\Event\EventData\EventDataCollection;
use Shopware\Core\Framework\Event\EventData\EntityType;

class MyCustomEvent extends Event implements FlowEventAware
{
    public function __construct(
        private readonly OrderEntity $order,
        private readonly Context $context,
    ) {}

    public function getName(): string
    {
        return 'ff.content_plus.my_event';
    }

    public static function getAvailableData(): EventDataCollection
    {
        return (new EventDataCollection())
            ->add('order', new EntityType(OrderDefinition::class));
    }

    public function getContext(): Context
    {
        return $this->context;
    }
}
```

## Awareness Interfaces

Add awareness interfaces to make data available in Flow Builder:

| Interface | Provides | Storer |
|-----------|----------|--------|
| `OrderAware` | Order ID | `OrderStorer` |
| `CustomerAware` | Customer ID | `CustomerStorer` |
| `MailAware` | Mail recipients | `MailStorer` |
| `SalesChannelAware` | Sales channel ID | — |
| `CustomerGroupAware` | Customer group ID | `CustomerGroupStorer` |

## Event Data Types

Used in `getAvailableData()`:

```php
use Shopware\Core\Framework\Event\EventData\EntityType;
use Shopware\Core\Framework\Event\EventData\ScalarValueType;
use Shopware\Core\Framework\Event\EventData\ArrayType;
use Shopware\Core\Framework\Event\EventData\ObjectType;

$data = (new EventDataCollection())
    ->add('order', new EntityType(OrderDefinition::class))
    ->add('amount', new ScalarValueType(ScalarValueType::TYPE_FLOAT))
    ->add('tags', new ArrayType(new ScalarValueType(ScalarValueType::TYPE_STRING)));
```

## EntityWrittenEvent Details

```php
public function onProductWritten(EntityWrittenEvent $event): void
{
    foreach ($event->getWriteResults() as $result) {
        $id = $result->getPrimaryKey();           // string (UUID)
        $payload = $result->getPayload();          // array of written fields
        $operation = $result->getOperation();      // 'insert' or 'update'
        $existence = $result->getExistence();      // EntityExistence
    }
}
```
