# sw-product-cross-selling-form

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| crossSelling | `any` | — | yes |  |
| allowEdit | `any` | `true` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onShowDeleteModal` | |
| `onCloseDeleteModal` | |
| `onConfirmDelete` | |
| `openModalPreview` | |
| `closeModalPreview` | |
| `loadStreamPreview` | |
| `getProductStreamFilter` | |
| `updateProductStreamFilterTree` | |
| `onSortingChanged` | |
| `onTypeChanged` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `crossSellingNameError` | |
| `crossSellingTypeError` | |
| `crossSellingPositionError` | |
| `product` | |
| `isLoading` | |
| `productCrossSellingRepository` | |
| `productStreamRepository` | |
| `productStreamFilterRepository` | |
| `productStreamFilterCriteria` | |
| `crossSellingAssigmentRepository` | |
| `crossSellingTitle` | |
| `sortingTypes` | |
| `crossSellingTypes` | |
| `previewDisabled` | |
| `sortingConCat` | |
| `disablePositioning` | |
| `associationValue` | |
| `crossSellingTypeOptions` | |
| `sortingTypeOptions` | |
| `productStreamCriteria` | |

## Examples

### Example 1
Source: `sw-product/view/sw-product-detail-cross-selling/sw-product-detail-cross-selling.html.twig`
```twig
        <sw-product-cross-selling-form
            v-for="item in product.crossSellings"
            :key="item.id"
            :cross-selling="item"
            :allow-edit="acl.can('product.editor')"
        />
    </ul>
    {% endblock %}

    {% block sw_product_detail_cross_selling_add %}
    <mt-button
        v-tooltip="{
            message: onAddCrossSellingTooltipMessage,
            disabled: acl.can('product.editor') && isSystemDefaultLanguage,
            showOnDisabledElements: true
```
