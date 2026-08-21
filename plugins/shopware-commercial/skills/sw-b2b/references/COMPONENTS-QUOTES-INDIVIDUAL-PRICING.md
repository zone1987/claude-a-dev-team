# Individual Pricing — Developer reference

**Available as of Shopware 6.7.8.0**

## Contents

- [Concept](#concept)
- [Price types (actionType)](#price-types-actiontype)
- [Entities](#entities)
- [Price workflow (runtime)](#price-workflow-runtime)
- [Caching strategy](#caching-strategy)
- [HTTP cache behavior](#http-cache-behavior)
- [Known limitations](#known-limitations)
- [Extension points](#extension-points)
- [Prerequisites](#prerequisites)

## Concept

Individual Pricing enables merchants to define catalog-wide discounts and special prices for
B2B customers — based on companies, organizational units, employees or tags.

## Price types (actionType)

| Type             | Description                                   |
|------------------|-----------------------------------------------|
| `by_percent`     | Percentage deduction (e.g. 10% discount)      |
| `by_fixed`       | Fixed deduction (e.g. 5 EUR discount)         |
| `to_fixed`       | Fixed price (e.g. exactly 99.99 EUR)          |
| `volume_pricing` | Tiered prices by quantity                     |

## Entities

```sql
b2b_components_individual_pricing:
  id, active, show_strike_through, name, target (companies|tags),
  priority (INT), apply_to_all_products (BOOL), product_stream_id (FK),
  use_validity_range (BOOL), valid_from, valid_until,
  description, action_type, action_amount,
  created_by_id, updated_by_id, custom_fields

b2b_components_individual_pricing_tier:
  id, individual_pricing_id (FK), qty_from (INT), qty_to (INT, NULL = unlimited), price (JSON)

b2b_components_individual_pricing_company_assignment:
  id, individual_pricing_id (FK), customer_id (FK),
  scope (whole_company|all_org_units|specific_units), organization_unit_ids (JSON)

b2b_components_individual_pricing_computed_cache:
  id, individual_pricing_id (FK), product_id (FK, NULL = all products)

b2b_components_individual_pricing_tag:
  individual_pricing_id (FK), tag_id (FK)
```

## Price workflow (runtime)

**Phase 1: context creation** — `AudienceContextResolver` determines the customer type
(business partner, employee, tag-based customer)

**Phase 2: product loading** — `IndividualPricingProductSubscriber` is triggered on the product load event

**Phase 3: price resolution** — the computed cache is queried, rules are filtered by priority

**Phase 4: price application** — single prices or volume prices are applied, optionally
with a strike-through of the original price

### Prioritization logic

1. Only rules of the highest priority are evaluated
2. With several matching rules of equal priority: the rule with the lowest price wins
3. No rule matches → standard catalog price

### Overall priority hierarchy

1. Individual Pricing (highest priority, when applicable)
2. Shopware Custom Pricing
3. Product tiered prices/advanced prices
4. Rule-based prices
5. Standard list price

## Caching strategy

**Hybrid approach:**
- Specific products: pre-computed cache entries per product-rule pair (immediate lookup)
- All products: single NULL entry per rule (fast lookup + runtime calculation)

The cache is updated automatically via the message queue (asynchronously), in batches of 1,000 products.

**Note:** After creating/changing price rules with specific products:
wait until the queue has been processed before prices become visible.
Rules with "all products" take effect immediately (runtime).

## HTTP cache behavior

| Customer type                | Cacheable    | Reason                                     |
|------------------------------|--------------|--------------------------------------------|
| Tag-based                    | Yes (shared) | Same tags → same prices                    |
| Org. unit employee           | Yes (shared) | Same department → same prices              |
| Business partner             | No           | Customer-specific prices                   |
| Employee without org. unit   | No           | Individual                                 |

## Known limitations

Price filtering and sorting in product listings is based on indexed original prices.
Individual Pricing is applied **after** database queries → price sorting/filtering
can show incorrect results.

**Workaround:** price sorting and price range filtering are disabled automatically in the
storefront when Individual Pricing is active for the logged-in customer.

## Extension points

### Extension: `IndividualPricingApplyExtension`

Hook when applying the price (validation, logging, triggering external systems):

```php
class IndividualPricingLogger implements EventSubscriberInterface
{
    public static function getSubscribedEvents(): array
    {
        return [IndividualPricingApplyExtension::NAME => 'onPricingApply'];
    }

    public function onPricingApply(IndividualPricingApplyExtension $extension): void
    {
        // $extension->product, $extension->individualPricing, $extension->context
        $this->logger->info('Individual pricing applied', [
            'product_id' => $extension->product->getId(),
            'rule_id' => $extension->individualPricing->getIndividualPricingId(),
        ]);
    }
}
```

### Events

| Event                                       | Purpose                                     |
|---------------------------------------------|---------------------------------------------|
| `IndividualPricingIndexerEvent`             | React to indexing requests                  |
| `IndividualPricingLookupCriteriaEvent`      | Adjust criteria for single-product lookup   |
| `IndividualPricingLookupBatchCriteriaEvent` | Adjust criteria for batch lookup            |

### Messages (asynchronous)

| Message                                         | Purpose                                        |
|-------------------------------------------------|------------------------------------------------|
| `IndividualPricingCacheEntryUpdaterMessage`     | Rebuild cache on rule changes                  |
| `IndividualPricingBuildCacheSingleRuleMessage`  | Rebuild cache for a single rule                |

## Prerequisites

- Employee Management + Organization Unit must be installed and activated
- As of Shopware 6.7.8.0
