# sw-order-inline-field

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | `''` | no |  |
| displayValue | `any` | `''` | yes |  |
| editable | `any` | `false` | yes |  |
| required | `any` | `false` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onInput` | |

## Examples

### Example 1
Source: `sw-order/component/sw-order-user-card/sw-order-user-card.html.twig`
```twig
    <sw-order-inline-field
        v-model:value="currentOrder.orderCustomer.email"
        :display-value="currentOrder.orderCustomer.email ? currentOrder.orderCustomer.email : $tc('sw-order.detailBase.labelNoEmail')"
        required
        :editable="isEditing"
        @update:value="$emit('order-change')"
    />
</dd>
{% endblock %}

{% block sw_order_detail_base_order_overview_billing_address %}
<dt>
    {{ $tc('sw-order.detailBase.headlineBillingAddress') }}
    <mt-button
        v-if="isEditing"
```

### Example 2
Source: `sw-order/component/sw-order-user-card/sw-order-user-card.html.twig`
```twig
    <sw-order-inline-field
        v-model:value="billingAddress.phoneNumber"
        :display-value="billingAddress.phoneNumber? billingAddress.phoneNumber : $tc('sw-order.detailBase.labelNoPhoneNumber')"
        :editable="isEditing"
        class="sw-order-inline-field__truncateable"
        @update:value="$emit('order-change')"
    />
</dd>
{% endblock %}

{% block sw_order_detail_base_order_overview_shipping_address %}
<dt>
    {{ $tc('sw-order.detailBase.headlineDeliveryAddress') }}
    <mt-button
        v-show="hasDifferentBillingAndShippingAddress && isEditing"
```
