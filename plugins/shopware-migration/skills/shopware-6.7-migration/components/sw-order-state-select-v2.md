# sw-order-state-select-v2

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| transitionOptions | `any` | — | no |  |
| stateType | `any` | — | yes |  |
| roundedStyle | `any` | `false` | no |  |
| placeholder | `any` | `null` | no |  |
| label | `any` | `null` | no |  |
| backgroundStyle | `any` | `''` | no |  |
| disabled | `any` | `false` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| state-select | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onStateChangeClicked` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `selectStyle` | |
| `selectPlaceholder` | |
| `selectable` | |

## Examples

### Example 1
Source: `sw-order/component/sw-order-details-state-card/sw-order-details-state-card.html.twig`
```twig
<sw-order-state-select-v2
    v-tooltip="{
        message: $tc('sw-privileges.tooltip.warning'),
        disabled: acl.can('order.editor'),
        showOnDisabledElements: true
    }"
    :transition-options="stateOptions"
    :state-type="entityName"
    rounded-style
    :placeholder="entity.stateMachineState.translated.name"
    :label="stateLabel"
    :background-style="stateSelectBackgroundStyle"
    :disabled="disabled"
    :is-loading="statesLoading"
    @state-select="onStateSelected"
```

### Example 2
Source: `sw-order/component/sw-order-create-general-info/sw-order-create-general-info.html.twig`
```twig
    <sw-order-state-select-v2
        class="sw-order-create-general-info__order-state-payment"
        state-type="order_transaction"
        rounded-style
        :placeholder="$tc('sw-order.stateCard.draftPlaceholder')"
        :label="$tc('sw-order.stateCard.headlineTransactionState')"
        disabled
    />
</div>
{% endblock %}

{% block sw_order_create_general_info_order_state_delivery %}
<div class="sw-order-create-general-info__order-state">
    <sw-order-state-select-v2
        class="sw-order-create-general-info__order-state-delivery"
```

### Example 3
Source: `sw-order/component/sw-order-general-info/sw-order-general-info.html.twig`
```twig
    <sw-order-state-select-v2
        v-tooltip="{
            message: $tc('sw-privileges.tooltip.warning'),
            disabled: acl.can('order.editor'),
            showOnDisabledElements: true
        }"
        class="sw-order-general-info__order-state-payment"
        :transition-options="paymentStateOptions"
        state-type="order_transaction"
        rounded-style
        :placeholder="transaction.stateMachineState.translated.name"
        :label="$tc('sw-order.stateCard.headlineTransactionState')"
        :background-style="backgroundStyle('order_transaction')"
        :disabled="!acl.can('order.editor') || isLoading"
        @state-select="onStateSelected"
```

### Example 4
Source: `sw-order/component/sw-order-general-info/sw-order-general-info.html.twig`
```twig
        <sw-order-state-select-v2
            v-tooltip="{
                message: $tc('sw-privileges.tooltip.warning'),
                disabled: acl.can('order.editor'),
                showOnDisabledElements: true
            }"
            class="sw-order-general-info__order-state-order"
            :transition-options="orderStateOptions"
            rounded-style
            state-type="order"
            :placeholder="order.stateMachineState.translated.name"
            :label="$tc('sw-order.stateCard.headlineOrderState')"
            :background-style="backgroundStyle('order')"
            :disabled="!acl.can('order.editor') || isLoading"
            @state-select="onStateSelected"
```
