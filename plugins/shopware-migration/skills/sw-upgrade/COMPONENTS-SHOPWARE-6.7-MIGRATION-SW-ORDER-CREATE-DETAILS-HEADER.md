# sw-order-create-details-header

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| customer | `any` | — | no |  |
| orderDate | `any` | — | yes |  |
| cartPrice | `any` | — | no |  |
| currency | `any` | — | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| on-select-existing-customer | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onSelectExistingCustomer` | |
| `onShowNewCustomerModal` | |
| `onCloseNewCustomerModal` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `customerId` | |
| `customerCriteria` | |
| `currencyFilter` | |

## Examples

### Example 1
Source: `sw-order/view/sw-order-create-base/sw-order-create-base.html.twig`
```twig
    <sw-order-create-details-header
        :customer="customer"
        :order-date="orderDate"
        :cart-price="cartPrice"
        :currency="currency"
        @on-select-existing-customer="onSelectExistingCustomer"
    />
    {% endblock %}
    {% block sw_order_create_details_body %}
    <sw-order-create-details-body
        :customer="customer"
        :is-customer-active="isCustomerActive"
        @on-edit-billing-address="onEditBillingAddress"
        @on-edit-shipping-address="onEditShippingAddress"
    />
```
