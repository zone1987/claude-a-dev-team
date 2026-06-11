# sw-product-feature-set-form

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
| `isLoading` | |

## Examples

### Example 1
Source: `sw-product/view/sw-product-detail-specifications/sw-product-detail-specifications.html.twig`
```twig
<sw-product-feature-set-form :allow-edit="acl.can('product.editor')" />
```
