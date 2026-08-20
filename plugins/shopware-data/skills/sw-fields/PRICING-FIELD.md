# Shopware 6 — Pricing field

Prices are stored in a `PriceField` (JSON per currency with net/gross + currency).

```php
(new PriceField('price', 'price'))->addFlags(new Required()),
```
```php
$payload = ['price' => [[
    'currencyId' => Defaults::CURRENCY,
    'gross' => 19.99, 'net' => 16.80, 'linked' => true,
]]];
$price = $entity->getPrice()->getCurrencyPrice($currencyId); // reading
```

`linked` couples gross and net through the tax rate. Multiple currencies become multiple array entries. Cart price
calculation (tax, discounts, rounding) belongs in the checkout (`shopware-checkout` → `sw-cart-price`), not in the entity.

→ Pricing details: [PRICING.md](PRICING.md)
