# sw-promotion-v2-sales-channel-select

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| promotion | `any` | `null` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `getChangeset` | |
| `getAssociationBySalesChannelId` | |
| `handleLocalMode` | |
| `handleWithRepository` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `salesChannelRepository` | |
| `promotionSalesChannelRepository` | |
| `salesChannelIds` | |
| `salesChannelCriteria` | |

## Examples

### Example 1
Source: `sw-promotion-v2/view/sw-promotion-v2-conditions/sw-promotion-v2-conditions.html.twig`
```twig
<sw-promotion-v2-sales-channel-select
    class="sw-promotion-v2-conditions__sales-channel-selection"
    :promotion="promotion"
    :entity-collection="promotion.salesChannels"
    :disabled="!acl.can('promotion.editor')"
    :label="$tc('sw-promotion-v2.detail.conditions.preConditions.labelPromotionSalesChannel')"
    :placeholder="$tc('sw-promotion-v2.detail.conditions.preConditions.labelPromotionSalesChannel')"
/>
{% endblock %}

{% block sw_promotion_v2_conditions_pre_conditions_prevent_combination %}

<mt-switch
    v-model="promotion.preventCombination"
    class="sw-promotion-v2-conditions__prevent-combination"
```
