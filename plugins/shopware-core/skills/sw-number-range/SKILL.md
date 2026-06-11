---
name: sw-number-range
description: >
  Fortlaufende Nummern in Shopware 6 über NumberRange erzeugen (Bestell-/Kunden-/eigene Nummernkreise):
  NumberRangeValueGeneratorInterface, eigenen Nummernkreis-Typ registrieren. Trigger: "NumberRange",
  "Nummernkreis", "fortlaufende Nummer", "NumberRangeValueGenerator", "order number generieren",
  "eigene laufende Nummer". Shopware 6.7.
---

# Shopware 6 — NumberRange

Für fortlaufende, konfigurierbare Nummern (z.B. eigene Belegnummern) den `NumberRangeValueGenerator` nutzen —
nicht selbst hochzählen (Race-Conditions, Cluster-sicher gelöst).

```php
$number = $this->valueGenerator->getValue(
    'ff_content_export',   // technischer Name des NumberRange-Typs
    $context,
    $salesChannelId        // optional je Sales Channel
);
```

Einen eigenen Nummernkreis-Typ über eine Migration/Fixture in `number_range_type` + `number_range` anlegen
(Pattern z.B. `EXP{n}`). Der Generator ist transaktions-/clustersicher. Sales-Channel-spezifische Ranges möglich.
