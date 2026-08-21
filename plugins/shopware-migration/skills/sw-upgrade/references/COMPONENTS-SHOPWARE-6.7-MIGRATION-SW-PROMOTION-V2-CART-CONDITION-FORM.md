# sw-promotion-v2-cart-condition-form

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| promotion | `any` | `null` | no |  |
| restrictedRules | `any` | — | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `addSetGroup` | |
| `duplicateSetGroup` | |
| `deleteSetGroup` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `promotionGroupRepository` | |
| `ruleFilter` | |
| `packagers` | |
| `sorters` | |
| `isEditingDisabled` | |
| `packagerOptions` | |
| `sorterOptions` | |
| `setGroupCriteria` | |

## Examples

### Example 1
Source: `sw-promotion-v2/view/sw-promotion-v2-conditions/sw-promotion-v2-conditions.html.twig`
```twig
        <sw-promotion-v2-cart-condition-form
            :promotion="promotion"
            :restricted-rules="cartRestrictedRules"
        />
        {% endblock %}

        {% block sw_promotion_v2_rule_conditions_rule_select_order_conditions %}
        <sw-select-rule-create
            v-if="promotion"
            v-model:rules="promotion.orderRules"
            class="sw-promotion-v2-conditions__rule-select-order-conditions"
            :local-mode="promotion.isNew()"
            :label="$tc('sw-promotion-v2.detail.conditions.preConditions.labelOrderConditionSelect')"
            :placeholder="$tc('sw-promotion-v2.detail.conditions.preConditions.placeholderOrderConditionSelect')"
            :rule-filter="orderConditionsFilter"
```
