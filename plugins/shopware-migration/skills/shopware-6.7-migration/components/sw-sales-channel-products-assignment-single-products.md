# sw-sales-channel-products-assignment-single-products

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| salesChannel | `any` | — | yes |  |
| containerStyle | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| selection-change | — | |

## Methods

| Method | Description |
|--------|-------------|
| `getProducts` | |
| `onChangeSearchTerm` | |
| `onSelectionChange` | |
| `onChangePage` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `productRepository` | |
| `productCriteria` | |
| `productColumns` | |
| `assetFilter` | |

## Examples

### Example 1
Source: `sw-sales-channel/component/sw-sales-channel-products-assignment-modal/sw-sales-channel-products-assignment-modal.html.twig`
```twig
<sw-sales-channel-products-assignment-single-products
    ref="product"
    v-hide="active === 'singleProducts'"
    :sales-channel="salesChannel"
    :container-style="productContainerStyle"
    @selection-change="onChangeSelection"
/>
{% endblock %}

{% block sw_sales_channel_products_assignment_modal_tab_content_categories %}
<sw-sales-channel-product-assignment-categories
    ref="category"
    v-hide="active === 'categories'"
    :sales-channel="salesChannel"
    :container-style="categoryContainerStyle"
```
