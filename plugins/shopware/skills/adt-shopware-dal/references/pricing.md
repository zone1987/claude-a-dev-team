# Pricing

## Price (extends Struct)

**Constructor:**
```php
(
    string $currencyId,
    float $net,
    float $gross,
    bool $linked,
    ?Price $listPrice = null,
    ?array $percentage = null,
    ?Price $regulationPrice = null
)
```

- `$linked`: Whether net/gross are linked (changing one auto-calculates the other in admin)
- `$listPrice`: Original/crossed-out price (recursive Price struct)
- `$regulationPrice`: EU Omnibus Directive compliance price
- `add(self $price)`: Sums both gross and net

## PriceCollection (extends Collection<Price>)

Keyed by `currencyId` - each currency has exactly one price entry.

**Key method:** `getCurrencyPrice(string $currencyId, bool $fallback = true): ?Price`

Falls back to `Defaults::CURRENCY` (system default) if specific currency not found and `$fallback = true`. This is how multi-currency pricing works.

## CashRoundingConfig (extends Struct)

```php
(int $decimals, float $interval, bool $roundForNet)
```

- `$interval`: Rounding interval (0.01 for cent-precision, 0.05 for Swiss 5-Rappen)
- `$roundForNet`: Whether rounding applies to net prices

## PriceRuleEntity (extends Entity)

Properties: `$ruleId` (string), `$price` (PriceCollection). Represents a rule-specific price that applies only when a business rule matches.
