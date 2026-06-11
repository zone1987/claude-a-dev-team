# sw-entity-multi-select

> Multi-select dropdown for Shopware entities with tag display.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| labelProperty | `null \| null` | `'name'` | no |  |
| resultLimit | `any` | `25` | no |  |
| valueLimit | `any` | `5` | no |  |
| placeholder | `any` | `''` | no |  |
| alwaysShowPlaceholder | `any` | `false` | no |  |
| criteria | `any` | — | no |  |
| disabled | `any` | — | no |  |
| highlightSearchTerm | `any` | `true` | no |  |
| entityCollection | `any` | — | yes |  |
| entityName | `any` | `null` | no |  |
| context | `any` | — | no |  |
| hideLabels | `any` | `false` | no |  |
| selectionDisablingMethod | `any` | — | no |  |
| descriptionPosition | `any` | `'right'` | no | Valid: `bottom`, `right` |
| advancedSelectionComponent | `any` | — | no |  |
| advancedSelectionParameters | `any` | — | no |  |
| displayVariants | `any` | `false` | no |  |
| label | `any` | — | no |  |
| autocomplete | `any` | — | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| selection-label-property | — | |
| before-item-list | — | |
| result-item | — | |
| result-label-preview | — | |
| result-label-property | — | |
| result-description-property | — | |
| after-item-list | — | |
| label | — | |
| hint | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| search | — | |
| update:entityCollection | — | |
| item-add | — | |
| item-remove | — | |
| display-values-expand | — | |
| search-term-change | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `refreshCurrentCollection` | |
| `createEmptyCollection` | |
| `isSelected` | |
| `loadData` | |
| `search` | |
| `displaySearch` | |
| `displayLabelProperty` | |
| `resetActiveItem` | |
| `resetCriteria` | |
| `paginate` | |
| `emitChanges` | |
| `addItem` | |
| `remove` | |
| `removeLastItem` | |
| `onSelectExpanded` | |
| `onSelectCollapsed` | |
| `expandValueLimit` | |
| `onSearchTermChange` | |
| `debouncedSearch` | |
| `resetResultCollection` | |
| `getKey` | |
| `isSelectionDisabled` | |
| `openAdvancedSelectionModal` | |
| `closeAdvancedSelectionModal` | |
| `onAdvancedSelectionSubmit` | |
| `clearSelection` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `repository` | |
| `visibleValues` | |
| `totalValuesCount` | |
| `invisibleValueCount` | |
| `isAdvancedSelectionActive` | |

## Examples

### Example 1
Source: `sw-bulk-edit/page/sw-bulk-edit-product/sw-bulk-edit-product.html.twig`
```twig
<sw-entity-multi-select
    v-else-if="bulkEditProduct[formField.name].type === 'remove'"
    class="sw-bulk-edit-product-base__advanced-prices-selection"
    :placeholder="$tc('sw-bulk-edit.product.advancedPrices.selectRule')"
    :criteria="ruleCriteria"
    entity-name="rule"
    :entity-collection="!!bulkEditProduct[formField.name].isInherited ? [] : entity[formField.name]"
    :disabled="!!bulkEditProduct[formField.name].isInherited || undefined"
    @update:entity-collection="onRuleChange"
>
    <template #selection-label-property="{ item }">
        {{ item.ruleName }}
    </template>

    <template #result-item="{ item, index, labelProperty, isSelected, addItem, getKey }">
```

### Example 2
Source: `sw-category/view/sw-landing-page-detail-base/sw-landing-page-detail-base.html.twig`
```twig
    <sw-entity-multi-select
        v-model:entity-collection="landingPage.salesChannels"
        required
        class="sw-landing-page-detail-base__sales_channel"
        entity-name="sales_channel"
        :disabled="!acl.can('landing_page.editor')"
        :label="$tc('sw-landing-page.base.seo.labelSalesChannel')"
        :placeholder="$tc('sw-landing-page.base.seo.placeholderSalesChannel')"
        :error="landingPageSalesChannelsError"
    />
    {% endblock %}

    {% block sw_landing_page_detail_base_information_tags %}
    <sw-entity-tag-select
        v-if="landingPage && !isLoading"
```

### Example 3
Source: `sw-cms/component/sw-cms-layout-assignment-modal/sw-cms-layout-assignment-modal.html.twig`
```twig
    <sw-entity-multi-select
        v-model:entity-collection="page.landingPages"
        class="sw-cms-layout-assignment-modal__landing-page-select"
        :label="$tc('global.entities.landing_page')"
        :placeholder="$tc('sw-cms.components.cmsLayoutAssignmentModal.placeholderLandingPages')"
        entity-name="landing_page"
    />
    {% endblock %}
</template>
{% endblock %}

{% block sw_cms_layout_assignment_modal_category_select %}
<template v-if="!isProductDetailPage && active === 'categories'">

    {% block sw_cms_layout_assignment_modal_category_select_field %}
```

### Example 4
Source: `sw-cms/elements/product-listing/config/sw-cms-el-config-product-listing.html.twig`
```twig
<sw-entity-multi-select
    v-model:entity-collection="productSortings"
    class="sw-cms-el-config-product-listing-config-sorting-grid__select"
    label-property="label"
    :criteria="allProductSortingsCriteria"
    :hide-labels="true"
    :placeholder="$t('sw-cms.elements.productListing.config.sorting.placeHolderProductSortings')"
    :disabled="isInherited"
>
    <template #result-item="{ item, index, labelProperty, valueProperty, searchTerm, highlightSearchTerm, isSelected, addItem, getKey }">
        <slot
            name="result-item"
            v-bind="{ item, index, labelProperty, valueProperty: 'id', searchTerm, highlightSearchTerm, isSelected, addItem, getKey }"
        >
            <sw-select-result
```

### Example 5
Source: `sw-cms/elements/product-slider/config/sw-cms-el-config-product-slider.html.twig`
```twig
<sw-entity-multi-select
    v-model:entity-collection="productCollection"
    class="sw-cms-el-config-product-slider__tab-content-products"
    :placeholder="$tc('sw-cms.elements.productSlider.config.placeholder.selection')"
    :context="productMultiSelectContext"
    :criteria="productMediaFilter"
    :disabled="isInherited"
    @update:entity-collection="onProductsChange"
>
    <template #selection-label-property="{ item }">
        <sw-product-variant-info :variations="item.variation">
            {{ item.translated.name || item.name }}
        </sw-product-variant-info>
    </template>
    <template #result-item="{ item, index }">
```
