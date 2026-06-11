# sw-customer-detail-addresses

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| customer | `any` | — | yes |  |
| customerEditMode | `any` | — | yes |  |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `getAddressColumns` | |
| `setAddressSorting` | |
| `onCreateNewAddress` | |
| `createNewCustomerAddress` | |
| `onSaveAddress` | |
| `isValidAddress` | |
| `onCloseAddressModal` | |
| `onEditAddress` | |
| `onDeleteAddress` | |
| `onConfirmDeleteAddress` | |
| `onCloseDeleteAddressModal` | |
| `isDefaultAddress` | |
| `onChangeDefaultBillingAddress` | |
| `onChangeDefaultShippingAddress` | |
| `onDuplicateAddress` | |
| `onChangeDefaultAddress` | |
| `onChange` | |
| `refreshList` | |
| `createPrefix` | |
| `getDefaultSalutation` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `customerRepository` | |
| `customFieldSetRepository` | |
| `customerAddressRepository` | |
| `addressColumns` | |
| `addressRepository` | |
| `sortedAddresses` | |
| `salutationRepository` | |
| `salutationCriteria` | |

## Examples

### Basic Usage
```twig
<sw-customer-detail-addresses
    customer="..."
    customerEditMode="..."
>
    <!-- content -->
</sw-customer-detail-addresses>
```
