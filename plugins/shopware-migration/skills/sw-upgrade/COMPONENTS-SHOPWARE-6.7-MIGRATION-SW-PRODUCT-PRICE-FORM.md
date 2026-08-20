# sw-product-price-form

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| allowEdit | `any` | `true` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `removePriceInheritation` | |
| `inheritationCheckFunction` | |
| `onMaintainCurrenciesClose` | |
| `getTaxLabel` | |
| `updatePrices` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `isLoading` | |
| `defaultPrice` | |
| `defaultCurrency` | |
| `productTaxRate` | |
| `showModeSetting` | |
| `product` | |
| `parentProduct` | |
| `taxes` | |
| `currencies` | |
| `productTaxIdError` | |
| `productPriceError` | |
| `productPurchasePricesError` | |
| `taxRateHelpText` | |
| `prices` | |
| `parentPrices` | |
| `taxRateOptions` | |

## Examples

### Example 1
Source: `sw-product/view/sw-product-detail-base/sw-product-detail-base.html.twig`
```twig
<sw-product-price-form :allow-edit="acl.can('product.editor')" />
```
