# sw-order-details-state-card

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| order | `any` | — | yes |  |
| title | `any` | `''` | no |  |
| entity | `any` | — | yes |  |
| stateLabel | `any` | `''` | no |  |
| isLoading | `any` | `false` | no |  |
| disabled | `any` | `false` | no |  |
| position | `any` | `''` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| show-status-history | — | |
| save-edits | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onShowStatusHistory` | |
| `getTransitionOptions` | |
| `buildTransitionOptions` | |
| `onStateSelected` | |
| `onLeaveModalClose` | |
| `onLeaveModalConfirm` | |
| `createStateChangeErrorNotification` | |
| `getLastChange` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `stateMachineStateRepository` | |
| `stateMachineHistoryRepository` | |
| `stateMachineStateCriteria` | |
| `stateMachineHistoryCriteria` | |
| `entityName` | |
| `stateName` | |
| `stateSelectBackgroundStyle` | |
| `stateTransitionMethod` | |
| `cardPosition` | |
| `lastChangeAuthorLabel` | |

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
