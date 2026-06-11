---
name: sw-tax-provider
description: >
  Eigener Tax-Provider in Shopware 6 (externe Steuerberechnung): AbstractTaxProvider, provide(), TaxProviderResult,
  Registrierung, App-Mode. Trigger: "Tax Provider", "AbstractTaxProvider", "externe Steuerberechnung", "TaxProviderResult",
  "Steueranbieter shopware", "tax provider app". Shopware 6.7.
---

# Shopware 6 — Tax-Provider

Tax-Provider überschreiben die Steuerermittlung des Warenkorbs (z.B. externer Dienst wie Avalara). ADR „tax providers".

```php
class FfTaxProvider extends AbstractTaxProvider
{
    public function provide(Cart $cart, SalesChannelContext $context): TaxProviderResult
    {
        // externe Berechnung -> pro LineItem/Delivery CalculatedTax-Collection
        return new TaxProviderResult($lineItemTaxes, $deliveryTaxes, $cartPriceTaxes);
    }
}
```

Registrierung als `tax_provider`-Entity + Service (`shopware.tax.provider`-Tag); im Admin pro SalesChannel mit Priorität
aktivierbar. Apps können Tax-Provider per Manifest stellen (`shopware-apps`). Standard-Steuerlogik (ohne Provider) läuft
über `TaxRuleCollection`/`TaxDetector` (`sw-cart-price`). Steuersätze pflegen: `shopware-merchant` (`sw-merchant-settings-tax`).
