# sw-customer-imitate-customer-modal

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| customer | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onSalesChannelDomainMenuItemClick` | |
| `onCancel` | |
| `fetchSalesChannelDomains` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `modalTitle` | |
| `modalDescription` | |
| `salesChannelDomainRepository` | |
| `currentUser` | |
| `salesChannelDomainCriteria` | |
| `hasSalesChannelDomains` | |

## Examples

### Example 1
Source: `sw-customer/component/sw-customer-card/sw-customer-card.html.twig`
```twig
<sw-customer-imitate-customer-modal
    v-if="showImitateCustomerModal"
    :customer="customer"
    @modal-close="onCloseImitateCustomerModal"
/>
{% endblock %}

{% block sw_customer_card_action_customer_impersonation %}
<mt-button
    v-tooltip="{
        message: customerImitationWarning,
        disabled: canUseCustomerImitation,
        showOnDisabledElements: true
    }"
    :disabled="!canUseCustomerImitation"
```
