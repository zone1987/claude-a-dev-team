# sw-select-rule-create

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| ruleId | `any` | `null` | no |  |
| rules | `any` | `null` | no |  |
| ruleFilter | `any` | — | no |  |
| ruleAwareGroupKey | `any` | `null` | no |  |
| restrictedRuleIds | `any` | — | no |  |
| restrictedRuleIdsTooltipLabel | `any` | — | no |  |
| size | `any` | `'default'` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| result-item | — | |
| result-label-property | — | |
| rule-modal | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| save-rule | — | |
| dismiss-rule | — | |
| update:rules | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onSaveRule` | |
| `onSelectRule` | |
| `onUpdateCollection` | |
| `openCreateRuleModal` | |
| `onCloseRuleModal` | |
| `onRuleSelectInput` | |
| `isRuleRestricted` | |
| `getAdvancedSelectionParameters` | |
| `tooltipConfig` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `collection` | |

## Examples

### Example 1
Source: `sw-settings-tax/page/sw-settings-tax-provider-detail/sw-settings-tax-provider-detail.html.twig`
```twig
                    <sw-select-rule-create
                        v-if="!isLoading"
                        class="sw-settings-tax-tax-provider-detail__field-availability-rule"
                        :disabled="!acl.can('tax.editor') || undefined"
                        :rule-id="taxProvider.availabilityRuleId"
                        :rule-filter="ruleFilter"
                        :placeholder="$tc('sw-settings-tax.taxProviderDetail.placeholderAvailabilityRule')"
                        rule-aware-group-key="taxProvider"
                        @save-rule="onSaveRule"
                        @dismiss-rule="onDismissRule"
                    />
                </mt-card>

                <sw-extension-component-section
                    v-if="hasIdentifier"
```

### Example 2
Source: `sw-promotion-v2/component/sw-promotion-v2-cart-condition-form/sw-promotion-v2-cart-condition-form.html.twig`
```twig
<sw-select-rule-create
    v-if="promotion"
    v-model:rules="promotion.cartRules"
    class="sw-promotion-v2-cart-condition-form__rule-select-cart"
    :local-mode="promotion.isNew()"
    :rule-filter="ruleFilter"
    :label="$tc('sw-promotion-v2.detail.conditions.preConditions.labelCartConditionSelect')"
    :placeholder="$tc('sw-promotion-v2.detail.conditions.preConditions.placeholderCartConditionSelect')"
    :rule-scope="['checkout', 'global', 'lineItem']"
    rule-aware-group-key="cartPromotions"
    :disabled="isEditingDisabled"
/>
{% endblock %}

{% block sw_promotion_v2_cart_condition_form_use_setgroups_field %}
```

### Example 3
Source: `sw-promotion-v2/component/sw-promotion-v2-cart-condition-form/sw-promotion-v2-cart-condition-form.html.twig`
```twig
        <sw-select-rule-create
            v-model:rules="group.setGroupRules"
            class="sw-promotion-v2-cart-condition-form__setgroup-rules"
            :label="$tc('sw-promotion-v2.detail.conditions.setgroups.labelRules')"
            :placeholder="$tc('sw-promotion-v2.detail.conditions.setgroups.placeholder')"
            :rule-filter="ruleFilter"
            :rule-scope="['checkout', 'global', 'lineItem']"
            :disabled="isEditingDisabled"
            rule-aware-group-key="promotionSetGroups"
        />
        {% endblock %}

    </sw-container>
</mt-card>
{% endblock %}
```

### Example 4
Source: `sw-promotion-v2/component/discount/sw-promotion-v2-settings-rule-selection/sw-promotion-v2-settings-rule-selection.html.twig`
```twig
    <sw-select-rule-create
        v-model:rules="discount.discountRules"
        :rule-filter="ruleCriteria"
        :rule-scope="['cart']"
        local-mode
        :label="$tc('sw-promotion-v2.detail.discounts.settings.ruleSelection.labelSelection')"
        :placeholder="$tc('sw-promotion-v2.detail.discounts.settings.ruleSelection.placeholderSelection')"
        :disabled="!acl.can('promotion.editor')"
    />
    {% endblock %}

</div>
{% endblock %}

```

### Example 5
Source: `sw-promotion-v2/component/discount/sw-promotion-v2-settings-trigger/sw-promotion-v2-settings-trigger.html.twig`
```twig
        <sw-select-rule-create
            v-model:rules="discount.discountRules"
            local-mode
            class="sw-promotion-v2-settings-trigger-settings__rule-selection"
            :rule-filter="ruleCriteria"
            :rule-scope="['cart']"
            :label="$tc('sw-promotion-v2.detail.discounts.settings.ruleSelection.labelSelection')"
            :placeholder="$tc('sw-promotion-v2.detail.discounts.settings.ruleSelection.placeholderSelection')"
            :disabled="!acl.can('promotion.editor')"
        />
        {% endblock %}

    </sw-container>
    {% endblock %}

```
