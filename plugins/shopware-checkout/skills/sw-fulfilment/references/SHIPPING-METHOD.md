# Shopware 6 — Shipping Method (technical)

A shipping method is a `shipping_method` entity. Plugins create it via migration/lifecycle (with `technicalName`,
availability rule, price matrix, delivery time).

```php
$this->shippingMethodRepo->upsert([[
    'id' => $id, 'technicalName' => 'ff_express', 'name' => 'FF Express', 'active' => true,
    'deliveryTimeId' => $deliveryTimeId, 'availabilityRuleId' => $ruleId,
    'prices' => [[ 'calculation' => 1, 'currencyPrice' => [[ 'currencyId' => Defaults::CURRENCY, 'gross' => 4.9, 'net' => 4.12, 'linked' => false ]] ]],
]], $context);
```

Availability comes from a rule (`sw-custom-rule`); assign it to the sales channel and activate it. Shipping cost calculation
in the cart: `sw-delivery`. Configuring it from the merchant view: `shopware-merchant` (`sw-merchant-settings-shipping-methods`).
