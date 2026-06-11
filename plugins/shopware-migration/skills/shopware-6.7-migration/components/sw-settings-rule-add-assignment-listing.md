# sw-settings-rule-add-assignment-listing

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| ruleId | `any` | — | yes |  |
| entityContext | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| select-item | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onSelectItem` | |
| `isNotAssigned` | |
| `paginate` | |
| `doSearch` | |
| `shippingTaxTypeLabel` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `criteria` | |
| `shippingCostTaxOptions` | |

## Examples

### Example 1
Source: `sw-settings-rule/component/sw-settings-rule-add-assignment-modal/sw-settings-rule-add-assignment-modal.html.twig`
```twig
<sw-settings-rule-add-assignment-listing
    v-else
    class="sw-settings-rule-detail-assignments__entity-listing"
    :entity-context="entityContext"
    :rule-id="rule.id"
    @select-item="onSelect"
/>
{% endblock %}

{% block sw_settings_rule_add_assignment_modal_footer %}
<template #modal-footer>

    {% block sw_settings_rule_add_assignment_modal_cancel %}
    <mt-button
        class="sw-settings-rule-add-assignment-modal__cancel-button"
```
