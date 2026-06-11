# sw-customer-base-info

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| customer | `any` | — | yes |  |
| customerEditMode | `any` | `false` | yes |  |
| isLoading | `any` | `false` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `orderRepository` | |
| `languageRepository` | |
| `languageId` | |
| `customerLanguageName` | |
| `languageCriteria` | |
| `orderCriteria` | |
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
| `isBusinessAccountType` | |
| `dateFilter` | |
| `currencyFilter` | |

## Examples

### Example 1
Source: `sw-customer/view/sw-customer-detail-base/sw-customer-detail-base.html.twig`
```twig
    <sw-customer-base-info
        :customer="customer"
        :is-loading="isLoading"
        :customer-edit-mode="customerEditMode"
    />
    {% endblock %}
</sw-customer-card>
{% endblock %}

{% block sw_customer_detail_base_default_addresses_card %}
<mt-card
    v-if="customer.defaultShippingAddress || customer.defaultBillingAddress"
    :title="$tc('sw-customer.detailBase.labelAddressesCard')"
    position-identifier="sw-customer-detail-base-default-addresses"
    class="sw-customer-detail-base__default-addresses"
```
