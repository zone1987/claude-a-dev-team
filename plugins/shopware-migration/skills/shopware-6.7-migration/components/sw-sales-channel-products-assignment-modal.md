# sw-sales-channel-products-assignment-modal

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| salesChannel | `any` | — | yes |  |
| isAssignProductLoading | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |
| products-add | — | |

## Methods

| Method | Description |
|--------|-------------|
| `mountedComponent` | |
| `getProductContainerStyle` | |
| `getCategoryContainerStyle` | |
| `getProductGroupContainerStyle` | |
| `onChangeSelection` | |
| `onCloseModal` | |
| `onAddProducts` | |
| `setProductLoading` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `productCount` | |
| `products` | |

## Examples

### Example 1
Source: `sw-sales-channel/view/sw-sales-channel-detail-products/sw-sales-channel-detail-products.html.twig`
```twig
    <sw-sales-channel-products-assignment-modal
        v-if="showProductsModal"
        :sales-channel="salesChannel"
        :is-assign-product-loading="isAssignProductLoading"
        @modal-close="showProductsModal = false"
        @products-add="onAddProducts"
    />
    {% endblock %}
</mt-card>
{% endblock %}

```
