# Shopware 6 — Cart Validator

Validators inspect the calculated cart and can attach **blocking** or informational errors
(e.g. minimum order value, availability).

```php
class FfMinOrderValidator implements CartValidatorInterface
{
    public function validate(Cart $cart, ErrorCollection $errors, SalesChannelContext $context): void
    {
        if ($cart->getPrice()->getTotalPrice() < 10.0) {
            $errors->add(new FfMinOrderError(10.0)); // blocking error prevents checkout
        }
    }
}
```

Register via the `shopware.cart.validator` tag. A `CartError` with `blockOrder() === true` prevents order
completion; otherwise it is only a notice. Errors surface in the storefront and Store API. Derive your own error class
from `Error` (level/key/message).
