# sw-customer-card

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| customer | `any` | — | yes |  |
| title | `any` | — | yes |  |
| editMode | `any` | `false` | no |  |
| isLoading | `any` | `false` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| metadata-additional | — | |
| actions | — | |
| default | — | |

## Methods

| Method | Description |
|--------|-------------|
| `getMailTo` | |
| `onImitateCustomer` | |
| `onCloseImitateCustomerModal` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `hasActionSlot` | |
| `hasAdditionalDataSlot` | |
| `hasSummarySlot` | |
| `moduleColor` | |
| `fullName` | |
| `salutationCriteria` | |
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
| `accountTypeOptions` | |
| `isBusinessAccountType` | |
| `canUseCustomerImitation` | |
| `customerImitationWarning` | |
| `hasSingleBoundSalesChannelUrl` | |
| `currentUser` | |
| `emailIdnFilter` | |

## Examples

### Example 1
Source: `sw-customer/view/sw-customer-detail-base/sw-customer-detail-base.html.twig`
```twig
<sw-customer-card
    :title="$tc('sw-customer.detailBase.labelAccountCard')"
    :customer="customer"
    :edit-mode="customerEditMode"
    :is-loading="isLoading"
>
    {% block sw_customer_detail_base_info_metadata %}
    <sw-customer-base-info
        :customer="customer"
        :is-loading="isLoading"
        :customer-edit-mode="customerEditMode"
    />
    {% endblock %}
</sw-customer-card>
```
