# sw-order-address-selection

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| address | `any` | — | no |  |
| label | `any` | `''` | no |  |
| addressId | `any` | `null` | no |  |
| disabled | `any` | `false` | no |  |
| type | `any` | `''` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| change-address | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onEditAddress` | |
| `onCreateNewAddress` | |
| `createNewCustomerAddress` | |
| `onSaveAddress` | |
| `isValidAddress` | |
| `onChangeDefaultAddress` | |
| `createPrefix` | |
| `onAddressChange` | |
| `getCustomer` | |
| `getCustomFieldSet` | |
| `addressLabel` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `order` | |
| `versionContext` | |
| `orderCustomer` | |
| `orderRepository` | |
| `addressRepository` | |
| `customerRepository` | |
| `customerCriteria` | |
| `customFieldSetRepository` | |
| `customFieldSetCriteria` | |
| `addressOptions` | |
| `modalTitle` | |
| `selectedAddressId` | |

## Examples

### Example 1
Source: `sw-order/view/sw-order-detail-details/sw-order-detail-details.html.twig`
```twig
    <sw-order-address-selection
        class="sw-order-detail-details__billing-address"
        type="billing"
        :address="billingAddress"
        :address-id="selectedBillingAddressId"
        :disabled="!acl.can('order.editor') || undefined"
        :label="$tc('sw-order.createBase.detailsBody.labelBillingAddress')"
        @change-address="onChangeOrderAddress"
    />
    {% endblock %}

    {% block sw_order_detail_details_payment_method_select %}
    <sw-entity-single-select
        v-model:value="transaction.paymentMethodId"
        entity="payment_method"
```

### Example 2
Source: `sw-order/view/sw-order-detail-details/sw-order-detail-details.html.twig`
```twig
<sw-order-address-selection
    class="sw-order-detail-details__shipping-address"
    type="shipping"
    :address="shippingAddress"
    :address-id="selectedShippingAddressId"
    :disabled="!acl.can('order.editor') || undefined"
    :label="$tc('sw-order.createBase.detailsBody.labelShippingAddress')"
    @change-address="onChangeOrderAddress"
/>
{% endblock %}

{% block sw_order_detail_details_shipping_method_select %}
<sw-entity-single-select
    v-model:value="delivery.shippingMethodId"
    entity="shipping_method"
```
