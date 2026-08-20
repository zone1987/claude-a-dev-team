# sw-customer-address-form-options

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| customer | `any` | — | yes |  |
| address | `any` | — | yes |  |
| customFieldSets | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| default-address-change | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onChangeDefaultShippingAddress` | |
| `onChangeDefaultBillingAddress` | |

## Examples

### Example 1
Source: `sw-customer/view/sw-customer-detail-addresses/sw-customer-detail-addresses.html.twig`
```twig
    <sw-customer-address-form-options
        :address="currentAddress"
        :customer="activeCustomer"
        :custom-field-sets="customerAddressCustomFieldSets"
        @default-address-change="onChangeDefaultAddress"
    />

</sw-customer-address-form>
{% endblock %}

{% block sw_customer_detail_addresses_add_modal_footer %}
<template #modal-footer>
    {% block sw_customer_detail_addresses_add_modal_cancel %}
    <mt-button
        size="small"
```

### Example 2
Source: `sw-order/component/sw-order-address-selection/sw-order-address-selection.html.twig`
```twig
    <sw-customer-address-form-options
        :address="currentAddress"
        :customer="customer"
        :custom-field-sets="customerAddressCustomFieldSets"
        @default-address-change="onChangeDefaultAddress"
    />
</sw-customer-address-form>
{% endblock %}

{% block sw_order_address_modal_actions %}
<template #modal-footer>
    {% block sw_order_address_modal_action_close %}
    <mt-button
        size="small"
        variant="secondary"
```

### Example 3
Source: `sw-order/component/sw-order-create-address-modal/sw-order-create-address-modal.html.twig`
```twig
    <sw-customer-address-form-options
        :address="currentAddress"
        :customer="activeCustomer"
        :custom-field-sets="[]"
        @default-address-change="onChangeDefaultAddress"
    />
</sw-customer-address-form>
{% endblock %}

{% block sw_order_create_address_form_modal_footer %}
<template #modal-footer>
    {% block sw_order_create_address_form_modal_cancel_button %}
    <mt-button
        size="small"
        variant="secondary"
```
