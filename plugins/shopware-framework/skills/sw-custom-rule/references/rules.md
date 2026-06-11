# Custom Rules

## Overview

Rules define conditions for the Rule Builder. They determine when promotions apply, shipping methods are available, or flow actions trigger. Each rule implements `match()` and `getConstraints()`.

## Rule Class

```php
<?php declare(strict_types=1);

namespace FfContentPlus\Core\Rule;

use Shopware\Core\Checkout\CheckoutRuleScope;
use Shopware\Core\Framework\Log\Package;
use Shopware\Core\Framework\Rule\Rule;
use Shopware\Core\Framework\Rule\RuleConfig;
use Shopware\Core\Framework\Rule\RuleConstraints;
use Shopware\Core\Framework\Rule\RuleScope;

/**
 * @class MinCartQuantityRule
 * @package FfContentPlus\Core\Rule
 */
#[Package('custom-plugins')]
class MinCartQuantityRule extends Rule
{
    /**
     * @var string
     */
    final public const RULE_NAME = 'ff_content_plus_min_cart_quantity';

    /**
     * @param int $minQuantity
     * @param string $operator
     */
    public function __construct(
        protected int $minQuantity = 1,
        protected string $operator = self::OPERATOR_GTE,
    ) {
        parent::__construct();
    }

    /**
     * @param RuleScope $scope
     * @return bool
     */
    public function match(RuleScope $scope): bool
    {
        if (!$scope instanceof CheckoutRuleScope) {
            return false;
        }

        $cart = $scope->getCart();
        $totalQuantity = $cart->getLineItems()->count();

        return match ($this->operator) {
            self::OPERATOR_GTE => $totalQuantity >= $this->minQuantity,
            self::OPERATOR_LTE => $totalQuantity <= $this->minQuantity,
            self::OPERATOR_GT => $totalQuantity > $this->minQuantity,
            self::OPERATOR_LT => $totalQuantity < $this->minQuantity,
            self::OPERATOR_EQ => $totalQuantity === $this->minQuantity,
            self::OPERATOR_NEQ => $totalQuantity !== $this->minQuantity,
            default => false,
        };
    }

    /**
     * @return array<string, array<Constraint>>
     */
    public function getConstraints(): array
    {
        return [
            'minQuantity' => RuleConstraints::int(),
            'operator' => RuleConstraints::numericOperators(),
        ];
    }

    /**
     * @return RuleConfig
     */
    public function getConfig(): RuleConfig
    {
        return (new RuleConfig())
            ->operatorSet(RuleConfig::OPERATOR_SET_NUMBER)
            ->intField('minQuantity');
    }
}
```

## Service Registration

```xml
<service id="FfContentPlus\Core\Rule\MinCartQuantityRule">
    <tag name="shopware.rule.definition"/>
</service>
```

## Rule Scopes

| Scope | Available Data | Use Case |
|-------|---------------|----------|
| `CheckoutRuleScope` | Cart, SalesChannelContext | Cart-based rules |
| `LineItemScope` | LineItem, SalesChannelContext | Per-item rules |
| `FlowRuleScope` | Order, Context | Flow Builder rules |
| `CartRuleScope` | Cart, SalesChannelContext | Cart validation |

## RuleConstraints Helpers

```php
RuleConstraints::bool()                // Boolean validation
RuleConstraints::int()                 // Integer validation
RuleConstraints::float()               // Float validation
RuleConstraints::string()              // String validation
RuleConstraints::numericOperators()    // >=, <=, >, <, =, !=
RuleConstraints::stringOperators()     // =, !=, empty
RuleConstraints::uuids()               // Array of UUIDs
```

## RuleConfig Helpers (Admin UI)

```php
$config = (new RuleConfig())
    ->operatorSet(RuleConfig::OPERATOR_SET_NUMBER)  // Shows operator dropdown
    ->intField('quantity')                           // Integer input
    ->stringField('code')                            // Text input
    ->booleanField('active')                         // Toggle
    ->selectField('status', [                        // Select dropdown
        ['value' => 'open', 'label' => ['en-GB' => 'Open']],
        ['value' => 'closed', 'label' => ['en-GB' => 'Closed']],
    ])
    ->entitySelectField('productIds', 'product', true); // Entity multi-select
```

## Simple Boolean Rule

```php
class IsNewCustomerRule extends Rule
{
    final public const RULE_NAME = 'ff_content_plus_is_new_customer';

    public function __construct(
        protected bool $isNew = true,
    ) {
        parent::__construct();
    }

    public function match(RuleScope $scope): bool
    {
        if (!$scope instanceof CheckoutRuleScope) {
            return false;
        }

        $customer = $scope->getSalesChannelContext()->getCustomer();
        if (!$customer) {
            return false;
        }

        $isNew = $customer->getCreatedAt() > new \DateTimeImmutable('-30 days');

        return $this->isNew === $isNew;
    }

    public function getConstraints(): array
    {
        return [
            'isNew' => RuleConstraints::bool(true),
        ];
    }

    public function getConfig(): RuleConfig
    {
        return (new RuleConfig())->booleanField('isNew');
    }
}
```

## Naming Convention

Rule names: `{vendor_prefix}_{plugin_snake}_{rule_description}`

Examples:
- `ff_content_plus_min_cart_quantity`
- `ff_content_plus_is_new_customer`
- `adt_product_export_has_external_id`
