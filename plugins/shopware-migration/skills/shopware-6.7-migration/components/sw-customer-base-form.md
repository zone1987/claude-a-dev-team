# sw-customer-base-form

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| customer | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| sales-channel-change | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onSalesChannelChange` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `customerSalutationIdError` | |
| `customerFirstNameError` | |
| `customerLastNameError` | |
| `customerEmailError` | |
| `customerGroupIdError` | |
| `customerSalesChannelIdError` | |
| `customerCustomerNumberError` | |
| `customerPasswordError` | |
| `customerVatIdsError` | |
| `customerCompanyError` | |
| `customerPasswordNewError` | |
| `customerPasswordConfirmError` | |
| `salutationCriteria` | |
| `accountTypeOptions` | |
| `isBusinessAccountType` | |

## Examples

### Example 1
Source: `sw-customer/page/sw-customer-create/sw-customer-create.html.twig`
```twig
                <sw-customer-base-form
                    v-if="customer"
                    :is-loading="isLoading"
                    :customer="customer"
                    @sales-channel-change="onChangeSalesChannel"
                />
            </mt-card>
            {% endblock %}

            {% block sw_customer_create_adress_form %}
            <mt-card
                :title="$tc('sw-customer.detailBase.labelAddressesCard')"
                position-identifier="sw-customer-create-address-form"
            >
                <sw-customer-address-form
```

### Example 2
Source: `sw-order/component/sw-order-new-customer-modal/sw-order-new-customer-modal.html.twig`
```twig
    <sw-customer-base-form
        :is-loading="isLoading"
        :customer="customer"
        @sales-channel-change="onChangeSalesChannel"
    />
    {% endblock %}
</div>
{% endblock %}

{% block sw_order_new_customer_modal_content_shipping %}
<div v-if="active === 'shippingAddress'">
    {% block sw_order_new_customer_modal_content_shipping_same_billing %}

    <mt-switch
        v-model="isSameBilling"
```
