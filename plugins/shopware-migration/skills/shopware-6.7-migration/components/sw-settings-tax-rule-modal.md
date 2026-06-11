# sw-settings-tax-rule-modal

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| tax | `any` | — | yes |  |
| currentRule | `any` | `null` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |

## Methods

| Method | Description |
|--------|-------------|
| `changeRuleType` | |
| `createdComponent` | |
| `onConfirm` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `taxRuleRepository` | |
| `taxRuleTypeRepository` | |
| `additionalComponent` | |
| `taxRuleTypeCriteria` | |
| `countryCriteria` | |
| `taxRuleTaxRuleTypeIdError` | |
| `taxRuleCountryIdError` | |
| `taxRuleTaxRateError` | |
| `taxRuleActiveFromError` | |

## Examples

### Example 1
Source: `sw-settings-tax/component/sw-tax-rule-card/sw-tax-rule-card.html.twig`
```twig
<sw-settings-tax-rule-modal
    v-if="showModal"
    :tax="tax"
    :current-rule="currentRule"
    @modal-close="onModalClose"
/>
{% endblock %}

{% block sw_tax_rule_card_empty_state %}
<template v-if="taxRulesEmpty || disabled">
    <div class="sw-settings-tax-rule-card__empty-state">
        {% block sw_tax_rule_card_empty_state_image %}
        <img
            :src="assetFilter('administration/administration/static/img/empty-states/settings-empty-state.svg')"
            alt=""
```
