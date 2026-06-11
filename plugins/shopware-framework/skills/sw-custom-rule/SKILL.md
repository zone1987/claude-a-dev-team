---
name: sw-custom-rule
description: >
  Eigene Rule (Bedingung) für den Shopware-6 Rule Builder: Rule-Klasse (extends Rule), match(), constraints(),
  Admin-Komponente, Registrierung. Trigger: "Custom Rule", "Rule Builder eigene Bedingung", "extends Rule",
  "match() rule", "RuleConstraints", "eigene Regel shopware", "rule scope". Shopware 6.7. Scaffolder: /sw-rule.
---

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

→ Rule-Builder-Details: [references/rules.md](references/rules.md) · Beispiel: [examples/CustomRule.php](examples/CustomRule.php)
