# sw-order-create-details-body

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| customer | `any` | — | no |  |
| isCustomerActive | `any` | `false` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| on-edit-billing-address | — | |
| on-edit-shipping-address | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onEditBillingAddress` | |
| `onEditShippingAddress` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `email` | |
| `phoneNumber` | |
| `billingAddress` | |
| `shippingAddress` | |
| `isAddressIdentical` | |

## Examples

### Example 1
Source: `sw-order/view/sw-order-create-base/sw-order-create-base.html.twig`
```twig
                <sw-order-create-details-body
                    :customer="customer"
                    :is-customer-active="isCustomerActive"
                    @on-edit-billing-address="onEditBillingAddress"
                    @on-edit-shipping-address="onEditShippingAddress"
                />
                {% endblock %}
            </sw-card-section>
            <sw-card-section
                secondary
                divider="top"
            >
                {% block sw_order_create_details_footer %}
                <sw-order-create-details-footer
                    :customer="customer"
```
