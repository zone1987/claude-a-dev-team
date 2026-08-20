# sw-cms-reset-inheritance

> Shopware Administration component.

## Methods

| Method | Description |
|--------|-------------|
| `onConfirm` | |
| `resetSlotOverrides` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `cmsPageStore` | |
| `hasOverrides` | |

## Examples

### Example 1
Source: `sw-category/component/sw-category-layout-card/sw-category-layout-card.html.twig`
```twig
<sw-cms-reset-inheritance />
```

### Example 2
Source: `sw-product/component/sw-product-layout-assignment/sw-product-layout-assignment.html.twig`
```twig
<sw-cms-reset-inheritance v-if="product" />
```
