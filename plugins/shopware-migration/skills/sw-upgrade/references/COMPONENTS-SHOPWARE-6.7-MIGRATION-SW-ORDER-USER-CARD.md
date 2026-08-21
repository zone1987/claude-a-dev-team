# sw-order-user-card

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| currentOrder | `any` | — | yes |  |
| versionContext | `any` | — | yes |  |
| isLoading | `any` | — | yes |  |
| isEditing | `any` | — | yes |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| additional-actions | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| error | — | |
| order-change | — | |
| onEditDeliveryAddress | — | |
| order-reset | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `renderFormattingAddress` | |
| `reload` | |
| `countryCriteria` | |
| `onEditBillingAddress` | |
| `onEditDeliveryAddress` | |
| `onAddressModalSave` | |
| `onResetOrder` | |
| `onAddressModalAddressSelected` | |
| `onAddNewDeliveryAddress` | |
| `emitChange` | |
| `onAddTag` | |
| `onRemoveTag` | |
| `renderTrackingUrl` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `countryRepository` | |
| `orderAddressRepository` | |
| `OrderTagRepository` | |
| `billingAddress` | |
| `delivery` | |
| `orderDate` | |
| `hasDeliveries` | |
| `hasDeliveryTrackingCode` | |
| `hasDifferentBillingAndShippingAddress` | |
| `lastChangedDate` | |
| `hasTags` | |
| `fullName` | |
| `currencyFilter` | |

## Examples

### Basic Usage
```twig
<sw-order-user-card
    currentOrder="..."
    versionContext="..."
    isLoading="..."
>
    <!-- content -->
</sw-order-user-card>
```
