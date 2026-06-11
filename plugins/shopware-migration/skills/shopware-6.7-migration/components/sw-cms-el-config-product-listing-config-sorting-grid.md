# sw-cms-el-config-product-listing-config-sorting-grid

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| productSortings | `any` | — | yes |  |
| defaultSorting | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| sorting-delete | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `fetchCustomFields` | |
| `formatProductSortingFields` | |
| `isItemACustomField` | |
| `stripCustomFieldPath` | |
| `getCustomFieldLabelByCriteriaName` | |
| `getCustomFieldByName` | |
| `onDelete` | |
| `isDefaultSorting` | |
| `onPageChange` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `visibleProductSortings` | |
| `paginationVisible` | |
| `customFieldRepository` | |
| `customFieldCriteria` | |
| `total` | |
| `gridColumns` | |

## Examples

### Example 1
Source: `sw-cms/elements/product-listing/config/sw-cms-el-config-product-listing.html.twig`
```twig
            <sw-cms-el-config-product-listing-config-sorting-grid
                :product-sortings="productSortings"
                :default-sorting="defaultSorting"
                :disabled="isInherited"
            />
            {% endblock %}
        </template>
    </sw-cms-inherit-wrapper>
</template>

<template v-if="active === 'filter'">
    <sw-cms-inherit-wrapper
        field="filters"
        :element="element"
        :label="$t('sw-cms.elements.productListing.config.tab.filter')"
```
