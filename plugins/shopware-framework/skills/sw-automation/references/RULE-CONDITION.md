# Shopware 6 — Rule condition (admin)

Every custom rule (`sw-custom-rule`) needs an admin component that renders the condition in the Rule Builder.

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

Register the condition with the `ruleConditionDataProviderService` (name = `RULE_NAME` of the PHP rule, scopes,
component). The `sw-condition-base` mixin supplies `condition`/`operators`. Tie the fields to the PHP `getConstraints()`.
Reuse the operator sets (`number`/`string`/`bool`/`multiStore`).
