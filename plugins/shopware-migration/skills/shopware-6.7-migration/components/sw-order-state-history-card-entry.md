# sw-order-state-history-card-entry

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| history | `any` | — | yes |  |
| transitionOptions | `any` | — | yes |  |
| stateMachineName | `any` | — | yes |  |
| title | `any` | `''` | no |  |
| disabled | `any` | `false` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `userDisplayName` | |
| `integrationDisplayName` | |
| `getDisplayName` | |
| `getIconFromState` | |
| `getIconColorFromState` | |
| `getBackgroundColorFromState` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `dateFilter` | |

## Examples

### Example 1
Source: `sw-order/component/sw-order-state-history-card/sw-order-state-history-card.html.twig`
```twig
<sw-order-state-history-card-entry
    v-if="transaction"
    v-tooltip="{
        message: $tc('sw-privileges.tooltip.warning'),
        disabled: acl.can('order.editor'),
        showOnDisabledElements: true
    }"
    class="sw-order-state-history-card__payment-state"
    :disabled="!acl.can('order.editor') || undefined"
    :history="transactionHistory"
    :transition-options="transactionOptions"
    state-machine-name="order_transaction.state"
    :title="$tc('sw-order.stateCard.headlineTransactionState')"
    @state-select="onTransactionStateSelected"
/>
```

### Example 2
Source: `sw-order/component/sw-order-state-history-card/sw-order-state-history-card.html.twig`
```twig
        <sw-order-state-history-card-entry
            v-tooltip="{
                message: $tc('sw-privileges.tooltip.warning'),
                disabled: acl.can('order.editor'),
                showOnDisabledElements: true
            }"
            class="sw-order-state-history-card__order-state"
            :history="orderHistory"
            :disabled="!acl.can('order.editor') || undefined"
            :transition-options="orderOptions"
            state-machine-name="order.state"
            :title="$tc('sw-order.stateCard.headlineOrderState')"
            @state-select="onOrderStateSelected"
        />
        {% endblock %}
```
