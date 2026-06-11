# sw-cms-product-assignment

> Shopware Administration component.

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| select | — | |
| before-item-list | — | |
| result-item | — | |
| result-label-property | — | |
| after-item-list | — | |
| `column-${column.property}` | — | |
| empty-state | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| change | — | |
| paginate | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `initData` | |
| `searchItems` | |
| `onItemSelect` | |
| `removeItem` | |
| `onSelectCollapsed` | |
| `paginateGrid` | |
| `removeFromGrid` | |

## Examples

### Example 1
Source: `sw-cms/component/sw-cms-layout-assignment-modal/sw-cms-layout-assignment-modal.html.twig`
```twig
<sw-cms-product-assignment
    class="sw-cms-layout-assignment-modal__product-select"
    :local-mode="true"
    :entity-collection="page.products"
    :columns="productColumns"
    :criteria="productCriteria"
    :select-label="$tc('sw-cms.components.cmsLayoutAssignmentModal.products.productAssignmentLabel')"
    :placeholder="$tc('sw-cms.components.cmsLayoutAssignmentModal.products.productAssignmentPlaceholder')"
>
    {% block sw_cms_layout_assignment_modal_product_detail_pages_column_name %}
    <template #column-name="{ item, column }">
        <router-link
            :to="{ name: column.routerLink, params: { id: item.id } }"
        >
            <sw-product-variant-info
```
