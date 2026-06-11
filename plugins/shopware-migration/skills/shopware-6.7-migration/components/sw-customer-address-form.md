# sw-customer-address-form

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| customer | `any` | — | yes |  |
| address | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `getCountryStates` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `addressRepository` | |
| `countryRepository` | |
| `countryStateRepository` | |
| `addressCompanyError` | |
| `addressDepartmentError` | |
| `addressSalutationIdError` | |
| `addressTitleError` | |
| `addressFirstNameError` | |
| `addressLastNameError` | |
| `addressStreetError` | |
| `addressAdditionalAddressLine1Error` | |
| `addressAdditionalAddressLine2Error` | |
| `addressZipcodeError` | |
| `addressCityError` | |
| `addressCountryIdError` | |
| `addressPhoneNumberError` | |
| `addressCountryStateIdError` | |
| `countryId` | |
| `countryCriteria` | |
| `stateCriteria` | |
| `salutationCriteria` | |
| `hasStates` | |
| `isBusinessAccountType` | |

## Examples

### Example 1
Source: `sw-customer/page/sw-customer-create/sw-customer-create.html.twig`
```twig
                <sw-customer-address-form
                    v-if="customer"
                    v-bind="{ customer, address }"
                />
            </mt-card>
            {% endblock %}
        </sw-card-view>
    </template>
    {% endblock %}
</sw-page>
{% endblock %}

```

### Example 2
Source: `sw-customer/view/sw-customer-detail-addresses/sw-customer-detail-addresses.html.twig`
```twig
<sw-customer-address-form
    :address="currentAddress"
    :customer="activeCustomer"
>

    <sw-customer-address-form-options
        :address="currentAddress"
        :customer="activeCustomer"
        :custom-field-sets="customerAddressCustomFieldSets"
        @default-address-change="onChangeDefaultAddress"
    />

</sw-customer-address-form>
{% endblock %}

```

### Example 3
Source: `sw-order/component/sw-order-address-modal/sw-order-address-modal.html.twig`
```twig
    <sw-customer-address-form
        :address="address"
        :customer="orderCustomer"
        :countries="countries"
    />
    <sw-custom-field-set-renderer
        :entity="address"
        variant="tabs"
        :sets="addressCustomFieldSets"
    />
    {% endblock %}
</div>
<div v-if="active==='addresses'">
    {% block sw_order_address_modal_tabs_content_select_address %}
    <mt-button
```

### Example 4
Source: `sw-order/component/sw-order-address-selection/sw-order-address-selection.html.twig`
```twig
<sw-customer-address-form
    :address="currentAddress"
    :customer="customer"
>
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
```

### Example 5
Source: `sw-order/component/sw-order-create-address-modal/sw-order-create-address-modal.html.twig`
```twig
<sw-customer-address-form
    :address="currentAddress"
    :customer="activeCustomer"
    :disabled="isLoading"
>
    <sw-customer-address-form-options
        :address="currentAddress"
        :customer="activeCustomer"
        :custom-field-sets="[]"
        @default-address-change="onChangeDefaultAddress"
    />
</sw-customer-address-form>
{% endblock %}

{% block sw_order_create_address_form_modal_footer %}
```
