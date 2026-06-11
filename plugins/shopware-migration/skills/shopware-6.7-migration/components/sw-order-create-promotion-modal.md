# sw-order-create-promotion-modal

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| currency | `any` | — | yes |  |
| salesChannelId | `any` | `null` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| close | — | |
| save | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onCancel` | |
| `onSave` | |
| `disableAutomaticPromotions` | |
| `getDescription` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `cart` | |
| `cartAutomaticPromotionItems` | |
| `hasNoAutomaticPromotions` | |

## Examples

### Example 1
Source: `sw-order/view/sw-order-create-details/sw-order-create-details.html.twig`
```twig
<sw-order-create-promotion-modal
    v-if="showPromotionModal"
    :is-loading="isLoading"
    :currency="currency"
    :sales-channel-id="salesChannelId"
    @close="onClosePromotionModal"
    @save="onSavePromotionModal"
/>
{% endblock %}

{% block sw_order_create_details_payment %}
<mt-card
    class="sw-order-create-details__payment"
    position-identifier="sw-order-create-details-payment"
    :title="$tc('sw-order.createBase.detailsTab.labelTransactionCard')"
```

### Example 2
Source: `sw-order/view/sw-order-create-base/sw-order-create-base.html.twig`
```twig
<sw-order-create-promotion-modal
    v-if="showPromotionModal"
    :is-loading="isLoading"
    :currency="currency"
    :sales-channel-id="customer.salesChannelId"
    @close="onClosePromotionModal"
    @save="onSavePromotionModal"
/>
{% endblock %}

{% block sw_order_create_details %}
<mt-card
    :title="$tc('sw-order.createBase.labelDetailsCard')"
    :is-loading="isLoadingDetail"
    position-identifier="sw-order-create-base-details"
```
