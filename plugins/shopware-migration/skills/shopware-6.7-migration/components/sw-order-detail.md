# sw-order-detail

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| orderId | `any` | `null` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `beforeDestroyComponent` | |
| `updateCreatedById` | |
| `onChangeLanguage` | |
| `saveEditsFinish` | |
| `onStartEditing` | |
| `onSaveEdits` | |
| `handleOrderAddressUpdate` | |
| `onCancelEditing` | |
| `onSaveAndRecalculate` | |
| `onRecalculateAndReload` | |
| `onSaveAndReload` | |
| `saveAndReload` | |
| `onUpdateLoading` | |
| `onUpdateEditing` | |
| `onError` | |
| `onLeaveModalClose` | |
| `onLeaveModalConfirm` | |
| `reloadEntityData` | |
| `createNewVersionId` | |
| `updateOrderAddresses` | |
| `updateEditing` | |
| `convertMissingProductLineItems` | |
| `handleCartErrors` | |
| `askAndSaveEdits` | |
| `onAskAndSaveEditsConfirm` | |
| `onAskAndSaveEditsCancel` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `order` | |
| `versionContext` | |
| `orderAddressIds` | |
| `editing` | |
| `loading` | |
| `isLoading` | |
| `isSaveSuccessful` | |
| `orderIdentifier` | |
| `orderChanges` | |
| `showTabs` | |
| `showWarningTabStyle` | |
| `isOrderEditing` | |
| `orderRepository` | |
| `automaticPromotions` | |
| `deliveryDiscounts` | |
| `orderCriteria` | |
| `convertedProductLineItems` | |

## Examples

### Example 1
Source: `sw-order/view/sw-order-detail-details/sw-order-detail-details.html.twig`
```twig
<sw-order-details-state-card
    v-if="transaction"
    position="transaction"
    :title="$tc('sw-order.detailsTab.labelTransactionCard')"
    :order="order"
    :entity="transaction"
    :state-label="$tc('sw-order.stateCard.headlineTransactionState')"
    :disabled="!acl.can('order.editor') || undefined"
    @show-status-history="showStateHistoryModal = true"
    @save-edits="onSaveEdits"
>

    {% block sw_order_detail_details_payment_billing_address %}
    <sw-order-address-selection
        class="sw-order-detail-details__billing-address"
```

### Example 2
Source: `sw-order/view/sw-order-detail-details/sw-order-detail-details.html.twig`
```twig
<sw-order-details-state-card
    v-if="delivery"
    position="delivery"
    :title="$tc('sw-order.detailsTab.labelDeliveryCard')"
    :order="order"
    :entity="delivery"
    :state-label="$tc('sw-order.stateCard.headlineDeliveryState')"
    :disabled="!acl.can('order.editor') || undefined"
    @show-status-history="showStateHistoryModal = true"
    @save-edits="onSaveEdits"
>

    {% block sw_order_detail_details_shipping_address %}
    <sw-order-address-selection
        class="sw-order-detail-details__shipping-address"
```
