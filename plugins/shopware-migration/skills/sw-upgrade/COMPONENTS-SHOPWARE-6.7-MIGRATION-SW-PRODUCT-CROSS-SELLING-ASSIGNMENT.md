# sw-product-cross-selling-assignment

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| assignedProducts | `any` | — | yes |  |
| crossSellingId | `any` | — | yes |  |
| allowEdit | `any` | `true` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| result-item | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onToggleProduct` | |
| `removeItem` | |
| `isSelected` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `product` | |
| `isLoading` | |
| `isLoadingGrid` | |
| `assignmentRepository` | |
| `productRepository` | |
| `searchCriteria` | |
| `searchContext` | |
| `total` | |
| `assignedProductColumns` | |
| `variantProductIds` | |
| `variantCriteria` | |
| `assetFilter` | |

## Examples

### Example 1
Source: `sw-product/component/sw-product-cross-selling-form/sw-product-cross-selling-form.html.twig`
```twig
        <sw-product-cross-selling-assignment
            v-else
            :assigned-products="crossSelling.assignedProducts"
            :cross-selling-id="crossSelling.id"
            :searchable-fields="['name', 'productNumber']"
            :allow-edit="allowEdit"
        />
        {% endblock %}

        {% block sw_product_detail_cross_selling_modal_preview_modal %}
        <sw-product-stream-modal-preview
            v-if="showModalPreview"
            ref="modalPreview"
            :filters="productStreamFilterTree"
            @modal-close="closeModalPreview"
```
