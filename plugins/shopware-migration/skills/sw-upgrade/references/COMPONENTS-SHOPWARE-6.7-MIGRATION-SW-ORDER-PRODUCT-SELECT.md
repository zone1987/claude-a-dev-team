# sw-order-product-select

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| item | `any` | — | yes |  |
| salesChannelId | `any` | `''` | yes |  |
| taxStatus | `any` | `''` | yes |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| selection-label-property | — | |
| result-item | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onItemChanged` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `productRepository` | |
| `lineItemTypes` | |
| `lineItemPriceTypes` | |
| `isShownProductSelect` | |
| `isShownItemLabelInput` | |
| `contextWithInheritance` | |
| `productCriteria` | |

## Examples

### Example 1
Source: `sw-order/component/sw-order-line-items-grid-sales-channel/sw-order-line-items-grid-sales-channel.html.twig`
```twig
<sw-order-product-select
    v-if="isInlineEdit"
    :item="item"
    :tax-status="taxStatus"
    :sales-channel-id="salesChannelId"
/>
{% endblock %}

{% block sw_order_line_items_grid_sales_channel_grid_columns_label_link %}
<div
    v-else-if="!isInlineEdit && isProductItem(item)"
>

    {% block sw_order_line_items_grid_column_payload_options %}
    <mt-link
```

### Example 2
Source: `sw-order/component/sw-order-line-items-grid/sw-order-line-items-grid.html.twig`
```twig
<sw-order-product-select
    v-if="isInlineEdit"
    name="sw-field--item-label"
    :sales-channel-id="salesChannelId"
    :tax-status="taxStatus"
    :item="item"
/>
{% endblock %}

{% block sw_order_line_items_grid_grid_columns_label_link %}
<div
    v-else-if="!isInlineEdit && (isProductItem(item) || isContainerItem(item))"
    class="sw-order-line-items-grid__item-product"
>

```
