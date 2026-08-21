# sw-cms-el-config-product-listing

> Shopware Administration component.

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onUpdateProductSortings` | |
| `initProductSorting` | |
| `fetchProductSortings` | |
| `updateValuesFromConfig` | |
| `transformProductSortings` | |
| `initDefaultSorting` | |
| `loadFilterableProperties` | |
| `sortProperties` | |
| `onDefaultSortingChange` | |
| `isDefaultSorting` | |
| `isActiveFilter` | |
| `updateFilters` | |
| `unpackFilters` | |
| `onFilterProperties` | |
| `onPropertiesPageChange` | |
| `propertyStatusChanged` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `showSortingGrid` | |
| `showFilterGrid` | |
| `productSortingRepository` | |
| `propertyRepository` | |
| `productSortingsCriteria` | |
| `propertyCriteria` | |
| `allProductSortingsCriteria` | |
| `excludedDefaultSortingCriteria` | |
| `productSortingsConfigValue` | |
| `filterByManufacturer` | |
| `filterByRating` | |
| `filterByPrice` | |
| `filterByFreeShipping` | |
| `filterByProperties` | |
| `showPropertySelection` | |
| `gridColumns` | |
| `gridClasses` | |
| `assetFilter` | |
| `boxLayoutOptions` | |
| `boxHeadlineLevel` | |

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
