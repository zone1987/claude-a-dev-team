# sw-promotion-v2-settings-discount-type

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| discount | `any` | — | yes |  |
| discountScope | `any` | — | yes |  |
| preselectedDiscountType | `any` | — | no |  |
| preselectedApplyDiscountTo | `any` | — | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `getDiscountTypeSelection` | |
| `getApplyDiscountToSelection` | |
| `onClickAdvancedPrices` | |
| `clearAdvancedPrices` | |
| `setCurrencyForDiscountPrices` | |
| `prepareAdvancedPrices` | |
| `onMaxValueChanged` | |
| `onCloseAdvancedPricesModal` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `isPercentageType` | |
| `labelValue` | |
| `showAdvancedPricesLink` | |
| `currencyPriceColumns` | |
| `currencyRepository` | |
| `advancedPricesRepo` | |
| `currencyCriteria` | |
| `showMaxValueAdvancedPrices` | |
| `discountTypeOptions` | |
| `applierOptions` | |

## Examples

### Basic Usage
```twig
<sw-promotion-v2-settings-discount-type
    discount="..."
    discountScope="..."
>
    <!-- content -->
</sw-promotion-v2-settings-discount-type>
```
