# sw-product-variant-modal

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| productEntity | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `fetchProductMedias` | |
| `fetchProductConfiguration` | |
| `fetchSystemCurrency` | |
| `fetchProductVariants` | |
| `getDefaultPriceForVariant` | |
| `onInheritanceRestore` | |
| `onInheritanceRemove` | |
| `sortOptions` | |
| `buildVariantOptions` | |
| `buildVariantName` | |
| `getVariantPrice` | |
| `onPageChange` | |
| `visitProduct` | |
| `getItemMedia` | |
| `deleteVariants` | |
| `canVariantsBeDeleted` | |
| `onInlineEditSave` | |
| `onInlineEditCancel` | |
| `onClickBulkDelete` | |
| `closeDeleteModal` | |
| `onDeleteVariant` | |
| `onSearchTermChange` | |
| `onSortColumn` | |
| `getNoPermissionsTooltip` | |
| `isMediaFieldInherited` | |
| `onMediaInheritanceRestore` | |
| `onMediaInheritanceRemove` | |
| `loadGroups` | |
| `resetFilterOptions` | |
| `filterOptionChecked` | |
| `getOptionsForGroup` | |
| `toggleFilterMenu` | |
| `toggleBulkEditModal` | |
| `onEditItems` | |
| `variantIsDigital` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `modalTitle` | |
| `openMainProductText` | |
| `productRepository` | |
| `productMediaRepository` | |
| `productConfigurationRepository` | |
| `currencyRepository` | |
| `groupRepository` | |
| `contextMenuEditText` | |
| `filterCriteria` | |
| `productVariantCriteria` | |
| `gridColumns` | |
| `canBeDeletedCriteria` | |
| `groupCriteria` | |
| `selectedGroups` | |
| `filterOptionsListing` | |
| `stockColorVariantFilter` | |

## Examples

### Example 1
Source: `sw-product/page/sw-product-list/sw-product-list.html.twig`
```twig
    <sw-product-variant-modal
        v-if="showVariantModal"
        :product-entity="productEntityVariantModal"
        @modal-close="closeVariantModal"
    />
    {% endblock %}
</template>

{% block sw_product_list_sidebar %}
<template #sidebar>
    <sw-sidebar>
        {% block sw_product_list_sidebar_refresh %}
        <sw-sidebar-item
            icon="regular-undo"
            :title="$tc('sw-product.list.titleSidebarItemRefresh')"
```
