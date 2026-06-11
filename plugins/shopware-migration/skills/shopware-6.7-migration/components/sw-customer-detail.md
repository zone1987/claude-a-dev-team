# sw-customer-detail

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| customerId | `any` | — | yes |  |

## Methods

| Method | Description |
|--------|-------------|
| `loadCustomer` | |
| `createdComponent` | |
| `saveFinish` | |
| `validateEmail` | |
| `onSave` | |
| `onAbortButtonClick` | |
| `onActivateCustomerEditMode` | |
| `abortOnLanguageChange` | |
| `saveOnLanguageChange` | |
| `onChangeLanguage` | |
| `validPassword` | |
| `acceptCustomerGroupRegistration` | |
| `declineCustomerGroupRegistration` | |
| `createErrorMessageForCompanyField` | |
| `getDefaultSalutation` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `identifier` | |
| `customerRepository` | |
| `editMode` | |
| `defaultCriteria` | |
| `generalRoute` | |
| `addressesRoute` | |
| `ordersRoute` | |
| `emailHasChanged` | |
| `validCompanyField` | |
| `salutationRepository` | |
| `salutationCriteria` | |
| `swCustomerDetailBaseError` | |

## Examples

### Basic Usage
```twig
<sw-customer-detail
    customerId="..."
>
    <!-- content -->
</sw-customer-detail>
```
