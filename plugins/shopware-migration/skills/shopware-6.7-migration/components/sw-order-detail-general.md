# sw-order-detail-general

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| orderId | `any` | — | yes |  |
| isSaveSuccessful | `any` | `false` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| save-and-recalculate | — | |
| save-edits | — | |
| recalculate-and-reload | — | |
| save-and-reload | — | |
| reload-entity-data | — | |
| error | — | |

## Methods

| Method | Description |
|--------|-------------|
| `sortByTaxRate` | |
| `onShippingChargeEdited` | |
| `onShippingChargeUpdated` | |
| `saveAndRecalculate` | |
| `onSaveEdits` | |
| `recalculateAndReload` | |
| `updateLoading` | |
| `reloadEntityData` | |
| `saveAndReload` | |
| `showError` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `isLoading` | |
| `loading` | |
| `order` | |
| `versionContext` | |
| `delivery` | |
| `deliveryDiscounts` | |
| `shippingCostsDetail` | |
| `sortedCalculatedTaxes` | |
| `taxStatus` | |
| `displayRounded` | |
| `orderTotal` | |
| `currency` | |
| `currencyFilter` | |

## Examples

### Basic Usage
```twig
<sw-order-detail-general
    orderId="..."
>
    <!-- content -->
</sw-order-detail-general>
```
