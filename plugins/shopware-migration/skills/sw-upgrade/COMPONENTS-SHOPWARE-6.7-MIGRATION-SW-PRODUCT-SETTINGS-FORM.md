# sw-product-settings-form

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| allowEdit | `any` | `true` | no |  |

## Computed Properties

| Name | Description |
|------|-------------|
| `product` | |
| `parentProduct` | |
| `productReleaseDateError` | |
| `productStockError` | |
| `productMinPurchaseError` | |
| `productMaxPurchaseError` | |
| `productEanError` | |
| `productManufacturerNumberError` | |
| `productShippingFreeError` | |
| `productMarkAsTopsellerError` | |

## Examples

### Example 1
Source: `sw-product/view/sw-product-detail-base/sw-product-detail-base.html.twig`
```twig
<sw-product-settings-form :allow-edit="acl.can('product.editor')" />
```
