# sw-product-category-form

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| allowEdit | `any` | `true` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `displayAdvancedVisibility` | |
| `closeAdvancedVisibility` | |
| `visibilitiesRemoveInheritanceFunction` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `product` | |
| `parentProduct` | |
| `loading` | |
| `isChild` | |
| `showModeSetting` | |
| `productTagsError` | |
| `productActiveError` | |
| `hasSelectedVisibilities` | |
| `productVisibilityRepository` | |
| `salesChannelRepository` | |

## Examples

### Example 1
Source: `sw-product/view/sw-product-detail-base/sw-product-detail-base.html.twig`
```twig
<sw-product-category-form :allow-edit="acl.can('product.editor')" />
```
