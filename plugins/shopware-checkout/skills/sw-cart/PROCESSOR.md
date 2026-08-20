# Shopware 6 — Cart-Processor

Der Warenkorb wird in zwei Phasen berechnet: **Collector** (Daten sammeln, `sw-cart-collector`) → **Processor**
(Preise/Struktur berechnen). Ein Processor implementiert `CartProcessorInterface`.

```php
class FfFeeProcessor implements CartProcessorInterface
{
    public function process(CartDataCollection $data, Cart $original, Cart $toCalculate,
                            SalesChannelContext $context, CartBehavior $behavior): void
    {
        // LineItems/Gebühren zu $toCalculate hinzufügen, Preise via Calculator berechnen
    }
}
```

Registrierung via `shopware.cart.processor`-Tag (Priorität beachtet die Reihenfolge). Arbeite immer auf `$toCalculate`
(nicht `$original`). Preisberechnung über die Price-Services (`sw-cart-price`). Rabatte → `sw-cart-discount`,
Lieferkosten → `sw-delivery`. Für App-basierte Manipulation: `sw-cart-facade-script`.

→ Cart-Details: [PROCESSOR-CHECKOUT.md](PROCESSOR-CHECKOUT.md)
