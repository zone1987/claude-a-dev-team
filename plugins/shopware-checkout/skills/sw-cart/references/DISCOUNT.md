# Shopware 6 — cart discounts

A discount is added through the **processor pattern**: a `CartProcessorInterface` implementation that
creates a discount line item and gives it a price definition.

## Contents

- [The processor](#the-processor)
- [The discount line item](#the-discount-line-item)
- [The price definition](#the-price-definition)
- [Registration and priority](#registration-and-priority)

## The processor

Implement `Shopware\Core\Checkout\Cart\CartProcessorInterface` and inject
`Shopware\Core\Checkout\Cart\Price\PercentagePriceCalculator`. Everything happens in `process()`,
where the product items already carry a name and a price.

```php
// <plugin root>/src/Core/Checkout/ExampleProcessor.php
public function process(CartDataCollection $data, Cart $original, Cart $toCalculate,
                        SalesChannelContext $context, CartBehavior $behavior): void
{
    $products = $this->findExampleProducts($toCalculate);

    // no matching products? early return
    if ($products->count() === 0) {
        return;
    }

    $discountLineItem = $this->createDiscount('EXAMPLE_DISCOUNT');

    // how this price is to be recalculated
    $definition = new PercentagePriceDefinition(
        -10,
        new LineItemRule(LineItemRule::OPERATOR_EQ, $products->getKeys())
    );

    $discountLineItem->setPriceDefinition($definition);

    $discountLineItem->setPrice(
        $this->calculator->calculate($definition->getPercentage(), $products->getPrices(), $context)
    );

    $toCalculate->add($discountLineItem);
}
```

Filtering is by type first, then by whatever the discount applies to — here a label containing
"example". **Only products**, not custom or promotional line items:

```php
private function findExampleProducts(Cart $cart): LineItemCollection
{
    return $cart->getLineItems()->filter(function (LineItem $item) {
        if ($item->getType() !== LineItem::PRODUCT_LINE_ITEM_TYPE) {
            return false;
        }

        $exampleInLabel = stripos($item->getLabel(), 'example') !== false;

        if (!$exampleInLabel) {
            return false;
        }

        return $item;
    });
}
```

## The discount line item

```php
private function createDiscount(string $name): LineItem
{
    $discountLineItem = new LineItem($name, 'example_discount', null, 1);

    $discountLineItem->setLabel('Our example discount!');
    $discountLineItem->setGood(false);
    $discountLineItem->setStackable(false);
    $discountLineItem->setRemovable(false);

    return $discountLineItem;
}
```

| Call | Why |
|---|---|
| `setGood(false)` | a discount is not a good |
| `setStackable(false)` | it must not be multiplied by quantity |
| `setRemovable(false)` | the customer must not delete it from the cart |

## The price definition

**The definition is not optional, and not a formality.** It tells the core how the price can be
recalculated — including after the plugin that created it is uninstalled. For a percentage discount
use `PercentagePriceDefinition`, which takes a value, the currency precision, and rules where needed.

`LineItemRule` takes two arguments:

- the operator, e.g. `LineItemRule::OPERATOR_EQ` (equals) or `LineItemRule::OPERATOR_NEQ` (not equals)
- the line item identifiers the rule applies to — here the keys of the filtered products

The current price is then calculated with the core's `PercentagePriceCalculator`, and the discount is
added to `$toCalculate`.

## Registration and priority

```php
// <plugin root>/src/Resources/config/services.php
use Symfony\Component\DependencyInjection\Loader\Configurator\ContainerConfigurator;

return static function (ContainerConfigurator $configurator): void {
    $services = $configurator->services();

    $services->set(ExampleProcessor::class)
        ->tag('shopware.cart.processor', ['priority' => 4500]);
};
```

**Priority `4500` runs after the product processor**, which is what makes the products' prices
available to discount in the first place.

## Source

[developer.shopware.com/docs/guides/plugins/plugins/checkout/cart/add-cart-discounts.html](https://developer.shopware.com/docs/guides/plugins/plugins/checkout/cart/add-cart-discounts.html),
Shopware 6.7, retrieved 2026-08-21.
