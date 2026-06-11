# sw-product-layout-assignment

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| cmsPage | `any` | `null` | no |  |
| product | `any` | `null` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-layout-open | — | |
| button-edit-click | — | |
| button-delete-click | — | |

## Methods

| Method | Description |
|--------|-------------|
| `openLayoutModal` | |
| `openInPageBuilder` | |
| `onLayoutReset` | |

## Examples

### Example 1
Source: `sw-product/view/sw-product-detail-layout/sw-product-detail-layout.html.twig`
```twig
    <sw-product-layout-assignment
        :cms-page="currentPage"
        :product="product"
        @modal-layout-open="onOpenLayoutModal"
        @button-edit-click="onOpenInPageBuilder"
        @button-delete-click="onResetLayout"
    />
    {% endblock %}

    {% block sw_product_detail_layout_modal %}
    <sw-cms-layout-modal
        v-if="showLayoutModal"
        :headline="$tc('sw-product.layoutAssignment.subtitle')"
        :pre-selection="currentPage"
        :cms-page-types="['product_detail']"
```
