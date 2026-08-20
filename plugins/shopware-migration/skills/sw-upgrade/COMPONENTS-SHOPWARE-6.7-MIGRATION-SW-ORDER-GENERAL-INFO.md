# sw-order-general-info

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| order | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| save-edits | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `getLiveOrder` | |
| `onTagAdd` | |
| `onTagRemove` | |
| `getAllStates` | |
| `buildTransitionOptions` | |
| `backgroundStyle` | |
| `getTransitionOptions` | |
| `onStateSelected` | |
| `onLeaveModalClose` | |
| `onLeaveModalConfirm` | |
| `loadHistory` | |
| `createStateChangeErrorNotification` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `isLoading` | |
| `savedSuccessful` | |
| `lastChangedUser` | |
| `lastChangedDateTime` | |
| `lastChangedByCriteria` | |
| `orderRepository` | |
| `orderTagRepository` | |
| `stateMachineStateRepository` | |
| `stateMachineStateCriteria` | |
| `transaction` | |
| `delivery` | |
| `currencyFilter` | |
| `dateFilter` | |
| `emailIdnFilter` | |

## Examples

### Example 1
Source: `sw-order/view/sw-order-detail-general/sw-order-detail-general.html.twig`
```twig
    <sw-order-general-info
        ref="swOrderGeneralInfo"
        :order="order"
        @save-edits="onSaveEdits"
    />
    {% endblock %}
</mt-card>
{% endblock %}

{% block sw_order_detail_general_line_items_card %}
<sw-extension-component-section
    position-identifier="sw-order-detail-base-line-items__before"
/>

<mt-card
```
