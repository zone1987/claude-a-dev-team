# sw-order-create-base

> Shopware Administration component.

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| error | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `createCart` | |
| `loadCart` | |
| `onSelectExistingCustomer` | |
| `updateCustomerContext` | |
| `setCustomer` | |
| `setCurrency` | |
| `onEditBillingAddress` | |
| `onEditShippingAddress` | |
| `setCustomerAddress` | |
| `closeModal` | |
| `save` | |
| `onSaveItem` | |
| `onRemoveItems` | |
| `updateLoading` | |
| `sortByTaxRate` | |
| `onSubmitCode` | |
| `onRemoveExistingCode` | |
| `updatePromotionList` | |
| `handlePromotionCodeTags` | |
| `onShippingChargeEdited` | |
| `switchAutomaticPromotions` | |
| `enableAutomaticPromotions` | |
| `onClosePromotionModal` | |
| `onSavePromotionModal` | |
| `onShippingChargeUpdated` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `cartErrors` | |
| `customerRepository` | |
| `customerAddressRepository` | |
| `currencyRepository` | |
| `customerAddressCriteria` | |
| `defaultCriteria` | |
| `orderDate` | |
| `customer` | |
| `salesChannelId` | |
| `isCustomerActive` | |
| `cart` | |
| `cartLineItems` | |
| `cartAutomaticPromotionItems` | |
| `cartPrice` | |
| `currency` | |
| `cartDelivery` | |
| `promotionCodeTags` | |
| `cartDeliveryDiscounts` | |
| `filteredCalculatedTaxes` | |
| `promotionCodeLineItems` | |
| `hasLineItem` | |
| `shippingCostsDetail` | |
| `disabledAutoPromotionVisibility` | |
| `taxStatus` | |
| `displayRounded` | |
| `orderTotal` | |
| `currencyFilter` | |

## Examples

### Basic Usage
```twig
<sw-order-create-base>
    <!-- content -->
</sw-order-create-base>
```
