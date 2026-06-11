# Checkout (Cart & Order)

## Overview

Plugins can modify the cart through processors, collectors, and validators. They can also hook into the order state machine and generate documents.

## Cart Processor

Modifies cart line items (prices, quantities, custom data):

```php
<?php declare(strict_types=1);

namespace FfContentPlus\Core\Checkout\Cart;

use Shopware\Core\Checkout\Cart\Cart;
use Shopware\Core\Checkout\Cart\CartBehavior;
use Shopware\Core\Checkout\Cart\CartProcessorInterface;
use Shopware\Core\Checkout\Cart\LineItem\CartDataCollection;
use Shopware\Core\Framework\Log\Package;
use Shopware\Core\System\SalesChannel\SalesChannelContext;

/**
 * @class DiscountProcessor
 * @package FfContentPlus\Core\Checkout\Cart
 */
#[Package('custom-plugins')]
class DiscountProcessor implements CartProcessorInterface
{
    /**
     * @param CartDataCollection $data
     * @param Cart $original
     * @param Cart $toCalculate
     * @param SalesChannelContext $context
     * @param CartBehavior $behavior
     * @return void
     */
    public function process(
        CartDataCollection $data,
        Cart $original,
        Cart $toCalculate,
        SalesChannelContext $context,
        CartBehavior $behavior,
    ): void {
        // Modify line items, add discounts, etc.
        foreach ($toCalculate->getLineItems() as $lineItem) {
            // Process each line item
        }
    }
}
```

## Cart Data Collector

Fetches additional data needed by processors:

```php
use Shopware\Core\Checkout\Cart\CartDataCollectorInterface;

class ProductDataCollector implements CartDataCollectorInterface
{
    public function collect(
        CartDataCollection $data,
        Cart $original,
        SalesChannelContext $context,
        CartBehavior $behavior,
    ): void {
        // Fetch data and store in CartDataCollection
        $data->set('ff_content_plus_data', $myData);
    }
}
```

## Cart Validator

Validates cart before checkout:

```php
use Shopware\Core\Checkout\Cart\CartValidatorInterface;
use Shopware\Core\Checkout\Cart\Error\ErrorCollection;

class MinOrderValidator implements CartValidatorInterface
{
    public function validate(
        Cart $cart,
        ErrorCollection $errors,
        SalesChannelContext $context,
    ): void {
        if ($cart->getPrice()->getTotalPrice() < 10.0) {
            $errors->add(new MinOrderValueError(10.0));
        }
    }
}
```

## Service Registration

```xml
<service id="FfContentPlus\Core\Checkout\Cart\DiscountProcessor">
    <tag name="shopware.cart.processor" priority="4000"/>
</service>

<service id="FfContentPlus\Core\Checkout\Cart\ProductDataCollector">
    <tag name="shopware.cart.collector"/>
</service>

<service id="FfContentPlus\Core\Checkout\Cart\MinOrderValidator">
    <tag name="shopware.cart.validator"/>
</service>
```

## Order State Machine

Subscribe to state transitions:

```php
use Shopware\Core\Checkout\Order\Event\OrderStateMachineStateChangeEvent;

class OrderStateSubscriber implements EventSubscriberInterface
{
    public static function getSubscribedEvents(): array
    {
        return [
            'state_enter.order.state.completed' => 'onOrderCompleted',
            'state_enter.order_delivery.state.shipped' => 'onDeliveryShipped',
            'state_enter.order_transaction.state.paid' => 'onTransactionPaid',
        ];
    }

    public function onOrderCompleted(OrderStateMachineStateChangeEvent $event): void
    {
        $order = $event->getOrder();
        // React to order completion
    }
}
```

## State Machine States

### Order States
`open` → `in_progress` → `completed` / `cancelled`

### Delivery States
`open` → `shipped` / `shipped_partially` → `returned` / `returned_partially`

### Transaction (Payment) States
`open` → `paid` / `paid_partially` → `refunded` / `refunded_partially` / `cancelled` / `failed`

## Adding Line Items

```php
use Shopware\Core\Checkout\Cart\LineItem\LineItem;
use Shopware\Core\Checkout\Cart\Price\Struct\AbsolutePriceDefinition;

$lineItem = new LineItem(
    Uuid::randomHex(),
    'ff-content-plus-discount',
    null,
    1
);
$lineItem->setLabel('Content Plus Discount');
$lineItem->setGood(false);
$lineItem->setRemovable(false);
$lineItem->setPriceDefinition(new AbsolutePriceDefinition(-5.00));

$cart->add($lineItem);
```
