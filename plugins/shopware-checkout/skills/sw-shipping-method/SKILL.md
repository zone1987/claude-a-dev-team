---
name: sw-shipping-method
description: >
  Eigene Versandart in Shopware 6 programmatisch bereitstellen: shipping_method-Entity (Migration), Verfügbarkeitsregel,
  Preismatrix, Tracking-URL, Aktivierung je SalesChannel. Trigger: "Versandart anlegen", "shipping_method entity",
  "eigene Versandart plugin", "shipping method migration", "Versandart Regel", "delivery method". Shopware 6.7.
---

# Shopware 6 — Versandart (technisch)

Eine Versandart ist eine `shipping_method`-Entity. Plugins legen sie per Migration/Lifecycle an (mit `technicalName`,
Verfügbarkeitsregel, Preismatrix, Lieferzeit).

```php
$this->shippingMethodRepo->upsert([[
    'id' => $id, 'technicalName' => 'ff_express', 'name' => 'FF Express', 'active' => true,
    'deliveryTimeId' => $deliveryTimeId, 'availabilityRuleId' => $ruleId,
    'prices' => [[ 'calculation' => 1, 'currencyPrice' => [[ 'currencyId' => Defaults::CURRENCY, 'gross' => 4.9, 'net' => 4.12, 'linked' => false ]] ]],
]], $context);
```

Verfügbarkeit über eine Rule (`sw-custom-rule`); Zuordnung zum SalesChannel + Aktivierung. Versandkosten-Berechnung
im Cart: `sw-delivery`. Aus Betreibersicht konfigurieren: `shopware-merchant` (`sw-merchant-settings-shipping-methods`).
