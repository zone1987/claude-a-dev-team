# Shopware 6 — Custom Rule (Rule Builder)

Eine Rule kapselt eine Bedingung, die der Rule Builder (Versand/Zahlung/Promotion/…) auswertet.

```php
class FfMinAgeRule extends Rule
{
    public const RULE_NAME = 'ffMinAge';
    protected int $minAge = 18;

    public function match(RuleScope $scope): bool
    {
        if (!$scope instanceof CartRuleScope) { return false; }
        return /* Kundenalter */ >= $this->minAge;
    }
    public function getConstraints(): array { return ['minAge' => [new NotBlank(), new Type('int')]]; }
    public function getName(): string { return self::RULE_NAME; }
}
```

Registrierung via `shopware.rule.definition`-Tag. Der `RuleScope` liefert Kontext (Cart/LineItem/Checkout). Daten,
die `match()` braucht, vorab über `CartRuleScope`/Data-Collector bereitstellen (ADR „preparing data for rule evaluation").
Admin-UI: zugehörige Komponente registrieren (`shopware-admin`). Bedingungsfelder: `sw-rule-condition`.

→ Rule-Builder-Details: [CUSTOM-RULE-RULES.md](CUSTOM-RULE-RULES.md) · Beispiel: [examples/CustomRule.php](examples/CustomRule.php)
