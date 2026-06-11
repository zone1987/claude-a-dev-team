# sw-bulk-edit-modal

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| selection | `any` | — | no |  |
| steps | `any` | — | no |  |
| bulkGridEditColumns | `any` | — | yes |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| slot | — | |
| sw-bulk-edit-modal-cancel | — | |
| sw-bulk-edit-modal-confirm | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |
| edit-items | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `paginate` | |
| `updateBulkEditSelection` | |
| `editItems` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `itemCount` | |
| `paginateRecords` | |
| `getSlots` | |

## Examples

### Example 1
Source: `sw-product/page/sw-product-list/sw-product-list.html.twig`
```twig
<sw-bulk-edit-modal
    v-if="showBulkEditModal"
    class="sw-product-bulk-edit-modal"
    :selection="selection"
    :bulk-grid-edit-columns="productBulkEditColumns"
    @edit-items="onBulkEditItems"
    @modal-close="showBulkEditModal = false"
>
    {% block sw_product_list_bulk_edit_grid_columns_name %}
    <template #column-name="{ item }">
        <router-link
            :to="{ name: 'sw.product.detail', params: { id: item.id } }"
            target="_blank"
            rel="noreferrer noopener"
        >
```

### Example 2
Source: `sw-product/component/sw-product-variant-modal/sw-product-variant-modal.html.twig`
```twig
<sw-bulk-edit-modal
    v-if="showBulkEditModal"
    class="sw-product-variant-modal__bulk-edit-modal"
    :selection="selection"
    :bulk-grid-edit-columns="gridColumns"
    @edit-items="onEditItems"
    @modal-close="toggleBulkEditModal"
>
    {% block sw_product_variant_modal_bulk_edit_modal_column_name %}
    <template #column-name="{ item }">
        <sw-media-preview-v2 :source="getItemMedia(item)" />
        <router-link :to="{ name: 'sw.product.detail', params: { id: item.id } }">
            <span
                v-if="item.translated.name"
                class="sw-product-variant-modal__variant-name"
```

### Example 3
Source: `sw-product/component/sw-product-variants/sw-product-variants-overview/sw-product-variants-overview.html.twig`
```twig
<sw-bulk-edit-modal
    v-if="showBulkEditModal"
    class="sw-product-variants-overview__bulk-edit-modal"
    :selection="selection"
    :bulk-grid-edit-columns="variantColumns"
    @edit-items="onEditItems"
    @modal-close="toggleBulkEditModal"
>
    {% block sw_product_variants_overview_bulk_edit_modal_column_name %}
    <template #column-name="{ item }">
        <template v-if="item.options">
            <router-link
                class="sw-product-variants-overview__variation-link"
                :to="{ name: 'sw.product.detail.base', params: { id: item.id } }"
                @click="onOptionEdit(item)"
```

### Example 4
Source: `sw-customer/page/sw-customer-list/sw-customer-list.html.twig`
```twig
<sw-bulk-edit-modal
    v-if="showBulkEditModal"
    ref="bulkEditModal"
    class="sw-customer-bulk-edit-modal"
    :selection="selection"
    :bulk-grid-edit-columns="customerColumns"
    @edit-items="onBulkEditItems"
    @modal-close="onBulkEditModalClose"
>
    {% block sw_customer_list_bulk_edit_grid_columns_name %}
    <template #column-firstName="{ item }">
        <router-link
            :to="{ name: 'sw.customer.detail', params: { id: item.id } }"
            target="_blank"
            rel="noreferrer noopener"
```

### Example 5
Source: `sw-order/page/sw-order-list/sw-order-list.html.twig`
```twig
<sw-bulk-edit-modal
    v-if="showBulkEditModal"
    ref="bulkEditModal"
    class="sw-order-bulk-edit-modal"
    :selection="selection"
    :bulk-grid-edit-columns="orderColumns"
    @edit-items="onBulkEditItems"
    @modal-close="showBulkEditModal = false"
>
    {% block sw_order_list_bulk_edit_grid_columns_order_number %}
    <template #column-orderNumber="{ item }">
        {% block sw_order_list_bulk_edit_grid_order_number_link %}
        <router-link
            :to="{ name: 'sw.order.detail', params: { id: item.id } }"
            target="_blank"
```
