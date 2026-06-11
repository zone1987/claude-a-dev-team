# sw-order-customer-address-select

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| customer | `any` | — | yes |  |
| value | `any` | — | yes |  |
| sameAddressLabel | `any` | `''` | no |  |
| sameAddressValue | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `getSelectionLabel` | |
| `getCustomerAddress` | |
| `getCustomerAddresses` | |
| `searchAddress` | |
| `searchAddressResults` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `addressId` | |
| `isSameAddress` | |
| `addressRepository` | |
| `addressCriteria` | |

## Examples

### Example 1
Source: `sw-order/component/sw-order-create-options/sw-order-create-options.html.twig`
```twig
    <sw-order-customer-address-select
        v-model:value="context.billingAddressId"
        class="sw-order-create-options__billing-address"
        :label="$tc('sw-order.createBase.labelBillingAddress')"
        :placeholder="$tc('sw-order.createBase.placeholderBillingAddress')"
        :same-address-value="context.shippingAddressId"
        :customer="customer"
    />
    {% endblock %}

    {% block sw_order_create_options_order_currency %}
    <sw-entity-single-select
        v-model:value="context.currencyId"
        class="sw-order-create-options__currency-select"
        entity="currency"
```

### Example 2
Source: `sw-order/component/sw-order-create-options/sw-order-create-options.html.twig`
```twig
        <sw-order-customer-address-select
            v-model:value="context.shippingAddressId"
            class="sw-order-create-options__shipping-address"
            :label="$tc('sw-order.createBase.labelShippingAddress')"
            :placeholder="$tc('sw-order.createBase.placeholderShippingAddress')"
            :same-address-label="$tc('sw-order.initialModal.options.textSameAsBillingAddress')"
            :same-address-value="context.billingAddressId"
            :customer="customer"
            :disabled="isSameAsBillingAddress"
        />
        {% endblock %}
    </sw-container>
    {% endblock %}
    {% endblock %}
</div>
```

### Example 3
Source: `sw-order/view/sw-order-create-details/sw-order-create-details.html.twig`
```twig
<sw-order-customer-address-select
    v-model:value="context.billingAddressId"
    :label="$tc('sw-order.createBase.labelBillingAddress')"
    :placeholder="$tc('sw-order.createBase.placeholderBillingAddress')"
    :same-address-value="context.shippingAddressId"
    :customer="customer"
/>

<sw-entity-single-select
    v-model:value="context.paymentMethodId"
    entity="payment_method"
    label-property="distinguishableName"
    class="sw_order_create-details__payment-method"
    :criteria="paymentMethodCriteria"
    :label="$tc('sw-order.createBase.labelPaymentMethod')"
```

### Example 4
Source: `sw-order/view/sw-order-create-details/sw-order-create-details.html.twig`
```twig
<sw-order-customer-address-select
    v-model:value="context.shippingAddressId"
    :label="$tc('sw-order.createBase.labelShippingAddress')"
    :placeholder="$tc('sw-order.createBase.placeholderShippingAddress')"
    :same-address-label="$tc('sw-order.initialModal.options.textSameAsBillingAddress')"
    :same-address-value="context.billingAddressId"
    :customer="customer"
/>

<sw-entity-single-select
    v-model:value="context.shippingMethodId"
    show-clearable-button
    class="sw_order_create-details__shipping"
    entity="shipping_method"
    :criteria="shippingMethodCriteria"
```
