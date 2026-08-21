# sw-product-stream-grid-preview

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| filters | `any` | — | yes |  |
| columns | `any` | — | no |  |
| criteria | `any` | — | no |  |
| showSelection | `any` | `false` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| additional-columns | — | |
| empty-state | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| selection-change | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onSearchTermChange` | |
| `createdComponent` | |
| `loadSystemDefaultCurrency` | |
| `loadProducts` | |
| `onPageChange` | |
| `getPriceForDefaultCurrency` | |
| `onSelectionChange` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `productRepository` | |
| `currencyRepository` | |
| `salesChannelRepository` | |
| `salesChannelCriteria` | |
| `defaultColumns` | |
| `productColumns` | |
| `emptyStateMessage` | |
| `assetFilter` | |
| `currencyFilter` | |

## Examples

### Example 1
Source: `sw-category/view/sw-category-detail-products/sw-category-detail-products.html.twig`
```twig
    <sw-product-stream-grid-preview
        :filters="productStreamFilter"
        :columns="productColumns"
    />
</template>
{% endblock %}

{% block sw_category_detail_product_assignment_column_name %}
<template #[nameColumn]="{ item, column }">
    <router-link
        :to="{ name: column.routerLink, params: { id: item.id } }"
    >
        <sw-product-variant-info :variations="item.variation">
            {{ getItemName(item) }}
        </sw-product-variant-info>
```
