# Shopware 6 — Tax Provider

Tax providers override the cart tax determination (e.g. an external service such as Avalara). ADR "tax providers".

```php
class FfTaxProvider extends AbstractTaxProvider
{
    public function provide(Cart $cart, SalesChannelContext $context): TaxProviderResult
    {
        // external calculation -> CalculatedTax collection per line item/delivery
        return new TaxProviderResult($lineItemTaxes, $deliveryTaxes, $cartPriceTaxes);
    }
}
```

Register it as a `tax_provider` entity plus a service (`shopware.tax.provider` tag); it can be enabled per sales channel with a priority
in the admin. Apps can supply tax providers through the manifest (`shopware-apps`). The default tax logic (without a provider) runs
through `TaxRuleCollection`/`TaxDetector` (`sw-cart-price`). Maintaining tax rates: `shopware-merchant` (`sw-merchant-settings-tax`).
