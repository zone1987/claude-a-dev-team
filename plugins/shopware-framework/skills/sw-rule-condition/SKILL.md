---
name: sw-rule-condition
description: >
  Die Admin-Seite einer Shopware-6 Rule: Bedingungs-Komponente registrieren (sw-condition), Operatoren, Felder an
  die Rule-Constraints binden, Config-Component. Trigger: "Rule condition component", "sw-condition", "Rule Builder UI",
  "Operatoren rule", "condition-store rule", "Bedingungsfeld admin". Shopware 6.7.
---

# Shopware 6 — Rule-Bedingung (Admin)

Jede Custom Rule (`sw-custom-rule`) braucht eine Admin-Komponente, die die Bedingung im Rule Builder darstellt.

```js
Shopware.Component.register('sw-condition-ff-min-age', {
    template,
    mixins: ['sw-condition-base'],
    computed: {
        operators() { return this.conditionDataProviderService.getOperatorSet('number'); },
        minAge: { get() { return this.condition.value?.minAge; }, set(v) { /* set value */ } },
    },
});
```

Registrierung der Bedingung beim `ruleConditionDataProviderService` (Name = `RULE_NAME` der PHP-Rule, Scopes,
Komponente). `sw-condition-base`-Mixin liefert `condition`/`operators`. Felder an die PHP-`getConstraints()` koppeln.
Operator-Sets (`number`/`string`/`bool`/`multiStore`) wiederverwenden.
