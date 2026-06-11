# sw-product-visibility-detail

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| disabled | `any` | `false` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onPageChange` | |
| `changeVisibilityValue` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `product` | |
| `truncateFilter` | |
| `filteredItems` | |
| `names` | |

## Examples

### Example 1
Source: `sw-bulk-edit/component/product/sw-bulk-edit-product-visibility/sw-bulk-edit-product-visibility.html.twig`
```twig
<sw-product-visibility-detail />
```

### Example 2
Source: `sw-product/component/sw-product-category-form/sw-product-category-form.html.twig`
```twig
<sw-product-visibility-detail :disabled="!allowEdit" />
```
