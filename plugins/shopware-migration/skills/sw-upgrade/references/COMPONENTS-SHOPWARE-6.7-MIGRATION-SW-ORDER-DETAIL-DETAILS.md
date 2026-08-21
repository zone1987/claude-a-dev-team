# sw-order-detail-details

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| orderId | `any` | — | yes |  |
| isSaveSuccessful | `any` | `false` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update-loading | — | |
| save-and-recalculate | — | |
| save-and-reload | — | |
| save-edits | — | |
| reload-entity-data | — | |
| error | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onShippingChargeEdited` | |
| `loadingChange` | |
| `saveAndRecalculate` | |
| `saveAndReload` | |
| `onSaveEdits` | |
| `reloadEntityData` | |
| `showError` | |
| `updateLoading` | |
| `validateTrackingCode` | |
| `onChangeOrderAddress` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `isLoading` | |
| `order` | |
| `versionContext` | |
| `orderAddressIds` | |
| `orderOrderCustomerEmailError` | |
| `delivery` | |
| `transaction` | |
| `customFieldSetRepository` | |
| `customFieldSetCriteria` | |
| `salesChannelCriteria` | |
| `paymentMethodCriteria` | |
| `taxStatus` | |
| `currency` | |
| `billingAddress` | |
| `shippingAddress` | |
| `selectedBillingAddressId` | |
| `selectedShippingAddressId` | |
| `shippingCosts` | |

## Examples

### Basic Usage
```twig
<sw-order-detail-details
    orderId="..."
>
    <!-- content -->
</sw-order-detail-details>
```
