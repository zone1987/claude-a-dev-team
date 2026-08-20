# Shopware 6 — Cart-Validator

Validatoren prüfen den berechneten Warenkorb und können **blockierende** oder informative Fehler anhängen
(z.B. Mindestbestellwert, Verfügbarkeit).

```php
class FfMinOrderValidator implements CartValidatorInterface
{
    public function validate(Cart $cart, ErrorCollection $errors, SalesChannelContext $context): void
    {
        if ($cart->getPrice()->getTotalPrice() < 10.0) {
            $errors->add(new FfMinOrderError(10.0)); // blocking error verhindert Checkout
        }
    }
}
```

Registrierung via `shopware.cart.validator`-Tag. Ein `CartError` mit `blockOrder() === true` verhindert den
Bestellabschluss; sonst nur Hinweis. Fehler werden im Storefront/Store-API ausgegeben. Eigene Error-Klasse von
`Error` ableiten (Level/Key/Message).
