# Shopware 6 — cart validators

The cart is validated continuously by **validators**: they check for invalid line items (a missing
label), shipping addresses and anything else that should stop a checkout. A custom validator needs
three parts — the validator, an error class, and snippets for the message.

## Contents

- [The validator](#the-validator)
- [The error class](#the-error-class)
- [The snippets](#the-snippets)

## The validator

Implement `Shopware\Core\Checkout\Cart\CartValidatorInterface`, which forces a `validate` method.
**Place it in the domain it validates**: an address validator under
`<plugin root>/src/Core/Checkout/Cart/Address`, so a `CustomCartValidator` goes to
`<plugin root>/src/Core/Checkout/Cart/Custom`.

```php
// <plugin root>/src/Core/Checkout/Cart/Custom/CustomCartValidator.php
public function validate(Cart $cart, ErrorCollection $errorCollection, SalesChannelContext $context): void
{
    foreach ($cart->getLineItems()->getFlat() as $lineItem) {
        if (!array_key_exists('customPayload', $lineItem->getPayload())
            || $lineItem->getPayload()['customPayload'] !== 'example') {
            $errorCollection->add(new CustomCartBlockedError($lineItem->getId()));

            return;
        }
    }
}
```

`validate()` receives the cart, the error collection and the sales channel context. The collection
may already hold errors from validators that ran earlier.

**The `return` after adding the error is deliberate.** Without it the loop adds one error per invalid
line item — four invalid items produce four messages on the cart page. Returning shows one. Which
behaviour is right depends on what you validate, but the choice has to be made consciously.

An error must extend `Shopware\Core\Checkout\Cart\Error\Error`; an arbitrary exception will not do.

Register with the tag `shopware.cart.validator`:

```php
// <plugin root>/src/Resources/config/services.php
use Symfony\Component\DependencyInjection\Loader\Configurator\ContainerConfigurator;

return static function (ContainerConfigurator $configurator): void {
    $services = $configurator->services();

    $services->set(CustomCartValidator::class)
        ->tag('shopware.cart.validator');
};
```

## The error class

The error belongs in an `Error` directory inside the validator's own domain — for the validator
above, `<plugin root>/src/Core/Checkout/Cart/Custom/Error`. Extending
`Shopware\Core\Checkout\Cart\Error\Error` asks for these methods:

| Method | What it returns |
|---|---|
| `getId` | a unique id, since the collection stores the error under it — the line item id serves well |
| `getMessageKey` | the snippet key of the message, e.g. `custom-line-item-blocked` |
| `getLevel` | `LEVEL_NOTICE`, `LEVEL_WARNING` or `LEVEL_ERROR` — rendered as a blue, yellow or red box |
| `blockOrder` | whether the error prevents finishing the checkout |
| `blockResubmit` | optional; whether the customer is blocked from trying again. Defaults to `true` when the method is absent |
| `getParameters` | custom payload; any plugin reading the cart's errors can act on it |

Level and `blockOrder` belong together: blocking the checkout while showing a mere notice makes no
sense.

```php
// <plugin root>/src/Core/Checkout/Cart/Custom/Error/CustomCartBlockedError.php
public function __construct(private string $lineItemId)
{
    parent::__construct();
}

public function getId(): string
{
    return $this->lineItemId;
}

public function getMessageKey(): string
{
    return self::KEY;
}

public function getLevel(): int
{
    // return self::LEVEL_NOTICE;
    // return self::LEVEL_WARNING;
    return self::LEVEL_ERROR;
}

public function blockOrder(): bool
{
    return true;
}

public function getParameters(): array
{
    return ['lineItemId' => $this->lineItemId];
}
```

## The snippets

Shopware looks up the message key in **two** places, so the cart and the later checkout steps can
carry different wording:

| Where | Key |
|---|---|
| the cart | `checkout.<messageKey>` |
| the checkout steps | `error.<messageKey>` |

```json
// <plugin root>/src/Resources/snippet/en_GB/example.en-GB.json
{
    "checkout": {
        "custom-line-item-blocked": "Example error message for the cart"
    },
    "error": {
        "custom-line-item-blocked": "Example error message for the checkout"
    }
}
```

## Source

[developer.shopware.com/docs/guides/plugins/plugins/checkout/cart/add-cart-validator.html](https://developer.shopware.com/docs/guides/plugins/plugins/checkout/cart/add-cart-validator.html),
Shopware 6.7, retrieved 2026-08-21.
