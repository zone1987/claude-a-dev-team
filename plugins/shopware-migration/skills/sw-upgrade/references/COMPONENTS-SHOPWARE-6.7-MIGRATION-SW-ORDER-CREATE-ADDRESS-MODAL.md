# sw-order-create-address-modal

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| customer | `any` | — | yes |  |
| address | `any` | — | yes |  |
| addAddressModalTitle | `any` | — | yes |  |
| editAddressModalTitle | `any` | — | yes |  |
| cart | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| set-customer-address | — | |
| close-modal | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `getCustomerAddresses` | |
| `onNewActiveItem` | |
| `isCurrentSelected` | |
| `onSearchAddress` | |
| `onSelectExistingAddress` | |
| `findSelectedAddress` | |
| `updateOrderContext` | |
| `saveCurrentCustomer` | |
| `saveCurrentAddress` | |
| `closeModal` | |
| `onCancel` | |
| `onSave` | |
| `onCloseAddressModal` | |
| `onAddNewAddress` | |
| `onEditAddress` | |
| `onChangeDefaultAddress` | |
| `onSubmitAddressForm` | |
| `getAddressFormModalTitle` | |
| `createNewCustomerAddress` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `addressCriteria` | |
| `customerRepository` | |
| `addressRepository` | |
| `isValidCompanyField` | |

## Examples

### Example 1
Source: `sw-order/view/sw-order-create-base/sw-order-create-base.html.twig`
```twig
<sw-order-create-address-modal
    v-if="showAddressModal"
    :address="address"
    :add-address-modal-title="addAddressModalTitle"
    :edit-address-modal-title="editAddressModalTitle"
    :customer="customer"
    :cart="cart"
    @close-modal="closeModal"
    @set-customer-address="setCustomerAddress"
/>
{% endblock %}

{% block sw_order_create_promotion_modal %}
<sw-order-create-promotion-modal
    v-if="showPromotionModal"
```
