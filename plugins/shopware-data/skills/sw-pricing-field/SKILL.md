---
name: sw-pricing-field
description: >
  Preise in Shopware 6 DAL: PriceField/PriceCollection, Price (net/gross je Currency), CashRounding,
  Preise schreiben/lesen. Trigger: "PriceField", "Price collection", "Preis speichern entity", "net gross price",
  "CashRounding", "currency price DAL". Shopware 6.7.
---

# Shopware 6 — Pricing-Field

Preise werden als `PriceField` gespeichert (JSON je Währung mit netto/brutto + Currency).

```php
(new PriceField('price', 'price'))->addFlags(new Required()),
```
```php
$payload = ['price' => [[
    'currencyId' => Defaults::CURRENCY,
    'gross' => 19.99, 'net' => 16.80, 'linked' => true,
]]];
$price = $entity->getPrice()->getCurrencyPrice($currencyId); // Lesen
```

`linked` koppelt brutto/netto über die Steuer. Mehrere Währungen als Einträge im Array. Cart-Preisberechnung
(Steuer, Rabatte, Rundung) gehört in den Checkout (`shopware-checkout` → `sw-cart-price`), nicht in die Entity.

→ Pricing-Details: [references/pricing.md](references/pricing.md)
