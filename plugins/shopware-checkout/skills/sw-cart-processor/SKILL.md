---
name: sw-cart-processor
description: >
  Eigener Cart-Processor in Shopware 6: CartProcessorInterface, in die Warenkorb-Berechnungspipeline einklinken
  (process), Preise/LineItems berechnen, Verhältnis zu Collector. Trigger: "Cart Processor", "CartProcessorInterface",
  "Warenkorb berechnen", "process cart", "Cart-Pipeline", "cart.processor tag", "eigener Warenkorb-Schritt". Shopware 6.7.
  Scaffolder: /sw-cart-processor.
---

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

→ Cart-Details: [references/checkout.md](references/checkout.md)
