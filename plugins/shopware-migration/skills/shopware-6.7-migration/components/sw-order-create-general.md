# sw-order-create-general

> Shopware Administration component.

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onSaveItem` | |
| `onShippingChargeEdited` | |
| `onRemoveItems` | |
| `loadCart` | |
| `sortByTaxRate` | |
| `onShippingChargeUpdated` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `customer` | |
| `cart` | |
| `currency` | |
| `context` | |
| `isCustomerActive` | |
| `cartDelivery` | |
| `cartDeliveryDiscounts` | |
| `taxStatus` | |
| `shippingCostsDetail` | |
| `filteredCalculatedTaxes` | |
| `displayRounded` | |
| `orderTotal` | |
| `currencyFilter` | |

## Examples

### Example 1
Source: `sw-order/view/sw-order-create-general/sw-order-create-general.html.twig`
```twig
    <sw-order-create-general-info
        :cart="cart"
        :context="context"
        :is-loading="isLoading"
    />
</mt-card>

<sw-extension-component-section
    position-identifier="sw-order-create-base-line-items__before"
/>

<sw-order-line-items-grid-sales-channel
    class="sw-order-create-general__line-items"
    position-identifier="sw-order-create-line-items"
    :is-loading="isLoading"
```
