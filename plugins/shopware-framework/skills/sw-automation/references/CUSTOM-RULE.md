# Shopware 6 — Custom Rule (Rule Builder)

A rule encapsulates a condition that the Rule Builder (shipping/payment/promotion/…) evaluates.

```php
class FfMinAgeRule extends Rule
{
    public const RULE_NAME = 'ffMinAge';
    protected int $minAge = 18;

    public function match(RuleScope $scope): bool
    {
        if (!$scope instanceof CartRuleScope) { return false; }
        return /* customer age */ >= $this->minAge;
    }
    public function getConstraints(): array { return ['minAge' => [new NotBlank(), new Type('int')]]; }
    public function getName(): string { return self::RULE_NAME; }
}
```

Registration via the `shopware.rule.definition` tag. The `RuleScope` supplies context (cart/line item/checkout). Data
that `match()` needs must be provided up front via `CartRuleScope`/a data collector (ADR "preparing data for rule evaluation").
Admin UI: register the matching component (`shopware-admin`). Condition fields: `sw-rule-condition`.

→ Rule Builder details: [CUSTOM-RULE-RULES.md](CUSTOM-RULE-RULES.md) · Example: [examples/CustomRule.php](examples/CustomRule.php)
