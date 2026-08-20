# Shopware 6 — NumberRange

Use the `NumberRangeValueGenerator` for sequential, configurable numbers (e.g. your own document numbers) —
never count up yourself (it solves race conditions and is cluster-safe).

```php
$number = $this->valueGenerator->getValue(
    'ff_content_export',   // technical name of the NumberRange type
    $context,
    $salesChannelId        // optional, per sales channel
);
```

Create your own number range type via a migration/fixture in `number_range_type` + `number_range`
(pattern e.g. `EXP{n}`). The generator is transaction- and cluster-safe. Sales-channel-specific ranges are possible.
