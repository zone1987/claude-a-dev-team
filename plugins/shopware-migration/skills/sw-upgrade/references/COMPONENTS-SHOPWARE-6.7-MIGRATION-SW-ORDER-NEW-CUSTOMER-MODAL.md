# sw-order-new-customer-modal

> Shopware Administration component.

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| on-select-existing-customer | — | |
| close | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onSave` | |
| `saveCustomer` | |
| `onChangeSalesChannel` | |
| `onClose` | |
| `createErrorMessageForCompanyField` | |
| `validateEmail` | |
| `loadLanguage` | |
| `getDefaultSalutationId` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `swOrderNewCustomerDetailError` | |
| `swOrderNewCustomerAddressError` | |
| `customerRepository` | |
| `addressRepository` | |
| `shippingAddress` | |
| `billingAddress` | |
| `isSameBilling` | |
| `validCompanyField` | |
| `languageRepository` | |
| `languageCriteria` | |
| `languageId` | |
| `salutationRepository` | |
| `salutationCriteria` | |

## Examples

### Example 1
Source: `sw-order/component/sw-order-create-details-header/sw-order-create-details-header.html.twig`
```twig
<sw-order-new-customer-modal
    v-if="showNewCustomerModal"
    @close="onCloseNewCustomerModal"
    @on-select-existing-customer="onSelectExistingCustomer"
/>
{% endblock %}

{% block sw_order_create_details_header_profile %}
<sw-container
    class="sw-order-user-card__container"
    columns="80px 1fr max-content"
    gap="0 24px"
>
    {% block sw_order_create_details_header_profile_avatar %}
    <sw-avatar
```

### Example 2
Source: `sw-order/component/sw-order-customer-grid/sw-order-customer-grid.html.twig`
```twig
<sw-order-new-customer-modal
    v-if="showNewCustomerModal"
    @on-select-existing-customer="onAddNewCustomer"
    @close="showNewCustomerModal = false"
/>
{% endblock %}

{% block sw_order_customer_grid_sales_channel_select_modal %}
<sw-modal
    v-if="showSalesChannelSelectModal"
    class="sw-order-customer-grid__sales-channel-selection-modal"
    :title="$tc('sw-order.initialModal.customerGrid.titleSelectSalesChannel')"
    @modal-close="onCloseSalesChannelSelectModal"
>
    <template #default>
```
