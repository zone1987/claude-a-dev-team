# Shopware 6 — Cart Processor

The cart is calculated in two phases: **collector** (gather data, `sw-cart-collector`) → **processor**
(calculate prices/structure). A processor implements `CartProcessorInterface`.

```php
class FfFeeProcessor implements CartProcessorInterface
{
    public function process(CartDataCollection $data, Cart $original, Cart $toCalculate,
                            SalesChannelContext $context, CartBehavior $behavior): void
    {
        // add line items/fees to $toCalculate, calculate prices via calculator
    }
}
```

Register via the `shopware.cart.processor` tag (priority controls the order). Always work on `$toCalculate`
(not `$original`). Calculate prices through the price services (`sw-cart-price`). Discounts → `sw-cart-discount`,
delivery costs → `sw-delivery`. For app-based manipulation: `sw-cart-facade-script`.

→ Cart details: [PROCESSOR-CHECKOUT.md](PROCESSOR-CHECKOUT.md)
