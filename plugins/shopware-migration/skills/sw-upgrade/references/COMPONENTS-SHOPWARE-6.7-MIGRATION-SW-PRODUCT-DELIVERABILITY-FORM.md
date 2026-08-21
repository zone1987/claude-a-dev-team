# sw-product-deliverability-form

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| allowEdit | `any` | `true` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `product` | |
| `parentProduct` | |
| `loading` | |
| `showModeSetting` | |
| `productStockError` | |
| `productDeliveryTimeIdError` | |
| `productIsCloseoutError` | |
| `productMaxPurchaseError` | |
| `productPurchaseStepsError` | |
| `productMinPurchaseError` | |
| `productShippingFreeError` | |
| `productRestockTimeError` | |

## Examples

### Example 1
Source: `sw-product/view/sw-product-detail-base/sw-product-detail-base.html.twig`
```twig
<sw-product-deliverability-form :allow-edit="acl.can('product.editor')" />
```
