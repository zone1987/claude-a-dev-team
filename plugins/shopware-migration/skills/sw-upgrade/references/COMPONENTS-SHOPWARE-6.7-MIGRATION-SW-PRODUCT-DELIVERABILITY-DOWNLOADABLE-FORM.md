# sw-product-deliverability-downloadable-form

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| disabled | `any` | `false` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onSwitchInput` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `product` | |
| `parentProduct` | |
| `showModeSetting` | |
| `showStockSetting` | |
| `productStockError` | |
| `productDeliveryTimeIdError` | |
| `productIsCloseoutError` | |
| `productMaxPurchaseError` | |

## Examples

### Example 1
Source: `sw-product/view/sw-product-detail-base/sw-product-detail-base.html.twig`
```twig
<sw-product-deliverability-downloadable-form :disabled="!acl.can('product.editor')" />
```
